window.onload = function(){
    var slider = document.getElementById("sss");
     var  result = document.getElementById("final");
    slider.oninput = function(){
        result.innerHTML = slider.value;
        var sliderValue = slider.value;
        sendSliderValue();
        console.log(sliderValue);
    }
    }

function sendSliderValue() {
    var sliderValue = document.getElementById("sss").value;

    // Erstellen Sie eine HTTP-Anfrage an den MicroPython-Server
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/set_slider_value?value=" + sliderValue, true);
    xhr.send();
}