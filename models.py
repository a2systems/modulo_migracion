from odoo import tools, models, fields, api, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    old_system_code = fields.Char('Old System Code')
    old_system_id = fields.Integer('Old System ID')
