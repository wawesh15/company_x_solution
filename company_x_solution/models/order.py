# company_x_solution/models/order.py

from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    advance_payment = fields.Float(string='Advance Payment (%)')
    deadline = fields.Datetime(string='Deadline')
    state = fields.Selection(
        selection_add=[('closed', 'Closed')],
        ondelete={'closed': 'set default'}
    )
    
    def action_cancel(self):
        # Custom logic for cancellation
        if self.state != 'delivered':
            # Handle advance payment retention
            pass

    def action_deliver(self):
        # Custom logic for delivery
        pass
