""""Customer Order Comment"""
# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2022-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
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


class CustomerComment(models.Model):
    _inherit = 'sale.order'

    comment = fields.Char(string="Comment", readonly=True)
    rating = fields.Selection([('1', 'Poor'), ('2', 'Too Bad'), ('3', 'Average Quality'), ('4', 'Nice'),
                               ('5', 'Good')], readonly=True)


class WebsiteConfiguration(models.TransientModel):
    _inherit = 'res.config.settings'

    comment_configuration = fields.Boolean(config_parameter='customer_order_comment.comment_configuration')
