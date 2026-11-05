function SetupSongs(SongID, MusicID) {

    const song = document.getElementById(SongID);
    var music = document.getElementById(MusicID);

    song.addEventListener("mouseover", function(){
        music.play()

        song.style.color = "red";
        song.style.textTransform = "uppercase";
        song.style.fontWeight = "bold";
        song.style.fontFamily = "Barlow Condensed";
        song.style.fontSize = "30px";
    });

    song.addEventListener("mouseleave", function(){
        music.pause();
        music.currentTime = 0;

        song.style.color = "";
        song.style.textTransform = "";
        song.style.fontWeight = "";
        song.style.fontFamily = "";
        song.style.fontSize = "";
    });
}

SetupSongs("LoseYourself", "LoseYourselfMusic")
SetupSongs("Lucifer", "LuciferMusic")
SetupSongs("Mockingbird", "MockingbirdMusic")
SetupSongs("Mosh", "MoshMusic")
SetupSongs("RockBottom", "RockBottomMusic")
SetupSongs("RapGod", "RapGodMusic")
SetupSongs("RapGodT", "RapGodMusic")
SetupSongs("SquareDance", "SquareDanceMusic")
SetupSongs("TheRealSlimShady", "TheRealSlimShadyMusic")
SetupSongs("WeAsAmericans", "WeAsAmericansMusic")
SetupSongs("WithoutMe", "WithoutMeMusic")