document.addEventListener('DOMContentLoaded', function () {
    const audio = document.getElementById('musica');
    audio.addEventListener('seeked', () => {
        console.log('Música pulada para: ', audio.currentTime);
    });
});