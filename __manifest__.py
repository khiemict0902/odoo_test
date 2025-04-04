{
    'name': 'Student Management',
    # 'summary': 'Summery',
    'description': 'Description',
    'category': 'Category',
    'author': 'Author',
    # 'website': 'Website',
    # 'license': 'License',
    'depends': ['base'],
    'data': ['views/menu.xml',
             'views/book_view.xml',
             'views/student_view.xml',
             'views/inherit_partner.xml',
             'security/ir.model.access.csv'
             ],
    # 'demo': ['Demo'],
    'installable': True,
    'application': True,
    'auto_install': True
}
