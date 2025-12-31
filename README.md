# FastAPI Microservice Template

Production-ready FastAPI microservice template with PostgreSQL, Redis, JWT authentication, Docker, and comprehensive testing. A complete backend starter for scalable applications.

## 🎯 Features

### Core Stack
- **FastAPI** - Modern, fast web framework with automatic API documentation
- **PostgreSQL** - Robust relational database with SQLAlchemy ORM
- **Redis** - High-performance caching and session storage
- **Docker** - Containerization for consistent environments
- **Pytest** - Comprehensive test suite with 80%+ coverage

### Security & Authentication
- JWT (JSON Web Tokens) authentication
- Password hashing with bcrypt
- Protected routes with dependency injection
- Token refresh mechanism

### Database
- SQLAlchemy ORM with async support
- Alembic migrations for schema management
- Proper connection pooling
- Transaction management

### Best Practices
- Modular architecture (routes, models, schemas, CRUD)
- Environment-based configuration
- Structured logging
- Error handling middleware
- CORS configuration
- API versioning ready

### Developer Experience
- Automatic API documentation (Swagger UI)
- Docker Compose for local development
- Hot reload in development mode
- Type hints throughout
- Comprehensive test coverage

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.11+ (for local development)

### Using Docker (Recommended)
```bash
# Clone repository
git clone https://github.com/yourusername/fastapi-microservice-template.git
cd fastapi-microservice-template

# Copy environment file
cp .env.example .env

# Start services
docker-compose up -d

# View logs
docker-compose logs -f app

# Access API documentation
# Open browser: http://localhost:8000/docs
```

### Local Development
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env

# Start PostgreSQL & Redis (using Docker)
docker-compose up -d db redis

# Run migrations
alembic upgrade head

# Start development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 📖 API Documentation

Once running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json

## 🔑 Authentication Flow

### 1. Register User
```bash
POST /api/v1/auth/register
{
  "email": "user@example.com",
  "password": "SecurePassword123",
  "full_name": "John Doe"
}
```

### 2. Login
```bash
POST /api/v1/auth/login
{
  "email": "user@example.com",
  "password": "SecurePassword123"
}

Response:
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer"
}
```

### 3. Access Protected Route
```bash
GET /api/v1/users/me
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...
```

## 🧪 Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# View coverage report
open htmlcov/index.html
```

## 📁 Project Structure
```
app/
├── main.py              # Application entry point
├── config.py            # Settings and environment variables
├── database.py          # Database connection setup
├── api/
│   └── routes/          # API endpoints
├── core/
│   ├── security.py      # Authentication & security utilities
│   └── cache.py         # Redis caching
├── models/              # SQLAlchemy models
├── schemas/             # Pydantic schemas (request/response)
└── crud/                # Database operations
```

## 🔧 Configuration

Environment variables (`.env`):
```env
# Application
APP_NAME=FastAPI Microservice
DEBUG=True
SECRET_KEY=your-secret-key-here

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# Redis
REDIS_URL=redis://localhost:6379/0

# JWT
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 🐳 Docker Commands
```bash
# Build and start
docker-compose up --build

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# Execute commands in container
docker-compose exec app bash

# Run migrations in container
docker-compose exec app alembic upgrade head
```

## 📊 Database Migrations
```bash
# Create new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1

# View migration history
alembic history
```

## 🛣 Available Endpoints

### Health Check
- `GET /health` - Service health status

### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login and get JWT token

### Users
- `GET /api/v1/users/me` - Get current user info
- `PUT /api/v1/users/me` - Update current user
- `GET /api/v1/users/{user_id}` - Get user by ID (admin only)

## 🚀 Deployment

Ready for deployment to:
- AWS (ECS, EC2, Lambda)
- Google Cloud (Cloud Run, GKE)
- Heroku
- DigitalOcean
- Any Docker-compatible platform

## 📝 License

MIT License - Use freely for personal and commercial projects.

## 👤 Author

Built as a production-ready template for scalable backend development.

**Tech Stack**: FastAPI, PostgreSQL, Redis, Docker, SQLAlchemy, JWT