from odoo import fields, models, api


class Property(models.Model):
    _name = 'property.property'
    _description = 'Property'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", required=True, copy=False)
    code = fields.Char(string='Reference', readonly=True,
                       required=True, copy=False, default='New')
    type_id = fields.Many2one('property.type', string='Property Type')
    type_id_base = fields.Selection(related='type_id.type', string="Property Base Type")
    street = fields.Char(required=True)
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    country_id = fields.Many2one("res.country", string="Country", ondelete="restrict",
                                 required=True)
    state_id = fields.Many2one("res.country.state", string="State", ondelete="restrict",
                               domain="[('country_id', '=?', country_id)]")
    latitude = fields.Float(string="Latitude", digits=(16, 5))
    longitude = fields.Float(string="Longitude", digits=(16, 5))
    date = fields.Date(string="Date", default=fields.Date.today)
    measure_value = fields.Float()
    measure = fields.Selection([('meter', 'Meter'), ('square_foot', 'Square Yard'),
                                ('square_feet', 'Square Feet'), ('acre', 'Acre'), ('hectare', 'Hectare')])
    usable_sqft = fields.Float("Usable Square Feet", readonly=True, compute='_compute_usable_sqft')
    residence_measure_ids = fields.One2many('residence.measurement', 'property_id')
    state = fields.Selection([('available', 'Available'),
                              ('booked', 'Booked')],
                             default='available', tracking=True)
    currency_id = fields.Many2one("res.currency", string="Currency")
    book_price = fields.Monetary(string="Book Price", required=True)
    owner_id = fields.Many2one("res.partner", string="Property Owner")
    property_manager_id = fields.Many2one('res.users', string="Property Manager")
    property_management_company_id = fields.Many2one('res.company',
                                                     string="Property Management Company",
                                                     required=True,
                                                     default=lambda
                                                     self: self.env.company)
    image = fields.Binary(string="Image")
    url_ids = fields.One2many('property.url', 'property_id')
    facility_ids = fields.Many2many('property.facilities')
    tags = fields.Many2many('property.tags')
    construct_year = fields.Char(string='Construct Year', size=4)
    license_no = fields.Char(string='License No.')
    property_line_ids = fields.One2many('property.nearby.connectivity', 'property_line_id', string='Order Lines')
    neighbours_line_ids = fields.One2many('neighbours.data', 'neighbours_line_id', string='Order Lines')
    property_image_ids = fields.One2many('property.image', 'property_id')
    description = fields.Text('Description')

    @api.model
    def create(self, vals):
        if vals.get('code', 'New') == 'New':
            vals['code'] = self.env['ir.sequence'].next_by_code(
                'property.property') or 'New'
        res = super(Property, self).create(vals)
        return res

    @api.model
    def _geo_localize(self, street='', zip='', city='', state='', country=''):
        geo_obj = self.env['base.geocoder']
        print(geo_obj)
        search = geo_obj.geo_query_address(street=street, zip=zip, city=city, state=state, country=country)
        result = geo_obj.geo_find(search, force_country=country)
        if result is None:
            search = geo_obj.geo_query_address(city=city, state=state, country=country)
            result = geo_obj.geo_find(search, force_country=country)
        return result

    @api.onchange('street', 'zip', 'city', 'state_id', 'country_id')
    def geo_localize(self):
        for property in self.with_context(lang='en_US'):
            result = property._geo_localize(property.street,
                                            property.zip,
                                            property.city,
                                            property.state_id.name,
                                            property.country_id.name)
            print(property, result)
            if result:
                property.write({
                    'latitude': result[0],
                    'longitude': result[1],
                })

    @api.depends('residence_measure_ids')
    def _compute_usable_sqft(self):
        self.usable_sqft = sum(self.residence_measure_ids.mapped("carpet_area"))

    def get_map(self):
        print(self.longitude, self.latitude)
        return {
            'type': 'ir.actions.act_url',
            'name': "View Map",
            'target': 'self',
            'url': '/map/%s/%s' % (self.latitude, self.longitude),
        }

    class ResidenceMeasurement(models.Model):
        _name = 'residence.measurement'
        _description = "Measurement of the Residence Property"

        property_id = fields.Many2one('property.property')
        section = fields.Char('Residence Section')
        length = fields.Float('Length(ft)')
        width = fields.Float('Width(ft)')
        height = fields.Float('Height(ft)')
        carpet_area = fields.Float('Carpet Area(ft)')

        @api.onchange('length', 'width')
        def _compute_carpet_area(self):
            self.carpet_area = self.length * self.width
