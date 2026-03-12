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