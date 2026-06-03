import os
from datetime import datetime
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 1. Cargar las variables secretas
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# 2. Función para registrar incidentes en el archivo de logs corporativo
def registrar_incidente(usuario: str, categoria: str, mensaje_cliente: str):
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea_reporte = f"[{fecha_hora}] Usuario: {usuario} | Categoría: {categoria} | Reporte: {mensaje_cliente}\n"
    
    with open("reportes_soporte.txt", "a", encoding="utf-8") as archivo:
        archivo.write(linea_reporte)
    print(f"📁 [LOG EN CORE] Incidente registrado exitosamente en la categoría: {categoria}")

# 3. Comando /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usuario = update.message.from_user.first_name
    await update.message.reply_text(
        f"¡Hola, {usuario}! Bienvenido a la Mesa de Control Automatizada de BYUTECH.\n\n"
        "Por favor, describa de forma detallada el fallo técnico que presenta su terminal o la infraestructura de la oficina para iniciar el protocolo de diagnóstico guiado."
    )

# 4. Comando /servicios
async def servicios_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto_servicios = (
        "💻 *Mesa de Soluciones Tecnológicas BYUTECH:*\n\n"
        "1️⃣ *Soporte y Continuidad Operativa de Infraestructura:*\n"
        "   Gestión, mantenimiento y optimización de Servidores, Redes de Datos, Telefonía IP Corporativa, Periféricos y Sistemas Audiovisuales.\n\n"
        "2️⃣ *Automatización de Procesos:* Despliegue de scripts, bots avanzados e Inteligencia Artificial.\n"
        "3️⃣ *Ciberseguridad y Blindaje Perimetral:* Auditorías inalámbricas, control de intrusos y cifrado de datos críticos.\n\n"
        "👉 Si el asistente interactivo no logra resolver su incidente tras agotar el manual, puede solicitar soporte avanzado vía /contacto."
    )
    await update.message.reply_text(texto_servicios, parse_mode="Markdown")

# 5. Comando /contacto
async def contacto_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto_contacto = (
        "📞 *Escalación de Casos Especiales - BYUTECH:*\n\n"
        "Si ya agotó la totalidad de los manuales interactivos de autogestión proporcionados por Annubis y el fallo persiste, su caso requiere intervención de campo de nivel 2 o 3:\n\n"
        "📧 *Correo Corporativo:* jobrenes12@gmail.com\n"
        "📱 *Línea de Ingeniería / WhatsApp:* +506 7148 6745\n"
        "🌐 *LinkedIn Oficial:* linkedin.com/company/byu-tech\n\n"
        "⚠️ *Aviso de Operación:* Las llamadas o mensajes sin ticket previo de autogestión agotado podrían verse retrasados para priorizar emergencias perimetrales."
    )
    await update.message.reply_text(texto_contacto, parse_mode="Markdown")

# 6. MOTOR DE INFERENCIA PROFUNDA: Manuales extensos de resolución para evitar saturación
def analizar_y_registrar(mensaje_usuario: str, nombre_usuario: str) -> str:
    texto = mensaje_usuario.lower()
    
    diagnosticos = {
        "PC_HARDWARE": (
            "⚙️ *MANUAL DE AUTOGESTIÓN BYUTECH (Rendimiento y Temperatura Estaciones):*\n\n"
            "El ruido elevado de abanicos o la congelación del sistema ocurre cuando la CPU alcanza su límite térmico de seguridad, lo cual reduce la velocidad para evitar que la placa se queme.\n\n"
            "📋 *Siga rigurosamente este protocolo técnico antes de reportar un ticket:* \n"
            "1️⃣ *Aislamiento Físico:* Si es una laptop, levántela de la superficie usando un soporte u objeto rígido en las esquinas. Jamás obstruya las rejillas de ventilación inferiores colocándola sobre superficies suaves.\n"
            "2️⃣ *Análisis de Procesos:* Presione simultáneamente las teclas `Ctrl + Shift + Esc` para abrir el *Administrador de Tareas*. Haga clic en la columna de *CPU* o *Memoria* para ordenar de mayor a menor y localice si hay un navegador, programa o proceso colgado consumiendo más del 80%. Dele clic derecho y seleccione 'Finalizar tarea'.\n"
            "3️⃣ *Purga de Temporales:* Presione `Windows + R`, escriba `%temp%` y presione Enter. Borre de forma definitiva todos los archivos de esa carpeta (los que el sistema le bloquee, déles 'Omitir').\n"
            "4️⃣ *Ciclo de Energía:* Guarde su trabajo, apague el equipo por completo, desconecte el cargador, mantenga presionado el botón de encendido físico durante 20 segundos para liberar la estática de los componentes, vuelva a conectar todo e inicie de nuevo.\n\n"
            "👉 *¿El problema continúa?* Deje enfriar el equipo un momento. Si tras realizar estos 4 pasos el rendimiento no se restablece, escriba /contacto para coordinar una limpieza física y cambio de pasta térmica interna."
        ),
        "RED_CONECTIVIDAD": (
            "🌐 *MANUAL DE AUTOGESTIÓN BYUTECH (Fallas de Red, Internet y Softphones / VoIP):*\n\n"
            "En un entorno de Call Center o corporativo, los microcortes, la latencia alta o la pérdida de paquetes degradan las llamadas de voz sobre IP. Esto suele ser un conflicto de la tarjeta de red local con el servidor DHCP o saturación de caché en el switch.\n\n"
            "📋 *Siga rigurosamente este protocolo técnico antes de reportar un ticket:*\n"
            "1️⃣ *Inspección Física:* Desconecte el cable de red RJ45 de la computadora (el cable con el gancho plástico). Verifique que los pines de cobre no estén sucios, y vuélvalo a conectar presionando firmemente hasta escuchar el 'clic' de enganche mecánico. Si usa Wi-Fi, apague el receptor de su equipo durante 10 segundos.\n"
            "2️⃣ *Renovación de Parámetros IP desde Consola:* Vamos a refrescar la conexión de forma lógica. Presione la tecla `Windows`, escriba `cmd` y abra el *Símbolo del Sistema*. Digite los siguientes comandos en orden, presionando Enter después de cada uno:\n"
            "   • `ipconfig /release` *(Esto liberará su IP actual y lo desconectará de la red)*\n"
            "   • `ipconfig /renew` *(Esto obligará al enrutador de la empresa a asignarle una IP limpia)*\n"
            "   • `ipconfig /flushdns` *(Esto borrará el historial de rutas DNS corruptas que congelan los aplicativos)*\n"
            "3️⃣ *Validación Cruzada:* Verifique si sus compañeros de pasillo o estación también perdieron la conexión. Si ellos tienen internet normal, el fallo se limita exclusivamente a su terminal o a su cable de red.\n\n"
            "👉 *¿El enlace sigue caído?* Si tras realizar la purga por consola la tarjeta de red sigue sin dar salida de datos ni levantar el sistema de llamadas, escriba /contacto para el reemplazo físico del cableado o reconfiguración del puerto del switch."
        ),
        "SALAS_PANTALLAS": (
            "📽️ *MANUAL DE AUTOGESTIÓN BYUTECH (Sistemas de Proyección, HDMI/VGA y Salas):*\n\n"
            "Que un proyector o pantalla de sala de juntas muestre la leyenda 'Sin Señal' o se quede en negro suele deberse a un desfase en la tasa de refresco de la tarjeta de video de la compu o a una mala selección del canal físico de entrada.\n\n"
            "📋 *Siga rigurosamente este protocolo técnico antes de reportar un ticket:*\n"
            "1️⃣ *Comando de Proyección de Windows:* En su computadora, presione la combinación de teclas `Windows + P`. Verifique que la opción seleccionada no sea 'Solo pantalla de equipo'. Cambie la selección obligatoriamente a *'Duplicar'* o *'Extender'*. \n"
            "2️⃣ *Reinicio del Controlador de Gráficos:* Si la pantalla sigue sin reaccionar, resetee el software de video de Windows presionando simultáneamente: `Windows + Ctrl + Shift + B`. La pantalla parpadeará y emitirá un pitido; esto es normal y reestablece el puerto de video.\n"
            "3️⃣ *Ciclo de Conexión y Fuente:* Desconecte el cable HDMI o VGA tanto de la computadora como de la entrada del proyector. Espere 5 segundos, conéctelos de nuevo y asegúrese de que estén totalmente atornillados o insertados. Luego, use los botones físicos del proyector o su control remoto para alternar manualmente entre las fuentes de entrada (`Source` / `Input`) hasta posicionarse en el puerto correcto (ej: HDMI 1, HDMI 2 o Computer 1).\n"
            "4️⃣ *Prueba de Resolución:* Si la imagen se ve cortada o no se muestra, cambie la resolución de su pantalla en Windows a `1920x1080` o `1280x720` para emparejarla con la capacidad nativa de la lámpara del proyector.\n\n"
            "👉 *¿Continúa sin dar video?* Si tras validar los cables, reiniciar los gráficos y alternar los canales de entrada el sistema sigue sin dar señal, escriba /contacto para el envío de un ingeniero de campo para revisión de lámparas o matrices."
        ),
        "AUDIO_HEADSETS": (
            "🎧 *MANUAL DE AUTOGESTIÓN BYUTECH (Diademas de Call Center, Audio y Micrófonos):*\n\n"
            "Si las diademas USB o analógicas se escuchan cortadas, con estática, o si el micrófono de operación no transmite la voz, el incidente responde en un 90% a una desconfiguración en las prioridades de audio del sistema operativo o a una caída de energía en el puerto USB.\n\n"
            "📋 *Siga rigurosamente este protocolo técnico antes de reportar un ticket:*\n"
            "1️⃣ *Verificación y Cambio de Puerto USB (Crítico):* Desconecte la diadema por completo. Si se encuentra conectada a un concentrador externo (Hub USB) o a los puertos frontales de la torre, retírela de ahí de inmediato. Conéctela directamente a un *puerto USB trasero directo de la tarjeta madre* de la PC. Los puertos frontales sufren caídas de voltaje que distorsionan el audio digital.\n"
            "2️⃣ *Asignación de Dispositivo Predeterminado:* Haga clic derecho sobre el icono de la bocina/altavoz en la esquina inferior derecha de la barra de tareas de Windows y seleccione *'Configuración de sonido'*. \n"
            "   • En la sección de *Salida*, verifique que esté seleccionado el nombre exacto de su diadema USB (no los altavoces de la computadora).\n"
            "   • Baje a la sección de *Entrada (Micrófono)*, hable por la diadema y observe si la barra azul de prueba se mueve. Si no se mueve, despliegue la lista y predetermine el micrófono de su headset USB.\n"
            "3️⃣ *Ajuste de Niveles y Ganancia:* Dentro de esa misma ventana, vaya a las propiedades del micrófono de la diadema y asegúrese de que el volumen de captura esté al 100% y que el botón de 'Silenciar' (Mute) físico del cable de la diadema no esté activado en rojo.\n"
            "4️⃣ *Reinicio del Software Operativo:* Cierre por completo la aplicación que utiliza para recibir llamadas (Softphone, Teams, Webex o el sistema interno del Call Center) e iníciela de nuevo para que el sistema reconozca los controladores limpios.\n\n"
            "👉 *¿Persiste la estática o el fallo de audio?* Pruebe la diadema en otra computadora de la oficina si es posible. Si el fallo se repite en otro equipo, la diadema presenta daño físico en el cableado interno. Escriba /contacto para coordinar la entrega de un periférico de repuesto."
        ),
        "CIBERSEGURIDAD": (
            "🛡️ *ALERTA Y PROTOCOLO DE CONTENCIÓN CRÍTICA BYUTECH (Sospecha de Intrusión o Malware):*\n\n"
            "La aparición de ventanas emergentes sospechosas, redirecciones forzadas, alertas de cifrado o bloqueos inesperados comprometen los datos de los clientes y los servidores centrales.\n\n"
            "📋 *Ejecute estas acciones de seguridad perimetral de forma inmediata:*\n"
            "1️⃣ *Aislamiento Inmediato:* Desconecte el cable de red RJ45 de la terminal o apague el interruptor de Wi-Fi de inmediato. No apague la máquina de golpe, pero sí córtele el acceso a la red para evitar que el software malicioso se propague lateralmente hacia otras estaciones de trabajo del Call Center.\n"
            "2️⃣ *Examen Local:* En la barra de búsqueda de Windows, escriba 'Seguridad de Windows', acceda a 'Protección contra virus y amenazas' y ejecute un 'Examen rápido'.\n"
            "3️⃣ *Protección de Credenciales:* No introduzca nombres de usuario, contraseñas corporativas ni acceda a cuentas bancarias bajo ninguna circunstancia mientras el equipo esté en este estado.\n\n"
            "⚠️ *Nota de Emergencia:* No intente remover software malicioso avanzado por su cuenta para evitar destrucción de evidencia forense. Una vez aislado el equipo de la red, escriba /contacto de manera urgente para que un ingeniero especializado tome el control perimetral."
        ),
        "GAMING_TERMIC": (
            "🎮 *BYUTECH Gaming (Manual Térmico de Consolas):*\n\n"
            "Si la consola suena fuerte, límpiela externamente, colóquela en un área libre con espacio en las rejillas y déjela enfriar. Si tras reposar sigue apagándose por temperatura, ocupa mantenimiento físico. Escribe /contacto."
        ),
        "GENERICO": (
            "🤖 *Mesa de Control y Ayuda Automatizada - BYUTECH:*\n\n"
            "He recibido su reporte de incidente técnico. En BYUTECH somos los encargados de asegurar la disponibilidad tecnológica de la infraestructura corporativa:\n"
            "💻 *Estaciones de Trabajo, Laptops y Servidores*\n"
            "🌐 *Redes Corporativas, Conectividad LAN/WAN y Enlaces VoIP*\n"
            "🎧 *Periféricos de Operación Avanzada (Headsets y Diademas de Call Center)*\n"
            "📽️ *Sistemas de Proyección, HDMI/VGA y Monitores de Salas de Juntas*\n\n"
            "Para iniciar el protocolo de autogestión guiada y evitar tiempos caídos, por favor descríbame detalladamente qué síntoma presenta la terminal o qué periférico está fallando."
        )
    }

    # REGLAS DE DETECCIÓN INTELIGENTE DE CATEGORÍAS
    if any(p in texto for p in ["proyector", "beam", "vga", "hdmi", "proyecta", "sala de juntas", "sala de reunion", "sala de reunión"]):
        categoria = "Infraestructura de Video y Salas"
        registrar_incidente(nombre_usuario, categoria, mensaje_usuario)
        return diagnosticos["SALAS_PANTALLAS"]
        
    elif any(p in texto for p in ["diadema", "headset", "audifono", "audífono", "microfono", "micrófono", "audio", "escucha", "estatica", "estática"]):
        categoria = "Periféricos de Audio (Call Center)"
        registrar_incidente(nombre_usuario, categoria, mensaje_usuario)
        return diagnosticos["AUDIO_HEADSETS"]
        
    elif any(p in texto for p in ["internet", "red", "wifi", "wi-fi", "cable", "caido", "caído", "desconecta", "no carga", "voip", "softphone", "llamadas"]):
        categoria = "Redes, Conectividad y VoIP"
        registrar_incidente(nombre_usuario, categoria, mensaje_usuario)
        return diagnosticos["RED_CONECTIVIDAD"]
        
    elif any(p in texto for p in ["virus", "hackeo", "publicidad", "malware", "seguridad", "intruso"]):
        categoria = "Ciberseguridad e Infecciones"
        registrar_incidente(nombre_usuario, categoria, mensaje_usuario)
        return diagnosticos["CIBERSEGURIDAD"]
        
    elif any(p in texto for p in ["calienta", "calentamiento", "temperatura", "ventilador", "abanico", "suena", "ruido", "lenta", "lento", "pegada", "pegado", "traba"]):
        if any(p in texto for p in ["xbox", "play", "nintendo", "ps4", "ps5", "consola"]):
            categoria = "Hardware Gaming"
            registrar_incidente(nombre_usuario, categoria, mensaje_usuario)
            return diagnosticos["GAMING_TERMIC"]
        else:
            categoria = "Hardware de Estaciones de Trabajo"
            registrar_incidente(nombre_usuario, categoria, mensaje_usuario)
            return diagnosticos["PC_HARDWARE"]
            
    else:
        return diagnosticos["GENERICO"]

# 7. Manejador de entrada de mensajes
async def manejar_mensajes_texto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje_recibido = update.message.text
    usuario_telegram = update.message.from_user.first_name
    
    print(f"📥 Entrada de: {usuario_telegram} -> '{mensaje_recibido}'")
    respuesta_ia = analizar_y_registrar(mensaje_recibido, usuario_telegram)
    await update.message.reply_text(respuesta_ia, parse_mode="Markdown")

# 8. Hilo Principal de Ejecución
def main():
    print("Iniciando Core de Annubis 2.0 con Alto Filtro de Tickets...")
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("servicios", servicios_command))
    app.add_handler(CommandHandler("contacto", contacto_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensajes_texto))
    
    print("🚀 Helpdesk Corporativo blindado en línea. Maximizando autogestión.")
    app.run_polling()

if __name__ == "__main__":
    main()