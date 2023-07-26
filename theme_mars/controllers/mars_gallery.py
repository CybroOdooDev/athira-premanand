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
from odoo import http
from odoo.http import request


class PageGallery(http.Controller):
    """Controller for the page gallery."""
    @http.route('/gallery', type='http', auth='public', website=True,
                sitemap=False)
    def gallery(self):
        """Render the gallery page.Fetches the image data from the backend. """
        images = request.env['mars.gallery'].search([])
        vals = {
            'result': images,
        }
        return request.render("theme_mars.page_gallery", vals)


class GalleryCategory(http.Controller):
    """Controller for gallery categories."""
    @http.route('/gallery/category/<string:category>', type='http',
                auth='public', website=True,
                sitemap=False)
    def category(self, category=None):
        """Render the gallery category page.
           Categorizes images based on the specified category."""
        image = request.env['mars.gallery'].search(
            [('image_category_id.category', '=', category)])
        val = {
            'result': image,
        }
        return request.render("theme_mars.category_gallery", val)
