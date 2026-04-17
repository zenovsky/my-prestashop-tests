import pytest

from api.api_client import APIClient
from api.endpoints.addresses import AddressesAPI
from api.endpoints.carts import CartsAPI
from api.endpoints.categories import CategoriesAPI
from api.endpoints.customers import CustomersAPI
from api.endpoints.orders import OrdersAPI
from api.endpoints.products import ProductsAPI
from api.helpers.address_factory import AddressFactory
from api.helpers.cart_factory import CartFactory
from api.helpers.category_factory import CategoryFactory
from api.helpers.customer_factory import CustomerFactory
from api.helpers.order_factory import OrderFactory
from api.helpers.product_factory import ProductFactory
from api.scenarios.address_scenarios import AddressScenario
from api.scenarios.cart_scenarios import CartScenario
from api.scenarios.category_scenarios import CategoryScenario
from api.scenarios.customer_scenarios import CustomerScenario
from api.scenarios.order_scenarios import OrderScenario
from api.scenarios.product_scenarios import ProductScenario


@pytest.fixture(scope="session")
def api_client(base_url):
    api_url = f"{base_url.rstrip('/')}/api"
    return APIClient(base_url=api_url)


@pytest.fixture
def products_api(api_client):

    return ProductsAPI(api_client)


@pytest.fixture
def products_factory(products_api):
    factory = ProductFactory(products_api)
    yield factory
    factory.cleanup()


@pytest.fixture
def categories_api(api_client):
    return CategoriesAPI(api_client)


@pytest.fixture
def categories_factory(categories_api):
    factory = CategoryFactory(categories_api)
    yield factory
    factory.cleanup()


@pytest.fixture
def customers_api(api_client):
    return CustomersAPI(api_client)


@pytest.fixture
def customers_factory(customers_api):
    factory = CustomerFactory(customers_api)
    yield factory
    factory.cleanup()


@pytest.fixture
def addresses_api(api_client):
    return AddressesAPI(api_client)


@pytest.fixture
def addresses_factory(addresses_api, customers_factory):
    factory = AddressFactory(addresses_api, customers_factory)
    yield factory
    factory.cleanup()


@pytest.fixture
def carts_api(api_client):
    return CartsAPI(api_client)


@pytest.fixture
def cart_factory(carts_api, products_factory, customers_factory, addresses_factory):
    factory = CartFactory(carts_api, customers_factory, addresses_factory, products_factory)
    yield factory
    factory.cleanup()


@pytest.fixture
def orders_api(api_client):
    return OrdersAPI(api_client)


@pytest.fixture
def order_factory(orders_api, customers_factory, addresses_factory, cart_factory):
    factory = OrderFactory(orders_api, customers_factory, addresses_factory, cart_factory)
    yield factory
    factory.cleanup()


@pytest.fixture
def product_scenario(products_factory):
    return ProductScenario(products_factory)


@pytest.fixture
def category_scenario(categories_factory):
    return CategoryScenario(categories_factory)


@pytest.fixture
def customer_scenario(customers_factory):
    return CustomerScenario(customers_factory)


@pytest.fixture
def address_scenario(addresses_factory):
    return AddressScenario(addresses_factory)


@pytest.fixture
def cart_scenario(cart_factory):
    return CartScenario(cart_factory)


@pytest.fixture
def order_scenario(order_factory):
    return OrderScenario(order_factory)

@pytest.fixture(autouse=True)
def clear_api_history(api_client):
    api_client.request_history.clear()
    yield                  
