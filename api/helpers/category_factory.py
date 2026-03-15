import logging

from api.models.category_builder import CategoryBuilder
from utils.decorators import log_action

logger = logging.getLogger(__name__)

class CategoryFactory:

    def __init__(self, categories_api):
        self.api = categories_api
        self._ids = []

    @log_action
    def create(
        self,
        name="Test Category",
        description="Testing API",
        meta_title="Test API",
        meta_description="Testing for API",
        active_status="1"
        ):
        xml = CategoryBuilder.create(
            name=name,
            description=description,
            meta_title=meta_title,
            meta_description=meta_description,
            active_status=active_status
        )
        category_id = self.api.create(xml)
        self._ids.append(category_id)
        return {
            "category_id": category_id,
            "name": name,
            "active_status": active_status
        }
    
    @log_action
    def get(self, category_id):
        response = self.api.get(category_id)
        return response    

    @log_action
    def update(self, category_id, new_name=None, new_active_status=None):
        xml = CategoryBuilder.update(
            category_id=category_id,
            name=new_name,
            active_status=new_active_status
        )
        self.api.update(category_id, xml)
        updated_data = self.api.get(category_id)
        if new_active_status:
            assert updated_data['active_status'] == new_active_status
        return updated_data    

    @log_action
    def delete(self, category_id):
        self.api.delete(category_id)
        try:
            self.api.get(category_id)
            raise AssertionError(f"Category {category_id} still exists after DELETE request!")
        except AssertionError as e:
            if "404" in str(e):
                logger.info(f"Confirmed: Category {category_id} is no longer accessible (404).")
            else:
                raise e    

    @log_action
    def cleanup(self):
        for pid in self._ids[:]:
            try:
                self.api.delete(pid)
                logger.info(f"Category cleanup: {pid}")
            except Exception:
                pass
            self._ids.remove(pid)