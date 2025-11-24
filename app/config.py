import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '_1Zj0xYQ0FJQqbdj_Wp_IZG61j9foReI0fhSnadgk2suq8K-qaofXJeHLGp1Vd38J0A'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "postgresql://admin:3132@localhost/pokemon_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
