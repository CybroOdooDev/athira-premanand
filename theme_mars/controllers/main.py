from odoo import fields, http
from odoo.http import request, route
from odoo.addons.website_blog.controllers.main import WebsiteBlog
from odoo.addons.website.controllers.main import Home



class BlogSidebar(WebsiteBlog):
    @route()
    def blog_post(self, blog, blog_post, tag_id=None, page=1, enable_editor=None, **post):
        res = super(BlogSidebar, self).blog_post(blog, blog_post, tag_id=None, page=1, enable_editor=None, **post)
        posts_recent = request.env['blog.post'].sudo().search(
            [('website_published', '=', True),
             ('post_date', '<=', fields.Datetime.now())],
            order='published_date desc', limit=3)
        print("qwerty", posts_recent)

        website_id = request.website.id
        posts_featured = request.env['website'].sudo().search(
            [('id', '=', website_id)])
        print("posts_featured", posts_featured)
        posts_popular = request.env['website'].sudo().search(
            [('id', '=', website_id)])
        print("posts_popular", posts_popular)
        print(website_id, "website id")
        res.qcontext.update({
            'posts_recent': posts_recent,
            'posts_featured': posts_featured,
            'posts_popular': posts_popular,
        })
        return res


class WebsiteBlog(http.Controller):
    @http.route('/get_blog_post', auth="public", type='json', website=True)
    def get_blog_post(self):
        blogs_recent = request.env['blog.post'].sudo().search(
            [('website_published', '=', True),
             ('post_date', '<=', fields.Datetime.now())],
            order='published_date desc', limit=3)
        print("poosts", blogs_recent)
        values = {
            'posts_recent': blogs_recent.read(['name', 'published_date', 'blog_id', 'tag_ids', 'teaser', 'cover_properties']),
        }
        return values
