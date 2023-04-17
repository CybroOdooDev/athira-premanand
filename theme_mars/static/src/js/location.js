odoo.define('theme_mars.blogs', function(require){
    'use strict';

    var publicWidget = require('web.public.widget');
    var ajax = require('web.ajax');
    var core = require('web.core')
    var QWeb = core.qweb

    publicWidget.registry.get_blog_post = publicWidget.Widget.extend({
        xmlDependencies: ['theme_mars/static/src/xml/blog.xml'],
        selector : '.blog_mars',
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
        getBackground: function(data){
            data = JSON.parse(data)
            return data['background-image']
        },
        changeDateFormat: function(data){
            var formattedDate = moment(new Date(data)).format('MMM DD YYYY')
            return formattedDate
        }
    });
});