from machine import Pin
import time

FULL_TURN = 200

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

    def turn_on_motor(self):
        self.en_pin.low()

    def turn_off_motor(self):
        self.en_pin.high() 

    # def switch_dir(self, dir:int):
    #     self.dir_pin.value(dir)

    def step(self, steps:int, delay_ms:float):
        iterator = 1
        # getting index of step_pin in Step_pins array
        # decide direction
        if steps > 0:
            self.dir_pin.high()
            iterator = 1
        else:
            self.dir_pin.low()
            iterator = -1

        # enable Motor
        self.turn_on_motor()
        for i in range(int(abs(steps))):
            self.step_pin.high()
            time.sleep_ms(delay_ms)
            self.step_pin.low()
            time.sleep_ms(delay_ms)
            self.step_count += iterator

            if self.step_count / FULL_TURN >= self.MAX_TURN or self.step_count <= self.MIN_TURN:
                return

        # disable motor
        self.turn_off_motor()

    def full_turn(self, turns:float, delay_ms:float):
        iterator = 1
        # getting index of step_pin in Step_pins array
        # decide direction
        if turns > 0:
            self.dir_pin.high()
            iterator = 1
        else:
            self.dir_pin.low()
            iterator = -1

        # enable Motor
        self.turn_on_motor()
        for i in range(int(abs(turns * FULL_TURN))):
            self.step_pin.high()
            time.sleep_ms(delay_ms)
            self.step_pin.low()
            time.sleep_ms(delay_ms)
            self.step_count += iterator

            if self.step_count / FULL_TURN >= self.MAX_TURN or self.step_count <= self.MIN_TURN:
                return

        # disable motor
        self.turn_off_motor()


    def interpolate(self, t:float):
        if t not in range(0,1):
            return

        position =(1 - t) * self.MIN_TURN + t * self.MAX_TURN
        to_move = int(position * FULL_TURN - self.step_count)
        self.step(to_move, 1)