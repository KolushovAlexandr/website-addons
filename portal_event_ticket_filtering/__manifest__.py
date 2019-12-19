# -*- coding: utf-8 -*-
{
    "name": """Portal Tciket Filtering Page""",
    "summary": """Allows to customers see their tickets for events at the Portal""",
    "category": "Marketing",
    # "live_test_url": "http://apps.it-projects.info/shop/product/portal-event-tickets?version=10.0",
    "images": ["images/banner.jpg"],
    "version": "10.0.1.1.1",
    "application": False,

    "author": "IT-Projects LLC, Kolushov Alexandr",
    "support": "apps@it-projects.info",
    "website": "https://it-projects.info/team/KolushovAlexandr",
    "license": "LGPL-3",
    "price": 150.00,
    "currency": "EUR",

    "depends": [
        "portal_event_tickets",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/portal_templates.xml",
    ],
    "qweb": [
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,

    "demo_title": "Event extensions",
    "demo_addons": ["website_event_attendee_fields", "website_event_attendee_signup", "website_event_require_login"],
    "demo_addons_hidden": ["website_event_attendee_fields_custom"],
    "demo_url": "portal-event-tickets",
    "demo_summary": "Set of modules to extend Event application.",
    "demo_images": [
    ]
}
