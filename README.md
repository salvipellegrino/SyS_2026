# SyS_2026
Trabajo para la materia señales y sistemas.

# RIR-API

API REST desarrollada en Python utilizando FastAPI para el cálculo de parámetros acústicos a partir de respuestas al impulso (RIR), siguiendo la norma ISO 3382.

El sistema permite generar señales de excitación, procesar respuestas al impulso y calcular parámetros como RT60, C50 y EDT. La API está diseñada para ser consumida por clientes externos como aplicaciones web, scripts o herramientas de análisis.

---

## 👥 Integrantes

-Pellegrino Salvador - Legajo: 75978 - Rol:
-Castrillo Lautaro -  Legajo: 70558 - Rol:
-Maiolo Ivan - Legajo: - Rol:

---

## ⚙️ Instalación

Clonar el repositorio:

```bash
git clone https://github.com/salvipellegrino/SyS_2026.git
cd SyS_2026

```crear entorno virtual

python -m venv venv
source venv/bin/activate

```instalar dependencias
pip install -r requirements.txt

ejecutar la api:
uvicorn app.main:app --reload


Estructura del proyecto
app/
├── main.py          # Punto de entrada
├── routers/         # Endpoints
├── services/        # Lógica (vacío por ahora)
├── schemas/         # Validación (vacío por ahora)

Estrategia de ramas
Main -> rama protegida
Feature/nombre -> nuevas funcionalidades

Convencion de commits
feat: nueva funcionalidad
fix: corrección de errores

---



