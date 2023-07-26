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
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Website(models.Model):
    """ Represents the Website model in Odoo."""
    _inherit = 'website'

    featured_blog_ids = fields.Many2many('blog.post', relation="featured_blog",
                                         column1='blog', column2='featured',
                                         string="Featured Blogs",
                                         help="Select the blogs to be "
                                              "featured on the website.")
    popular_ids = fields.Many2many('blog.post', relation="popular_blog",
                                   column1='blog', column2='featured',
                                   string="Popular Blogs",
                                   help="Select the blogs to be displayed as "
                                        "popular on the website.")

    @api.constrains('featured_blog_ids')
    def _featured_blog(self):
        """ Constraint to validate the number of featured blogs.
            Raises: ValidationError: If more than three blogs are added."""
        if len(self.featured_blog_ids) > 3:
            raise ValidationError(_('Only three blogs should be added'))

    @api.constrains('popular_ids')
    def _popular_blog(self):
        """Constraint to validate the number of popular blogs.
             Raises:ValidationError: If more than three blogs are added."""
        if len(self.popular_ids) > 3:
            raise ValidationError(_('Only three blogs should be added'))
