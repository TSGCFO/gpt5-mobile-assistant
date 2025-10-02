# GPT-5 Mobile Assistant - Backend

Production-ready FastAPI backend with OpenAI GPT-5 integration featuring web search, code interpreter, reasoning, and dual-tier memory system.

## Features

### 🤖 OpenAI GPT-5 Integration
- **Responses API** with streaming support
- **Reasoning effort**: Configurable (low/medium/high)
- **Web Search**: Real-time web search with citations
- **Code Interpreter**: Python code execution sandbox
- **MCP Server Support**: Extensible with Model Context Protocol servers

### 💾 Dual-Tier Memory System
- **Long-term Memory**: PostgreSQL for persistent storage
- **Working Memory**: Redis for fast context retrieval (30-minute cache)
- Automatic cache invalidation
- Context window management

### 🔐 Authentication & Security
- HTTP Basic Authentication
- Bcrypt password hashing
- Rate limiting (60 requests/minute per user)
- Input validation with Pydantic
- SQL injection prevention
- CORS configuration

### 📊 Additional Features
- Structured JSON logging
- Comprehensive error handling
- Database migrations with Alembic
- Docker Compose for development
- Full API documentation (Swagger/ReDoc)

## Tech Stack

- **Framework**: FastAPI 0.115+
- **Python**: 3.11+
- **Database**: PostgreSQL 16
- **Cache**: Redis 7
- **ORM**: SQLAlchemy 2.0
- **Migrations**: Alembic
- **OpenAI**: openai==1.58.0+
- **Server**: Uvicorn (ASGI)

## Project Structure

```
backend/
├── app/
│   ├── api/v1/          # API endpoints
│   │   ├── auth.py      # Authentication
│   │   ├── chat.py      # Chat completions
│   │   ├── conversations.py  # Conversation management
│   │   └── health.py    # Health check
│   ├── core/            # Core configuration
│   │   ├── config.py    # Settings
│   │   ├── security.py  # Password hashing
│   │   ├── logging_config.py  # Logging setup
│   │   └── exceptions.py  # Custom exceptions
│   ├── models/          # Database models
│   │   ├── user.py
│   │   ├── conversation.py
│   │   └── message.py
│   ├── schemas/         # Pydantic schemas
│   │   ├── auth.py
│   │   ├── chat.py
│   │   └── conversation.py
│   ├── services/        # Business logic
│   │   ├── openai_service.py  # GPT-5 integration
│   │   ├── memory_service.py  # Memory management
│   │   ├── auth_service.py    # Authentication
│   │   └── mcp_service.py     # MCP integration
│   ├── middleware/      # Middleware
│   │   ├── auth_middleware.py  # Basic auth
│   │   └── rate_limit.py       # Rate limiting
│   ├── db/              # Database
│   │   └── database.py  # Connection & session
│   ├── utils/           # Utilities
│   │   ├── cache.py     # Redis operations
│   │   └── helpers.py   # Helper functions
│   └── main.py          # FastAPI app
├── migrations/          # Alembic migrations
├── tests/               # Unit tests
├── requirements.txt     # Dependencies
├── .env.example         # Environment template
├── alembic.ini         # Alembic config
└── README.md           # This file
```

## Setup Instructions

### Prerequisites

- Python 3.11 or higher
- PostgreSQL 16 or higher
- Redis 7 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Option 1: Local Development (Recommended)

#### 1. Install Dependencies

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 2. Setup Database & Redis

```bash
# Start PostgreSQL and Redis using Docker Compose
cd ..  # Go to project root
docker-compose up -d postgres redis

# Verify services are running
docker-compose ps
```

#### 3. Configure Environment

```bash
# Copy environment template
cd backend
cp .env.example .env

# Edit .env with your settings
# IMPORTANT: Add your OpenAI API key
```

**Required Environment Variables:**
```env
OPENAI_API_KEY=sk-proj-your-openai-api-key-here
DATABASE_URL=postgresql://gpt5user:gpt5password@localhost:5432/gpt5_assistant
REDIS_URL=redis://localhost:6379/0
```

#### 4. Run Database Migrations

```bash
# Create initial migration (first time only)
alembic revision --autogenerate -m "Initial migration"

# Apply migrations
alembic upgrade head
```

#### 5. Start the Server

```bash
# Development server with auto-reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Production server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

Server will be available at: `http://localhost:8000`

### Option 2: Docker Compose (Full Stack)

```bash
# Edit docker-compose.yml to uncomment backend service

# Start all services
docker-compose up -d

# View logs
docker-compose logs -f backend

# Stop services
docker-compose down
```

## API Endpoints

### Authentication

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/v1/auth/register` | Register new user | No |
| POST | `/api/v1/auth/verify` | Verify credentials | Yes (Basic) |
| GET | `/api/v1/auth/me` | Get current user | Yes (Basic) |

### Chat

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/v1/chat/completions` | Create chat completion | Yes (Basic) |
| POST | `/api/v1/chat/stream` | Stream chat completion | Yes (Basic) |

