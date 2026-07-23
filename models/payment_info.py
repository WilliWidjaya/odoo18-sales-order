from odoo import api, fields, models

class PaymentInfo(models.Model):
    _name = "payment_info"
    _description = "Ship Location"

    name = fields.Char() # Ga bakal di munculin di table
    payment_details = fields.Text()