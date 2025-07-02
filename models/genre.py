from odoo import models, fields

class GenreDetails(models.Model):
    _name = 'genre.details'    
    _description = 'Genre Details'


    name = fields.Char(required=True, unique=True)
    book_ids = fields.Many2many('book.details', string='Books')
