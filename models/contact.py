from odoo import fields, models

class SalesContact(models.Model):
    _name = "sales_contact"
    _description = "Sales Contact"

    name = fields.Char()
    location = fields.Text()