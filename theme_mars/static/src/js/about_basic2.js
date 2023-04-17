odoo.define('theme_mars.theme_mars', function (require) {
	"use strict";

var $window = $('#wrapwrap');

function run()
{
    console.log("argument", arguments[0])
	var fName = arguments[0],
		aArgs = Array.prototype.slice.call(arguments, 1);
		    console.log("argument", aArgs)
	try {
		fName.apply('#wrapwrap', aArgs);
		 console.log("submit", aArgs)
	} catch(err) {
        console.log("error", err)
	}
};

/* chart
================================================== */
function _chart ()
{
	$('.b-skills').appear(function() {
		setTimeout(function() {
			$('.charts').easyPieChart({
//                         easing: 'easeOutElastic',
                         delay: 5000,
                         barColor: '#369670',
                         trackColor: '#f2f2f2',
                         scaleColor: false,
                         lineWidth: 5,
                         trackWidth: 5,
                         size: 100,
                         animate:3000,

                         lineCap: 'square',
                         onStep: function (from, to, percent) {
                             this.el.children[0].innerHTML = Math.round(percent);
                         }
                    });

		}, 100);
	});
};



$(document).ready(function() {
    console.log("_chart", _chart)
	run(_chart);


//});


//	$(document).ready(function () {
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
                    // onInitialized: counter,
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
//        });
        // function counter() {
        //   var buttons = $('.owl-dots button');
        //   buttons.each(function (index, item) {
        //     $(item).find('span').text(index + 1);
        //   });
        // }


//            $(document).ready(function () {
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
//        });


//        $(document).ready(function () {
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
//        });


//        $(document).ready(function () {
            $(".owl-carousel").owlCarousel(
                {
                    // animateOut: 'slideOutDown',
                    // animateIn: 'flipinx',
                    items: 4,
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


            var delay = 500;
        $(".progress-bar").each(function (i) {
            $(this).delay(delay * i).animate({ width: $(this).attr('aria-valuenow') + '%' }, delay);
            $(this).prop('Counter', 0).animate({
                Counter: $(this).text()
            }, {
                duration: delay,
                easing: 'swing',
                step: function (now) {
                    $(this).text(Math.ceil(now) + '%');
                }
            });
        });
    });

});