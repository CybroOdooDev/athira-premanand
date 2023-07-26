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
from odoo import fields, models


class MarsPortfolio(models.Model):
    """ Represents a Mars portfolio in Odoo."""
    _name = 'mars.portfolio'
    _description = 'Mars Portfolio'
    _rec_name = "name"

    name = fields.Char(string="Name", help="user can create portfolio")
    portfolio_ids = fields.Many2many('portfolio.group',
                                     string="Portfolio Groups",
                                     help="select groups for portfolio")


class PortfolioImages(models.Model):
    """Represents images associated with a portfolio in Odoo."""
    _name = 'portfolio.images'
    _description = 'Portfolio Images'
    _rec_name = 'portfolio_image'

    portfolio_image = fields.Image(string="Image",
                                   help="Add images for creating portfolio")


class PortfolioGroup(models.Model):
    """Represents a group of images in a portfolio in Odoo."""
    _name = 'portfolio.group'
    _description = 'Portfolio Group'

    image_group_ids = fields.Many2many('portfolio.images', string="Images",
                                       help="Select images under the group")
    group_type = fields.Selection(
        [('modal', 'Modal'), ('carousel', 'Carousel')], string="Group Type",
        help="group show type")
