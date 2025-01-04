# FastAPI Website Scraping App

This application extracts details like industry, company size, and location from the homepage of a website. This API uses Mistral AI Codestral:latest API to generate the details.

## Requirements

- Python 3.9+
- FastAPI
- Uvicorn
- BeautifulSoup
- requests
- dotenv (optional)

## Setup

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/website-scraping-fastapi.git
    cd website-scraping-fastapi
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Export the following environment variables by running the following commands: 
    ```
    export SECRET_KEY=your_secret_key_here
    
    export MISTRAL_API_KEY=your_mistral_api_key_here
    ```

4. Run the application:
    ```
    uvicorn app:app --reload
    ```

5. Access the API at `http://localhost:8000`

6. Optionally, you can use the provided Dockerfile to build a Docker image and run the application in a container.

    Build the Docker image:
    ```
    docker build -t website-analyser-api .
    ```

    Run the Docker container and pass the environment variables:
    ```
    docker run -d --name website-analyser-api -p 8000:8000 -e AUTH_KEY=your_secret_key_here -e MISTRAL_API_KEY=your_mistrap_api_key_here website-analyser
    ```

## Endpoints

- `POST /scrape`: Accepts a URL and returns the extracted details.
  Example request:
    ```
    curl -X 'POST' \
        'http://localhost:8000/scrape' \
        -H 'Authorization: Bearer abcdefghijklmno' \
        -H 'Content-Type: application/json' \
        -d '{
            "url": "https://example.com"
        }'
  ```


