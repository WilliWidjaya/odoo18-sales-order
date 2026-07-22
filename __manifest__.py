{
    'name' : 'Sales Order IGU',
    'version' : '1.0',
    'author' : 'William Widjaya',
    'depends' : ['base'],
    'data' : [
        'security/ir.model.access.csv',
        'views/sales_views.xml',
        'views/sales_menus.xml',
    ],
    # 'assets': {
    #     'web.assets_frontend': [
    #     ],
    #     'web.assets_backend': [
    #     ]
    # },
    'application' : True,
}