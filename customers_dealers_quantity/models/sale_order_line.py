""""Customers Dealers Quantity"""
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
from odoo import api, models


class SaleOrderLine(models.Model):
    """This class helps to set the dealers price."""
    _inherit = "sale.order.line"

    @api.onchange('product_uom_qty')
    def _onchange_product_uom_qty(self):
        """This method is used for setting the dealers price"""
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
