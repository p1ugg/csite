$(function () {

  var mixer = mixitup('.directions__list');

  $('.directions__filter-btn').on('click', function () {
    $('.directions__filter-btn').removeClass('directions__filter-btn--active')
    $(this).addClass('directions__filter-btn--active')
  })

  $('.team__slider').slick({
    arrows: false,
    slidesToShow: 4,
    infinite: true,
    draggable: false,
    waitForAnimate: false,
    responsive:
      [
        {
          breakpoint: 1100,
          settings: {
            slidesToShow: 3,
          },
        },
        {
          breakpoint: 750,
          settings: {
            slidesToShow: 2,
          },
        },
        {
          breakpoint: 550,
          settings: {
            slidesToShow: 1,
            draggable: true,
          },
        },
      ]
  })
  $('.team__slider-prev').on('click', function (e) {
    e.preventDefault()
    $('.team__slider').slick('slickPrev')
  })
  $('.team__slider-next').on('click', function (e) {
    e.preventDefault()
    $('.team__slider').slick('slickNext')
  })

  $('.testimonials__slider').slick({
    arrows: false,
    dots: true,
    appendDots: $('.testimonials__dots'),
    waitForAnimate: false,
    // responsive:
    //   [
    //     {
    //       breakpoint: 700,
    //       settings: {

    //       },
    //     },
    //   ]
  })
  $('.testimonials__prev').on('click', function (e) {
    e.preventDefault()
    $('.testimonials__slider').slick('slickPrev')
  })
  $('.testimonials__next').on('click', function (e) {
    e.preventDefault()
    $('.testimonials__slider').slick('slickNext')
  })

  $('.program__acc-link').on('click', function (e) {
    e.preventDefault()
    if ($(this).hasClass('program__acc-link--active')) {
      $(this).removeClass('program__acc-link--active')
      $(this).children('.program__acc-text').slideUp()
    } else {
      $('.program__acc-link').removeClass('program__acc-link--active')
      $('.program__acc-text').slideUp()
      $(this).addClass('program__acc-link--active')
      $(this).children('.program__acc-text').slideDown()
    }
  })

  $(".header__nav-list a, .header__top-btn, .footer__go-top").on("click", function (e) {
    e.preventDefault();
    var id = $(this).attr('href');
    var top = $(id).offset().top;
    $('body, html').animate({ scrollTop: top }, 800);
});


  setInterval(() => {
    if ($(window).scrollTop() > 0 && $('.header__top').hasClass('header__top--open') === false) {
      $('.burger').addClass('burger--follow')
    } else {
      $('.burger').removeClass('burger--follow')
    }
  }, 0)
  $('.burger, .overlay, .header__top a').on('click', function (e) {
    e.preventDefault()
    $('.header__top').toggleClass('header__top--open')
    $('.overlay').toggleClass('overlay--show')
  })

  $('.footer__top-title--slide').on('click', function () {
    $(this).next().slideToggle()
  })
})

// Открыть модальное окно
document.querySelectorAll(".btn_buy").forEach(button => {
  button.addEventListener("click", function() {
    const modalId = this.getAttribute("data-modal");
    document.getElementById(modalId).classList.add("open");
  });
});

// Закрыть модальное окно
document.querySelectorAll(".modal__close-btn").forEach(button => {
  button.addEventListener("click", function() {
    this.closest(".modal").classList.remove("open");
  });
});


// Закрыть модальное окно при нажатии на Esc
window.addEventListener('keydown', (e) => {
  if (e.key === "Escape") {
    document.querySelectorAll(".modal.open").forEach(modal => {
      modal.classList.remove("open");
    });
  }
});

// Закрыть модальное окно при клике вне его
document.querySelectorAll(".modal").forEach(modal => {
  modal.querySelector(".modal__box").addEventListener('click', event => {
    event._isClickWithinModal = true;
  });

  modal.addEventListener('click', event => {
    if (event._isClickWithinModal) return;
    event.currentTarget.classList.remove('open');
  });
});


document.addEventListener('DOMContentLoaded', (event) => {
  const textElement = document.querySelector('.typing__text');
  const text = "У нас самое доступное обучение! \n               Курсы подойдут новичкам и профессионалам! \n                              Понятным языком поможем освоить самые разные профессии от бариста до менеджера по продажам.\n                                              Наши клиенты уверенно проходят собеседования и раскрываются в новой профессии!";
  let index = 0;

  function type() {
      if (index < text.length) {
          textElement.innerHTML += text.charAt(index);
          index++;
          setTimeout(type, 50); // Adjust speed here
      }
  }

  type();
});

function processPayment(courseId) {
  fetch('/process_payment', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({course_id: courseId})  // Отправляем идентификатор курса
  })
  .then(response => response.json())
  .then(data => {
      window.location.href = data.redirect_url;  // Перенаправляем пользователя на страницу оплаты
  });
};




