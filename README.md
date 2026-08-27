# Python Backend API

A clean, modern REST API built with **FastAPI**.

## Features

- FastAPI + Uvicorn
- Pydantic v2 models & validation
- Settings via environment variables
- Automatic interactive docs (Swagger UI + ReDoc)
- CRUD example for "Items"
- Health check endpoint
- CORS enabled
- Ready for Render deployment (Python 3.12)

## Project Structure

```
backend/
├── app/
│   ├── api/
│   │   └── routes.py      # API endpoints
│   ├── core/
│   │   └── config.py      # Settings
│   ├── models/
│   │   └── schemas.py     # Pydantic schemas
│   └── main.py            # Application entrypoint
├── requirements.txt
├── .python-version        # Forces Python 3.12.8 on Render
├── runtime.txt
├── render.yaml
├── .gitignore
└── README.md
```

## Local Development

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- Swagger UI: http://localhost:8000/docs
- ReDoc:     http://localhost:8000/redoc

## Deploy to Render

### Important: Python Version

Render now defaults to **Python 3.14**. This project pins **Python 3.12.8** via:

- `.python-version`
- `runtime.txt`
- `PYTHON_VERSION` env var in `render.yaml`

### Option A – Blueprint (recommended)

1. Push this folder to GitHub (repo root should contain `requirements.txt`, `app/`, etc.).
2. Go to https://dashboard.render.com → **New** → **Blueprint**.
3. Connect the repository. Render will use `render.yaml`.

### Option B – Manual Web Service

1. Push to GitHub.
2. **New** → **Web Service** → connect the repo.
3. Settings:

| Setting            | Value                                              |
|--------------------|----------------------------------------------------|
| **Runtime**        | Python                                             |
| **Build Command**  | `pip install -r requirements.txt`                  |
| **Start Command**  | `uvicorn app.main:app --host 0.0.0.0 --port $PORT` |
| **Instance Type**  | Free                                               |

4. In **Environment** tab, add:

```
PYTHON_VERSION = 3.12.8
```

(Also recommended: `DEBUG=false`)

5. Click **Create Web Service**.

### After Deploy

Your API will be at:  
`https://<your-service-name>.onrender.com`

- Health: `/api/v1/health`
- Docs:   `/docs`

> Free tier services spin down after ~15 min of inactivity. First request after sleep can take 30–60 s.

## API Endpoints

| Method | Endpoint              | Description          |
|--------|-----------------------|----------------------|
| GET    | `/`                   | Welcome message      |
| GET    | `/api/v1/health`      | Health check         |
| GET    | `/api/v1/items`       | List all items       |
| POST   | `/api/v1/items`       | Create an item       |
| GET    | `/api/v1/items/{id}`  | Get item by ID       |
| PUT    | `/api/v1/items/{id}`  | Update an item       |
| DELETE | `/api/v1/items/{id}`  | Delete an item       |

## License

MIT
