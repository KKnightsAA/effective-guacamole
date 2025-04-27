import streamlit as st
import requests
from datetime import datetime, date, timedelta


st.set_page_config(page_title="Guía de Ayuda para Ejecutivos CS", layout="centered")

st.title("📘 Manual para Ejecutivos CS")
st.markdown("Selecciona una categoría para ver preguntas frecuentes y cómo ayudar al arrendatario:")

# Categorías principales
categoria = st.selectbox("📂 Categoría", [
    "Selecciona una categoría",
    "Arriendo",
    "Gastos Comunes",
    "Servicios Básicos",
    "Reparaciones",
    "Renovaciones y Término de Contrato",
    "Mudanzas y Certificados de Salida",
    "Liquidaciones de Garantía"
])

# Subcategorías según selección
if categoria == "Arriendo":
    opcion = st.selectbox("¿Cuál es la duda del arrendatario?", [
        "💳 ¿Cómo ayudar al arrendatario a pagar el arriendo?",
        "🚫 El banco no le permite pagar el arriendo",
        "😟 Tengo dificultades económicas para pagar",
        "📈 ¿Por qué aumentó mi arriendo?",
        "🕓 Pago no reflejado en el sistema o duplicado"
    ])

    if opcion == "💳 ¿Cómo ayudar al arrendatario a pagar el arriendo?":
        st.subheader("¡Ayudar a pagar el arriendo es muy sencillo! 💼✨")
        st.write("")

        st.markdown("""
            Puedes guiarlo para que realice el pago directamente desde nuestra plataforma en línea:

            👉 [**www.assetplan.cl/paga-tu-arriendo**](https://www.assetplan.cl/paga-tu-arriendo)

            Al ingresar su **Rut** y presionar el botón **“Ingresar”** podrá visualizar todos los pagos pendientes a la fecha.
            """)
        st.write("")

        st.markdown("<h4>💳 ¿Qué opciones de pago tiene el arrendatario?</h4>", unsafe_allow_html=True)
        st.markdown("""
            Una vez dentro, el sistema le mostrará el Detalle De Pago.
                    
            Allí, podrá elegir entre dos opciones:

            1. **Transferencia bancaria mediante Khipu**  
            
            2. **Tarjeta de débito o crédito mediante MercadoPago**
            """)
        st.write("")

        st.markdown("""
            <div style="background-color: rgba(200, 255, 200, 0.4); padding: 10px; border-radius: 10px; border-left: 4px solid #4CAF50;">
            <strong>Importante 💡</strong><br>
            La plataforma de MercadoPago cobra una comisión ajena a Assetplan. Es bueno que el arrendatario lo sepa antes de elegir esa opción.
            </div>
         """, unsafe_allow_html=True)
        st.write("")
        
        st.markdown("<h4>✅ ¿Cómo guiarlo según la opción que elija?</h4>", unsafe_allow_html=True)
        st.write("")

        st.markdown("""
        <div style='
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        text-align: justify;
        '>
        <h4 style='margin-top:0;'>💸 Transferencia (Khipu)</h4>
        Debe elegir el banco, ingresar el correo asociado a su cuenta bancaria 
        y seguir las instrucciones de su banco paso a paso.

        </div>
        """, unsafe_allow_html=True)
        st.write("")

        st.markdown("""
        <div style='
        background-color: #e8f5e9;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        text-align: justify;
        '>
       <h4 style='margin-top:0;'>💳 Tarjeta de debito o crédito (MercadoPago)</h4>
        Será redirigido a la plataforma de MercadoPago para ingresar  
        los datos de su tarjeta y completar el pago de forma segura. 

        </div>
        """, unsafe_allow_html=True)
        st.write("")
        
        st.subheader("Por último, debe presionar “Pagar” y ¡listo! 🎉")
        

        # widget flotante:
        st.markdown("""
            <style>
            .floating-box {
            position: fixed;
            top: 100px;
            right: 45px;
            width: 250px;
            background-color: #93cdfd;
            border-left: 5px solid #3b82f6;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            z-index: 100;
            }

            .floating-box img {
            width: 100%;
            border-radius: 6px;
            margin-top: 10px;
            }
            </style>

            <div class="floating-box">
            <strong>¿Aún con dudas? </strong>
            <p style="margin: 8px 0;">¡Escríbenos para ayudarte!</p>
            """, unsafe_allow_html=True)
        
        with st.expander("¿Aún con dudas? Haz clic aquí para ver imágenes de ejemplo 📸"):
            st.markdown("""
            <div style='
            background-color: #93cdfd;
            padding: 5px;
            border-radius: 12px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            text-align: center;
            '>
            <h4 style='margin-top:0;'>Ejemplos visuales de ayuda al arrendatario</h4>
            <p>Puedes mostrarle estos pasos para que complete su pago sin problemas:</p>
            """, unsafe_allow_html=True)
            st.write("")


            st.image("https://www.assetplan.cl/img/icons/logo.svg", caption="Paso 1: Ingresar el RUT", use_container_width=True)

            st.markdown("</div>", unsafe_allow_html=True)
    if "mostrar_banco" not in st.session_state:
        st.session_state.mostrar_banco = False
    if "mostrar_limite" not in st.session_state:
        st.session_state.mostrar_limite = False
    elif opcion == "🚫 El banco no le permite pagar el arriendo":

        # Variables para controlar qué botón fue presionado
        mostrar_banco = False
        mostrar_limite = False

        # Mostrar los botones en dos columnas
        espacio_izq, col1, col2, espacio_der = st.columns([1, 2, 2, 1])

        with col1:
            if st.button("El banco presenta problemas"):
                st.session_state.mostrar_banco = True
                st.session_state.mostrar_limite = False

        with col2:
            if st.button("Límite bancario"):
                st.session_state.mostrar_limite = True
                st.session_state.mostrar_banco = False

            # Mostrar el contenido centrado (fuera de las columnas)
        if st.session_state.mostrar_banco:
            st.markdown("""
            <div style='
            background-color: #e3f2fd;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            text-align: justify;
            max-width: 700px;
            margin: auto;
            '>
            <h4 style='margin-top:0;'>¿Problemas con el banco?</h4>
            <h4 style='margin-top:0;'>Aquí te dejamos los pasos a seguir:</h4>

            <p>Si el arrendatario informa que no puede realizar el pago por un problema bancario, puedes orientarlo con esta guía:</p>

            <ul style="padding-left: 18px; line-height: 1.7;">
            <li>🖼️ <strong>Solicita imágenes</strong> que muestren claramente el intento de pago y el error presentado.</li>
            <li>🏦 <strong>Pregunta con qué banco está intentando pagar</strong>. Esto nos ayuda a verificar si hay otros reportes similares.</li>
            <li>👥 <strong>Consulta con tu equipo</strong> si han recibido casos similares recientemente.</li>
            <li>📩 Con toda esta información, podrás dar seguimiento al caso o derivarlo con mayor claridad.</li>
            </ul>

            <p style="margin-top: 10px;">✨ Este tipo de detalles nos permiten entregar una mejor experiencia al arrendatario y actuar con mayor rapidez.</p>
            </div>
            """, unsafe_allow_html=True)

        if st.session_state.mostrar_limite:
            bancos = {
            "Banco Estado (cuenta RUT)": "100.000",
            "Banco Estado (cuenta corriente)": "250.000",
            "Banco de Chile (Edwards, Citi) con DigiPass y Mi Pass": "350.000",
            "Banco de Chile (Edwards, Citi) con DigiCard": "350.000",
            "Scotiabank": "300.000",
            "Banco Santander": "250.000",
            "Banco BCI con BCIpass": "600.000",
            "Banco BCI con Multipass": "250.000",
            "Banco ITAU": "300.000",
            "Banco Ripley": "250.000",
            "Coopeuch": "250.000",
            "Banco Falabella": "1.000.000",
            "Banco BICE": "500.000",
            "Banco Estado - Empresas": "250.000",
            "Banco Consorcio": "250.000",
            "Banco Security": "350.000",
            "Banco Santander Officebanking": "Posiblemente sin límite",
            "BCI - Empresas": "600.000",
            "Banco de Chile - Empresas": "Sin límite diario",
            "Banco Security - Empresas con Tarjeta": "Posiblemente sin límite",
            "Banco Security - Empresas con Dispositivo": "Posiblemente sin límite",
            "Prepago los Héroes": "250.000"
            }

            st.markdown("""
                <div style='
                background-color: #fff3e0;
                padding: 5px;
                border-radius: 12px;
                box-shadow: 0 2px 6px rgba(0,0,0,0.1);
                text-align: justify;
                max-width: 700px;
                margin: auto;
                '>
                <h4 style='margin-top:0;'>🏦 Límite bancario</h4>
                <p>Selecciona el banco del arrendatario para conocer el monto máximo permitido en su primera transferencia:</p>
                """, unsafe_allow_html=True)

            banco_seleccionado = st.selectbox("Selecciona el banco", list(bancos.keys()))
            st.markdown(f"""
                <div style='
                background-color: #93c5fd;
                padding: 15px;
                margin-top: 10px;
                border-left: 6px solid #ff9800;
                border-radius: 8px;
                font-weight: bold;
                '>
                💳 El monto máximo de la primera transferencia con <i>{banco_seleccionado}</i> es: <strong>{bancos[banco_seleccionado]} CLP</strong>.
                </div>
                """, unsafe_allow_html=True)

            st.markdown("""
                <div style='
                background-color: #fbe9e7;
                padding: 15px;
                margin-top: 15px;
                border-left: 6px solid #d84315;
                border-radius: 8px;
                '>
                ⚠️ <strong>Recuerda:</strong> Si el cupón incluye una <strong>multa</strong>, el monto que dividas <u>aumentará</u>. Revisa bien antes de indicar los pasos.
                        
                </div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("""
                <div style='
                background-color: #fbe9e7;
                padding: 15px;
                margin-top: 15px;
                border-left: 6px solid #d84315;
                border-radius: 8px;
                '>
                ⚠️ Siempre debes validar que los cupones quedaron correctamente divididos ingresando en la plataforma de Assetplan e ingresando <strong>como si fueses un arrendatario.<strong>

                        
                </div>
                </div>
                """, unsafe_allow_html=True)
    elif opcion == "😟 Tengo dificultades económicas para pagar":
        # Obtener la fecha actual
        hoy = datetime.now()
        dia_actual = hoy.day
        mes_actual = hoy.strftime("%B").capitalize()
        if dia_actual <= 15:
            responsable = "👨‍💼 **Lo puedes gestionar tú como ejecutivo.**"
            color = "#e8f5e9"  # verde claro

            # Mostrar guía para evaluación
            st.markdown("""
                <div style='
                background-color: #f0f4c3;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 2px 6px rgba(0,0,0,0.1);
                margin-top: 20px;
                '>
                <h4 style='margin-top:0;'>🧐 Puntos clave para evaluar</h4>
                <ul style="line-height: 1.7;">
                <li>📞 ¿Se intentó comunicar <strong>antes de que se generaran multas</strong>?</li>
                <li>⭐ ¿Cómo está su <strong>rating de pago</strong>?</li>
                <li>🧠 Según tu criterio, ¿<strong>podría justificar una extensión</strong> del plazo de vencimiento?</li>
                <li>📁 ¿Hay <strong>tickets anteriores</strong> asociados?</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("""
                <div style='
                background-color: #fbe9e7;
                padding: 15px;
                margin-top: 15px;
                border-left: 6px solid #d84315;
                border-radius: 8px;
                '>
                ⚠️ Considera siempre tener un trato empático y sin juicio. En caso de que extiendas el plazo, debes preguntarle al arrendatario <strong>cuándo puede cancelar la deuda<strong>

                        
                </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            responsable = "📩 Debes derivarlo a Cobranza. Ellos toman la decisión final."
            color = "#fff3e0"  # naranjo claro
        
        st.markdown(f"""
            <div style='
            background-color: {color};
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            margin-top: 20px;
            '>
            <h4 style='margin-top:0;'>📆 Análisis según la fecha actual ({dia_actual} de {mes_actual})</h4>
            <p>{responsable}</p>
            </div>
            """, unsafe_allow_html=True)  
    elif opcion == "📈 ¿Por qué aumentó mi arriendo?":
        col1, col2 = st.columns([3, 1])
        with col1:
            valor_uf_arriendo = st.number_input("Ingresa el valor del arriendo en UF:", min_value=0.0, step=0.1)
        with col2:
            st.write("")
            calcular = st.button("Calcular 💰") 

        def obtener_valor_uf():
            try:
                response = requests.get("https://mindicador.cl/api")
                data = response.json()
                valor_uf = data["uf"]["valor"]
                fecha_uf = data["uf"]["fecha"]
                return valor_uf, fecha_uf
            except:
                st.error("❌ No se pudo obtener el valor de la UF. Intenta más tarde.")
                return None, None
            
        if calcular:
            valor_uf, fecha_uf = obtener_valor_uf()
            if valor_uf:
                valor_en_pesos = valor_uf_arriendo * valor_uf
      
            st.markdown(f"""
                <div style='
                background-color: #f1f8e9;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 2px 6px rgba(0,0,0,0.1);
                text-align: justify;
                max-width: 700px;
                margin: auto;
                font-size: 16px;
                '>
                <h4 style='margin-top:0;'>🔍 Revisión del valor del arriendo</h4>

                <h3 style='margin-top:0;'>✅ El valor aproximado del arriendo es de <strong>${valor_en_pesos:,.0f}<strong></h3>
                Calculado usando una UF de <strong>${valor_uf:,.0f}<strong> (actualizado al <strong>{fecha_uf[:10]})<strong>.<br><br>

                ℹ️ Este monto es solo una <strong>referencia estimada</strong>. Puede variar dependiendo del día exacto de cobro o si hubo un desfase en el valor de la UF publicado.<br><br>

                ⚠️ <strong>Importante:</strong> Si el monto parece más alto de lo esperado, te recomendamos:
                <ul>
                    <li>🔎 Verificar si existen <strong>multas asociadas</strong> por retrasos.</li>
                    <li>🧾 Revisar si hay <strong>otros cargos o reajustes</strong> cargados al arriendo.</li>
                </ul>

                🧠 Este cálculo puede ayudarte como ejecutivo a validar si el aumento tiene lógica, pero siempre es bueno revisar todos los factores en la plataforma.
                </div>
                """, unsafe_allow_html=True)
    elif opcion == "🕓 Pago no reflejado en el sistema o duplicado":
        st.markdown("""
            Por favor, selecciona la fecha en que el arrendatario **realizó el pago**. 
            Con esto podremos determinar si es necesario esperar o solicitar documentación adicional.  
            """)
        fecha_pago = st.date_input("📅 Fecha del pago", max_value=date.today())
        dias_transcurridos = (date.today() - fecha_pago).days
        if fecha_pago:
            if dias_transcurridos < 2:
                st.markdown(f"""
                    <div style='
                    background-color: #fff3cd;
                    padding: 20px;
                    border-radius: 12px;
                    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
                    text-align: justify;
                    max-width: 700px;
                    margin: auto;
                    '>
                    <h4 style='margin-top:0;'>⌛ Aún dentro del plazo</h4>
                    El pago se realizó hace <strong>{dias_transcurridos} días</strong>.  
                    <br><br>
                    🕒 Recuerda que los pagos pueden tardar hasta <strong>48 horas hábiles</strong> en consolidarse en el sistema.  
                    <br><br>
                    Por ahora, recomendamos <strong>esperar</strong> y monitorear tu bandeja de entrada por el comprobante enviado por <strong>Khipu</strong>. ✉️
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div style='
                    background-color: #f8d7da;
                    padding: 20px;
                    border-radius: 12px;
                    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
                    text-align: justify;
                    max-width: 700px;
                    margin: auto;
                    '>
                    <h4 style='margin-top:0;'>🔎 Han pasado más de 48 horas</h4>
                    Ya han pasado <strong>{dias_transcurridos} días</strong> desde que se realizó el pago.  
                    <br><br>
                    🧾 Para poder ayudarte, por favor solicita al arrendatario:
                    <br><br>
                    <ul>
                    <li>📄 Una imagen de la <strong>cartola bancaria</strong> donde se vea el débito.</li>
                    <li>📩 El <strong>comprobante de pago enviado por Khipu</strong> al correo electrónico.</li>
                    </ul>
                    Es importante hacer hincapié en que <strong>Khipu siempre envía</strong> este comprobante. 
                    <br><br>
                    Toda esta información debes enviarla al ejecutivo encargado de <strong>pagos no consolidados.<strong>
                    </div>
                    """, unsafe_allow_html=True)
elif categoria == "Servicios Básicos":
    opcion = st.selectbox("¿Cuál es la duda del arrendatario?", [
        "📎 ¿Dónde veo mis boletas?",
        "📬 ¿Cómo puedo pagar los servicios básicos?",
        "💰 Pagué una boleta de SSBB que no me correspondía",
        "💸 Assetplan debe pagar una boleta que no me corresponde",
        "🚨 Tengo un corte de servicio básico en trámite"
    ])

    if opcion == "📎 ¿Dónde veo mis boletas?":
        st.write("")
        st.markdown("""
            📬 **Recepción de boletas:**
            - Las boletas pueden llegar **físicamente a la conserjería** del edificio.
                    
            - En muchos casos, las boletas son **enviadas de manera digital** 🌱 para proteger el medio ambiente y reducir el uso de papel.
                    """)
        st.write("")
        st.markdown("""
            <div style="background-color: rgba(200, 255, 200, 0.4); padding: 15px; border-radius: 8px; border-left: 6px solid #4CAF50;">
            <strong>🔎 Importante</strong><br><br>
            Es fundamental entregar al arrendatario los números de cliente que están registrados en Streamrent para que pueda realizar los pagos directamente en las páginas oficiales de los servicios.
            <br><br></div>
         """, unsafe_allow_html=True)
        st.markdown("""
            <div style='
            background-color: #fbe9e7;
            padding: 15px;
            margin-top: 15px;
            border-left: 6px solid #d84315;
            border-radius: 8px;
            '>
            ⚠️ <strong>Recuerda:</strong> 
                          
            - Si los campos de número de cliente están vacíos en Streamrent, debes contactar a Eddy Espinoza vía Slack 📲 para solicitar que carguen la información correspondiente.
                    
            - Si no encuentras la opción de número de cliente habilitada en Streamrent, puede deberse a que el servicio se pague aparte, ya sea por el tipo de edificio o alguna particularidad del contrato.      
            </div>
            </div>
            """, unsafe_allow_html=True)

    elif opcion == "📬 ¿Cómo puedo pagar los servicios básicos?":
        st.write("")
        st.markdown("""
            El arrendatario puede realizar el pago de los servicios básicos ingresando a la página oficial del servicio, ingresando el número de cliente y siguiendo los pasos indicados en la plataforma.
            """)
        st.write("")
        st.info("""
            ✨ **Mejoras recientes:**

            - A partir del **Tech Day** 🚀, se están implementando mejoras para que el arrendatario pueda **pagar los servicios básicos directamente en la plataforma de Assetplan**.

            **¿Cómo verificar si ya está activo?**
            1. Ingresa a la **plataforma de Assetplan**.
            2. Busca al arrendatario utilizando su **RUT**.
            3. Revisa en la sección de **pago de arriendo** si aparecen **enlazadas las deudas** de los servicios básicos.

            """)
    elif opcion == "💰 Pagué una boleta de SSBB que no me correspondía":
        st.write("")
        st.subheader("Solicitudes de Reembolso")
        st.markdown("""
            Antes de iniciar tu solicitud de reembolso, ¡vamos a revisar algunas cosas importantes! 🚀✨

            1. **Primero, revisa en Streamrent**:<br>
                - Ingresa a la sección de **Gastos** y asegúrate de que **el reembolso no haya sido solicitado anteriormente**. 🔍
            <br><br>
        
            2. **Documentos que vas a necesitar**:<br>
                - **Comprobante de pago** del servicio. 🧾
                - **Boleta** correspondiente. 📄
                - **Datos bancarios** del arrendatario. 🔍
            <br><br>
                
            3. **¿Quién se encarga de tu solicitud? Depende de la fecha de inicio de contrato**:<br>
                - **Dentro de los primeros 60 días**: enviar solicitud a **analistaspagos@assetplan.cl** 📬.
                - **Después de los 60 días**: gestionar con el **equipo de C2 Contratos y Arriendos** 🏢.
            """,unsafe_allow_html=True)
        st.divider()
        st.header("📅 ¿Quién debe gestionar el reembolso?")

        fecha_inicio = st.date_input("Selecciona la fecha de inicio de contrato:")
        if st.button("Indicar responsable ✨"):
            hoy = datetime.now().date()
            dias_transcurridos = (hoy - fecha_inicio).days

            if dias_transcurridos <= 60:
                st.success(f"🎉 ¡Todo bien! Debes enviar tu solicitud a **analistaspagos@assetplan.cl**. (Han pasado {dias_transcurridos} días desde el inicio de contrato).")
            else:
                st.warning(f"📢 Atención: Debes gestionar tu solicitud con el **equipo de C2 Contratos y Arriendos**. (Han pasado {dias_transcurridos} días desde el inicio de contrato).")
    elif opcion == "💸 Assetplan debe pagar una boleta que no me corresponde":
        st.write("")
        st.markdown("""
            Antes de solicitar que Assetplan realice un **pago** de una boleta que no te corresponde, ¡vamos a revisar algunos puntos importantes! 🎯✨ 
                    <br><br> 

            1. **Primero, valida en Streamrent**:  
                - Ingresa a la sección de **Gastos** y verifica que **el pago no haya sido gestionado previamente**. 🔍
                <br><br>

            2. **Documentos necesarios**:  
                - **Boleta correspondiente** al servicio. 📄  
                <br><br>

            3. **¿Quién debe gestionar la solicitud? Depende de la fecha de inicio de contrato**:  
                - **Dentro de los primeros 60 días** desde el inicio de contrato:  
                👉 Envía la solicitud a **analistaspagos@assetplan.cl** a través de conversación secundaria.
                    <br><br>
                - **Después de los 60 días**:  
                👉 El caso debe ser derivado al equipo de **C2 Contratos y Arriendos**. 🏢  
        """,unsafe_allow_html=True)
        st.divider()
        st.markdown("### 🗓️ Indica aquí la fecha de inicio de contrato para saber a quién le corresponde:")

        fecha_inicio = st.date_input("Fecha de inicio de contrato")

        if st.button("Indicar responsable ✨"):
            
            hoy = datetime.now().date()
            diferencia_dias = (hoy - fecha_inicio).days

            if diferencia_dias <= 60:
                st.success(f"🎉 ¡Genial! Como han pasado {diferencia_dias} días, debes enviar la solicitud a **analistaspagos@assetplan.cl**.")
            else:
                st.info(f"📢 Como han pasado {diferencia_dias} días, el caso debe ser gestionado por el equipo de **C2 Contratos y Arriendos**.")

    elif opcion =="🚨 Tengo un corte de servicio básico en trámite":
        st.write("")
        st.markdown("""
            Cuando un arrendatario tiene un **corte de servicio básico en trámite**, ¡debemos actuar rápido! 🏃‍♂️  

            1. **Primero, revisa Streamrent**:  
                - Verifica si las deudas son **posteriores a la fecha de inicio de contrato**.  
                - Si **son previas**, no corresponde al arrendatario.  
                - Si **son posteriores**, el arrendatario debe realizar el pago urgente. <br><br> 

            2. **¿La deuda aparece en la sección de gastos de Streamrent?** 
        """,unsafe_allow_html=True) 

        deuda_en_streamrent = st.radio("¿La deuda aparece en Streamrent?", ["Sí", "No"])

        if deuda_en_streamrent == "Sí":
            st.success("✅ ¡Perfecto! Completa los datos para generar tu solicitud de pago urgente:")

            tipo_gasto = st.selectbox("Tipo de gasto:", ["SSBB", "GGCC", "SSBB y GGCC"])
            op = st.text_input("OP:")
            tk = st.text_input("TK:")
            titular = st.text_input("Titular del contrato:")
            fecha_inicio = st.date_input("Fecha de inicio de contrato:")
            motivo = st.selectbox("Motivo:", [
                "Corte de servicio en trámite",
                "No puede hacer uso de espacios comunes",
                "Me cortaron los suministros de servicio básico"
                "Otro (especificar)"
                ])
            
            motivo_otro = ""
            if motivo == "Otro (especificar)":
                motivo_otro = st.text_area("Especifica el motivo:")

            if st.button("🚀 Generar plantilla"):
                motivo_final = motivo_otro if motivo == "Otro (especificar)" else motivo
                fecha_inicio_texto = fecha_inicio.strftime("%d-%m-%Y") if fecha_inicio else "Fecha no indicada"

                plantilla = f"""
                @Elena Malet

                PAGO URGENTE
                TIPO DE GASTO: {tipo_gasto}
                OP: {op}
                TK: {tk}
                TITULAR: {titular}
                INICIO DE CONTRATO: {fecha_inicio_texto}
                MOTIVO: {motivo_final}
                """
                st.code(plantilla, language='markdown')
                st.success("✅ Plantilla generada con éxito. ¡Cópiala y pégala en Slack!")

        else:
            st.error("❌ La deuda **NO** aparece en Streamrent.")
            st.markdown("""
                En este caso:  

                - Solicita al arrendatario **las boletas correspondientes**. 📄  <br><br> 
                - Deriva la solicitud al equipo de **Contratos y Arriendo**. 🏢  <br><br> 
                - **No olvides notificarlo también a través de Slack**. 💬<br><br> 

                ¡Así aseguramos una gestión rápida y ordenada! 🚀
                """,unsafe_allow_html=True)
            
elif categoria == "Renovaciones y Término de Contrato":
    opcion = st.selectbox("¿Cuál es la duda del arrendatario?", [
        "🔄 Quiero renovar mi contrato",
        "🏁 Quiero dar término a mi contrato",
        "📊 Cálculo de Proporcional de Arriendo y Multas",
        "🆕 Quiero cambiar el titular o aval de mi contrato",
        "💸 Quiero solicitar una rebaja de cánon",
        "🚗 Quiero arrendar un estacionamiento o bodega adicional",
        "🐾 ¿Puedo tener mascota?"
    ])

    if opcion == "🔄 Quiero renovar mi contrato":
        st.markdown("""
            # 🏡 Renovaciones de Contrato

            ¡Buenas noticias! 🎉  <br><br>
            Las **renovaciones de contrato** en Assetplan son **automáticas**.  

            - Al finalizar el **primer año** de contrato, este **se mantiene vigente** de manera automática. ✅ <br><br>
            - **No es necesario firmar un nuevo documento** a menos que se envíe un **nuevo contrato** indicando modificaciones específicas. 📝

            ---

            # 🔄 Contratos Heredados

            Para los contratos heredados:<br><br>
                - **Siguen rigiéndose bajo los mismos términos y condiciones** del acuerdo original. 📜<br><br>
                - Solo se actualizarán si el equipo de **Analistas** notifica cambios oficiales.

            ---


            """,unsafe_allow_html=True)
        
        st.write("")

        st.markdown("""
            <div style="background-color: rgba(200, 255, 200, 0.4); padding: 10px; border-radius: 10px; border-left: 4px solid #4CAF50;">
            <strong>Recuerda 🔔</strong><br> 
            Si tienes dudas sobre un contrato en particular, ¡puedes siempre apoyarte en tu equipo! 🤝
            </div>
            """, unsafe_allow_html=True)
        
    elif opcion == "🏁 Quiero dar término a mi contrato":
        st.markdown("""
            Para gestionar un **término de contrato** de manera correcta, considera los siguientes puntos:

        - 📅 **Notificación anticipada:** El arrendatario debe notificar **al menos 60 días antes** de su fecha de salida para no afectar el saldo a favor de su garantía.<br><br>
        - 🗓️ **Duración mínima:** El contrato debe haber cumplido **al menos 365 días** (1 año completo) desde su inicio para evitar una multa por término anticipado.

        ---
        🔎 **¿Qué pasa si no cumple con estas condiciones?**<br><br>
            **Si finaliza antes del año de contrato:**<br><br> Se aplicará una multa de **dos meses de arriendo** y la **pérdida total de la garantía**, conforme al contrato firmado.
    
        ---
        📝 **Proceso a seguir si el arrendatario confirma la intención de dar término:** <br><br>
            1. Solicitar el **motivo de la salida** (para registro interno).<br><br>
            2. Solicitar la **fecha exacta de salida**.<br><br>
            3. Ingresar a Streamrent en la sección **cambiar estado**, ingresando la fecha indicada <br><br>

        """, unsafe_allow_html=True)

        st.divider()

        st.subheader("📆 Verificación de condiciones del contrato")

        fecha_inicio = st.date_input("Selecciona la fecha de inicio del contrato:")

        if fecha_inicio:
            hoy = datetime.today().date()
            fecha_minima_sin_multa = fecha_inicio + timedelta(days=365)
            fecha_minima_para_notificar = hoy + timedelta(days=60)

            st.markdown("---")
        
            if fecha_minima_para_notificar < fecha_minima_sin_multa:
                st.error(f"🚨 El arrendatario aún no cumple el primer año de contrato (mínimo hasta {fecha_minima_sin_multa.strftime('%d/%m/%Y')}).")
                st.warning("➡️ No puede evitar multa ni retención de garantía aún. Deberá esperar cumplir el año para dar término correctamente.")
            else:
                st.success(f"✅ El arrendatario puede dar término respetando el aviso de 60 días.")
                st.info(f"📅 Para no afectar el saldo positivo de garantía, debe notificar **a más tardar el {fecha_minima_para_notificar.strftime('%d/%m/%Y')}**.")

                st.info("""
                ✨ **Tip:** Siempre recuerda revisar bien las fechas en el contrato firmado, ya que pueden existir condiciones especiales en casos particulares.
                """)

    elif opcion == "📊 Cálculo de Proporcional de Arriendo y Multas":
        st.header("📝 Datos de entrada")
        valor_arriendo = st.number_input("💵 Valor total de arriendo ($)", min_value=0, step=1000)
        dias_mes = st.number_input("📅 Número de días del mes", min_value=1, max_value=31, value=30)
        dia_salida = st.number_input("🚪 Día de salida del arrendatario", min_value=1, max_value=31)

        if valor_arriendo > 0 and dias_mes > 0 and dia_salida > 0:
            # Cálculos
            valor_diario = valor_arriendo / dias_mes
            proporcional_a_pagar = valor_diario * dia_salida
            monto_a_descontar_streamrent = valor_arriendo - proporcional_a_pagar
            multa_dos_canones = valor_arriendo * 2

            st.header("📈 Resultados")

            st.success(f"💰 **Valor diario de arriendo:** ${valor_diario:,.0f}")
            st.success(f"🏠 **Proporcional de arriendo (hasta el día {dia_salida}):** ${proporcional_a_pagar:,.0f}")
            st.success(f"➖ **Monto que debes descontar en Streamrent:** ${monto_a_descontar_streamrent:,.0f}")
            st.success(f"⚡ **Multa de 2 cánones de arriendo:** ${multa_dos_canones:,.0f}")

            st.info("💡 Recuerda que podrían existir **descuentos especiales** en los primeros meses de contrato. ¡Verifica el contrato antes de realizar el cobro!")
        else:
            st.warning("Por favor ingresa todos los datos para calcular los valores.")

    elif opcion == "🆕 Quiero cambiar el titular o aval de mi contrato":
        st.write("")
        st.subheader("📝 Información Importante:")
        
        st.markdown("""
            - El cambio de titular implica **iniciar un nuevo contrato** de arriendo.
            - **Solo puede solicitarse si ya se cumplió el primer año de contrato**.
            - El nuevo titular y aval deben **acreditar renta suficiente** y ser **aprobados** conforme a los requisitos internos.
            - Se deben **firmar nuevos documentos** y actualizar toda la información personal.
            - **Las cuentas del contrato deben estar al día** para autorizar el cambio.
            - **Garantía**:
            - La garantía original se **reembolsa al titular saliente** en **45 días hábiles**.
            - El **nuevo titular debe pagar una nueva garantía** al momento de formalizar el cambio.
            """)

        st.subheader("✅ Checklist rápido para ejecutar la derivación:")
        st.write("")
        st.checkbox("Confirmar que el primer año de contrato se haya cumplido.")
        st.checkbox("Solicitar documentos actualizados del nuevo titular y aval.")
        st.checkbox("Confirmar que todas las cuentas asociadas estén pagadas.")
        st.checkbox("Informar al titular saliente sobre el proceso de devolución de garantía.")

        st.warning("⚠️ Atención: Si el arrendatario no ha cumplido el primer año, informar que no es posible gestionar el cambio aún.") 
        st.warning("El único que puede realizar estas solicitudes es el titular de arriendo, no el aval") 

    elif opcion == "💸 Quiero solicitar una rebaja de cánon":
        st.markdown("""
            ### 🌟 ¿Cómo gestionar esta solicitud?

            - Para que un arrendatario pueda pedir una rebaja en su cánon de arriendo, debe haber **cumplido al menos 1 año de contrato**. 📅
            - También es importante **verificar que su rating de pago sea positivo**. ✅ <br><br>

            **📩 ¿Qué necesitamos del arrendatario?** 
            - Solicitarle un **correo explicativo** donde cuente: <br><br>
                - **Cuál es su situación actual**.
                - **Qué tipo de rebaja espera** obtener. <br><br>

            **🛠️ ¿Qué hacemos después?**
            - Una vez recibido el correo, debes **enviar la solicitud al equipo de Contratos y Arriendos**.
            - El equipo **evaluará** el caso en conjunto con el ejecutivo de cuenta del propietario. <br><br>

            **🔔 Mensaje para el arrendatario:**
            - Explica amablemente que su solicitud:
            - **Será evaluada** internamente. 🔎
            - **Depende de la autorización del propietario**. 🏡
            - **Será notificado** por correo electrónico una vez haya una respuesta. 📧
            - **Recuerda**: No podemos asegurar un resultado positivo, pero gestionaremos su solicitud con mucho respeto y dedicación. 🤝

            ---
        """, unsafe_allow_html=True)

        st.subheader("✅ Checklist para completar el proceso:")

        st.checkbox("🔍 Verificar que haya cumplido 1 año de contrato.")
        st.checkbox("📊 Confirmar que su rating de pago sea adecuado.")
        st.checkbox("✉️ Solicitar correo explicativo de su situación.")
        st.checkbox("📤 Enviar solicitud a Contratos y Arriendos.")
        st.checkbox("💬 Informar de forma cordial el proceso al arrendatario.")

        st.info("✨ Siempre mantener una comunicación cercana, cordial y empática. ¡Cada solicitud cuenta!")


    elif opcion == "🚗 Quiero arrendar un estacionamiento o bodega adicional":
        st.subheader("¿Qué debes hacer?")

        st.markdown("""
            1. **Revisar si hay stock disponible** en el edificio.
            * **Importante:** Algunos estacionamientos o bodegas vienen asociados a una unidad y no se pueden arrendar de forma individual.
            2. **Si no hay stock disponible:**
            * **Edificio normal (Retail):** Indicarle al cliente que puede consultar directamente en el condominio del edificio para ver alternativas.
            * **Edificio Multifamily:** Informar al cliente que debe comunicarse directamente con el edificio **y además** enviar un **correo** al administrador del edificio notificando su solicitud.
        """)

        st.markdown("---")

        st.subheader("🏢 ¿Cómo saber si es Multifamily o Retail?")

        st.markdown("""
            1. Copiar la OP.
            2. Extraer las **3 primeras letras** de la OP (por ejemplo, OP **BEZ1234** ➔ "BEZ").
            3. **Buscar esas siglas** en la tabla de edificios:
            * Si existe ➔ **Es un edificio Multifamily**.
            * Si no existe ➔ **Es un edificio Retail**.
        """)
        st.markdown("---")

        st.subheader("📧 Plantilla de correo para edificios Multifamily:")

        st.markdown("""
            > **Asunto:** Solicitud de cliente - Arriendo de Estacionamiento/Bodega  
            >  
            > **Cuerpo del correo:**  
            > Estimado/a,  
            >  
            > Junto con saludar, les informamos que el renter de la OP [] ha solicitado información para arrendar:  
            >  
            > *   **Estacionamiento:** ✅/❌  
            > *   **Bodega:** ✅/❌  
            >  
            > Agradecemos su gestión y quedamos atentos a sus comentarios.  
            >  
            > Saludos,  
        """)

        st.markdown("---")

        st.subheader("✨ Ejemplo rápido")

        st.markdown("""
            *   OP: **VMP8721**  
            *   3 primeras letras: **VMP**  
            *   Buscamos en la tabla: ✅ existe ➔ **Edificio Multifamily**.  
            *   Correo a enviar: **recepcion.activavicuna@apcomunidades.cl**  
            """)

        st.markdown("---")
        st.markdown("¡Listo! Ya ha sido enviada la solicitud de estacionamiento y/o bodega. 🚗✨")

    elif opcion == "🐾 ¿Puedo tener mascota?":
        st.subheader("¿Qué debes hacer?")

        st.markdown("""
            1. **Revisar el contrato de arriendo** del cliente.
            * **Buscar una cláusula relacionada con mascotas**.  <br><br>
                * Si **sí hay cláusula** que mencione la prohibición o autorización de mascotas: Indicar que su contrato lo prohibe pero que se enviará al equipo encargado para que analicen el caso y tomen una decisión. <br><br>
                * Si **no hay cláusula específica**: **Informar al cliente que se revisará el caso con el equipo de Contratos y Arriendo**.
            2. **Si no se puede tomar una decisión inmediata**, asegurarse de que el cliente reciba una respuesta clara y amable, explicando que el equipo de Contratos revisará el tema y se comunicará con él.
        """, unsafe_allow_html=True)
        st.markdown("---")

        st.subheader("⚖️ ¿Cómo manejar la situación si no hay cláusula de mascota?")

        st.markdown("""
            - Si no se menciona nada en el contrato sobre las mascotas, lo más adecuado es enviar el caso al **equipo de Contratos y Arriendo** para que ellos analicen y determinen si es posible permitir mascotas.<br><br>
            - Es importante ser claro con el cliente, asegurándole que el equipo de Contratos tomará una decisión a la brevedad.
            """, unsafe_allow_html=True)
        st.markdown("---")

        st.subheader("¡Listo! Ahora sabes cómo manejar la solicitud de mascotas. 🐶✨") 

elif categoria == "Gastos Comunes":
    opcion = st.selectbox("¿Cuál es la duda del arrendatario?", [
        "📎 ¿Dónde veo mi boleta de GGCC?",
        "📬 Cómo se pagan los GGCC?",
        "💰 Pagué una boleta de GGCC que no me correspondía",
        "💸 Assetplan debe pagar un proporcional de GGCC",
        "🚨 Hay cobros especiales en la boleta de GGCC que no me corresponden",
        "🚫 Tengo un corte de servicios por deuda de GGCC"
    ])
    if opcion == "📎 ¿Dónde veo mi boleta de GGCC?":
        st.write("😄 Te explicamos dónde puede encontrar el arrendatario la boleta de gastos comunes:")

        st.info("🔎 **Formas de recibir la boleta:**\n\n"
            "- Generalmente, el arrendatario está registrado en la plataforma online que administra el gasto común. De ser así, debería recibir la boleta de forma automática 📬.\n\n"
            "- En otros edificios, aún se entrega digitalmente en la correspondencia de cada unidad 📨.")
        st.success("🏢 **¿Quién entrega la boleta?**\n\n"
           "La responsabilidad de entregar la boleta con el detalle de cada mes es de la **comunidad** del edificio. "
           "¡No te preocupes! Siempre debería recibirla a tiempo para su revisión.")
        st.warning("⏳ **Boletas desfasadas:**\n\n"
           "Normalmente, las boletas reflejan los gastos del **mes anterior**. \n"
           "¡Así que no te preocupes si ves una diferencia de fechas! Es completamente normal. "
           "Solo en algunos edificios Multifamily el cobro corresponde al mes en curso.")
        st.write("💡 **Recuerda:** En las boletas también pueden aparecer:")
        st.markdown("- 🕐 **Intereses por atraso** en pagos anteriores.\n"
            "- 🚫 **Multas aplicadas** por la comunidad.\n"
            "- 🧾 **Cobros especiales:** Hay ítems que corresponden al **arrendatario** y otros al **propietario**.\n\n"
            "¡Es muy importante revisar bien los conceptos para poderlo explicar bien! 😉")
        st.success("👉 Si tienes dudas sobre algún cobro, preguntar al equipo será siempre la mejor opción. ¡Estamos para ayudarnos! 🎉")
    elif opcion == "📬 Cómo se pagan los GGCC?":
        st.write("¡Hola, hola! 😃 Te contamos cómo puede el arrendatario pagar sus gastos comunes:")
        st.info("💻 **Plataforma en línea:**\n\n"
            "La mayoría de las comunidades cuentan con una plataforma online donde puedes realizar el pago de forma fácil y rápida. Solo debes seguir las instrucciones que te entregue la administración. 🖥️✨")
        st.success("🏦 **Transferencia bancaria:**\n\n"
           "En casi todos los casos, pueden pagar directamente mediante una transferencia bancaria a la cuenta de la administración. "
           "Recuérdales siempre incluir el **número de unidad** y el **mes** que está pagando en el detalle de la transferencia. 📄✅")
        st.warning("📢 **Importante:**\n\n"
           "Cada comunidad maneja su propio método de pago, así que puedes recomendarle verificar la información en la boleta mensual 📄 o consultar directamente con la administración 🏢.")
        st.success("¡Listo! Así de fácil es mantener todo al día 😎🎉")
    elif opcion == "💰 Pagué una boleta de GGCC que no me correspondía":
        st.write("¡Tranquilidad! 🧘‍♂️ A veces puede pasar, y aquí te explicamos cómo debes guiar al arrendatario:")
        st.write("Si el arrendatario pagó una boleta o un proporcional que **no le correspondía**, corresponde gestionar un **reembolso**. Para ello, necesitaremos:")
        st.success("📄 **Documentos necesarios:**\n\n"
           "- Comprobante de pago realizado 💳\n"
           "- Boleta de gastos comunes pagada 📋")
        st.divider()
        st.header("📅 ¿Quién debe gestionar el reembolso?")

        fecha_inicio = st.date_input("Selecciona la fecha de inicio de contrato:")
        if st.button("Indicar responsable ✨"):
            hoy = datetime.now().date()
            dias_transcurridos = (hoy - fecha_inicio).days

            if dias_transcurridos <= 60:
                st.success(f"🎉 ¡Todo bien! Debes enviar tu solicitud a **analistaspagos@assetplan.cl**. (Han pasado {dias_transcurridos} días desde el inicio de contrato).")
            else:
                st.warning(f"📢 Atención: Debes gestionar tu solicitud con el **equipo de C2 Contratos y Arriendos**. (Han pasado {dias_transcurridos} días desde el inicio de contrato).")
    elif opcion == "💸 Assetplan debe pagar un proporcional de GGCC":
        st.write("")
        st.markdown("""
            Antes de solicitar que Assetplan realice un **pago** de un gasto común que no le correspondía al arrendatario, ¡vamos a revisar algunos puntos importantes! 🎯✨ 
                    <br><br> 

            1. **Primero, valida en Streamrent**:  
                - Ingresa a la sección de **Gastos** y verifica que **el pago no haya sido gestionado previamente**. 🔍
                <br><br>

            2. **Documentos necesarios**:  
                - **Boleta de gasto común correspondiente** al mes. 📄  
                <br><br>

            3. **¿Quién debe gestionar la solicitud? Depende de la fecha de inicio de contrato**:  
                - **Dentro de los primeros 60 días** desde el inicio de contrato:  
                👉 Envía la solicitud a **analistaspagos@assetplan.cl** a través de conversación secundaria.
                    <br><br>
                - **Después de los 60 días**:  
                👉 El caso debe ser derivado al equipo de **C2 Contratos y Arriendos**. 🏢  
        """,unsafe_allow_html=True)
        st.warning("📢 **Importante:**\n\n"
           "Hay que tomar en consideración que, a diferencia de las boletas de servicios básicos, en los gastos comunes solo pagamos el proporcional que nos corresponde, por lo que el arrendatario deberá cancelar su parte.")
        st.divider()
        st.markdown("### 🗓️ Indica aquí la fecha de inicio de contrato para saber a quién le corresponde:")

        fecha_inicio = st.date_input("Fecha de inicio de contrato")

        if st.button("Indicar responsable ✨"):
            
            hoy = datetime.now().date()
            diferencia_dias = (hoy - fecha_inicio).days

            if diferencia_dias <= 60:
                st.success(f"🎉 ¡Genial! Como han pasado {diferencia_dias} días, debes enviar la solicitud a **analistaspagos@assetplan.cl**.")
            else:
                st.info(f"📢 Como han pasado {diferencia_dias} días, el caso debe ser gestionado por el equipo de **C2 Contratos y Arriendos**.")
    elif opcion == "🚨 Hay cobros especiales en la boleta de GGCC que no me corresponden":
        st.write("¡Vamos a aclararlo! 🌟 En los gastos comunes pueden aparecer **cobros especiales** y es normal que surjan dudas sobre quién debe pagarlos.")
        st.success("📋 **¿Qué ítems le corresponden al arrendatario?**\n\n"
           "- Todo gasto relacionado con el **bienestar de la comunidad**.\n"
           "- Ejemplos: mantenimiento de espacios comunes, reparaciones de áreas compartidas, servicios comunitarios, etc.")
        st.error("🏠 **¿Qué ítems le corresponden al propietario?**\n\n"
         "- **Seguros de incendio**.\n"
         "- **Cobros por bodegas o estacionamientos** que no fueron contratados por el arrendatario.\n"
         "- **Gastos extraordinarios** (por ejemplo, mejoras o ampliaciones del edificio).")
        st.divider()
        st.info("🔍 **¿Tienes dudas sobre un cobro en particular?**\n\n"
        "No te preocupes. Puedes **consultar con el equipo** para analizar el ítem y definir a quién le corresponde. ¡Estamos aquí para ayudarnos! 🤗")
        st.divider()
        st.write("¡Así nos aseguramos de que todo se gestione correctamente y sin complicaciones!")
    elif opcion == "🚫 Tengo un corte de servicios por deuda de GGCC":
        st.write("¡Manos a la obra! 🛠️ Cuando ocurre un corte de servicios por deuda en los gastos comunes, es muy importante actuar con rapidez y claridad. ¡Vamos paso a paso!")
        st.subheader("❓ Preguntas clave para analizar el caso:")
        st.warning("- ¿El gasto común le corresponde **totalmente al arrendatario** o **nosotros debemos una parte**?\n"
            "- ¿El pago está solicitado en **Streamrent** en la sección de gastos?\n"
            "- ¿En qué **estado** se encuentra la solicitud en Streamrent?")
        st.divider()
        st.subheader("⚡ Acciones que debes tomar:")
        st.success("✅ **Si NO está en Streamrent:**\n"
           "- Solicitar el pago de forma urgente a **Contratos y Arriendo**.")
        st.success("✅ **Si está en Streamrent en estado PENDIENTE:**\n"
           "- Solicitar el pago urgente a tu coordinadora: **Elena Malet**.")
        st.success("✅ **Si está en Streamrent en estado APROBADO pero SIN COMPROBANTE:**\n"
           "- Pedir el comprobante a **Elena Malet** de forma urgente.")
        st.divider()
        st.info("💬 **Comunicación con la Comunidad:**\n\n"
        "Si confirmamos que **nosotros debemos** realizar el pago, es ideal contactar al condominio mediante **conversación secundaria** para informar que se realizará el pago correspondiente y solicitar la **reconexión de los servicios básicos**. 🙌")
        st.write("¡Con estas acciones rápidas, aseguramos una solución efectiva para el arrendatario! 🚀🎯")
elif categoria == "Liquidaciones de Garantía":
    opcion = st.selectbox("¿Cuál es la duda del arrendatario?", [
        "📅 ¿Cuándo llegará mi liquidación de garantía?",
        "❗ No estoy de acuerdo con la liquidación de garantía",
        "📞 Necesito comunicarme con alguien acerca de la liquidación de garantía",
        "📈 Necesito realizar un acuerdo de pago"
    ])
    if opcion == "📅 ¿Cuándo llegará mi liquidación de garantía?":
        st.write("""
            La liquidación de garantía se genera **30 días después** de la **visita de inspección**. 📅

            Este tiempo es necesario ya que:
            - Hay un **desfase** en la recepción de boletas de **servicios básicos** (agua, luz, gas). 💧⚡
            - También en las **boletas de gastos comunes**. 🧾🏢

            Por eso, debemos esperar ese plazo para garantizar que todo esté correctamente facturado antes de emitir la liquidación.

            ---

            ✅ **Importante:**  
            Si ves que han pasado más de 30 días desde tu inspección y aún no tienes novedades, puedes indicarle al arrendatario que vuelva a llamar para hacer insistencia en su caso directamente con el analista de rotación correspondiente
            """)
    elif opcion == "❗ No estoy de acuerdo con la liquidación de garantía":
        st.write("""
            Cuando un arrendatario **no esté de acuerdo** con la liquidación de garantía, debe seguir el siguiente proceso:

            🔹 **Rechazo de la liquidación:**  
            El arrendatario debe **rechazar** la liquidación directamente a través de la **plataforma** o **correo** donde recibió la propuesta.  
            👉 *Este es el canal oficial y nosotros no podemos resolver directamente su solicitud.*

            ---

            🔹 **Importante:**  
            Si ya realizó el rechazo, es fundamental que **adjunte evidencia o soportes** que respalden su desacuerdo (fotos, documentos, boletas, etc.).  
            📸🧾 *Sin evidencia, el caso no podrá ser analizado de manera efectiva.*

            ---

            🔹 **Nuestro rol:**  
            Aunque el proceso debe seguirse por el canal correspondiente, ¡podemos ayudarlo!  
            ✅ Escuchamos su duda, analizamos su caso y le damos las **orientaciones** necesarias para que pueda avanzar de la mejor manera.

            """)
    elif opcion == "📞 Necesito comunicarme con alguien acerca de la liquidación de garantía":
        st.write("""""")
        st.write("""
            Cuando el arrendatario necesite comunicarse acerca de su liquidación de garantía:

            🔹 **Canal Oficial:**  \n
            La comunicación siempre debe realizarse **por correo electrónico** directamente con el **analista de rotación** que maneja su caso.  \n
            ✉️ Este es el único canal formal para tratar temas de liquidación.

            ---

            🔹 **¿Qué podemos hacer como apoyo?**  \n
            En situaciones **muy puntuales** y **justificadas**, podemos contactar **internamente** al analista de rotación **por Slack** para insistir o consultar algún detalle.

            👉 *Recuerda:* Solo se debe usar esta vía si realmente **amerita** una gestión.

            """)
    elif opcion == "📈 Necesito realizar un acuerdo de pago":
        st.write("""""")
        st.write("""
            Cuando un arrendatario nos indique que necesita realizar un acuerdo de pago:

            🔹 **Acción Principal:**  \n
            Debemos **derivar directamente a cobranza** ✉️, informando que el renter desea generar un **acuerdo de pago**.

            ---

            🔹 **Buenas Prácticas:**  \n
            Antes de derivar, es ideal **preguntar**:  \n
            💬 *"¿Deseas pagar en cuotas?"*

            De esta forma, podremos entregar **mayor información** y hacer una derivación **más efectiva**.

            ---

            🔹 **Importante:**  \n
            Además de derivar, es necesario **dejar la insistencia en Slack** 📲 para asegurar que el equipo de cobranza pueda priorizar el caso.

            """)
elif categoria == "Mudanzas y Certificados de Salida":
    opcion = st.selectbox("¿Cuál es la duda del arrendatario?", [
        "📦 Necesito ingresar o retirar algunas pertenencias",
        "🔑 Quiero saber cómo entregar las llaves de la unidad",
        "🚛 Necesito realizar la mudanza"
        ])
    if opcion == "📦 Necesito ingresar o retirar algunas pertenencias":
        st.write("""
            Para poder gestionar el **documento de autorización** que permite **sacar o ingresar objetos** (sin ser una mudanza total), debemos considerar lo siguiente: \n
                 
            ✅ El arriendo, los servicios básicos y los gastos comunes deben estar **al día**. 
            ✅ El arrendatario debe **informar la cantidad de artículos** que desea mover.

            🔹 Se permite un máximo de:
            - **2 artículos grandes** 🛋️🖼️
            - **3 artículos pequeños** 📦👜🖥️
            """)
    elif opcion == "🔑 Quiero saber cómo entregar las llaves de la unidad":
        st.write("""""")
        st.write("""
            La entrega de llaves debe realizarse **a más tardar el siguiente día hábil** posterior a la **fecha de término de contrato**.
            """)
        st.write("""""")
        st.info("""
            📢 **¡Buenas noticias!**

            Estamos realizando **cambios** para que próximamente este proceso se pueda hacer **en conjunto con la inspección de salida**.  \n
            Será un proceso **mucho más ágil** 🚀 y que **beneficiará a todos**. 🎉
            """)
    elif opcion == "🚛 Necesito realizar la mudanza":
        st.write("""
            El **certificado de salida** le llegará al arrendatario aproximadamente **10 días antes** de su **fecha de salida**,  
            siempre que **no presente deudas** en arriendo, servicios básicos o gastos comunes. 🏢✅
            """)
        st.info("""
            ⚡ **¿Necesita el certificado con urgencia?**

            Si el arrendatario requiere el certificado en el **transcurso de 5 días**,  
            debemos **enviar una solicitud** al área de **Contratos y Arriendo**. \n 
            Importante: Solo si **todos los pagos** están **al día**. 📑💸
            """)
elif categoria == "Reparaciones":
    opcion = st.selectbox("¿Cuál es la duda del arrendatario?", [
        "🚨 Reparaciones Urgentes",
        "⏳ Reparaciones No Urgentes",
        "🛠️ Preguntas Clave según tipo de Problema"
        ])
    if opcion == "🚨 Reparaciones Urgentes":
        st.markdown("""
        - **Filtraciones Sifones, flexibles, grifería:** Fugas que impidan el uso adecuado o presenten riesgo de inundación.
        - **Accesorios de baño:** Fallas que afectan funcionalidad (ej: porta confort, tapa WC).
        - **Caldera individual:** No provee calefacción o agua caliente, o presenta fugas.
        - **Campana de cocina:** No extrae humo u olores o tiene fallas eléctricas.
        - **Tableros y fallas eléctricas:** Riesgo evidente o problemas de funcionamiento seguro.
        - **Vidrios/ventanas:** Rotos, trizados o que no cierren correctamente (riesgo de seguridad).
        - **Cerámicas rotas:** Representan riesgo de seguridad o impermeabilidad.
        """)
    elif opcion == "⏳ Reparaciones No Urgentes":
        st.markdown("""
        - **Bisagras de puertas y muebles:** Ligeramente desajustadas pero funcionales.
        - **Ampolletas, soquetes y focos LED:** No afectan la habitabilidad.
        - **Cortinas:** Decoloradas o con manchas pequeñas.
        - **Pintura de muros/papel mural:** Marcas o desgaste estético.
        - **Elementos ajenos o escombros:** No impiden el uso de la propiedad.
        """)
    elif opcion == "🛠️ Preguntas Clave según tipo de Problema":
        problema = st.selectbox("Selecciona el tipo de problema:", [
            "Problemas con alarma o citófono",
            "Daños en pisos, estructuras o puertas",
            "Filtraciones",
            "Equipos eléctricos o a gas",
            "Problemas de agua",
            "Problemas de hongos",
            "Problemas de luces o enchufes",
            "Problemas con plagas",
            "Problemas con chapa o llaves",
            "Problemas con calefacción o agua caliente"
        ])
        
        if problema == "Problemas con alarma o citófono":
            st.markdown("""
                - ¿Cuál es la marca de la alarma o citófono?
                - ¿El problema ocurre constantemente o solo a veces?
                - ¿Consultó con la administración del edificio?
                - ¿El citófono tiene alguna señal/luz de error?
                """)

        elif problema == "Daños en pisos, estructuras o puertas":
            st.markdown("""
                - ¿Hace cuánto notó el daño?
                - ¿Puede enviarnos fotos?
                - ¿El daño ocurrió después del check-in o ya existía?
                """)

        elif problema == "Filtraciones":
            st.markdown("""
                - ¿Dónde exactamente está la filtración?
                - ¿Desde cuándo ocurre?
                - ¿La fuga sigue activa?
                - ¿Alguien revisó anteriormente?
                - ¿Hay contacto con vecinos superiores/inferiores?
                - ¿Hay instalaciones comunes sobre su unidad (terraza, piscina, etc.)?
                """)

        elif problema == "Equipos eléctricos o a gas":
            st.markdown("""
                - ¿Puede enviarnos fotos del área afectada?
                - ¿Hay olor a gas o señales de fuga?
                - ¿Fuga en la red o en equipo específico?
                """)

        elif problema == "Problemas de agua":
            st.markdown("""
                - ¿Falta de agua en toda la unidad o en zonas específicas?
                - ¿Llaves de paso abiertas?
                - ¿Se nota presión baja o corte en el medidor?
                """)

        elif problema == "Problemas de hongos":
            st.markdown("""
                - ¿Puede enviarnos fotos de los hongos?
                - ¿Hay fuente de humedad visible?
                - ¿Se ventila adecuadamente la unidad?
                """)

        elif problema == "Problemas de luces o enchufes":
            st.markdown("""
                - ¿Automáticos revisados?
                - ¿Probó otro artefacto en el enchufe?
                - ¿Cuenta de electricidad al día?
                """)

        elif problema == "Problemas con plagas":
            st.markdown("""
                - ¿Puede enviarnos fotos/videos?
                - ¿Plaga localizada en una zona específica?
                - ¿Informó a la administración?
                """)

        elif problema == "Problemas con chapa o llaves":
            st.markdown("""
                - ¿Cuándo usó las llaves por última vez?
                - ¿Puede enviarnos fotos de la chapa o llaves?
                - ¿El daño ocurrió después del check-in?
                """)

        elif problema == "Problemas con calefacción o agua caliente":
            st.markdown("""
                - ¿Puede enviarnos fotos del equipo (caldera, calefón, termo)?
                - ¿Realizó mantenciones? ¿Fecha y respaldos?
                - ¿Fuga visible o interna?
                - ¿Hay pérdida de agua en el equipo?
                """)

        # Nota final
        st.info("💡 Recuerda registrar toda esta información en la nota interna para agilizar el proceso de reparación y postventa.")