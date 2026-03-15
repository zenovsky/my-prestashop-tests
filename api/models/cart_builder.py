class CartBuilder:

    @staticmethod
    def create(address_id, customer_id, product_id):
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <cart>
        <id_address_delivery><![CDATA[{address_id}]]></id_address_delivery>
        <id_address_invoice><![CDATA[{address_id}]]></id_address_invoice>
        <id_currency><![CDATA[1]]></id_currency>
        <id_customer><![CDATA[{customer_id}]]></id_customer>
        <id_lang><![CDATA[1]]></id_lang>
        <id_shop_group><![CDATA[1]]></id_shop_group>
        <id_shop><![CDATA[1]]></id_shop>
        <id_carrier><![CDATA[1]]></id_carrier>
        <id_guest><![CDATA[0]]></id_guest>
        <recyclable><![CDATA[0]]></recyclable>
        <gift><![CDATA[0]]></gift>
        <gift_message><![CDATA[]]></gift_message>
        <mobile_theme><![CDATA[0]]></mobile_theme>
        <delivery_option><![CDATA[]]></delivery_option>
        <secure_key><![CDATA[]]></secure_key>
        <allow_seperated_package><![CDATA[0]]></allow_seperated_package>
        <associations>
            <cart_rows>
                <cart_row>
                    <id_product><![CDATA[{product_id}]]></id_product>
                    <id_product_attribute><![CDATA[0]]></id_product_attribute>
                    <id_address_delivery><![CDATA[{address_id}]]></id_address_delivery>
                    <id_customization><![CDATA[0]]></id_customization>
                    <quantity><![CDATA[1]]></quantity>
                </cart_row>
            </cart_rows>
        </associations>
    </cart>
</prestashop>
"""

    @staticmethod
    def update(cart_id, address_id, customer_id, product_id, quantity):
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <cart>
        <id><![CDATA[{cart_id}]]></id>
        <id_address_delivery><![CDATA[{address_id}]]></id_address_delivery>
        <id_address_invoice><![CDATA[{address_id}]]></id_address_invoice>
        <id_currency><![CDATA[1]]></id_currency>
        <id_customer><![CDATA[{customer_id}]]></id_customer>
        <id_lang><![CDATA[1]]></id_lang>
        <id_shop_group><![CDATA[1]]></id_shop_group>
        <id_shop><![CDATA[1]]></id_shop>
        <id_carrier><![CDATA[1]]></id_carrier>
        <id_guest><![CDATA[0]]></id_guest>
        <recyclable><![CDATA[0]]></recyclable>
        <gift><![CDATA[0]]></gift>
        <gift_message><![CDATA[]]></gift_message>
        <mobile_theme><![CDATA[0]]></mobile_theme>
        <delivery_option><![CDATA[]]></delivery_option>
        <secure_key><![CDATA[]]></secure_key>
        <allow_seperated_package><![CDATA[0]]></allow_seperated_package>
        <associations>
            <cart_rows>
                <cart_row>
                    <id_product><![CDATA[{product_id}]]></id_product>
                    <id_product_attribute><![CDATA[0]]></id_product_attribute>
                    <id_address_delivery><![CDATA[{address_id}]]></id_address_delivery>
                    <id_customization><![CDATA[0]]></id_customization>
                    <quantity><![CDATA[{quantity}]]></quantity>
                </cart_row>
            </cart_rows>
        </associations>
    </cart>
</prestashop>
"""