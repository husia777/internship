// Скрипт не начнет выполняться пока не загрузится DOM-дерево
window.addEventListener('DOMContentLoaded', () => {
    const currenciesTableBody = document.querySelector('.dinamic__courses tbody')
    currenciesTableBody.replaceWith(...currenciesTableBody.childNodes)
    
    Chart.defaults.color = 'white'
    Chart.defaults.font.family = 'Rubik'
    const meritChartCanvas = document.getElementById('meritChart')

    new Chart(meritChartCanvas, {
        type: 'bar',
        data: {
            labels: [ 'Label 1', 'Label 2', 'Label 3', 'Label 4' ], // Надписи для столбов графика
            datasets: [{
                label: 'Data',
                data: [ 10, 20, 10, 50, ], // Данные для графика
            }]
        },
        options: {
            responsive: true, // Делает график адаптивным относительно родителя

            plugins: {
                legend: {
                    labels: {
                        font: {
                            size: 18,
                        }
                    }
                },
            },

            scales: {
                y: {
                    beginAtZero: true
                }
            },

            elements: {
                bar: {
                    backgroundColor: '#2b67ffc9'
                }
            }
        },
    })


    // Получает все слайдеры
    const sliders = document.querySelectorAll('.slider')

    sliders.forEach(slider => {
        initializeSlider(slider)
    })
})

function initializeSlider(slider) {
    const sliderName = slider.getAttribute('data-slider-name')

    const sliderArrows = slider.querySelector(`.${sliderName}__navigation-arrows`)
    const rightArrowButton = sliderArrows.querySelector('.right-arrow-button')
    const leftArrowButton = sliderArrows.querySelector('.left-arrow-button')
    rightArrowButton.addEventListener('click', goToNextSlide)
    leftArrowButton.addEventListener('click', goToPreviousSlide)

    const slidesTagName = slider.getAttribute('data-slides-tag-name') || 'div'
    const slideElementsCount = slider.getAttribute('data-slide-elements-count')
    const sliderElements = [...slider.querySelectorAll(`.${sliderName}__element`)]
    const slides = [ createNewSlide() ] // Создает массив слайдов с одним начальным слайдом

    sliderElements.forEach(element => {
        // Удаляет элементы из DOM-дерева, чтобы потом поместить в отдельный слайд
        element.remove()
        const lastSlide = slides[slides.length - 1]

        // Если слайд уже заполнен указанным числом элементов - создает новый
        if (lastSlide.children.length == slideElementsCount) {
            const newSlide = createNewSlide()
            newSlide.hidden = true
            newSlide.insertAdjacentElement('beforeend', element)
            slides.push(newSlide)
        }
        else {
            lastSlide.insertAdjacentElement('beforeend', element)
        }
    })

    // Вставляет слайдеры в DOM-дерево
    const nearElement = document.querySelector(`.${sliderName}__near-element`)
    slides.forEach(slide => {
        if(nearElement != null) {
            nearElement.insertAdjacentElement('beforebegin', slide)
        }
        else {
            sliderArrows.insertAdjacentElement('beforebegin', slide)
        }
    })


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

    function createNewSlide() {
        const newSlide = document.createElement(slidesTagName)
        newSlide.classList.add(`${sliderName}__slide`)
    
        return newSlide
    }
}