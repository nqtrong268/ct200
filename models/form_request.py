from odoo import models, fields, api


class Form_request(models.Model):
    _name = 'form_request'

    date_request = fields.Datetime(string='Thời gian thực hiện: ')