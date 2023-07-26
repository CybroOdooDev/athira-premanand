# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo.addons.website_blog.controllers.main import WebsiteBlog
from odoo import fields, http
from odoo.http import request, route


class BlogSidebar(WebsiteBlog):
    """ Controller for the blog sidebar."""
    @route()
    def blog_post(self, blog, blog_post, tag_id=None, page=1,
                  enable_editor=None, **post):
        """ Handle the blog post route."""
        res = super(BlogSidebar, self).blog_post(blog, blog_post, tag_id=None,
                                                 page=1, enable_editor=None,
                                                 **post)
        posts_recent = request.env['blog.post'].sudo().search(
            [('website_published', '=', True),
             ('post_date', '<=', fields.Datetime.now())],
            order='published_date desc', limit=3)
        website_id = request.website.id
        posts_featured = request.env['website'].sudo().search(
            [('id', '=', website_id)])
        posts_popular = request.env['website'].sudo().search(
            [('id', '=', website_id)])
        res.qcontext.update({
            'posts_recent': posts_recent,
            'posts_featured': posts_featured,
            'posts_popular': posts_popular,
        })
        return res


class WebsiteBlog(http.Controller):
    """Controller for the website blog."""
    @http.route('/get_blog_post', auth="public", type='json', website=True)
    def get_blog_post(self):
        """ Get the blog posts."""
        blogs_recent = request.env['blog.post'].sudo().search(
            [('website_published', '=', True),
             ('post_date', '<=', fields.Datetime.now())],
            order='published_date desc', limit=3)
        values = {
            'posts_recent': blogs_recent.read(
                ['name', 'published_date', 'blog_id', 'tag_ids', 'teaser',
                 'cover_properties']),
        }
        return values
