odoo.define('website_sale_checkout_store.tour', function (require) {
'use strict';

var tour = require("web_tour.tour");
var base = require("web_editor.base");

tour.register('shop_mandatory_fields_nobill_ship', {
    test: true,
    url: '/shop',
    wait_for: base.ready()
},
    [
        {
            content: "log out dropdown",
            trigger: '#top_menu a[href="#"]',
        },
        {
            content: "log out",
            trigger: '#o_logout a[href="/web/session/logout?redirect=/"]',
        },
        {
            content: "log out",
            extra_trigger: 'a[href="/web/login"]',
            trigger: 'a[href="/shop"]',
        },
        // further for unsigned user
        {
            content: "search ipod",
            extra_trigger: 'a[href="/web/login"]',
            trigger: 'form input[name="search"]',
            run: "text ipod",
        },
        {
            content: "search ipod",
            trigger: 'form:has(input[name="search"]) .oe_search_button',
        },
        {
            content: "select ipod",
            trigger: '.oe_product_cart a:contains("iPod")',
        },
        {
            content: "click on add to cart",
            trigger: '#product_detail form[action^="/shop/cart/update"] .btn',
        },
        //--------------------------DEFAULT PART ENDS--------------------------------------
        {
            content: "select payment",
            trigger: 'a[id="nobill_ship"]',
        },
        {
            content: "filling in name",
            trigger: '.div_name input[name="name"]',
            run: "text name",
        },
        {
            content: "filling in email",
            trigger: '#div_email input[name="email"]',
            run: "text email@email.mn",
        },
        {
            content: "filling in phone",
            trigger: '#div_phone input[name="phone"]',
            run: "text 1234567890",
        },
        {
            content: "filling in street",
            trigger: '.div_street input[name="street"]',
            run: "text Street and Number",
        },
        {
            content: "filling in city",
            trigger: '.div_city input[name="city"]',
            run: "text city",
        },
        {
            content: "Confirm checkout",
            trigger: 'a:contains("Next")',
        },
        {
            content: "click confirm",
            trigger: 'a[href="/shop/confirm_order"]',
        },
        {
            content: "Confirm checkout",
            extra_trigger: 'h2:contains(Thank you for your order)',
            trigger: 'a[href="/shop/print"]',
        },
    ]
);

});
