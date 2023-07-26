odoo.define('theme_mars.index', function(require){
    'use strict';
    $(document).ready(function() {
        // Carousel for slider
        var owl = $('.owl-theme');
            $(".owl-theme").owlCarousel(
                {
                    items: 1,
                    loop: true,
                    margin: 0,
                    stagePadding: 0,
                    smartSpeed: 450,
                    autoplay: false,
                    autoPlaySpeed: 1000,
                    autoPlayTimeout: 1000,
                    autoplayHoverPause: true,
                    dots: true,
                    nav: true,
                    navText: ['<div class="pre"><i class="material-icons" style="font-size:36px">keyboard_arrow_left</i></div>', '<div class="nxt"><i class="material-icons" style="font-size:36px">keyboard_arrow_right</i></div>'],
                }
            );
            function setAnimation(_elem, _InOut) {
                var animationEndEvent = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
                _elem.each(function () {
                    var $elem = $(this);
                    var $animationType = 'animated ' + $elem.data('animation-' + _InOut);
                    $elem.addClass($animationType).one(animationEndEvent, function () {
                        $elem.removeClass($animationType); // remove animate.css Class at the end of the animations
                    });
                });
            }
            // Fired before current slide change
            owl.on('change.owl.carousel', function (event) {
                var $currentItem = $('.owl-item', owl).eq(event.item.index);
                var $elemsToanim = $currentItem.find("[data-animation-out]");
                setAnimation($elemsToanim, 'out');
            });
            // Fired after current slide has been changed
            owl.on('changed.owl.carousel', function (event) {
                var $currentItem = $('.owl-item', owl).eq(event.item.index);
                var $elemsToanim = $currentItem.find("[data-animation-in]");
                setAnimation($elemsToanim, 'in');
            })
            $('.owl-theme2').owlCarousel({
                loop: true,
                margin: 0,
                dots: true,
                items: 1,
                nav: true,
                mouseDrag: true,
                autoplay: true,
                navSpeed: 1000,
            });
            $('#owl-theme3').owlCarousel({
                loop: true,
                margin: 0,
                dots: true,
                items: 1,
                nav: true,
                mouseDrag: false,
                autoplay: false,
                navSpeed: 1000,
            });
            $(".owl-carousel").owlCarousel(
                {
                    items: 4,
                    loop: true,
                    margin: 0,
                    stagePadding: 0,
                    smartSpeed: 450,
                    autoplay: false,
                    autoPlaySpeed: 1000,
                    autoPlayTimeout: 1000,
                    autoplayHoverPause: true,
                    dots: true,
                    nav: false,
                    animateOut: 'fadeOut'
                }
            );
            var delay = 500;
     });
});
