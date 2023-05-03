from typing import Optional

from pydantic import BaseModel


class ConnectData(BaseModel):
    call: Optional[str]
    addr: Optional[str]
    clientid: Optional[str]
    app: Optional[str]
    flashver: Optional[str]
    swfurl: Optional[str]
    tcurl: Optional[str]
    pageurl: Optional[str]
    name: Optional[str]
