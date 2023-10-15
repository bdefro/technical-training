from odoo import fields, models
from dateutil.relativedelta import relativedelta

class Property(models.Model):
    """ Estate Property
    """
    _name = "estate_property"
    _description = "Model representing an estate property"

    name = fields.Char(required=True, default="Unknown")
    description = fields.Text()

    three_months = lambda self: fields.Datetime.now() + \
relativedelta(months = 3)

    postcode = fields.Char()
    date_availability = fields.Date(copy=False,
                                    default=three_months)

    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)

    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(string='Garden Orientation',
        selection=[("north", "North"), ("south", "South"),
                   ("east", "East"), ("west", "West")],
        help="Garden Orientation")

    active = fields.Boolean(default=True)
    state = fields.Selection(string='State',
        selection=[("new", "New"), ("offer received", "Offer Received"),
                   ("offer accepted", "Offer Accepted"), ("sold", "Sold"),
                   ("cancelled", "Cancelled")],
        help="State of the property")