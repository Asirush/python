from typing import Any

class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs) -> object:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__initialized = False
        return cls.instance
    
    def __init__(self, user, password, port) -> None:
        if not self.__initialized:
            self.user = user
            self.password = password
            self.port = port
            self.__initialized = True

    def __del__(self) -> None:
        DataBase.__instance = None

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self.__instance is not None:
            raise TypeError("This class is a Singleton")