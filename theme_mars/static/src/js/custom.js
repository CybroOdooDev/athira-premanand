odoo.define('theme_mars.theme_mars', function (require) {
	"use strict";
	var ajax = require('web.ajax');
    var $window = $('#wrapwrap');
    var publicWidget = require('web.public.widget');
// define widget for pie chart
    publicWidget.registry.Mars_PIEChart = publicWidget.Widget.extend({
        selector: '.pie_chart',
        start: function() {
            this. _chart()
        },
        /* chart
        ================================================== */
         _chart: function()
        {
            $('.b-skills').appear(function() {
                setTimeout(function() {
                    $('.charts').easyPieChart({
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
        }
    })
    function run()
    {
        var fName = arguments[0],
            aArgs = Array.prototype.slice.call(arguments, 1);
        try {
            fName.apply('#wrapwrap', aArgs);
        } catch(err) {
        }
    };
// define widget for barchart
    publicWidget.registry.Mars_BARChart = publicWidget.Widget.extend({
    selector: '.progress_wrapp',
        start: function() {
        this._chartbar()
        },
    _chartbar: function() {
        /* Progress Bar */
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
    },
    })
// define widget for load contents
publicWidget.registry.Load_content = publicWidget.Widget.extend({
    selector: '.product_grid_load_more',
        start: function() {
        this._loadmore()
        },
        _loadmore: function() {
              $(".results-container__title_shop").slice(0, 3).show();
              $("#loadMore").on("click", function(e){
                e.preventDefault();
                $(".results-container__title_shop:hidden").slice(0, 3).slideDown();
                if($(".results-container__title_shop:hidden").length == 0) {
                    $("#loadMore").hide();
                    $('.hidden-pager').show();
                }
          });
          //        Shop Page Image
       $('.mars_oe_product_image').mouseover(function(){
            if ($(this).find('.mars_alternate_img').length > 0){
              $(this).find('.mars_alternate_img').removeClass('d-none')
              $(this).find('.mars_alternate_img').show()
              $(this).find('.mars_default_img').hide()
              $(this).addClass('img_wrapper')
              }
        })
        $('.mars_oe_product_image').mouseleave(function(){
              $(this).find('.mars_alternate_img').hide()
              $(this).find('.mars_default_img').show()
              $(this).removeClass('img_wrapper')
        })
        // load restricted number of images
           $(".load_more_images").slice(0, 4).show();
              $("#loadGallery").on("click", function(){
              //load remaining images
                       $(".load_more_images:hidden").slice(0,4).slideDown()
                if($(".load_more_images :hidden").length == 0) {
                    $("#loadGallery").hide();
                }
          });
        }
    });
// function define visible
 function checkVisible( elm, evalType ) {
       evalType = evalType || "visible";
       var vpH = $('#wrapwrap').height(), // Viewport Height
           st = $('#wrapwrap').scrollTop(), // Scroll Top
           y = $(elm).offset().top,
           elementHeight = $(elm).height();
       if (evalType === "visible") return ((y < (vpH + st)) && (y > (st - elementHeight)));
       if (evalType === "above") return ((y < (vpH + st)));
   }
   // define widget for infinity scroll
publicWidget.registry.infinity_scroll = publicWidget.Widget.extend({
     selector: '.infinite_scroll',
        start: function() {
        this._infinityScroll()
        },
        _infinityScroll: function(){
         // This needs a debounce method added to improve performance
   $('.o_wsale_products_page').on("scroll mousemove", function(){
     // Check if the user at the bottom of the content block/list
     if(checkVisible("#footer")){
       //This is where you would make a request for new content
       $(".infinite_scroll").append($(".image").clone())
   }
   })
  $('.o_mars_gallery_page1').on("scroll mousemove", function(){
     // Check if the user at the bottom of the content block/list
     if(checkVisible("#footer")){
      //This is where you would make a request for new content
         $(".infinite_scroll").append($(".infinity_image").clone())
     }
   })
        }
});
// Define product rating widget
publicWidget.registry.ProductRating = publicWidget.Widget.extend({
    selector: '.single_product',
    events: {
        'click #rate_us_single_product': 'RateUs',
        'click .rate': 'RateClick',
        'click #submit_my_review': 'ReviewSubmit',
    },
        start: function() {
            this.mouseoverleave();
        },
   //        Single Product Review and Submit
        RateUs: function(){
            $('.rate_this_prod').hasClass('mars_hide') ? $('.rate_this_prod').removeClass('mars_hide') : $('.rate_this_prod').addClass('mars_hide')
        },
        mouseoverleave: function() {
            $(document).on({
                    mouseover: function(event) {
                        $(this).find('.far').addClass('star-over');
                        $(this).prevAll().find('.far').addClass('star-over');
                    },
                    mouseleave: function(event) {
                        $(this).find('.far').removeClass('star-over');
                        $(this).prevAll().find('.far').removeClass('star-over');
                    }
            }, '.rate');
        },
        RateClick: function() {
            if ( !$(this).find('.star').hasClass('rate-active') ) {
                $(this).siblings().find('.star').addClass('far').removeClass('fas rate-active');
                $(this).find('.star').addClass('rate-active fas').removeClass('far star-over');
                $(this).prevAll().find('.star').addClass('fas').removeClass('far star-over');
            }
        },
        ReviewSubmit: function() {
            var stars = $('.rate_this_prod').find('.star')
            var count = 0
            var rating = 0
            stars.each(function(i,star){
                count += 1
                if( $(star).hasClass('rate-active') ){
                    rating = count
                }
            })
            var message = $('#w3review').val()
            var res_id = $('#res_id').val()
            var res_name = $('#res_code').val() == undefined ? '' + $('#res_name').val() : $('res_code').val() + $('#res_name').val()
            var partner_id = $('#partner_id').val()
            var params = {
                'message': message,
                'res_id':parseInt(res_id),
                'res_name':res_name,
                'partner_id': parseInt(partner_id),
                'rating_count': rating
            }
            ajax.jsonRpc('/add/my/review', 'call',params, )
            .then(function (data) {
                    $( "#review_comments" ).load(window.location.href + " #review_comments" );
            });
        },
});
 // widget for loading heading in portfolio page
publicWidget.registry.portfolio_heading = publicWidget.Widget.extend({
    selector: '.o_mars_portfolio_page',
         events: {
            'click .filter-button': 'filterButton',
         },
         filterButton: function(e){
            var data_id = Object.values(e.target.dataset)[0]
            var div_id = document.getElementById(data_id)
            document.getElementById('load_modal').style.display = "flex"
              if (div_id){
                document.getElementById("all_heading").style.display = "none"
                document.getElementById("all-heading").classList.remove('active');
                 for (var element = 0; element < document.getElementsByClassName('main-portfolio').length; element++) {
                    if(data_id == document.getElementsByClassName('main-portfolio')[element].id){
                        document.getElementsByClassName('main-portfolio')[element].style.display = "flex"
                    }else{
                        document.getElementsByClassName('main-portfolio')[element].style.display = "none"
                    }
                 }
                 for (var element = 0; element < document.getElementsByClassName('filter-button').length; element++) {
                    if(data_id == document.getElementsByClassName('filter-button')[element].id){
                        document.getElementsByClassName('filter-button')[element].classList.add('active');
                    }else{
                        document.getElementsByClassName('filter-button')[element].classList.remove('active');
                    }
                 }
              } else {
                document.getElementById('load_modal').style.display = "none"
                document.getElementById("all_heading").style.display = "flex"
                document.getElementById("all-heading").classList.add('active');
                for (var element = 0; element < document.getElementsByClassName('filter-button').length; element++) {
                    if (document.getElementsByClassName('filter-button')[element].id != "all-heading"){
                        document.getElementsByClassName('filter-button')[element].classList.remove('active');
                    }
                }
              }
         },
         start: function() {
            this._Portfolio()
         },
         _Portfolio: function(e){
                this.$el.find('.load_modal').hide();
                this.$el.find('.all_heading').hide();
                 var main_div = document.getElementsByClassName('main-portfolio')
            $(main_div).each(function(div){
                main_div[div].style.display = "none"
            })
             var main = document.getElementsByClassName('main')
             $(main_div).each(function(div){
                main_div[div].style.display = "flex"
            })
            if(document.getElementById("all-heading")){
                document.getElementById("all-heading").classList.add('active');
            }
         }
         });
});
