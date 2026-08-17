document$.subscribe(async () => {
    const spoiler = document.querySelector('.spoiler');

    spoiler.addEventListener('click', function() {
        spoiler.classList.toggle('clicked');
    })
})