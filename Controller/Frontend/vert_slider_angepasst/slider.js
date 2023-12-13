const slider1 = document.getElementById('jalou-slider1');
const slider2 = document.getElementById('jalou-slider2');
const slider3 = document.getElementById('jalou-slider3');
const slider4 = document.getElementById('jalou-slider4');
const slider5 = document.getElementById('jalou-slider5');

const master = document.getElementById('master-slider');

const lamellen = document.querySelectorAll('.lamelle');
const lamPair = lamellen.length/5

const initialPosition = lamellen[0].offsetTop;

slider1.addEventListener('input', function() {
    const value = slider1.value;
    let i = 0;
    for(let j=0; j< lamPair; j++){
        lamellen[j].style.top = initialPosition + value * (100 / lamPair * j) + '%';
    }
});

slider2.addEventListener('input', function() {
    const value = slider2.value;
    let i = 0;
    for(let j=0; j< lamPair; j++){
        lamellen[j+lamPair].style.top = initialPosition + value * (100 / lamPair * j) + '%';
    }
});

slider3.addEventListener('input', function() {
    const value = slider3.value;
    let i = 0;
    for(let j=0; j< lamPair; j++){
        lamellen[j+2*lamPair].style.top = initialPosition + value * (100 / lamPair * j) + '%';
    }
});

slider4.addEventListener('input', function() {
    const value = slider4.value;
    let i = 0;
    for(let j=0; j< lamPair; j++){
        lamellen[j+3*lamPair].style.top = initialPosition + value * (100 / lamPair * j) + '%';
    }
});

slider5.addEventListener('input', function() {
    const value = slider5.value;
    let i = 0;
    for(let j=0; j< lamPair; j++){
        lamellen[j+4*lamPair].style.top = initialPosition + value * (100 / lamPair * j) + '%';
    }
});


master.addEventListener('input', function() {
    const value = master.value;
    slider1.value = value;
    slider2.value = value;
    slider3.value = value;
    slider4.value = value;
    slider5.value = value;

    for (let window = 0; window < 5; window++) {
        for (let lamelle = 0; lamelle < 16; lamelle++) {
            lamellen[window*16 + lamelle].style.top = initialPosition + value * (100 / 16 * lamelle) + '%';
        }
    }
});