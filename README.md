# desafio-python-b2bflow

Este projeto lê contatos cadastrados no Supabase e envia mensagens personalizadas via Z-API no WhatsApp.

## Visão Geral

O fluxo da aplicação é simples:

1. Busca os contatos na tabela `contatos` do Supabase.
2. Envia uma mensagem personalizada para cada contato.
3. Exibe no terminal o status do envio.

## Estrutura da Tabela no Supabase

Crie a tabela `contatos` no seu banco com o SQL abaixo:

```sql
create table contatos (
    id bigint generated always as identity primary key,
    nome text not null,
    telefone text not null
);
```

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com base no `.env.example` e preencha com suas credenciais:

```env
SUPABASE_URL=seu_url_do_supabase
SUPABASE_KEY=sua_chave_do_supabase

ZAPI_INSTANCE_ID=sua_instancia_zapi
ZAPI_TOKEN=seu_token_zapi
ZAPI_CLIENT_TOKEN=sua_client_token_zapi
```

## Instalação

Instale as dependências com:

```bash
pip install -r requirements.txt
```

## Execução

Para rodar o projeto:

```bash
python main.py
```

## Mensagem Enviada

O script envia a seguinte mensagem personalizada para cada contato:

```text
Olá, <nome_contato> tudo bem com você?
```