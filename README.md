# 🚀 Navegador - Full-Stack Status Monitoring App

Una aplicación web full-stack moderna para monitoreo de estado de clientes, construida con **FastAPI** + **React** + **MongoDB**.

## 📋 Características

- ✅ **Backend API REST** con FastAPI
- ✅ **Frontend React** con Tailwind CSS
- ✅ **Base de datos MongoDB** para persistencia
- ✅ **Sistema de Status Checks** para monitoreo de clientes
- ✅ **Dockerizado** para fácil deployment
- ✅ **CORS configurado** para desarrollo y producción
- ✅ **Logs estructurados** para debugging

## 🏗️ Arquitectura

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│                 │    │                 │    │                 │
│   React Frontend│───▶│  FastAPI Backend│───▶│    MongoDB      │
│   (Port 3000)   │    │   (Port 8001)   │    │  (Port 27017)   │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🛠️ Stack Tecnológico

### Backend
- **FastAPI** - Framework web moderno y rápido
- **Motor** - Driver asíncrono para MongoDB
- **Pydantic** - Validación de datos y serialización
- **Python 3.11** - Lenguaje base

### Frontend
- **React 19** - Librería UI moderna
- **Tailwind CSS** - Framework CSS utility-first
- **Axios** - Cliente HTTP para API calls
- **React Router** - Navegación SPA

### Base de Datos
- **MongoDB** - Base de datos NoSQL

### DevOps
- **Docker** - Containerización
- **Nginx** - Proxy reverso
- **Supervisor** - Gestión de procesos

## 🚀 Inicio Rápido

### Prerrequisitos
- Docker y Docker Compose
- Node.js 20+ (para desarrollo local)
- Python 3.11+ (para desarrollo local)
- MongoDB (para desarrollo local)

### Desarrollo Local

1. **Clonar el repositorio**
```bash
git clone <your-repo-url>
cd navegador
```

2. **Configurar variables de entorno**
```bash
# Backend
cd backend
cp .env.example .env
# Editar .env con tus configuraciones

# Frontend
cd ../frontend
cp .env.example .env
# Editar .env con tus configuraciones
```

3. **Instalar dependencias**

Backend:
```bash
cd backend
pip install -r requirements.txt
```

Frontend:
```bash
cd frontend
yarn install
```

4. **Iniciar servicios**
```bash
# Usando supervisor (recomendado)
sudo supervisorctl restart all

# O individualmente:
# Backend
cd backend && uvicorn server:app --host 0.0.0.0 --port 8001 --reload

# Frontend
cd frontend && yarn start
```

### Deployment con Docker

```bash
# Construir y ejecutar
docker build -t navegador .
docker run -p 80:80 -p 8001:8001 navegador
```

## 📡 API Endpoints

### Base URL: `/api`

| Método | Endpoint | Descripción | Payload |
|--------|----------|-------------|---------|
| GET    | `/`      | Health check | - |
| POST   | `/status` | Crear status check | `{"client_name": string}` |
| GET    | `/status` | Obtener todos los status checks | - |

### Ejemplos de uso

**Health Check:**
```bash
curl -X GET "http://localhost:8001/api/"
```

**Crear Status Check:**
```bash
curl -X POST "http://localhost:8001/api/status" \
  -H "Content-Type: application/json" \
  -d '{"client_name":"mi_cliente"}'
```

**Obtener Status Checks:**
```bash
curl -X GET "http://localhost:8001/api/status"
```

## 🗂️ Estructura del Proyecto

```
navegador/
├── backend/                 # FastAPI backend
│   ├── server.py           # Aplicación principal
│   ├── requirements.txt    # Dependencias Python
│   └── .env               # Variables de entorno
├── frontend/               # React frontend
│   ├── src/
│   │   ├── App.js         # Componente principal
│   │   ├── App.css        # Estilos
│   │   └── index.js       # Punto de entrada
│   ├── public/            # Assets estáticos
│   ├── package.json       # Dependencias Node.js
│   └── .env              # Variables de entorno
├── tests/                 # Tests automatizados
├── scripts/              # Scripts de utilidad
├── Dockerfile            # Configuración Docker
├── docker-compose.yml    # Orquestación de servicios
├── nginx.conf           # Configuración Nginx
├── entrypoint.sh        # Script de inicio
└── README.md           # Este archivo
```

## 🔧 Configuración

### Variables de Entorno

**Backend (.env):**
```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=test_database
```

**Frontend (.env):**
```env
REACT_APP_BACKEND_URL=http://localhost:8001
```

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
yarn test
```

## 📝 Desarrollo

### Agregar nuevos endpoints

1. Definir modelos en `backend/server.py`
2. Crear endpoints con decorador `@api_router`
3. Documentar en este README

### Agregar nuevas páginas

1. Crear componente en `frontend/src/`
2. Agregar ruta en `App.js`
3. Actualizar navegación si es necesario

## 🚀 Deployment

### Producción con Docker

```bash
# Variables de entorno para producción
export FRONTEND_ENV="REACT_APP_BACKEND_URL=https://tu-dominio.com"

# Construir imagen
docker build -t navegador:latest .

# Ejecutar
docker run -d \
  --name navegador-app \
  -p 80:80 \
  -e FRONTEND_ENV="$FRONTEND_ENV" \
  navegador:latest
```

### CI/CD con GitHub Actions

El proyecto incluye workflows de GitHub Actions para:
- ✅ Tests automatizados
- ✅ Build y deployment
- ✅ Linting y formateo

## 🤝 Contribuir

1. Fork el proyecto
2. Crear branch para feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit cambios (`git commit -am 'Agregar nueva característica'`)
4. Push al branch (`git push origin feature/nueva-caracteristica`)
5. Crear Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 👥 Equipo

- **Desarrollador Principal** - Desarrollo full-stack
- **Contribuidores** - Ver [contributors](../../contributors)

## 📞 Soporte

¿Tienes preguntas o necesitas ayuda?

- 📧 Email: soporte@navegador.com
- 🐛 Issues: [GitHub Issues](../../issues)
- 📖 Documentación: [Wiki](../../wiki)

---

⭐ Si este proyecto te resulta útil, ¡dale una estrella en GitHub!
