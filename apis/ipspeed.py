import asyncio
import json
import httpx
import bs4
import util.geo as geo
from .api import API
from .server import Server

class IpSpeed(API):
    url = "https://ipspeed.info/ovpn/"

    async def get_servers(self) -> list[Server]:
        async with httpx.AsyncClient() as client:
            data = (await client.get(self.url)).text
            soup = bs4.BeautifulSoup(data, "lxml")
        servers = []
        for tr in soup.find_all("tr")[2:]:
            servers.append(self.get_server(tr.td["data-sort"]))
        return await asyncio.gather(*servers)

    async def get_server(self, link: str) -> Server | None:
        host, proto, port = link.replace('.ovpn', '').split("_")
        try:
            city, region, country = await geo.get(host)
            return Server(host, city, region, country, proto, int(port), link)
        except json.decoder.JSONDecodeError:
            return None
