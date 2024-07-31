import httpx

cache = {}

async def get(ip: str) -> tuple[str, str, str]:
    global cache
    
    if ip in cache:
        return cache[ip]

    async with httpx.AsyncClient() as client:
        data = await client.get(f"https://ipwho.is/{ip}")
        data = data.json()

    cache[ip] = (
        data["city"].lower().replace(' ', '_'),
        data["region"].lower().replace(' ', '_'),
        data["country"].lower().replace(' ', '_'),
    )
    return cache[ip]
