from fastapi import FastAPI
from schemas import UserRegister
from schemas import UserLogin

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

@app.get("/about")
def about():

    return {
        "nom": "DAS IA",
        "slogan":
        "L'intelligence africaine qui accompagne votre réussite."
    }

@app.post("/register")
def register(user: UserRegister):

    return {
        "message": "Utilisateur enregistré",
        "nom": user.nom_complet,
        "email": user.email
    }

@app.post("/login")
def login(user: UserLogin):

    return {
        "message": "Connexion réussie",
        "email": user.email
    }
