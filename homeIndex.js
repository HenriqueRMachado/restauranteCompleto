function embedGlobalScope () {
    const getInfo = document.querySelector('.flex');
    getInfo.addEventListener('mouseon', (e) => {
        alert(123)
    })
}
embedGlobalScope()