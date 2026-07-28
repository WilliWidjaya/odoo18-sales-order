from odoo import fields, models, api

class ShippingType(models.Model):
    _name = "shipping_type"
    _description = "Shipping Type"

    name = fields.Char(compute = "set_name") # Ga bakal di munculin di table
    type = fields.Char()

    @api.depends('type')
    def set_name(self):
        for i in self:
            if i.type != False or i.type != "":
                i.name = i.type