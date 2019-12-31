from odoo import models, fields, api


class System_request(models.Model):
    _name = 'system.request'
    _rec_name = 'system_name'

    system_name = fields.Char(string='System')
    system_product_ids = fields.Many2one(comodel_name='product.request', string='Product')
