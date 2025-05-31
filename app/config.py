import os
from pathlib import Path
from dotenv import load_dotenv

env_secrets = Path(__file__).resolve().parent.parent / 'app/secrets.env'
load_dotenv(dotenv_path=env_secrets)

env_properties = Path(__file__).resolve().parent.parent / 'app/properties.env'
load_dotenv(dotenv_path=env_properties)

def get(configuracion):
    value = os.getenv(configuracion)
    if value is None:
        raise ValueError(f'La configuración "{configuracion}" no está definida en el archivo .env')
    return value