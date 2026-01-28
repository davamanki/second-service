from fastapi import FastAPI

app = FastAPI(
    title="second-service",
    description="performs some operations",
    docs_url="/second"
)

@app.get("/health")
async def health():
    return "OK"