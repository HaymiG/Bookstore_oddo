from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_author = fields.Boolean(string='Is Author')
