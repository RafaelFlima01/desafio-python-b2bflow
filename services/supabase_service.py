from supabase import create_client
import os

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

def buscar_contatos():
    response = (
        supabase
        .table("contatos")
        .select("*")
        .limit(3)
        .execute()
    )

    return response.data