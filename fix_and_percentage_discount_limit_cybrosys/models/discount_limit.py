from odoo import models, fields, _
from odoo.exceptions import UserError


class DiscountLimit(models.Model):
    _inherit = 'res.users'

    fixed_limit = fields.Float(string="Fixed Limit")
    percentage_limit = fields.Float(string="Percentage Limit")


class Sale(models.Model):
    _inherit = 'sale.order'

    limit_type = fields.Selection([('fixed', 'Fixed Limit'),
                                   ('percentage', 'Percentage Limit')], string="Limit Type")

    def action_confirm(self):
        if self._origin.user_id.id == self.env.uid:
            limit_fixed = self._origin.user_id.fixed_limit
            print(str(limit_fixed))
            limit_percentage = self._origin.user_id.percentage_limit
            for i in self.order_line:
                if i.discount > limit_fixed and self.limit_type == 'fixed':
                    raise UserError(_("Discount must be less than or equal to %s", str(limit_fixed)))
                if i.discount > limit_percentage and self.limit_type == 'percentage':
                    raise UserError(_("Discount must be less than or equal to %s", str(limit_percentage)))
        super(Sale, self).action_confirm()
