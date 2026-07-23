from odoo import api, fields, models

class SalesOrder(models.Model):
    _name = "sales_order"
    _description = "Sales Order Main"

    # ---------- Informasi Di Header
    name = fields.Char() # JANGAN TUNJUKIN INI, buat @api.depends('sales_id') untuk set name
    sales_id = fields.Char()
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
    item_or_service_type = fields.Selection(
        string = "Item or Service",
        selection = [('type_item', 'Item'), ('type_service', 'Service')],
        help = "Tentukan jenis"
    )
    summary_type = fields.Selection(
            string = "Summary Type",
            selection = [('st_summary', 'Summary'), ('st_none', 'No Summary')],
            help = "Tentukan jenis"
        )
    sales_contents = fields.One2many(comodel_name = "sales_content", inverse_name = "sales_id")
    # Ini bakal pake List dengan fields.One2many(comodel_name = "po_content", inverse_name = "po_id")

    # ------------- Informasi Logistics
    shipping_location = fields.Many2one('ship_location')
    payment_info = fields.Many2one('payment_info')
    ship_ta = fields.Text()
    pay_ta = fields.Text()

    shipping_type = fields.Selection(
        string = "Shipping Type",
        selection = [('type_1', 'type 1'), ('type_2', 'type_2')],
        help = "Tentukan shipping type"
    )
    bp_channel_name = fields.Char()
    bp_channel_contact = fields.Many2one('res.partner')

    # -------------- Accounting
    journal_remark = fields.Char()
    payment_term = fields.Selection(
        string = "Payment Term",
        selection = [('pay_cash', 'Cash'), ('pay_bank', 'bank')],
        help = "Payment term here.."
    ) 
    payment_method = fields.Selection(
        string = "Payment Method",
        selection = [('pm_1', 'method 1'), ('pm_2', 'method 2')],
        help = "Payment Method here.."
    )
    due_date = fields.Date()
    bp_project = fields.Char()
    cancellation_date = fields.Date()
    required_date = fields.Date()
    indicator = fields.Char()
    tax_id = fields.Char()
    order_number = fields.Char()
