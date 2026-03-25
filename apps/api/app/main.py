from fastapi import FastAPI


app = FastAPI(title="AIStart API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "project": "AIStart"}
