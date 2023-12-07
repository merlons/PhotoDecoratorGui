import shelve


class MyConfig:
    def __init__(self, file_path):
        self.file_path = file_path

    def get(self, key, default=None):
        with shelve.open(self.file_path) as data:
            kwargs = data.get("kwargs", {})
        return kwargs.get(key, default)

    def set(self, key, value):
        with shelve.open(self.file_path) as data:
            kwargs = data.get("kwargs", {})
            kwargs.update({key: value})
            data['kwargs'] = kwargs

    def update(self, kwargs: dict):
        with shelve.open(self.file_path) as data:
            kwargs_old = data.get("kwargs", {})
            kwargs_old.update(kwargs)
            data['kwargs'] = kwargs

    def all(self):
        with shelve.open(self.file_path) as data:
            kwargs = data.get("kwargs", {})
        return kwargs