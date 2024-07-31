from typing import Any, Self
from .server import Server

class API:
    __apis__: dict[str, type[Self]] = {}

    def __init_subclass__(cls):
        cls.__apis__[cls.__name__.lower()] = cls

    def __class_getitem__(cls, api_name: str) -> type[Self]:
        if api_name not in cls.__apis__:
            raise KeyError(f'API["{api_name}"] not found')
        return cls.__apis__[api_name]
    
    @classmethod
    @property
    def apis(cls) -> dict[str, type[Self]]:
        return cls.__apis__

    async def get_servers(self) -> list[Server]:
        ...

    async def get_server(self, *args: Any) -> Server:
        ...
