# -*- coding: utf-8 -*-
# Copyright 2016 Christophe CHAUVET.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "SCI",
    "summary": "Gestion de Société Civile Immobilière",
    "version": "8.0.1.0.0",
    'category': 'Localization',
    "website": "http://mirounga.fr/",
    "author": "Christophe CHAUVET, Mirounga",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    # "pre_init_hook": "pre_init_hook",
    # "post_init_hook": "post_init_hook",
    # "post_load": "post_load",
    # "uninstall_hook": "uninstall_hook",
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
        "account",
        "account_voucher",
        "account_accountant",
        "account_followup",
    ],
    "data": [
        "views/company_view.xml",
        "views/partner_view.xml",
        "views/account_view.xml",
        "views/report_receipt.xml",
    ],
    "demo": [],
    "qweb": []
}
