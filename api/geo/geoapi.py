from typing import Any

class GeoAPI:
    __apis__: dict[str, Any] = {}

    def __class_getitem__(cls, api_name: str) -> Any:
        return cls.__apis__[api_name]
    
    def __init_subclass__(cls):
        cls.__apis__[cls.__name__.lower()] = cls

    def __init__(self):
        self.__cache__: dict[str, tuple[str, str, str]] = {}

    async def __call__(self, ip: str) -> tuple[str, str, str]:
        if ip in self.__cache__:
            return self.__cache__[ip]
        self.__cache__[ip] = await self.__get__(ip)
        return self.__cache__[ip]

    async def __get__(self, ip: str) -> tuple[str, str, str]:
        raise NotImplementedError

    @classmethod
    @property
    def apis(cls) -> dict[str, Any]:
        return cls.__apis__
