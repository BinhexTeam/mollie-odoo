{
    'name': 'Mollie POS Terminal Multiple Profiles',
    'version': '18.0.1.0.0',
    'author': 'Custom',
    'license': 'LGPL-3',
    'depends': ['mollie_pos_terminal', 'point_of_sale'],
    'data': [
        'views/res_config_settings_views.xml',
        'wizard/mollie_sync_terminal.xml',
    ],
    'post_init_hook': 'post_init_hook'
}
