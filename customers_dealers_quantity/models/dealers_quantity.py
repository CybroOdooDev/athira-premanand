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

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class DealersQuantity(models.Model):
    _inherit = "res.partner"

    dealer = fields.Boolean()


class Dealers(models.Model):
    _inherit = "product.product"

    price = fields.Float(string="Dealers Price")
    minimum_quantity = fields.Float(string="Dealers Min Quantity")


class Sale(models.Model):
    _inherit = "sale.order"

    # def action_confirm(self):
    #     for rec in self.order_line:
    #         if rec.product_uom_qty < rec.product_id.minimum_quantity:
    #             raise UserError(_('Your order quantity is not enough as a dealer'))
    #     super(Sale, self).action_confirm()


class SaleLine(models.Model):
    _inherit = "sale.order.line"

    # @api.onchange('product_id')
    # def _onchange_product_id_warning(self):
    #     if self.order_id.partner_id.dealer:
    #         for rec in self:
    #             if rec.product_id.price and rec.product_id.minimum_quantity:
    #                 rec.write({
    #                             'product_uom_qty': rec.product_id.minimum_quantity,
    #                             'price_unit': rec.product_id.price
    #                         })
    #     super(SaleLine, self)._onchange_product_id_warning()

    @api.onchange('product_uom_qty')
    def _onchange_product_uom_qty(self):
        if self.order_id.partner_id.dealer:
            if self.product_id.price and self.product_id.minimum_quantity:
                if self.product_uom_qty >= self.product_id.minimum_quantity:
                    self.write({
                            'price_unit': self.product_id.price
                        })
                else:
                    self.write({
                        'price_unit': self.product_id.list_price
                    })
        print("swdcdgdfdhtf")

