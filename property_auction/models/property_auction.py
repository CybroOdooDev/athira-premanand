from odoo import fields, models, api


class PropertyAuction(models.Model):
    _name = 'property.auction'
    _description = 'Property Auction'
    _rec_name = 'auction_seq'

    auction_seq = fields.Char(string='Reference', readonly=True,
                              required=True, copy=False, default='New')
    property_id = fields.Many2one('property.property', required=True, domain="[('state', '=', 'for sale')]")
    responsible = fields.Many2one('res.users', required=True)
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id
                                  .currency_id.id,
                                  required=True)
    bid_start_price = fields.Monetary('Bid Start Price')
    final_price = fields.Monetary('Final Price', readonly=True)
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('started', 'Started'),
        ('ended', 'Ended'),
        ('canceled', 'Canceled')
    ], default='draft')
    participant_ids = fields.One2many('property.auction.line', 'auction_id')
    start_time = fields.Datetime('Start Time')
    end_time = fields.Datetime('End time')
    auction_winner = fields.Many2one('res.partner', readonly=True)

    @api.model
    def create(self, vals):
        if vals.get('auction_seq', 'New') == 'New':
            vals['auction_seq'] = self.env['ir.sequence'].next_by_code(
                'property.auction') or 'New'
        res = super(PropertyAuction, self).create(vals)
        return res

    def action_confirm(self):
        self.state = 'confirmed'

    def action_start(self):
        self.state = 'started'

    def action_end(self):
        selected_line = sorted(self.participant_ids, key=lambda x: x.bid_amount, reverse=True)[0]
        self.auction_winner = selected_line.partner_id.id
        self.final_price = selected_line.bid_amount
        self.end_time = fields.Datetime.now()
        self.state = 'ended'

    def action_cancel(self):
        self.state = 'canceled'

    def action_create_sale_order(self):
        self.env['property.sale'].create({
            'property_id': self.property_id.id,
            'partner_id': self.auction_winner.id,
            'date': fields.Date.today(),
            'sale_price': self.final_price,
        })


class AuctionLine(models.Model):
    _name = 'property.auction.line'
    _description = 'Auction Line'

    partner_id = fields.Many2one('res.partner')
    bid_time = fields.Datetime('Bid Time')
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id
                                  .currency_id.id,
                                  required=True)
    bid_amount = fields.Monetary('bid amount')
    auction_id = fields.Many2one('property.auction')
