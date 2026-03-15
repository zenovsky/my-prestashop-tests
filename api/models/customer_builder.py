
class CustomerBuilder:

    @staticmethod
    def create(lastname, firstname, email):
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <customer>
        <lastname><![CDATA[{lastname}]]></lastname>
        <firstname><![CDATA[{firstname}]]></firstname>
        <email><![CDATA[{email}]]></email>
        <passwd><![CDATA[test12345]]></passwd>
        <id_lang><![CDATA[1]]></id_lang>
        <id_shop><![CDATA[1]]></id_shop>
        <id_shop_group><![CDATA[1]]></id_shop_group>
        <id_default_group><![CDATA[3]]></id_default_group>
        <active><![CDATA[1]]></active>
        <deleted><![CDATA[0]]></deleted>
        <is_guest><![CDATA[0]]></is_guest>
        <id_gender><![CDATA[1]]></id_gender>
        <newsletter><![CDATA[0]]></newsletter>
        <optin><![CDATA[0]]></optin>
        <note><![CDATA[]]></note>
        <outstanding_allow_amount><![CDATA[0.000000]]></outstanding_allow_amount>
        <show_public_prices><![CDATA[0]]></show_public_prices>
        <max_payment_days><![CDATA[0]]></max_payment_days>
    </customer>
</prestashop>
"""

    @staticmethod
    def update(
        customer_id, 
        note,
        lastname,
        firstname,
        email
        ):
        hashed_password = "$2y$12$fweiUfwFpFYtsdv44XKKNu1DYi5w.rSTfqBJKIjdii8d3in25TuyK"

        return f"""<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <customer>
        <id><![CDATA[{customer_id}]]></id>
        <lastname><![CDATA[{lastname}]]></lastname>
        <firstname><![CDATA[{firstname}]]></firstname>
        <email><![CDATA[{email}]]></email>
        <birthday><![CDATA[1990-05-15]]></birthday>
        <passwd><![CDATA[{hashed_password}]]></passwd>
        <id_lang><![CDATA[1]]></id_lang>
        <id_shop><![CDATA[1]]></id_shop>
        <id_shop_group><![CDATA[1]]></id_shop_group>
        <id_default_group><![CDATA[3]]></id_default_group>
        <active><![CDATA[1]]></active>
        <deleted><![CDATA[0]]></deleted>
        <is_guest><![CDATA[0]]></is_guest>
        <id_gender><![CDATA[1]]></id_gender>
        <newsletter><![CDATA[0]]></newsletter>
        <optin><![CDATA[0]]></optin>
        <note><![CDATA[{note}]]></note>
        <outstanding_allow_amount><![CDATA[0.000000]]></outstanding_allow_amount>
        <show_public_prices><![CDATA[0]]></show_public_prices>
        <max_payment_days><![CDATA[0]]></max_payment_days>
    </customer>
</prestashop>
"""