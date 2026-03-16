class OrderBuilder:
    @staticmethod
    def create(cart_id, address_id, customer_id, secure_key):
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <order>
        <id_cart><![CDATA[{cart_id}]]></id_cart>
        <id_customer><![CDATA[{customer_id}]]></id_customer>
        <id_address_delivery><![CDATA[{address_id}]]></id_address_delivery>
        <id_address_invoice><![CDATA[{address_id}]]></id_address_invoice>

        <id_currency><![CDATA[1]]></id_currency>
        <id_lang><![CDATA[1]]></id_lang>
        <id_carrier><![CDATA[2]]></id_carrier>
        <current_state><![CDATA[1]]></current_state>

        <module><![CDATA[ps_checkpayment]]></module>
        <payment><![CDATA[Payment by check]]></payment>

        <total_paid><![CDATA[42.900000]]></total_paid>
        <total_paid_tax_incl><![CDATA[42.900000]]></total_paid_tax_incl>
        <total_paid_tax_excl><![CDATA[42.900000]]></total_paid_tax_excl>
        <total_paid_real><![CDATA[42.900000]]></total_paid_real>
        <total_products><![CDATA[42.900000]]></total_products>
        <total_products_wt><![CDATA[42.900000]]></total_products_wt>

        <secure_key><![CDATA[{secure_key}]]></secure_key>
        
        <valid><![CDATA[1]]></valid>

        <id_shop><![CDATA[1]]></id_shop>
        <id_shop_group><![CDATA[1]]></id_shop_group>

        <round_mode><![CDATA[2]]></round_mode>
        <round_type><![CDATA[1]]></round_type>

        <conversion_rate><![CDATA[1]]></conversion_rate>
    </order>
</prestashop>
"""

    @staticmethod
    def update(order_id, cart_id, customer_id, address_id, note="Updated note"):
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <order>
        <id><![CDATA[{order_id}]]></id>
        <id_cart><![CDATA[{cart_id}]]></id_cart>
        <id_customer><![CDATA[{customer_id}]]></id_customer>
        <id_address_delivery><![CDATA[{address_id}]]></id_address_delivery>
        <id_address_invoice><![CDATA[{address_id}]]></id_address_invoice>
        <id_currency><![CDATA[1]]></id_currency>
        <id_lang><![CDATA[1]]></id_lang>
        <id_carrier><![CDATA[2]]></id_carrier>
        <current_state><![CDATA[1]]></current_state>
        <module><![CDATA[ps_checkpayment]]></module>
        <payment><![CDATA[Payment by check]]></payment>
        <total_paid><![CDATA[42.90]]></total_paid>
        <total_paid_real><![CDATA[42.90]]></total_paid_real>
        <total_products><![CDATA[42.90]]></total_products>
        <total_products_wt><![CDATA[42.90]]></total_products_wt>
        <conversion_rate><![CDATA[1]]></conversion_rate>
        <note><![CDATA[{note}]]></note>
    </order>
</prestashop>"""
