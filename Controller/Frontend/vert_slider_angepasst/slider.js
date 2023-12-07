const slider = document.getElementById('jalou-slider1');
const lamellen = document.querySelectorAll('.lamelle');

const initialPosition = lamellen[0].offsetTop;

slider.addEventListener('input', function() {
    const value = slider.value;
    let i = 0;
    for (const lamelle of lamellen) {
        // lamelle.style.top = initialPosition + (value - slider.min) * (i * lamelle.offsetHeight * 0.8) / (slider.max - slider.min) + 'px';
        lamelle.style.top = initialPosition + value * (100 / lamellen.length * i) + '%';
        i++;
    }
});