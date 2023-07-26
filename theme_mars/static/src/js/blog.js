odoo.define('backend_theme_infinito_plus.resize', function(require){
    'use strict';
    // import required modules
    var publicWidget = require('web.public.widget');
    var ajax = require('web.ajax');
    var core = require('web.core')
    var QWeb = core.qweb
    // define widget for getting a single blog post
    publicWidget.registry.get_blog_post = publicWidget.Widget.extend({
        // specify the xml dependencies required for the widget
        xmlDependencies: ['theme_diva/static/src/xml/index3_blog.xml'],
        // specify the selector for the HTML element where the widget will be applied
        selector : '.blog_index',
        start: function(){
            // make an Ajax call to get the blog post data
            ajax.jsonRpc('/get_blog_post', 'call', {})
            .then((data) => {
              // render the blog post data using a QWeb template
              this.$el.html(QWeb.render('diva_index3_blog', {
                posts_recent: data.posts_recent,
                getBackground: this.getBackground,
                changeDateFormat: this.changeDateFormat
              }))
            });
        },
        // function to extract the background image URL from the data object
        getBackground: function(data){
            data = JSON.parse(data)
            return data['background-image']
        },
        // function to format the date in the data object
        changeDateFormat: function(data){
            var formattedDate = moment(new Date(data)).format('MMM DD YYYY')
            return formattedDate
        }
    });
    // define widget for getting multiple blog posts
    publicWidget.registry.get_blog_posts = publicWidget.Widget.extend({
        // specify the xml dependencies required for the widget
        xmlDependencies: ['theme_diva/static/src/xml/index2_blog.xml'],
        // specify the selector for the HTML element where the widget will be applied
        selector : '.blog_2',
        start: function(){
            var self = this;
            // make an Ajax call to get the blog post data
            ajax.jsonRpc('/get_blog_posts', 'call', {})
            .then((data) => {
              // render the blog post data using a QWeb template
              this.$el.html(QWeb.render('diva_index2_blog', {
                posts_recent: data.posts_recent,
                getBackground: this.getBackground,
                changeDateFormat: this.changeDateFormat
              }))
            });
        },
        // function to extract the background image URL from the data object
        getBackground: function(data){
            data = JSON.parse(data)
            return data['background-image']
        },
        // function to format the date in the data object
        changeDateFormat: function(data){
            var formattedDate = moment(new Date(data)).format('MMM DD YYYY')
            return formattedDate
        }
    });
});