### Conversations

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/v1/chat/conversations` | List conversations | Yes (Basic) |
| POST | `/api/v1/chat/conversations` | Create conversation | Yes (Basic) |
| GET | `/api/v1/chat/conversations/{id}` | Get conversation | Yes (Basic) |
| DELETE | `/api/v1/chat/conversations/{id}` | Delete conversation | Yes (Basic) |
| GET | `/api/v1/chat/conversations/{id}/messages` | Get messages | Yes (Basic) |

### Health

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/v1/health` | Health check | No |

## API Documentation

Once the server is running, access:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Usage Examples

### 1. Register a User

```bash
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "SecurePass123"
  }'
```

### 2. Chat Completion (with Basic Auth)

```bash
curl -X POST http://localhost:8000/api/v1/chat/completions \
  -u "john_doe:SecurePass123" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What is the weather like in Paris today?",
    "use_web_search": true,
    "reasoning_effort": "medium"
  }'
```

### 3. Stream Chat Completion

```bash
curl -X POST http://localhost:8000/api/v1/chat/stream \
  -u "john_doe:SecurePass123" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Tell me about GPT-5"}
    ],
    "use_web_search": true
  }'
```

### 4. List Conversations

```bash
curl -X GET http://localhost:8000/api/v1/chat/conversations \
  -u "john_doe:SecurePass123"
```

## Configuration

### Environment Variables

All configuration is done via environment variables (`.env` file):

```env
# Application
APP_NAME=GPT5-Mobile-Assistant
DEBUG=False
LOG_LEVEL=INFO

# OpenAI
OPENAI_API_KEY=sk-proj-...
OPENAI_MODEL=gpt-5
OPENAI_REASONING_EFFORT=medium  # low, medium, high

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# Redis
REDIS_URL=redis://localhost:6379/0
REDIS_CACHE_TTL=1800  # 30 minutes

# CORS
CORS_ORIGINS=["http://localhost:19000"]

# Rate Limiting
RATE_LIMIT_PER_MINUTE=60

# Server
HOST=0.0.0.0
PORT=8000
WORKERS=1
```

## Testing

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_auth.py
```

## Database Management

### Create Migration

```bash
alembic revision --autogenerate -m "Description of changes"
```

### Apply Migrations

```bash
# Upgrade to latest
alembic upgrade head

# Upgrade to specific revision
alembic upgrade <revision_id>

# Downgrade one revision
alembic downgrade -1
```

### View Migration History

```bash
alembic history
alembic current
```

## Troubleshooting

### Database Connection Error

```bash
# Check PostgreSQL is running
docker-compose ps postgres

# Test connection
psql -h localhost -U gpt5user -d gpt5_assistant

# Restart PostgreSQL
docker-compose restart postgres
```

### Redis Connection Error

```bash
# Check Redis is running
docker-compose ps redis

# Test connection
redis-cli ping

# Restart Redis
docker-compose restart redis
```

### OpenAI API Error

- Verify your API key is correct in `.env`
- Check your OpenAI account has credits
- Ensure `gpt-5` model access (may need waitlist approval)

### Port Already in Use

```bash
# Find process using port 8000
# Windows
netstat -ano | findstr :8000
# Linux/Mac
lsof -i :8000

# Kill the process or use different port
uvicorn app.main:app --reload --port 8001
```

## Production Deployment

### Security Checklist

- [ ] Set `DEBUG=False`
- [ ] Use strong database passwords
- [ ] Enable HTTPS (use reverse proxy like Nginx)
- [ ] Set restrictive CORS origins
- [ ] Use environment-based secrets management
- [ ] Enable firewall rules
- [ ] Regular database backups
- [ ] Monitor API rate limits

### Recommended Setup

- **Reverse Proxy**: Nginx or Caddy
- **Process Manager**: systemd or supervisord
- **SSL**: Let's Encrypt
- **Monitoring**: Prometheus + Grafana
- **Logging**: ELK Stack or CloudWatch

### Example systemd Service

```ini
[Unit]
Description=GPT-5 Mobile Assistant API
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/path/to/backend
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
Restart=always

[Install]
WantedBy=multi-user.target
```

## Performance Optimization

### Redis Caching

Conversation context is cached for 30 minutes. Adjust TTL:

```env
REDIS_CACHE_TTL=3600  # 1 hour
```

### Database Connection Pool

Configure in `app/db/database.py`:

```python
engine = create_engine(
    settings.DATABASE_URL,
    pool_size=10,        # Permanent connections
    max_overflow=20,     # Overflow connections
    pool_pre_ping=True,  # Verify connections
)
```

### Uvicorn Workers

Increase workers for production:

```bash
uvicorn app.main:app --workers 4  # 2x CPU cores
```

## License

See main project LICENSE file.

## Support

For issues and questions:
- GitHub Issues: [Project Repository]
- Documentation: [API Docs](/docs)
