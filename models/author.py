from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    author = fields.Boolean(string="Is an Author")
