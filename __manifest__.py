{
    'name': 'Student Management',
    # 'summary': 'Summery',
    'description': 'Description',
    'category': 'Category',
    'author': 'Author',
    # 'website': 'Website',
    # 'license': 'License',
    'depends': ['base'],
    'data': ['security/ir.model.access.csv',
             'views/inherit_partner.xml',
             'views/student_view.xml',
             'views/book_view.xml',
             'views/menu.xml',
             ],
    'demo': ['Demo'],
    'installable': True,
    'application': True,
    'auto_install': True
}
