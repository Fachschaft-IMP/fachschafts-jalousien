document.addEventListener('DOMContentLoaded', function() {

            const slider = document.getElementById('sss');
            const lamellen = document.querySelectorAll('.lamelle');

            const initialPosition = lamellen[0].offsetTop;

            slider.addEventListener('input', function() {
                const value = slider.value;
                let i = 0;
                for (const lamelle of lamellen) {
                    lamelle.style.top = initialPosition + (value - slider.min) * (i * lamelle.offsetHeight * 0.9) / (slider.max - slider.min) + 'px';
                    i++;
                }
            });
        });

// // document.addEventListener('DOMContentLoaded', function() {
// //     const slider = document.getElementById('sss');
// //     const lamellen = document.querySelectorAll('.lamelle');

// //     const initialPosition = lamellen[0].offsetTop;


// //     slider.addEventListener('input', function() {
// //         const value = slider.value;
// //         let i = 0;
// //         for (const lamelle of lamellen) {
// //             lamelle.style.top = initialosition + (value - slider.min) * (i * lamelle.offsetHeight*0.8) / (slider.max - slider.min) + 'px';
// //             i++;
// //             console.log("test");
// //         }
// //     });
// // });

// const slider = document.getElementById('sss');
// const lamellen = document.querySelectorAll('.lamelle');

// const initialPosition = lamellen[0].offsetTop;


// slider.addEventListener('input', function() {
//     const value = slider.value;
//     let i = 0;
//     for (const lamelle of lamellen) {
//         lamelle.style.top = initialosition + (value - slider.min) * (i * lamelle.offsetHeight*0.8) / (slider.max - slider.min) + 'px';
//         i++;
//         console.log("test");
//     }
// });