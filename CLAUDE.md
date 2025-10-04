# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Full-stack mobile application with Expo React Native frontend and FastAPI backend, powered by OpenAI GPT-5 Responses API. Features dual-tier memory system, web search, code interpreter, and HTTP Basic Authentication.

**Stack:**

- Backend: FastAPI + Python 3.11+ + PostgreSQL + Redis
- Frontend: Expo SDK 54 + React Native 0.81 + React 19.1 + TypeScript + Redux
- AI: OpenAI GPT-5 (Responses API) with reasoning_effort="medium"
- Architecture: React Native New Architecture enabled

## Architecture

### Backend Service Layer Pattern

The backend follows a clean service-oriented architecture with strict separation of concerns:

**Request Flow:**

```
HTTP Request → Middleware (auth/rate-limit) → API Endpoint → Service Layer → Database/Cache
```

**Key Patterns:**

1. **Services as Dependencies**: All business logic lives in services (`openai_service.py`, `memory_service.py`, `auth_service.py`, `mcp_service.py`). API endpoints should be thin wrappers that inject services via FastAPI's `Depends()`.

2. **Dual-Tier Memory System**:
   - **Long-term**: PostgreSQL stores all conversation history
   - **Working Memory**: Redis caches conversation context (30min TTL)
   - Memory service handles cache invalidation automatically on writes
   - Cache key pattern: `conv:{conversation_id}:context`

3. **Authentication Flow**: HTTP Basic Auth via `get_current_user()` dependency. Credentials sent with every request, validated against database, no session/token management needed.

4. **Password Security**: Uses PassLib's `bcrypt_sha256` for password hashing.
   - **Algorithm**: bcrypt_sha256 (pre-hashes with HMAC-SHA256 before bcrypt)
   - **Rounds**: 12 (PassLib default, targets ~300ms per hash)
   - **Password Length**: Supports passwords of ANY length (no 72-byte bcrypt limitation)
   - **Security**: Enhanced security vs plain bcrypt (fully mixes all password bytes)
   - **Configuration**: `backend/app/core/security.py`
   - **Documentation**: See `Docs/passlib/` for complete PassLib reference (77 files)

5. **Streaming Architecture**: SSE (Server-Sent Events) for streaming responses. The `/chat/stream` endpoint uses async generators to yield OpenAI events in real-time.

### OpenAI Integration Specifics

**Responses API Usage:**

```python
response = await client.responses.create(
    model="gpt-5",
    reasoning={"effort": "medium"},  # Configurable: low/medium/high
    tools=[
        {"type": "web_search"},
        {"type": "code_interpreter", "container": {"type": "auto"}}
    ],
    input=messages,
    stream=True  # For streaming
)
```

**Key Points:**

- Use `reasoning_effort` parameter (not `reasoning_level`)
- Code interpreter requires container config with `type: "auto"`
- Web search returns citations in `annotations` with `type: "url_citation"`
- Streaming events: `response.output_text.delta`, `response.completed`
- Reasoning tokens are billed but not retained in context

### Database Models

Three core models with cascade deletion:

- `User` → `Conversation` → `Message`
- All use UUID primary keys
- `Message.metadata` is JSONB for flexible storage (tokens, citations, tool_calls)

## Development Commands

### Backend Setup & Running

```bash
# Initial setup
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Start infrastructure
docker-compose up -d postgres redis

# Environment setup
cp .env.example .env
# Edit .env - MUST set OPENAI_API_KEY

# Database migrations
alembic revision --autogenerate -m "description"
alembic upgrade head

# Run development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Run production server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Frontend Setup & Running

```bash
# Initial setup
cd frontend
npm install --legacy-peer-deps  # React 19 peer dependency conflicts

# Configure API URL
cp .env.example .env
# Edit EXPO_PUBLIC_API_BASE_URL with your machine's IP

# Start Expo dev server (clears cache on first run after upgrade)
npm start -- --clear

# Run on specific platform
npm run android  # or 'ios' or 'web'

# Lint code
npm run lint

# Type check
npx tsc --noEmit
```

### Database Management

```bash
# View migration history
alembic history
alembic current

# Rollback one migration
alembic downgrade -1

# Create new migration after model changes
alembic revision --autogenerate -m "add column X to table Y"
alembic upgrade head
```

### Testing & Debugging

```bash
# Backend tests
cd backend
pytest
pytest tests/test_auth.py -v  # Single file

# View API docs (when server running)
# http://localhost:8000/docs (Swagger)
# http://localhost:8000/redoc

# Check service health
curl http://localhost:8000/api/v1/health
```

## Common Operations

### Adding a New API Endpoint

1. Define Pydantic schema in `app/schemas/`
2. Add endpoint to appropriate router in `app/api/v1/`
3. Use services via `Depends()` - never call database directly
4. Add authentication with `current_user: User = Depends(get_current_user)`
5. Include router in `app/main.py`

Example:

```python
@router.post("/new-endpoint")
async def new_endpoint(
    request: NewRequestSchema,
    current_user: User = Depends(get_current_user),
    service: MyService = Depends(get_service)
):
    result = await service.process(request, current_user)
    return result
```

### Adding OpenAI Tool Support

Tools are configured in `openai_service.py`. To add a new tool:

1. Add tool dict to `tools` array in `create_response()` or `create_streaming_response()`
2. Handle tool output in `_extract_citations()` or add new extraction method
3. Store tool results in `Message.metadata` when saving

### Working with Memory Service

```python
# Get conversation context (checks cache first)
context = await memory_service.get_conversation_context(conv_id, limit=20)

