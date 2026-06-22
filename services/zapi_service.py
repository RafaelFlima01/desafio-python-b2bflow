import os
import requests

def enviar_mensagem(telefone, nome):
    url = (
        f"https://api.z-api.io/instances/"
        f"{os.getenv('ZAPI_INSTANCE_ID')}/token/"
        f"{os.getenv('ZAPI_TOKEN')}/send-text"
    )

    payload = {
        "phone": telefone,
        "message": f"Olá, {nome} tudo bem com você?"
    }

    headers = {
        "Client-Token": os.getenv("ZAPI_CLIENT_TOKEN")
    }

    response = requests.post(url, json=payload, headers=headers)

    return response