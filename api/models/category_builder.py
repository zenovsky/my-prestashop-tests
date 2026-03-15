class CategoryBuilder:
    @staticmethod
    def create(
        name="Test Category",
        description="Testing API",
        meta_title="Test API",
        meta_description="Testing for API",
        parent_id=0,
        active_status="1",
    ):
        link_rewrite = name.lower().replace(" ", "-")

        return f"""<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <category>
        <id_parent><![CDATA[{parent_id}]]></id_parent>

        <name>
            <language id="1"><![CDATA[{name}]]></language>
        </name>

        <link_rewrite>
            <language id="1"><![CDATA[{link_rewrite}]]></language>
        </link_rewrite>

        <active><![CDATA[{active_status}]]></active>

        <description>
            <language id="1"><![CDATA[{description}]]></language>
        </description>

        <meta_title>
            <language id="1"><![CDATA[{meta_title}]]></language>
        </meta_title>

        <meta_description>
            <language id="1"><![CDATA[{meta_description}]]></language>
        </meta_description>

        <id_shop_default><![CDATA[1]]></id_shop_default>
        <is_root_category><![CDATA[0]]></is_root_category>
        <redirect_type><![CDATA[404]]></redirect_type>
        <id_type_redirected><![CDATA[0]]></id_type_redirected>

    </category>
</prestashop>
"""

    @staticmethod
    def update(category_id, active_status, name="Test Category"):
        link_rewrite = name.lower().replace(" ", "-")

        return f"""<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <category>

        <id><![CDATA[{category_id}]]></id>

        <id_parent><![CDATA[2]]></id_parent>

        <name>
            <language id="1"><![CDATA[{name}]]></language>
        </name>

        <link_rewrite>
            <language id="1"><![CDATA[{link_rewrite}]]></language>
        </link_rewrite>

        <active><![CDATA[{active_status}]]></active>

        <id_shop_default><![CDATA[1]]></id_shop_default>
        <is_root_category><![CDATA[0]]></is_root_category>
        <redirect_type><![CDATA[404]]></redirect_type>
        <id_type_redirected><![CDATA[0]]></id_type_redirected>

    </category>
</prestashop>
"""
