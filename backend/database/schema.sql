CREATE TABLE utilisateurs (

    id SERIAL PRIMARY KEY,

    nom_complet VARCHAR(200),

    telephone VARCHAR(50),

    email VARCHAR(150) UNIQUE,

    pays VARCHAR(100),

    ville VARCHAR(100),

    mot_de_passe VARCHAR(255),

    role VARCHAR(50),

    abonnement VARCHAR(50)

);
