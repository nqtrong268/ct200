from odoo import models, fields, api


class System_request(models.Model):
    _name = 'system.request'
    _rec_name = 'system_name'

    system_name = fields.Char(string='System')
    # system_product_ids = fields.Many2one(comodel_name='product.request', string='Product')
    sys_product = fields.Selection(string='Product', selection=[('nvn', 'Native Việt Nam'),
                                                                ('ntl', 'Native Thái Lan'),
                                                                ('ovn', 'OVN')])

    person_approve_system = fields.Selection(string='Approver', selection=[('thuylb3', 'Lê Biên Thùy')
                                                                    , ('hungcm', 'Chu Mạnh Hùng'),
                                                                    ('manhnv', 'Nguyễn Văn Mạnh')])
