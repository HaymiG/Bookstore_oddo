from odoo import models, fields

class BookArchiveLog(models.Model):
    _name = 'book.archive.log'
    _description = 'Archived Book Log'
    _order = 'archived_on desc'

    book_id = fields.Many2one('book.details', required=True, ondelete='cascade')
    archived_on = fields.Datetime(default=fields.Datetime.now)
    archived_by = fields.Many2one('res.users', default=lambda self: self.env.user)

