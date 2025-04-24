import streamlit as st
from datetime import datetime
from fpdf import FPDF
import os

# Titulo
st.set_page_config(page_title="Asistente Ejecutivo", layout="centered")
st.title("🤖 Asistente para Nuevos Ingresos")

# Función para generar PDF
def generar_pdf_gastos_comunes(fecha_inicio, mes_gasto, monto_gasto):
    fecha_inicio_dt = datetime.strptime(fecha_inicio, "%d/%m/%Y")
    dias_mes = 30
    dia_inicio = fecha_inicio_dt.day

    dias_arrendatario = dias_mes - dia_inicio + 1
    dias_empresa = dia_inicio - 1

    monto_arrendatario = round(monto_gasto * (dias_arrendatario / dias_mes))
    monto_empresa = monto_gasto - monto_arrendatario

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Informe de Prorrateo de Gastos Comunes", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Fecha de inicio de contrato: {fecha_inicio}", ln=True)
    pdf.cell(200, 10, txt=f"Mes del gasto común: {mes_gasto}", ln=True)
    pdf.cell(200, 10, txt=f"Monto total del gasto común: ${monto_gasto}", ln=True)
    pdf.cell(200, 10, txt=f"Días a cargo del arrendatario: {dias_arrendatario}", ln=True)
    pdf.cell(200, 10, txt=f"Monto proporcional arrendatario: ${monto_arrendatario}", ln=True)
    pdf.cell(200, 10, txt=f"Monto proporcional empresa: ${monto_empresa}", ln=True)

    output_path = "prorrateo_gasto_comun.pdf"
    pdf.output(output_path)
    return output_path


# Menú de categorías
categoria = st.selectbox("Selecciona una categoría", [
    "Pago de arriendo",
    "Gastos comunes",
    "Servicios básicos",
    "Contrato",
    "Reparaciones",
    "Mudanza",
    "Comunidad",
    "Actualización de datos"
])

# Subcategorías según categoría
if categoria == "Gastos comunes":
    subcat = st.selectbox("Selecciona una subcategoría", [
        "Gastos comunes que no corresponden a la línea de contrato",
        "Gasto común no ingresado en sistema",
        "Validación de cobros extraordinarios"
    ])

    if subcat == "Gastos comunes que no corresponden a la línea de contrato":
        st.markdown("---")
        st.subheader("📄 Proporcional de gastos comunes")
        fecha_inicio = st.text_input("Fecha de inicio de contrato (dd/mm/yyyy)", "14/04/2025")
        mes_gasto = st.selectbox("Mes del gasto común", ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])
        monto_gasto = st.number_input("Monto del gasto común ($)", min_value=0)

        if st.button("Calcular prorrateo"):
            try:
                archivo = generar_pdf_gastos_comunes(fecha_inicio, mes_gasto, monto_gasto)
                with open(archivo, "rb") as file:
                    st.success("Cálculo realizado con éxito")
                    st.download_button(
                        label="📥 Descargar PDF para enviar a área contable",
                        data=file,
                        file_name="gasto_comun_prorrateado.pdf",
                        mime="application/pdf"
                    )
            except Exception as e:
                st.error(f"Error en el cálculo: {e}")

        st.info("Este reporte solo se descarga si necesitas derivarlo a otra área. En caso contrario, puedes registrar internamente.")

    if subcat == "Gasto común no ingresado en sistema":
        st.markdown("""
        ### Instrucciones
        1. Verifica con Contabilidad si el gasto común fue reportado.
        2. Si no existe, debes ingresar manualmente en el sistema según protocolo.
        3. Notifica al área correspondiente con respaldo adjunto.
        """)

    if subcat == "Validación de cobros extraordinarios":
        st.markdown("""
        ### Pasos
        - Verifica si el ítem está especificado en el contrato.
        - Si no lo está, consulta con el Jefe de Administración.
        - Crea un reporte y almacénalo para auditoría interna.
        """)

elif categoria == "Pago de arriendo":
    st.markdown("""
    ### Información
    - Los pagos deben realizarse dentro de los 5 primeros días hábiles.
    - Validar con el área contable si existen abonos previos o notas de crédito.
    - Usa el formulario de pago si el inquilino necesita una boleta oficial.
    """)

elif categoria == "Mudanza":
    st.markdown("""
    ### Protocolo de mudanza
    - Solicitar fecha de entrada/salida.
    - Notificar a conserjería.
    - Enviar checklist de estado de unidad antes y después de la mudanza.
    """)

elif categoria == "Reparaciones":
    st.markdown("""
    ### Reparaciones
    - Validar si la reparación está cubierta por la garantía o es responsabilidad del arrendatario.
    - Crear ticket en el sistema y asignar técnico.
    - Hacer seguimiento y cierre de caso con firma del arrendatario.
    """)

# Puedes seguir agregando lógica para el resto de categorías si lo necesitas.

st.markdown("---")
st.caption("Versión prototipo • Desarrollado por Ronni")