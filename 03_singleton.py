class AppConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db_url=None):
        if not hasattr(self, "db_url"):
            self.db_url = db_url or "sqlite://local.db"


config1 = AppConfig("postgres://prod")
config2 = AppConfig("otro")  # no cambia, sigue siendo el primero
print(config1.db_url)  # postgres://prod
print(config2.db_url)  # postgres://prod
print(config1 is config2)  # True
