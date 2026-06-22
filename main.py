from dotenv import load_dotenv
from services.supabase_service import buscar_contatos
from services.zapi_service import enviar_mensagem

load_dotenv()

def main():
    contatos = buscar_contatos()

    if not contatos:
        print("Nenhum contato encontrado.")
        return

    for contato in contatos:
        try:
            resposta = enviar_mensagem(
                contato["telefone"],
                contato["nome"]
            )

            print(
                f"Mensagem enviada para "
                f"{contato['nome']} - "
                f"Status: {resposta.status_code}"
            )

        except Exception as erro:
            print(
                f"Erro ao enviar para "
                f"{contato['nome']}: {erro}"
            )

if __name__ == "__main__":
    main()