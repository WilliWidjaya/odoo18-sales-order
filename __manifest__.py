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
    'assets': {
        'web.assets_frontend': [
            'sales_order/static/src/css/sales_style.css',
        ],
        'web.assets_backend': [
            'sales_order/static/src/css/sales_style.css',
        ]
    },
    'application' : True,
}