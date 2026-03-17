document.addEventListener("DOMContentLoaded", function () {

    const audios = document.querySelectorAll("audio.fc-media");

    audios.forEach(function (audio, index) {

        audio.addEventListener("play", function () {

            audios.forEach(function (a, i) {
                if (i !== index) {
                    a.pause();
                }
            });

        });

        audio.addEventListener("ended", function () {

            if (index + 1 < audios.length) {
                audios[index + 1].currentTime = 0;
                audios[index + 1].play();
            }

        });

    });

});

const songs = document.querySelectorAll(".fc-media");

songs.forEach((song, index) => {

    song.addEventListener("ended", function(){

        let nextSong = songs[index + 1];

        if(nextSong){
            nextSong.play();
        }else{
            songs[0].play(); // restart playlist
        }

    });

});

let queue = [];
let currentIndex = 0;

const audio = document.getElementById("mainAudio");

function playSong(url, title, artist, image){

    if(!url){
        alert("No preview available");
        return;
    }

    // Add to queue
    queue.push({url, title, artist, image});
    currentIndex = queue.length - 1;

    loadSong(queue[currentIndex]);
}

function loadSong(song){

    document.getElementById("playerTitle").innerText = song.title;
    document.getElementById("playerArtist").innerText = song.artist;
    document.getElementById("playerImage").src = song.image;

    audio.src = song.url;
    audio.play();
}

// Auto next song
audio.addEventListener("ended", function(){

    currentIndex++;

    if(currentIndex < queue.length){
        loadSong(queue[currentIndex]);
    }else{
        currentIndex = 0; // loop queue
        loadSong(queue[currentIndex]);
    }

});