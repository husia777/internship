// Скрипт не начнет выполняться пока не загрузится DOM-дерево
window.addEventListener('DOMContentLoaded', () => {
    // Конвертирует список в массив, чтобы получить доступ к методам класса Array
    const slides = [...document.querySelectorAll('.currencies-section__currencies-slide')]
    const rightArrowButton = document.getElementById('rightArrowButton')
    const leftArrowButton = document.getElementById('leftArrowButton')

    rightArrowButton.addEventListener('click', goToNextSlide)
    leftArrowButton.addEventListener('click', goToPreviousSlide)

    // Получает индекс текущего слайда и, если он не последний, скрывает этот и показывает следующий слайд
    function goToNextSlide() {
        const currentSlide = slides.filter(slide => !slide.hidden)[0]
        const currentSlideIndex = slides.indexOf(currentSlide)
        if(currentSlideIndex < slides.length - 1) {
            currentSlide.hidden = true
            slides[currentSlideIndex + 1].hidden = false
        }
    }

    // Получает индекс текущего слайда и, если он не первый, скрывает этот и показывает предыдущий слайд
    function goToPreviousSlide() {
        const currentSlide = slides.filter(slide => !slide.hidden)[0]
        const currentSlideIndex = slides.indexOf(currentSlide)

        if(currentSlideIndex > 0) {
            currentSlide.hidden = true
            slides[currentSlideIndex - 1].hidden = false
        }
    }
})
fetch(`http://127.0.0.1/calculate/data?hash-rate=${hashRate}&unit=${unit}`)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));