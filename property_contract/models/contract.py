from odoo import fields, models, api


class Contract(models.Model):
    _name = 'property.contract'
    _description = "Property Contract"

    contract_number = fields.Char(string="Contract Number", readonly=True, default='New')
    name = fields.Char(string="Name", required=True)
    start_date = fields.Date(string="Start Date", required=True)
    property = fields.Many2one('property.property', string="Property", required=True)
    rent_price = fields.Float(string="Rent Price")
    deposit_amount = fields.Float(string="Deposit Amount")
    renter = fields.Many2one('res.partner', string="Renter")
    owner = fields.Many2one('res.partner', string="Owner")
    stages = fields.Selection(selection=[('new', 'New'), ('approval', 'Approval'), ('running', 'Running'),
                                         ('expired', 'Expired'), ('cancelled', 'Cancelled')], required=True,
                                         default="new")
    contract_line_ids = fields.One2many('contract.line', "contract_line_id", string="order line")
    terms_and_conditions = fields.Text(string="Terms and Conditions")
    contract_type = fields.Selection(selection=[('permanent', 'Permanent'), ('temporary', 'Temporary')])
    contract_expiry = fields.Date(string="Expiry Date")

    def btn_cancel(self):
        self.stages = 'cancelled'

    @api.model
    def create(self, vals):
        if vals.get('contract_number', 'New') == 'New':
            vals['contract_number'] = self.env['ir.sequence'].next_by_code(
                'property.contract') or 'New'
        res = super(Contract, self).create(vals)
        return res

    def expiring_contract(self):
        today = fields.Date.today()
        record = self.env['property.contract'].search(
            [('stages', '=', 'running'), ('contract_expiry', '<', 'today')])
        for rec in record:

            rec.stages = 'expired'
            print(rec, "rec")
            data = self.env['property.contract'].create({
                'contract_number': rec.contract_number,
                'name': rec.name,
                'current_date': rec.current_date,
                'start_date': rec.start_date,
                'property': rec.property.id,
                'rent_price': rec.rent_price,
                'deposit_amount': rec.deposit_amount,
                'renter': rec.renter.id,
                'owner': rec.owner.id,
                'contract_type': rec.contract_type,
                'contract_expiry': rec.contract_expiry,
            })

            display_id = rec.id
            action_id = self.env.ref(
                'property_contract.property_contract_action').id
            base_url = self.env['ir.config_parameter'].get_param(
                'web.base.url')
            redirect_link = "/web#id=%s&cids=1&menu_id=313&action=%s" \
                            "&model" \
                            "=property.contract&view_type=form" % (
                                display_id, action_id)
            url = base_url + redirect_link

            mail_template = self.env.ref('property_contract.contract_email_template')

            mail_body = """
                    <p>Hello,</p>
                           <p>Please note that your contract has been expired</p>
                           <p>To Approve Click on the Following 
                           Link:
                           <a href='%s' style="display: inline-block; 
                           padding: 10px; text-decoration: none; font-size: 12px; background-color: #875A7B; color: #fff; border-radius: 5px;"><strong>Click Here</strong></a>
                           </p>
                           <p>Thank You.</p>""" % (url)

            mail_template.write({
                'email_to': f'{rec.renter.email},{rec.owner.email}',
                'body_html': mail_body,
            })
            mail_template.send_mail(rec.id, force_send=True)


class ContractLine(models.Model):
    _name = 'contract.line'
    _description = "Contract Line"

    contract_line_id = fields.Many2one('property.contract')
