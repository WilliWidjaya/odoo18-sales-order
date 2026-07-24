from odoo import api, fields, models

class ShipLocation(models.Model):
    _name = "ship_location"
    _description = "Ship Location"

    name = fields.Char(compute = "change_name") # Ga bakal di munculin di table
    shipping_location = fields.Text()

    # Set name ketika item_no diganti (atau on save).
    @api.depends('shipping_location')
    def change_name(self):
        for i in self:
            i.name = str(i.shipping_location)