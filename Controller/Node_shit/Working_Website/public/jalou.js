function setVolume(id) {
    let volume = document.getElementById(id).value;

    fetch('/set-volume', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        id: id,
        volume: volume,
    }),
    })
    .then(response => response.text())
    .then(data => console.log(data))
    .catch((error) => {
    console.error('Error:', error);
    });
};

function changeSlider(id) {
    let volume = document.getElementById(id).value;

    let sliders = document.querySelectorAll('input[type="range"]');
    for (let i = 0; i < sliders.length-1; i++) {
        sliders[i].value = volume;
    }
}

function setMasterVolume(id) {
    let sliders = document.querySelectorAll('input[type="range"]')

    for (let slider of sliders) {
        let id = slider.id;
        let volume = slider.value;
     
        fetch('/set-volume', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                id: id,
                volume: volume,
            }),
        })
        .then(response => response.text())
        .then(data => console.log(data))
        .catch((error) => {
            console.error('Error:', error);
        });
     }
}

window.onload = function() {
    fetch('/get-volume')
    .then(response => response.json())
    .then(data => {
        for (let key in data) {
            if (data.hasOwnProperty(key)) {
                console.log(key)
                document.getElementById(key).value = data[key];
            }
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
};