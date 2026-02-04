from fastapi import FastAPI
import httpx

app = FastAPI(
    title="second-service",
    description="performs some operations",
    docs_url="/second"
)


FIRST_SERVICE_URL = "http://first-service:8001"

@app.get("/second/health")
async def health():
    return "OK"

@app.on_event("startup")
async def load_first_openapi():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{FIRST_SERVICE_URL}/openapi.json")
        first_openapi = r.json()

    for path, methods in first_openapi["paths"].items():
        app.openapi()["paths"][f"/first{path}"] = methods
