# cyberplanner-back

Backend FastAPI do CyberPlanner com arquitetura MVC (Model-View-Controller) adaptada para API REST.

## Arquitetura

```text
app/
	api/
		router.py              # Composicao central de rotas
	controllers/
		chat_controller.py     # Camada HTTP (request/response)
	core/
		config.py              # Configuracoes e variaveis de ambiente
		exceptions.py          # Excecoes de dominio/integracao
	models/
		chat_models.py         # Schemas Pydantic (entrada/saida)
	services/
		chat_service.py        # Regras de negocio + integracao Gemini
	main.py                  # Bootstrap da aplicacao
```

## Requisitos

- Python 3.11+

## Instalacao

```bash
pip install -r requirements.txt
cp .env.example .env
```

Depois, ajuste o arquivo `.env` com sua chave:

```env
GEMINI_API_KEY=sua_chave_aqui
GEMINI_MODEL=gemini-2.5-flash
```

## Executar

```bash
uvicorn app.main:app --reload
```

## Docker

Build da imagem:

```bash
docker build -t cyberplanner-back .
```

Execucao local do container:

```bash
docker run --rm -p 10000:10000 --env-file .env cyberplanner-back
```

## Deploy no Render

- Crie um novo Web Service a partir deste repositorio
- Configure o ambiente como Docker
- Defina as variaveis de ambiente `GEMINI_API_KEY` e `GEMINI_MODEL`
- O Render fornecera a variavel `PORT`, e o container ja esta preparado para escuta dinamica

## Endpoints

- `GET /health`: status da API
- `POST /chat`: proxy para Gemini com personalidade de agenda

Exemplo de request para `POST /chat`:

```json
{
	"pergunta": "Organize meus estudos e treino sem conflitos",
	"modo": "gestor"
}
```

Resposta esperada:

```json
{
	"resposta": "...",
	"modo_usado": "gestor"
}
```

## Boas praticas aplicadas

- Separacao de camadas (controller/service/models/core)
- Tratamento de erros de integracao externa
- Configuracao centralizada via ambiente
- Tipagem forte com Pydantic
- Endpoint de health check para observabilidade