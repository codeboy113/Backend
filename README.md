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
- Ready for Render deployment

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

### Option A – Blueprint (recommended)

1. Push this repo to GitHub / GitLab / Bitbucket.
2. Go to [https://dashboard.render.com](https://dashboard.render.com) → **New** → **Blueprint**.
3. Connect the repository.
4. Render will detect `render.yaml` and create the service automatically.

### Option B – Manual Web Service

1. Push this repo to GitHub / GitLab / Bitbucket.
2. Go to [https://dashboard.render.com](https://dashboard.render.com) → **New** → **Web Service**.
3. Connect the repository and select the `backend` folder (or root if this is the whole repo).
4. Use these settings:

| Setting          | Value                                              |
|------------------|----------------------------------------------------|
| **Runtime**      | Python                                             |
| **Build Command**| `pip install -r requirements.txt`                  |
| **Start Command**| `uvicorn app.main:app --host 0.0.0.0 --port $PORT` |
| **Instance Type**| Free                                               |

5. Add Environment Variables (optional):

```
APP_NAME=Python Backend API
APP_VERSION=1.0.0
DEBUG=false
API_PREFIX=/api/v1
```

6. Click **Create Web Service**.

### After Deploy

Your API will be available at:
`https://<your-service-name>.onrender.com`

Useful endpoints:
- Health: `https://<your-service-name>.onrender.com/api/v1/health`
- Docs:   `https://<your-service-name>.onrender.com/docs`

> **Note:** Free tier services spin down after ~15 min of inactivity. The first request after sleep may take 30–60 seconds.

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

### Example: Create an item

```bash
curl -X POST https://<your-service>.onrender.com/api/v1/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Laptop", "description": "A powerful laptop", "price": 1299.99}'
```

## Configuration

Create a `.env` file for local development (optional):

```env
APP_NAME="My Awesome API"
APP_VERSION="1.0.0"
DEBUG=true
API_PREFIX="/api/v1"
HOST=0.0.0.0
PORT=8000
```

## License

MIT
