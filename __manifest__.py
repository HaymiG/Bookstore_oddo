{
    'name': 'My Bookstore',
    'version': '17.0.1.0.0',
    'depends': ['base', 'mail'],  
    'summary': 'Manage bookstore inventory and sales',
    'sequence': 10,
    'description': """A simple module to manage bookstore""",
    'category': 'Productivity',
    'author': 'Haymanot',
    'website': '',
    'data': [
        
        'security/ir.model.access.csv',
      
        'data/genre_model.xml',
        'views/book_views.xml',
        'views/genre_views.xml',
        'views/book_kanban_view.xml',

    ],
    
    'demo': [
    'data/demo_data.xml',
],
    'installable': True,
    'application': True,
    'auto_install': False,
}