# Save message (invalidates cache automatically)
message = await memory_service.save_message(
    conversation_id=conv_id,
    role="assistant",
    content=text,
    metadata={"usage": {...}, "citations": [...]}
)

# Clear cache manually
await memory_service.clear_conversation_cache(conv_id)
```

## Configuration

### Environment Variables (Backend)

Critical settings in `.env`:

- `OPENAI_API_KEY` - Required for GPT-5 access
- `DATABASE_URL` - PostgreSQL connection string
- `REDIS_URL` - Redis connection (default: localhost:6379)
- `OPENAI_REASONING_EFFORT` - "low", "medium", or "high"
- `CORS_ORIGINS` - JSON array or comma-separated list
- `RATE_LIMIT_PER_MINUTE` - Per-user API rate limit

### Environment Variables (Frontend)

- `EXPO_PUBLIC_API_BASE_URL` - Backend API URL
  - Physical device: Use machine's network IP (e.g., `http://192.168.1.100:8000/api/v1`)
  - Android emulator: Use `http://10.0.2.2:8000/api/v1`
  - iOS simulator: Use `http://localhost:8000/api/v1`

## Frontend Configuration

### Expo SDK 54

This project uses Expo SDK 54 with the following key features:

**React Native New Architecture:**
- Enabled by default in `app.json` (`newArchEnabled: true`)
- Better performance and modern React features
- SDK 54 is the final release supporting Legacy Architecture
- SDK 55+ will only support New Architecture

**ESLint Configuration:**
- Uses ESLint 9.x with Flat Config format (`eslint.config.js`)
- Legacy `.eslintrc.js` format no longer supported
- Configuration includes Node.js globals for metro.config.js and babel.config.js
- Run `npm run lint` to check code quality

**TypeScript:**
- TypeScript 5.9.2
- `moduleResolution: "bundler"` for SDK 54 compatibility
- Path aliases configured (@/, @/components/*, etc.)

**Key SDK 54 Changes:**
- React 19.1.0 (from 18.3.1)
- React Native 0.81 (from 0.76)
- Precompiled React Native for iOS (faster builds)
- Android targets API 36 (Android 16)
- Edge-to-edge always enabled on Android
- Experimental autolinking module resolution enabled

**Documentation:**
- See `Docs/expo-sdk-54-upgrade.md` for complete upgrade guide
- See `Docs/expo-eslint-config.md` for ESLint configuration details

### Dependencies

**Critical peer dependencies:**
- `react-dom@19.1.0` - Required by react-native-web
- `react-native-worklets@0.5.1` - Required by react-native-reanimated v4

**Install with:**
```bash
npm install --legacy-peer-deps
```

The `--legacy-peer-deps` flag is required due to React 19 peer dependency conflicts.

## Troubleshooting

**Expo Doctor Checks:**

Run diagnostics to check for compatibility issues:
```bash
npx expo-doctor@latest
```

**OpenAI API Errors:**

- Verify API key has GPT-5 access (may require waitlist)
- Check `reasoning_effort` is one of: low/medium/high
- For streaming, ensure async iteration over response

**Database Connection Issues:**

- Verify PostgreSQL is running: `docker-compose ps postgres`
- Test connection: `psql -h localhost -U gpt5user -d gpt5_assistant`
- Check `DATABASE_URL` format in `.env`

**Redis Connection Issues:**

- Verify Redis is running: `docker-compose ps redis`
- Test: `redis-cli ping` (should return PONG)

**Frontend Can't Connect to Backend:**

- Backend MUST be accessible on network, not just localhost
- Add frontend origin to `CORS_ORIGINS` in backend `.env`
- For Android emulator, use `10.0.2.2` not `localhost`
- Check firewall allows connections on port 8000

**Migration Conflicts:**

- If migration fails, check `alembic_version` table in database
- Rollback: `alembic downgrade -1`
- Delete problematic migration file and regenerate

## Code Conventions

- All services use async/await pattern
- Database sessions injected via `Depends(get_db)`
- Never commit database passwords or API keys
- Log at appropriate levels: DEBUG for cache hits, INFO for operations, ERROR for failures
- Use custom exceptions from `app.core.exceptions` (e.g., `raise AuthenticationError()`)
- Type hints required on all function signatures
- Pydantic models for all API request/response validation

## API Authentication

Frontend must send Basic Auth header with every request:

```typescript
const credentials = btoa(`${username}:${password}`);
headers: { Authorization: `Basic ${credentials}` }
```

Credentials stored securely in `expo-secure-store` on device.

- Before replying to any user message, it is essential to take the time to thoroughly review and examine the contents of the document located at @Docs\expo-llms-full.txt, along with all relevant and pertinent files that can be found in the directory @Docs\responses-api\. It is of utmost importance to carefully analyze the user message to avoid making any assumptions that could potentially lead to the dissemination of misinformation. Confirm all information by cross-referencing it meticulously with the contents of @Docs\expo-llms-full.txt and the various files located in @Docs\responses-api\. Repeat this validation process with great attention to detail prior to making any edits to existing files, creating new files, or implementing any other types of changes that may be necessary. Once you have completed the task at hand, conduct a final and thorough validation of the modifications that were made to ensure they are accurate, consistent, and meet all required standards.

Example of validation steps:

1. Review the relevant documents thoroughly and comprehensively.
2. Analyze the user message carefully and critically without making any assumptions.
3. Confirm all information against the documents provided to ensure accuracy.
4. Implement necessary changes based on your detailed analysis.
5. Validate the changes again after implementation to ensure they are accurate and consistent.

- @.mcp.json is where MCP servers are configured for claude code only.
