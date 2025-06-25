{
    'name': 'Book-Store',
    'version': '1.0.0',
    'category': 'BookStore',
    'author': 'haymanot',
    'sequence': -100,
    'summary': 'BookStore managment system',
    'description': """
BookStore managment system
    """,
    'application': True,
    'depends': [ ],
    'data': [ 
        'security/ir.model.access.csv',
        'views/book_details_views.xml',
        'views/menu.xml',
    ],
    'demo': [],
    'installable': True,
    'license': 'LGPL-3',

}