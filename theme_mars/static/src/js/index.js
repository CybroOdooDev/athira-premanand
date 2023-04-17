odoo.define('theme_mars.index', function(require){
    'use strict';
       $(".owl-carousel1").owlCarousel(
                {
                    // animateOut: 'slideOutDown',
                    // animateIn: 'flipinx',
                    items: 1,
                    loop: true,
                    margin: 0,
                    stagePadding: 0,
                    smartSpeed: 450,
                    autoplay: false,
                    autoPlaySpeed: 1000,
                    autoPlayTimeout: 1000,
                    autoplayHoverPause: true,
                    //   onInitialized: counter,
                    dots: true,
                    nav: false,
                    //   navText: ['<div class="pre"><i class="material-icons" style="font-size:36px">keyboard_arrow_left</i></div>', '<div class="nxt"><i class="material-icons" style="font-size:36px">keyboard_arrow_right</i></div>'],
                    animateOut: 'fadeOut'
                }
            );

});