import httpx
from .geoapi import GeoAPI

class IpWhois(GeoAPI):
    async def __seek__(self, ip: str) -> tuple[str, str, str]:
        async with httpx.AsyncClient() as client:
            data = await client.get(f"https://ipwho.is/{ip}")
            data = data.json()

        return (
            data["city"].lower().replace(' ', '_'),
            data["region"].lower().replace(' ', '_'),
            data["country"].lower().replace(' ', '_'),
        )
