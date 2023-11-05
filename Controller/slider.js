window.onload = function(){
    var slider = document.getElementById("sss");
     var  result = document.getElementById("final");
    slider.oninput = function(){
        result.innerHTML = slider.value;
        var sliderValue = slider.value;
        console.log(sliderValue);
    }
    }