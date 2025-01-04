from pydantic import BaseModel, AnyUrl
from httpx import URL

class WebsiteInput(BaseModel):
    url: AnyUrl
 
    class Config:
        arbitrary_types_allowed = True

class WebsiteAnalyser(BaseModel):
    industry: str
    company_size: str
    location: str


