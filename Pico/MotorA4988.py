from machine import Pin
import time
import concurrent.futures

TURN_TO_STEP = 200
STEP_TO_TURN = 1 / 200

class MotorA4988:
    def __init__(self, step_pin:Pin, dir_pin:Pin, en_pin:Pin, MIN_TURN:float, MAX_TURN:float):
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        self.en_pin = en_pin
        self.step_count = 0
        self.MIN_TURN = MIN_TURN
        self.MAX_TURN = MAX_TURN

    def get_step_count(self):
        return self.step_count

    def step(self, steps:int, delay_ms:float):
        iterator = 1
        # decide direction
        if steps > 0:
            self.dir_pin.high()
            iterator = 1
        else:
            self.dir_pin.low()
            iterator = -1

        # enable Motor
        self.en_pin.low()
        for i in range(int(abs(steps))):
            self.step_pin.high()
            time.sleep_ms(delay_ms)
            self.step_pin.low()
            time.sleep_ms(delay_ms)
            self.step_count += iterator

            if self.step_count * STEP_TO_TURN >= self.MAX_TURN or self.step_count <= self.MIN_TURN:
                return

        # disable motor
        self.en_pin.high()

    def full_turn(self, turns:float, delay_ms:float):
        iterator = 1
        # decide direction
        if turns > 0:
            self.dir_pin.high()
            iterator = 1
        else:
            self.dir_pin.low()
            iterator = -1

        # enable Motor
        self.en_pin.low()

        for i in range(int(abs(turns * TURN_TO_STEP))):
            self.step_pin.high()
            time.sleep_ms(delay_ms)
            self.step_pin.low()
            time.sleep_ms(delay_ms)
            self.step_count += iterator

            if self.step_count / TURN_TO_STEP >= self.MAX_TURN or self.step_count <= self.MIN_TURN:
                return

        # disable motor
        self.en_pin.high()

    
    def bring_to_relative_position(self, t:float, delay_ms:float=50):
        """
        Interpolate position between MIN_TURN and MAX_TURN
        """
        # if not (0 <= t <= 1):
        #     print("t must be in range 0 to 1 but is", t)
        #     return

        position =(1 - t) * self.MIN_TURN + t * self.MAX_TURN
        to_move = int(position * TURN_TO_STEP - self.step_count)
        self.step(to_move, delay_ms)

    @staticmethod
    def bring_to_relative_positions_in_Threads(motors, t:float, delay_ms:float=50):
        """
        Interpolate positions between MIN_TURN and MAX_TURN in Threads
        """
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Starten Sie die full_turn-Methode für jeden Motor in einem separaten Thread
            futures = [executor.submit(motor.bring_to_relative_position, t, delay_ms) for motor in motors]

            # Warten Sie, bis alle Threads abgeschlossen sind
            concurrent.futures.wait(futures)

    @staticmethod
    def bring_to_relative_positions(motors, t:float, delay_ms:float=50):
        """
        Interpolate positions between MIN_TURN and MAX_TURN
        """
        # time_to_achieve = 10
        # delay_in_time = time_to_achieve/to_move

        if not (0 <= t <= 1):
            print("t must be in range 0 to 1 but is", t)
            return
        for motor in motors:
            position =(1 - t) * motor.MIN_TURN + t * motor.MAX_TURN
            to_move = int(position * TURN_TO_STEP - motor.step_count)
            motor.step(to_move, delay_ms)