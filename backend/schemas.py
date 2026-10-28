from pydantic import BaseModel

class UserRegister(BaseModel):

    nom_complet: str
    telephone: str
    email: str
    pays: str
    ville: str
    mot_de_passe: str


class UserLogin(BaseModel):

    email: str
    mot_de_passe: str
