document.addEventListener('DOMContentLoaded', function() {
    const slider = document.getElementById('slider');
    const lamellen = document.querySelectorAll('.lamell');

    slider.addEventListener('input', function() {
        const value = slider.value;
        let i = 0;
        for (const lamelle of lamellen) {
            lamelle.style.top = 50 + (value - slider.min) * (i * lamelle.offsetHeight*0.8) / (slider.max - slider.min) + 'px';
            i++;
        }
    });
});