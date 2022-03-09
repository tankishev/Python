from .category import Category
from .topic import Topic
from .document import Document


class Storage:

    def __init__(self) -> None:
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category) -> None:
        return self.__class__.add_obj(category, self.categories)

    def add_topic(self, topic: Topic) -> None:
        return self.__class__.add_obj(topic, self.topics)

    def add_document(self, document: Document) -> None:
        return self.__class__.add_obj(document, self.documents)

    def edit_category(self, category_id: int, new_name: str) -> None:
        return self.__class__.edit_obj(category_id, self.categories, name=new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_folder: str) -> None:
        return self.__class__.edit_obj(topic_id, self.topics, new_topic=new_topic, new_storage_folder=new_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        return self.__class__.edit_obj(document_id, self.documents, file_name=new_file_name)

    def delete_category(self, category_id) -> None:
        return self.__class__.delete_obj_by_id(category_id, self.categories)

    def delete_topic(self, topic_id) -> None:
        return self.__class__.delete_obj_by_id(topic_id, self.topics)

    def delete_document(self, document_id) -> None:
        return self.__class__.delete_obj_by_id(document_id, self.documents)

    def get_document(self, document_id) -> Document:
        return next(el for el in self.documents if el.id == document_id)

    def __repr__(self):
        return '\n'.join([repr(doc) for doc in self.documents])

    @staticmethod
    def add_obj(obj: object, obj_list: list) -> None:
        if not any(el.id == obj.id for el in obj_list):
            obj_list.append(obj)

    @staticmethod
    def edit_obj(obj_id: int, obj_list: list, **kwargs):
        obj = next(el for el in obj_list if el.id == obj_id)
        return obj.edit(**kwargs)

    @staticmethod
    def delete_obj_by_id(obj_id: int, obj_list: list):
        try:
            obj = next(el for el in obj_list if el.id == obj_id)
            obj_list.remove(obj)
            return
        except StopIteration:
            return
