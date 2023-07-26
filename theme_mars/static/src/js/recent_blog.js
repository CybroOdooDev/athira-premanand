odoo.define('theme_mars.blogs', function(require){
    'use strict';
    // Import required modules
    var publicWidget = require('web.public.widget');
    var ajax = require('web.ajax');
    var core = require('web.core')
    var QWeb = core.qweb
    // Define widget to get blog posts
    publicWidget.registry.get_blog_post = publicWidget.Widget.extend({
        xmlDependencies: ['theme_mars/static/src/xml/blogs.xml'],
        selector : '.blog_mars',
        /**
         * Function called when the widget is started.
         * Sends an AJAX request to retrieve recent blog posts
         * and renders them on the page.
         */
        start: function(){
            ajax.jsonRpc('/get_blog_post', 'call', {})
            .then((data) => {
              this.$el.html(QWeb.render('mars_blogs', {
                posts_recent: data.posts_recent,
                getBackground: this.getBackground,
                changeDateFormat: this.changeDateFormat
              }))
            });
        },
        /**
         * Function to retrieve the background image for a blog post.
         * @param {string} data - JSON string containing the post data.
         * @returns {string} - URL of the background image.
         */
        getBackground: function(data){
            data = JSON.parse(data)
            return data['background-image']
        },
        /**
         * Function to format the date of a blog post.
         * @param {string} data - Date string in ISO format.
         * @returns {string} - Formatted date string (e.g. "May 11 2023").
         */
        changeDateFormat: function(data){
            var formattedDate = moment(new Date(data)).format('MMM DD YYYY')
            return formattedDate
        }
    });
});
