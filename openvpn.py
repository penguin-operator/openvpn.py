#!/usr/bin/env python3.12
import sys
import asyncio
from util.cli import argparse
from apis import API

def cli_help():
    print("Usage: openvpn.py get <api>_name [<api_name>...]")
    print("Available APIs:")
    for api in API.apis:
        print(f"    {api}")

async def main(*args, **kv):
    match args:
        case ["get", *apis]:
            for api in apis:
                if api not in API.apis:
                    print(f"API {api} not found")
                    cli_help()
                    exit(1)
                api = API[api]()
                for server in await api.get_servers():
                    print(server)
        case ["check", *paths]:
            ...
        case [*_] | ["help"]:
            cli_help()

if __name__ == "__main__":
    args, kv = argparse(*sys.argv[1:])
    asyncio.run(main(*args, **kv))
