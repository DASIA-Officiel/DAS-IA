from fastapi import FastAPI

app = FastAPI(
    title="DAS IA"
)

@app.get("/")
def accueil():
    return {
        "application": "DAS IA",
        "fondateur": "SORO DOTANA ABDOULAYE",
        "email": "contact@dasia.africa"
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }
