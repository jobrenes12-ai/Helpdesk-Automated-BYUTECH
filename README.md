# 🤖 Annubis 2.0 - Mesa de Control Automatizada Helpdesk

## 💻 Sobre BYUTECH
BYUTECH es una iniciativa enfocada en asegurar la disponibilidad tecnológica y la continuidad operativa de la infraestructura corporativa, especializándose en entornos de alta demanda como Call Centers, oficinas y sistemas multiplataforma.

## 🚀 El Proyecto: Annubis Helpdesk
Annubis 2.0 es un sistema de asistencia técnica de Nivel 1 automatizado en Telegram diseñado en Python. Su objetivo principal es actuar como un **filtro inteligente de contención** frente a incidentes repetitivos de TI, forzando protocolos avanzados de autogestión antes de escalar el caso a un ingeniero humano.

### 🔥 Características Principales:
* **Triage de Alto Filtro:** Clasifica problemas críticos de hardware, conectividad de red, telefonía IP (VoIP), periféricos de Call Center (diademas/headsets), sistemas de proyección y ciberseguridad.
* **Protocolos de Autogestión Obligatorios:** Guía al usuario a través de tareas de recuperación reales (comandos de consola como `ipconfig /renew`, purga de temporales `%temp%`, reinicios de controladores gráficos y configuraciones físicas de hardware).
* **Core de Auditoría e Incidentes (Logs):** Registra de forma automática cada reporte válido en una bitácora local (`reportes_soporte.txt`) guardando fecha, hora, usuario y categoría para la generación de reportes mensuales de mantenimiento preventivo.
* **Multiplataforma Total:** Capacidad de respuesta adaptada a PCs, servidores, dispositivos móviles, consolas de videojuegos y Smart TVs.

## 🛠️ Tecnologías Utilizadas
* **Python 3**
* **python-telegram-bot** (Librería avanzada de automatización)
* **Manejo de flujo de datos y persistencia asíncrona**

## 📦 Instrucciones de Configuración
1. Clone este repositorio.
2. Cree un archivo `.env` basado en el archivo `.env.example`.
3. Inserte su token oficial generado por BotFather en la variable `TELEGRAM_TOKEN`.
4. Ejecute el core principal: `python main.py`.
