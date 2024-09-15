# company_x_solution/models/product.py

from odoo import models, fields

class Product(models.Model):
    _inherit = 'product.product'

    delivery_date = fields.Datetime(string='Delivery Date')
    canceled_by_client = fields.Boolean(string='Canceled by Client', default=False)
