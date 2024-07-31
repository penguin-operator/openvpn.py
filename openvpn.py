#!/usr/bin/env python3.12
import sys
import asyncio
import clean
from cli import argparse
from api import VPNApi

def cli_help():
    print("Available APIs:")
    for api in VPNApi.apis:
        print(f"    {api}")

async def main(*args, **kv):
    match args, kv:
        case ["get", *apis], {**kv}:
            for api in apis:
                if api not in VPNApi.apis:
                    print(f"API {api} not found")
                    cli_help()
                    exit(1)
                api = VPNApi[api](**kv)
                for server in await api.get_servers():
                    print(server)
        case ["check", *paths], {}:
            ...
        case [*_] | ["help"]:
            print("Usage: openvpn.py get <api>_name [<api_name>...]")
            cli_help()

if __name__ == "__main__":
    args, kv = argparse(*sys.argv[1:])
    asyncio.run(main(*args, **kv))
    clean.clean()
