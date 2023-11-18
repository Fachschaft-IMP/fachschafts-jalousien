// Post the slider value to Server
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

// Changes slider value of slider 1 to 5 when master slider is used
function changeSlider(id) {
    let volume = document.getElementById(id).value;

    let sliders = document.querySelectorAll('input[type="range"]');
    sliders = Array.from(sliders).filter(slider => slider.id !== 'master-slider');
    for (let i = 0; i < sliders.length; i++) {
        sliders[i].value = volume;
    }
}

// function setMasterVolume(id) {
//     let sliders = document.querySelectorAll('input[type="range"]')

//     for (let slider of sliders) {
//         let id = slider.id;
//         let volume = slider.value;
     
//         fetch('/set-volume', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({
//                 id: id,
//                 volume: volume,
//             }),
//         })
//         .catch((error) => {
//             console.error('Error:', error);
//         });
//      }
// }

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