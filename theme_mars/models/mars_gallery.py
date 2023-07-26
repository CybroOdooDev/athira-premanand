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
from odoo import models, fields


class MarsGallery(models.Model):
    """Model for storing images in a gallery."""
    _name = "mars.gallery"
    _description = "Mars Gallery"
    _rec_name = "image_gallery"

    image_gallery = fields.Image(string="Image", help="Upload images")
    image_category_id = fields.Many2one('gallery.category', string="Category",
                                        help="Select category for the image")


class GalleryCategory(models.Model):
    """Model for storing categories for images in a gallery."""
    _name = "gallery.category"
    _description = "Gallery Category"
    _rec_name = "category"

    category = fields.Char(string="Category",
                           help="Create different Categories")
