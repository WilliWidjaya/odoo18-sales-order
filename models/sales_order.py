from odoo import api, fields, models

class SalesOrder(models.Model):
    _name = "sales_order"
    _description = "Sales Order Main"

    # ---------- Informasi Di Header
    name = fields.Char()
    customer_id = fields.Char()
    contact_person = fields.Many2one('res.partner')
    customer_ref_no = fields.Char()
    currency = fields.Char()
    
    sales_order_number = fields.Char()
    sales_order_status = fields.Char()
    
    posting_date = fields.Date()
    delivery_date = fields.Date()
    document_date = fields.Date()

    # ------------- Informasi Kolom Contents
    # Ini bakal pake List dengan fields.One2many(comodel_name = "po_content", inverse_name = "po_id")

    # ------------- Informasi Logistics
    # Ini bakal ada ship_to dari master shipping locations
    # Disini ada pay_to dari master payment accounts
    # Text Area kosong buat alamat ship_to
    # Text Area kosong buat pay_to
    # Shipping Type (?)
    # BP Channel Name
    # BP Channel Contact

    # -------------- Accounting
    journal_remark = fields.Char()
    payment_terms = fields.Char() # NOTE : INI MUNGKIN BAKAL JADI DROPDOWN AJA
    payment_method = fields.Char() # NOTE : INI JUGA BAKAL AJDI DROPDOWN, TAPI GW LUPA CARANYA LOL!!!!
    due_date = fields.Date()
    bp_project = fields.Char()
    cancellation_date = fields.Date()
    required_date = fields.Date()
    indicator = fields.Char()
    tax_id = fields.Char()
    order_number = fields.Char()
