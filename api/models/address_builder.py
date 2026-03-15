class AddressBuilder:

    @staticmethod
    def create(customer_id):
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <address>
        <id_customer><![CDATA[{customer_id}]]></id_customer>
        <id_country><![CDATA[8]]></id_country>
        <alias><![CDATA[test-address]]></alias>
        <lastname><![CDATA[Test]]></lastname>
        <firstname><![CDATA[User]]></firstname>
        <address1><![CDATA[Test address]]></address1>
        <postcode><![CDATA[424242]]></postcode>
        <city><![CDATA[Test City]]></city>
        <phone><![CDATA[424242]]></phone>
    </address>
</prestashop>
"""
    
    def update(address_id, customer_id, phone_mobile):
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <address>
        <id><![CDATA[{address_id}]]></id>
        <id_customer><![CDATA[{customer_id}]]></id_customer>
        <id_country><![CDATA[8]]></id_country>
        <alias><![CDATA[test-address]]></alias>
        <lastname><![CDATA[Test]]></lastname>
        <firstname><![CDATA[User]]></firstname>
        <address1><![CDATA[Test address]]></address1>
        <postcode><![CDATA[424242]]></postcode>
        <city><![CDATA[Test City]]></city>
        <phone><![CDATA[424242]]></phone>
        <phone_mobile><![CDATA[{phone_mobile}]]></phone_mobile>
    </address>
</prestashop>
"""    