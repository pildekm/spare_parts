# -*- coding: utf-8 -*-
{
    "name": "Barcode scanner support for Stock Picking",
    "summary": """The module allows you to process Pickings by barcode scanner via special page /barcode/web (the same as it was in odoo 8.0)""",
    "category": "Warehouse",
    "images": [],
    "version": "1.0.2",

    "author": "GV",
    "support": "",
    "website": "",
    "license": "GPL-3",

    "depends": [
        "stock",
        "web_editor",
        "website",
        "picking_invoice",
        "stock_picking_checking",
    ],
    "external_dependencies": {"python": [], "bin": []},

    "data": [
        'views/stock.xml',
        'views/stock_view.xml',
        'views/stock_dashboard.xml',
    ],
    "qweb": [
        'static/src/xml/picking.xml',
    ],
    "demo": [],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "installable": True,
    "auto_install": False,
}
