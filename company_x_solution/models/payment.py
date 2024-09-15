# company_x_solution/models/payment.py

from odoo import models, fields

class Payment(models.Model):
    _name = 'order.payment'
    _description = 'Order Payment'

    order_id = fields.Many2one('sale.order', string='Order')
    amount = fields.Float(string='Amount')
    date = fields.Datetime(string='Payment Date')
