from odoo import fields, models, api


class ApprovalTeams(models.Model):
    _name = "approval.teams"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Approval Teams"

    name = fields.Char(string="Name")
    company_id = fields.Many2one('res.company', string='Company', required=True,
                                 default=lambda self: self.env.company)
    team_leader_id = fields.Many2one('team.leader', string="Team Leader")
    approver_line_ids = fields.One2many("approvers", "approver_line_id", string="order line")


class TeamLeader(models.Model):
    _name = "team.leader"
    _description = "Team Leader"

    name = fields.Many2one('res.users', string='Name', default=lambda self: self.env.user)


class Position(models.Model):
    _name = "position"
    _description = "Position"

    name = fields.Char(string="Name")


class Partner(models.Model):
    _name = "partner"
    _description = "Partner"

    name = fields.Char(string="Name")


class Approver(models.Model):
    _name = "approvers"
    _description = "Approvers"

    approver_line_id = fields.Many2one('approval.teams')
    approver_id = fields.Many2one('team.leader', string="Approver")
    min_amount = fields.Char(string="Minimum Amount")
    max_amount = fields.Char(string="Maximum Amount")
    position_id = fields.Many2one('position', string="Position")
    can_edit = fields.Boolean(string="Can Edit")
    custom_condition = fields.Char(string="Custom Condition Code")


class Contract(models.Model):
    _name = "contract"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Contract"

    name = fields.Char(string="Name")
    reference = fields.Char(string="Reference")
    company_id = fields.Many2one('res.company', string='Company', required=True,
                                 default=lambda self: self.env.company)
    current_user = fields.Many2one('res.users', 'Responsible User', default=lambda self: self.env.user)
    partner = fields.Many2one('partner', string="Partner")
    type = fields.Selection([('sales', 'Sales'), ('purchase', 'Purchase')])
    state = fields.Selection([('draft', 'Draft'), ('approval', 'Approval'), ('running', 'Running'),
                              ('expired', 'Expired'), ('closed', 'Closed'), ('to_renew', 'To Renew'),
                              ('cancelled', 'Cancelled')], group_expand='_group_expand_states', default='draft',
                             track_visibility='always')
    use_lines = fields.Boolean(string="Use Lines")
    approval_team_id = fields.Many2one('approval.teams', string="Approval Team")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    last_payment_date = fields.Date(string="Last Payment Date")
    expiring_state = fields.Selection([('draft', 'Draft'), ('approval', 'Approval'), ('running', 'Running'),
                                       ('to_renew', 'To Renew'), ('approval', 'Approval'), ('cancelled', 'Cancelled'),
                                       ('expired', 'Expired')])
    cost = fields.Integer(string="Cost")
    currency_id = fields.Many2one('res.currency',
                                  default=lambda self: self.env['res.currency'])
    contract_approval_ids = fields.One2many("contract_approval", "contract_approval_id", string="order line")
    contract_line_ids = fields.One2many("contract_line", "contract_line_id", string="order line")

    def _group_expand_states(self, state, domain, order):
        return [key for
                key, val in type(self).state.selection]

    def btn_confirm(self):
        self.state = 'approval'

    def btn_approve(self):
        self.state = 'running'

    def btn_cancel(self):
        self.state = 'cancelled'

    def btn_return(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'wizard.msg',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }

    @api.onchange('approval_team_id')
    def _onchange_approval_team_id(self):
        val = []
        for rec in self.approval_team_id.approver_line_ids:
            val.append((0, 0, {
                'approver_id': rec.approver_id,
                'position_id': rec.position_id,
            }))
        self.contract_approval_ids = False
        self.contract_approval_ids = val


class ContractApproval(models.Model):
    _name = "contract_approval"
    _description = "Contract Approval"

    contract_approval_id = fields.Many2one('contract')
    approver_id = fields.Many2one('team.leader', string="Approver")
    position_id = fields.Many2one('position', string="Role/Position")
    status = fields.Selection([('approved', 'Approved'), ('pending', 'Pending')])


class ContractLine(models.Model):
    _name = "contract_line"
    _description = "Contract Line"

    contract_line_id = fields.Many2one('contract')
    product = fields.Many2one('product.product', string="Product")
    product_label = fields.Char(string="Label")
    prod_quantity = fields.Float(string="Quantity", default="1")
    prod_uom = fields.Char(string="UoM")
    prod_price = fields.Float(string="Price")
    prod_discount = fields.Float(string="Discount")

    @api.onchange('product')
    def _onchange_product(self):
        for rec in self.product:
            self.prod_price = rec.list_price
            self.product_label = rec.name


class ReturnReason(models.Model):
    _name = "return.reason"
    _description = "Return Reason"

    name = fields.Char('Return Reason')
