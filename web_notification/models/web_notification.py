""""Web Notification"""
# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Technologies (<https://www.cybrosys.com>)
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

from odoo import fields, models, _


class Notification(models.Model):
    _name = 'web.notification'
    _description = "Web Notification"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char("Name")
    create_date = fields.Date("Creation Date")
    user_id = fields.Many2many('res.users', string="Users")
    description = fields.Char("Description")
    simple_text = fields.Boolean("Want Simple Text?")
    font_color = fields.Char("Font Color", default="#fff")
    background_color = fields.Char("Background Color", default="#000000")
    font_family = fields.Selection([('times_new_roman', 'Times New Roman'), ('sans-serif', "Sans Serif")])
    font_size = fields.Char("Font Size")
    padding = fields.Char("Padding")
    animation = fields.Boolean("Animation")
    direction = fields.Selection([
        ('left', 'Left'),
        ('right', 'Right')])
