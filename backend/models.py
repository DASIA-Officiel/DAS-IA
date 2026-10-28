from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Utilisateur(Base):

    __tablename__ = "utilisateurs"

    id = Column(Integer, primary_key=True)

    nom_complet = Column(String(200))

    telephone = Column(String(50))

    email = Column(String(150), unique=True)

    pays = Column(String(100))

    ville = Column(String(100))

    mot_de_passe = Column(String(255))

    role = Column(String(50))

    abonnement = Column(String(50))
