# API de Chamados de Suporte

**Estudante:** José Wellington Rodrigues da Silva

## Objetivo

Criar a estrutura inicial de uma API de chamados de suporte com Python e Flask,
usando o uv para gerenciar o ambiente e as dependências.

Nesta etapa, a API possui apenas a rota inicial, que confirma que a aplicação
está em funcionamento. Ainda não há cadastro de chamados nem banco de dados.

## Pré-requisitos

- uv
- Python 3.12 ou superior

Caso o `uv` não esteja disponível (por exemplo, em um Codespace novo):

```bash
pip install uv
```

## Instalação das dependências

Na pasta do projeto, execute:

```bash
uv sync --locked
```

## Execução

```bash
uv run flask --app app run --host=0.0.0.0 --port=5000
```

Para encerrar a aplicação, pressione `Ctrl+C`.

## Rota inicial

| Método | Rota | Status | Content-Type       |
| ------ | ---- | ------ | ------------------ |
| GET    | `/`  | 200    | `application/json` |

Com a aplicação em execução, acesse <http://localhost:5000/> no navegador. No
Codespaces, abra o endereço da porta 5000 pela aba **Portas/Ports**.

Também é possível testar em outro terminal:

```bash
curl -i http://localhost:5000/
```

Resposta esperada, com status `200 OK`:

```json
{
  "mensagem": "API de chamados em funcionamento"
}
```
