from pydantic_ai import Agent
from bs4 import BeautifulSoup
import httpx
from models import WebsiteInput, WebsiteAnalyser

async def fetch_website_content(url: WebsiteInput) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(str(url.url), timeout=30)
        return response.text


async def parse_website_content(data: str) -> str:
    try:
        soup = BeautifulSoup(data, 'html.parser')
        for element in soup(['script', 'style', 'nav', 'footer']):
            element.decompose()
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text
    except Exception: 
        return ""


async def analyse_website(text: str | None) -> WebsiteAnalyser | None:
    agent = Agent(
                model="mistral:codestral-latest",
                deps_type=str,
                result_type=WebsiteAnalyser,
                system_prompt=
                    """You are an AI agent tasked with extracting key information from a website. Based on the content of the website, generate the following details:
                    Industry: Identify the industry the company belongs to (e.g., technology, healthcare, finance, etc.).
                    Company Size: Determine the size of the company (e.g., small, medium, large) based on available information such as employee count, scale of operations, or any other relevant details. If nothing is mentioned, state the value is "Not Available". Do not try and get creative in hallucinating this field.
                    Location: Identify the location(s) of the company (e.g., city, country, global presence) based on any details provided on the website. If the location is not mentioned, state the value is "Not Available". Do not try and get creative in hallucinating this field.
                    Use the information provided on the website and return concise outputs for each of these categories. If any information is missing or unclear, indicate that it is unavailable
                    """,
            )
    result = await agent.run(text)
    return result.data


async def analyser(url: WebsiteInput) -> WebsiteAnalyser | None:
    data: str = await fetch_website_content(url)
    text: str | None = await parse_website_content(data)
    analysed_data: WebsiteAnalyser | None = await analyse_website(text)
    return analysed_data

    
async def main():
    input_ = httpx.URL("https://ubuntu.com/")
    url: WebsiteInput = WebsiteInput(url=input_)
    analysed_data: WebsiteAnalyser | None = await analyser(url)
    print(analysed_data)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

