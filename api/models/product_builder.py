class ProductBuilder:
    @staticmethod
    def create(name="Test product", price=29.90, category_id=4):
        link_rewrite = name.lower().replace(" ", "-") if name else ""
        price_value = f"{price:.6f}" if isinstance(price, (int, float)) else price
        return f"""
<prestashop>
  <product>
    <id_category_default><![CDATA[{category_id}]]></id_category_default>
    <price><![CDATA[{price_value}]]></price>
    <active><![CDATA[1]]></active>
    <state><![CDATA[1]]></state>
    <available_for_order><![CDATA[1]]></available_for_order>
    <show_price><![CDATA[1]]></show_price>
    <visibility><![CDATA[both]]></visibility>
    <name>
      <language id="1"><![CDATA[{name}]]></language>
    </name>
    <link_rewrite>
      <language id="1"><![CDATA[{link_rewrite}]]></language>
    </link_rewrite>
  </product>
</prestashop>
"""

    @staticmethod
    def update(product_id, price=None, name=None):
        name = name or "Test product"
        link_rewrite = name.lower().replace(" ", "-")
        return f"""
<prestashop>
  <product>
    <id><![CDATA[{product_id}]]></id>
    <id_category_default><![CDATA[4]]></id_category_default>
    <price><![CDATA[{price:.6f}]]></price>
    <active><![CDATA[1]]></active>
    <state><![CDATA[1]]></state>
    <available_for_order><![CDATA[1]]></available_for_order>
    <show_price><![CDATA[1]]></show_price>
    <visibility><![CDATA[both]]></visibility>
    <name>
      <language id="1"><![CDATA[{name}]]></language>
    </name>
    <link_rewrite>
      <language id="1"><![CDATA[{link_rewrite}]]></language>
    </link_rewrite>
  </product>
</prestashop>
"""
