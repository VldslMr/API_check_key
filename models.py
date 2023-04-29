from pydantic import BaseModel


class Client(BaseModel):
    call: str = 'play'
    addr: str
    clientid: str
    app: str
    flashVer: str
    swfUrl: str
    tcUrl: str
    pageUrl: int
    name: str
