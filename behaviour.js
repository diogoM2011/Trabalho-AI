const LoseYourself = document.getElementById("LoseYourself")
var music = document.getElementById("LoseYourselfMusic")

LoseYourself.addEventListener("mouseenter", function() {
    music.play();
    LoseYourself.style.color = "red";
});

LoseYourself.addEventListener("mouseleave", function(){
    music.pause();
    music.currentTime = 0;
    LoseYourself.style.color = "";
});

music.addEventListener("canplay", function(){
    console.log("Audio Loaded")
});

music.addEventListener("error", function(){
    console.log("Audio was not loaded and gave an error")
});