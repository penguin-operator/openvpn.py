class Server:
    def __init__(self, host: str, city: str, region: str, country: str, proto: str, port: int, link: str):
        self.host = host
        self.city = city
        self.port = port
        self.link = link
        self.region = region
        self.country = country
        self.proto = proto

    def __iter__(self):
        yield self.host
        yield self.city
        yield self.region
        yield self.country
        yield self.proto
        yield self.port
        yield self.link

    def __repr__(self) -> str:
        return f"{self.proto.upper()} server {self.host}:{self.port} locates in ({self.city}, {self.region}, {self.country})"

    def __str__(self) -> str:
        return self.__repr__()
