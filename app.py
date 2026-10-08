"""
Universidad Internacional de las Américas (U.I.A.)
Escuela de Economía - Cátedra de Macroeconomía y Pensamiento Crítico
Aplicación Educativa Interactiva: Disonancia del Mercado del Tesoro & Marco Mastery Flip
Autor: Diseñado para Sesión Sincrónica (Demostración, Aplicación y Defensa Oral)
"""

import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image

# -----------------------------------------------------------------------------
# 1. CONFIGURACIÓN DE PÁGINA Y ESTILO VISUAL INSTITUCIONAL UIA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="UIA Economía | Disonancia del Mercado del Tesoro",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inyección de estilos CSS de alta calidad (Fondo institucional, badges, tarjetas)
st.markdown("""
<style>
    /* Tipografía y jerarquía */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Contenedor del encabezado institucional */
    .uia-header {
        background: linear-gradient(135deg, #07162c 0%, #0d284f 50%, #153e75 100%);
        border: 1px solid rgba(217, 119, 6, 0.3);
        border-radius: 12px;
        padding: 24px 30px;
        color: #ffffff;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.25);
        margin-bottom: 25px;
    }
    
    .uia-badge {
        display: inline-block;
        background-color: #d97706;
        color: #ffffff;
        padding: 4px 12px;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        border-radius: 20px;
        margin-bottom: 10px;
    }

    .uia-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }

    .dark-card {
        background: #0f172a;
        color: #f8fafc;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }

    .pedagogical-alert {
        background-color: #f0fdf4;
        border-left: 5px solid #16a34a;
        padding: 15px 20px;
        border-radius: 6px;
        margin: 15px 0;
        color: #14532d;
    }

    .struggle-alert {
        background-color: #fffbeb;
        border-left: 5px solid #d97706;
        padding: 15px 20px;
        border-radius: 6px;
        margin: 15px 0;
        color: #78350f;
    }

    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s ease-in-out;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(13, 40, 79, 0.25);
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. GESTIÓN DEL ESTADO DE SESIÓN (st.session_state)
# -----------------------------------------------------------------------------
if "student_name" not in st.session_state:
    st.session_state.student_name = ""

if "session_answers" not in st.session_state:
    st.session_state.session_answers = {
        "socratic_debate": {
            "selected_debate": "Debate 1: Señales Distorsionadas vs Dinero Inteligente",
            "position": "",
            "arguments": "",
            "feedback": "",
            "score": 0
        },
        "case_study": {
            "liquidity_diagnosis": "",
            "policy_decision": "",
            "portfolio_impact": "",
            "feedback": "",
            "score": 0
        },
        "narrative_sim": {
            "step_choices": {},
            "final_status": "No iniciado",
            "score": 0,
            "feedback": ""
        },
        "mastery_viva": {
            "q1_defense": "",
            "q2_defense": "",
            "q3_defense": "",
            "q4_defense": "",
            "self_rating": 3,
            "score": 0
        }
    }

if "sim_step" not in st.session_state:
    st.session_state.sim_step = 1

# -----------------------------------------------------------------------------
# 3. BARRA LATERAL (SIDEBAR): LOGO, IDENTIFICACIÓN, PRINCIPIOS Y FUENTES
# -----------------------------------------------------------------------------
with st.sidebar:
    # Contenedor especial con fondo oscuro para resaltar el logo transparente
    logo_path = os.path.join(os.path.dirname(__file__), "Logo-transparente UIA.png")
    if os.path.exists(logo_path):
        st.markdown("""
        <div style="background-color: #0b1f3a; padding: 15px; border-radius: 12px; text-align: center; margin-bottom: 15px; border: 1px solid #1e3a5f;">
        """, unsafe_allow_html=True)
        st.image(logo_path, caption="Universidad Internacional de las Américas", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.title("🏛️ U.I.A. Economía")

    st.markdown("### 🎓 Identificación del Estudiante")
    student_input = st.text_input(
        "Nombre completo del estudiante:",
        value=st.session_state.student_name,
        placeholder="Ej: Randall Núñez Sancho",
        help="Tu nombre quedará registrado en todas las actividades y en el reporte final descargable."
    )
    if student_input:
        st.session_state.student_name = student_input

    st.markdown("---")
    
    # Plegables de Contexto Pedagógico y Metodológico
    with st.expander("📚 Marco Didáctico: 4 Principios de Merrill", expanded=False):
        st.markdown("""
        * **1. Activación:** Anclaje en estructuras cognitivas previas relevantes (repaso de curvas de rendimiento y tasa libre de riesgo).
        * **2. Demostración:** Evidencia visual y dinámica de la teoría en funcionamiento (gráficos interactivos y datos empíricos).
        * **3. Aplicación:** Resolución activa de problemas para romper la ilusión de comprensión (debates, casos y simulación).
        * **4. Integración:** Transferencia al mundo real y defensa pública ante pares y docentes.
        """)

    with st.expander("⚙️ Metodología Mastery Flip (Jon Bergmann)", expanded=False):
        st.markdown("""
        * **Motor de IA vs Muleta:** La aplicación actúa como un tutor socrático que fomenta la *lucha productiva* (*productive struggle*), nunca dando respuestas hechas.
        * **Raíces Analógicas:** Razonamiento reflexivo y modelado causal profundo sin atajos cognitivos.
        * **Comprobación Humana (Mastery Viva):** Todo el recorrido prepara al estudiante para la sustentación oral cara a cara con el docente.
        """)

    with st.expander("📖 Fuentes Estrictas del Cuaderno", expanded=False):
        st.markdown("""
        * **Lectura Central:** *Lyn Alden (16 agosto 2020) - "Disonancia del mercado del tesoro"*.
        * **Documentos Oficiales:** Actas del FOMC (Reuniones de Emergencia y Ordinarias: Marzo, Abril y Junio 2020).
        * **Investigación:** Fed de St. Louis (FRED), Fed de Cleveland, Robert Shiller, Aswath Damodaran.
        """)

    # Habilidades del Siglo XXI
    st.markdown("### 🌟 Habilidades del Siglo XXI")
    st.markdown("""
    * 🧠 **Pensamiento Crítico Sistémico:** Análisis de contradicciones macroeconómicas.
    * ⚖️ **Toma de Decisiones bajo Incertidumbre:** Evaluación de *trade-offs* de política monetaria.
    * 📊 **Alfabetización en Datos Financieros:** Interpretación de curvas de tipos, breakevens y tasas reales.
    * 🗣️ **Argumentación Rigurosa:** Preparación para defensa oral basada en evidencia empírica.
    """)

# -----------------------------------------------------------------------------
# 4. ENCABEZADO PRINCIPAL DE LA APLICACIÓN
# -----------------------------------------------------------------------------
st.markdown(f"""
<div class="uia-header">
    <span class="uia-badge">Economía I • Sesión Sincrónica</span>
    <h1 style="margin: 0; font-size: 2.2rem; font-weight: 800;">Disonancia del Mercado del Tesoro & Control de Rendimientos</h1>
    <p style="margin: 8px 0 0 0; color: #cbd5e1; font-size: 1.05rem;">
        Plataforma interactiva para el desarrollo del pensamiento crítico y comprobación de maestría oral.
    </p>
    <div style="margin-top: 15px; font-size: 0.95rem; color: #f59e0b; font-weight: 600;">
        👤 Alumno(a) activo(a): <span style="color: #ffffff;">{st.session_state.student_name if st.session_state.student_name else "Por favor ingrese su nombre en la barra lateral"}</span>
    </div>
</div>
""", unsafe_allow_html=True)

if not st.session_state.student_name:
    st.warning("⚠️ **Atención:** Para comenzar y asegurar que tus aportes queden consolidados en el informe final, por favor ingresa tu nombre en la barra lateral izquierda.")

# -----------------------------------------------------------------------------
# 5. ESTRUCTURA MODULAR POR PESTAÑAS (TABS)
# -----------------------------------------------------------------------------
tab_demo, tab_debate, tab_case, tab_sim, tab_viva, tab_summary = st.tabs([
    "📊 1. Demostración & Métricas Sincrónicas",
    "⚖️ 2. Debate Socrático",
    "📑 3. Estudio de Caso (Case Method)",
    "🎮 4. Simulador Interactivo",
    "🗣️ 5. Comprobación de Maestría (Mastery Viva)",
    "📥 6. Resumen & Exportación"
])

# =============================================================================
# TAB 1: DEMOSTRACIÓN & MÉTRICAS SINCRÓNICAS (Merrill: Demostración)
# =============================================================================
with tab_demo:
    st.markdown("## 1. Demostración Visual de la Dinámica Macroeconómica")
    st.markdown("""
    Durante la sesión sincrónica, analizamos la **disonancia** fundamental expuesta por Lyn Alden:
    históricamente el mercado de bonos del Tesoro representaba el *"dinero inteligente"* (anticipando recesiones sin falsos positivos).
    Sin embargo, en 2020 la Reserva Federal intervino con la compra de más de **$2.2 billones** en deuda pública (más del 50% de la emisión neta),
    generando una profunda distorsión de precios y rendimientos reales negativos.
    """)

    # Métricas Clave
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Rendimiento Nominal 10Y (Ago 2020)", value="0.71%", delta="+36% en 9 días")
    with col2:
        st.metric(label="Tasa Real a 10 Años", value="-0.94%", delta="Mínimo de -1.08% en Ago 6")
    with col3:
        st.metric(label="Compras Diarias Fed (Marzo 2020)", value="$75,000 M/día", delta=">$1B en 3 semanas")
    with col4:
        st.metric(label="Compras Fed vs Emisión Neta", value=">50%", delta="2.2 de 4 Billones USD")

    st.markdown("---")

    col_graph1, col_graph2 = st.columns(2)

    with col_graph1:
        st.markdown("### 📈 A. El Núcleo de la Disonancia: Nominal vs Inflación")
        st.caption("Divergencia entre la tasa de inflación anticipada por el mercado (Breakeven) y el rendimiento nominal anclado por la Fed.")
        
        # Generación de serie sintética representativa de los datos de la fuente (Enero a Agosto 2020)
        dates = pd.date_range(start="2020-01-01", end="2020-08-15", freq="W")
        nominal_10y = [1.8, 1.75, 1.6, 1.5, 1.2, 0.7, 0.55, 0.85, 0.65, 0.60, 0.62, 0.64, 0.68, 0.65, 0.59, 0.55, 0.52, 0.54, 0.58, 0.62, 0.58, 0.54, 0.53, 0.52, 0.52, 0.55, 0.54, 0.52, 0.53, 0.52, 0.62, 0.71][:len(dates)]
        breakeven_inf = [1.7, 1.65, 1.5, 1.3, 0.9, 0.6, 0.50, 0.75, 0.95, 1.10, 1.20, 1.25, 1.32, 1.38, 1.40, 1.42, 1.45, 1.50, 1.55, 1.58, 1.60, 1.62, 1.65, 1.67, 1.68, 1.70, 1.72, 1.74, 1.75, 1.73, 1.70, 1.68][:len(dates)]
        real_yield = [n - b for n, b in zip(nominal_10y, breakeven_inf)]

        df_disonancia = pd.DataFrame({
            "Fecha": dates,
            "Rendimiento Nominal 10Y": nominal_10y,
            "Breakeven Inflación 10Y": breakeven_inf,
            "Rendimiento Real (Nominal - Breakeven)": real_yield
        })

        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=df_disonancia["Fecha"], y=df_disonancia["Rendimiento Nominal 10Y"], mode='lines', name='Nominal 10Y', line=dict(color='#2563eb', width=2.5)))
        fig1.add_trace(go.Scatter(x=df_disonancia["Fecha"], y=df_disonancia["Breakeven Inflación 10Y"], mode='lines', name='Expectativa Inflación (Breakeven)', line=dict(color='#dc2626', width=2.5, dash='dash')))
        fig1.add_trace(go.Scatter(x=df_disonancia["Fecha"], y=df_disonancia["Rendimiento Real (Nominal - Breakeven)"], mode='lines', name='Rendimiento Real (Área Negativa)', line=dict(color='#059669', width=2), fill='tozeroy'))
        fig1.update_layout(
            height=380,
            margin=dict(l=20, r=20, t=30, b=20),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            yaxis_title="Tasa de Interés (%)",
            hovermode="x unified"
        )
        st.plotly_chart(fig1, use_container_width=True)
        st.info("💡 **Observación pedagógica:** Mientras la inflación anticipada se recuperó con fuerza hacia el 1.7%, los rendimientos nominales quedaron planchados en 0.5%-0.7% por la intervención de la Fed, empujando la tasa real a territorio profundamente negativo (-1.08%).")

    with col_graph2:
        st.markdown("### 🏦 B. Monetización del Déficit: Quién Financia al Tío Sam")
        st.caption("Comparación de la emisión neta total acumulada vs las compras directas de la Reserva Federal (T4 2019 a Ago 2020).")
        
        fig2 = go.Figure(data=[
            go.Bar(name='Emisión Neta Total del Tesoro', x=['Financiamiento 2019-2020'], y=[4.0], marker_color='#94a3b8', text=['$4.0 Trillones'], textposition='auto'),
            go.Bar(name='Compras Acumuladas Fed', x=['Financiamiento 2019-2020'], y=[2.2], marker_color='#1e3a8a', text=['$2.2 Trillones (>55%)'], textposition='auto'),
            go.Bar(name='Absorción Mercado Privado', x=['Financiamiento 2019-2020'], y=[1.8], marker_color='#d97706', text=['$1.8 Trillones'], textposition='auto')
        ])
        fig2.update_layout(
            barmode='group',
            height=380,
            margin=dict(l=20, r=20, t=30, b=20),
            yaxis_title="Billones de Dólares (Trillions USD)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig2, use_container_width=True)
        st.warning("⚠️ **Concepto Feynman:** 'Comer nuestra propia comida': La Fed imprimió dólares para absorber más bonos que todo el sector exterior acumuló en los últimos 8 años.")

    # Metáforas didácticas de la lectura
    st.markdown("### 🚴 Analogías Didácticas para Desmitificar Conceptos Complejos")
    c_m1, c_m2, c_m3 = st.columns(3)
    with c_m1:
        st.markdown("""
        **1. El Niño y la Bicicleta con Rueditas**
        * **Analogía:** La Fed sostuvo al mercado en marzo y luego intentó que pedaleara solo retirando levemente las compras.
        * **Falla en agosto:** Cuando el niño (mercado privado) intentó absorber las subastas de bonos a 30 años sin la Fed, la bicicleta empezó a tambalearse y los rendimientos se dispararon 36%.
        """)
    with c_m2:
        st.markdown("""
        **2. El Balón de Playa bajo el Agua**
        * **Analogía:** Mantener los rendimientos por debajo de la inflación es como hundir un balón de playa a la fuerza.
        * **Fuerza ascendente:** La presión inflacionaria y el déficit fiscal empujan el rendimiento hacia arriba. Si la Fed suelta el balón, los costes del servicio de la deuda del gobierno estallan.
        """)
    with c_m3:
        st.markdown("""
        **3. Rendimientos Reales y el Oro**
        * **Analogía:** El costo de oportunidad de guardar riqueza.
        * **Efecto:** Cuando los bonos pagan tasas reales negativas (-1%), el efectivo pierde poder adquisitivo. Guardar un activo escaso sin rendimiento (oro) se vuelve matemáticamente superior a financiar deuda que pierde valor.
        """)

# =============================================================================
# TAB 2: DEBATE SOCRÁTICO (Merrill: Aplicación & Contrastación)
# =============================================================================
with tab_debate:
    st.markdown("## 2. Módulo de Pensamiento Crítico: Debate Socrático")
    st.markdown("""
    En este espacio deberás analizar los desacuerdos fundamentales presentes en las fuentes, elegir una postura
    y defenderla con argumentos macroeconómicos rigurosos. **La aplicación evaluará la calidad de tu razonamiento.**
    """)

    debates = {
        "Debate 1: Señales Distorsionadas vs Dinero Inteligente": {
            "pregunta": "¿Podemos seguir confiando en la curva de rendimientos como 'dinero inteligente' si la Reserva Federal compra más de la mitad de la emisión?",
            "bando_a": "Postura A: El mercado ha sido totalmente intervenido. La Fed anula las fuerzas del mercado libre mediante QE agresivo y guía futura; los rendimientos ya no reflejan expectativas económicas reales sino el capricho del banco central.",
            "bando_b": "Postura B: El mercado aún emite señales verídicas si sabemos dónde mirar. Por ejemplo, los bonos TIPS (protegidos contra inflación) y el breakeven anticiparon correctamente el rebote inflacionario a pesar de las compras de la Fed."
        },
        "Debate 2: Deflación Estructural vs Estanflación / Inflación Secular": {
            "pregunta": "¿Hacia dónde se dirige la economía de los años 2020 tras el choque pandémico y la emisión masiva de deuda?",
            "bando_a": "Postura A: Campamento Deflacionario. El sobreendeudamiento extremo, el desempleo y la eventual retirada del estímulo fiscal provocarán insolvencias generalizadas y una espiral deflacionaria prolongada.",
            "bando_b": "Postura B: Campamento Estanflacionario. La monetización directa de déficits gigantescos combinada con limitaciones de oferta revivirá la inflación de los años 70 y obligará a licuar la deuda soberana mediante tasas reales negativas."
        },
        "Debate 3: Control Formal de la Curva (YCC) vs Guía Futura Exclusiva": {
            "pregunta": "¿Debe la Fed formalizar un Control de Curva de Rendimientos (YCC) al estilo de los años 1940 para topar las tasas a largo plazo?",
            "bando_a": "Postura A: Sí, es imperativo. Con déficits superiores al 100% del PIB, permitir que los rendimientos a 10 y 30 años suban tornaría impagable el servicio de la deuda del gobierno, requiriendo un tope formal como en 1942.",
            "bando_b": "Postura B: No, el riesgo es excesivo. Como demostró la experiencia histórica previa al Acuerdo de 1951, el YCC expande el balance sin control si las expectativas de inflación suben, poniendo en riesgo la independencia del banco central."
        }
    }

    selected_debate_key = st.selectbox("Selecciona la Controversia Macroeconómica a examinar:", list(debates.keys()))
    debate_info = debates[selected_debate_key]

    st.markdown(f"### ❓ Dilema Central: {debate_info['pregunta']}")
    
    col_da, col_db = st.columns(2)
    with col_da:
        st.markdown(f"""
        <div class="uia-card" style="border-top: 4px solid #2563eb;">
            <h4 style="color: #1e3a8a;">Lado 1</h4>
            <p>{debate_info['bando_a']}</p>
        </div>
        """, unsafe_allow_html=True)
    with col_db:
        st.markdown(f"""
        <div class="uia-card" style="border-top: 4px solid #d97706;">
            <h4 style="color: #b45309;">Lado 2</h4>
            <p>{debate_info['bando_b']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("#### ✍️ Tu Posicionamiento Estudiantil")
    user_stance = st.radio(
        "¿Cuál postura decides respaldar tras contrastar los datos de la fuente?",
        ["Respaldar Lado 1", "Respaldar Lado 2", "Proponer una síntesis dialéctica intermedia"],
        index=0
    )

    argument_text = st.text_area(
        "Desarrolla tu argumentación económica fundamentada (mínimo 2 premisas y 1 evidencia concreta del texto):",
        value=st.session_state.session_answers["socratic_debate"]["arguments"],
        height=140,
        placeholder="Ej: Respaldamos la postura de que las señales están distorsionadas porque la Fed monetizó el 55% de la deuda en meses, lo que mantiene artificialmente baja la tasa nominal frente al breakeven..."
    )

    if st.button("Someter Argumentación a Evaluación Formativa", key="btn_eval_debate"):
        if len(argument_text.strip()) < 50:
            st.error("⚠️ Tu argumentación es demasiado breve. Un economista en formación debe justificar con premisas y evidencia empírica clara.")
        else:
            # Algoritmo de feedback formativo heurístico
            kw_match = sum(1 for kw in ["fed", "rendimiento", "inflación", "breakeven", "liquidez", "déficit", "tesoro", "bonos", "tasas reales", "1940"] if kw in argument_text.lower())
            
            feedback_msg = ""
            score_delta = 0
            if kw_match >= 4:
                score_delta = 95
                feedback_msg = "✅ **Excelente Rigor Analítico:** Lograste articular conceptos macroeconómicos clave (monetización, tasas reales o inflación esperada) conectando la causa institucional con el efecto en precios de mercado. Estás listo para defender este punto oralmente."
            elif kw_match >= 2:
                score_delta = 80
                feedback_msg = "🔍 **Buen Razonamiento Inicial:** Identificas el conflicto principal, pero aún necesitas profundizar en cómo la compra de bonos por parte de la Fed altera específicamente el costo de oportunidad o las tasas reales. ¿Qué le pasa a un inversor que mantiene bonos a 10 años si la inflación sube más que el rendimiento?"
            else:
                score_delta = 65
                feedback_msg = "💡 **Lucha Productiva Requerida:** Tu postura es comprensible, pero carece de anclaje en los datos de la lectura. Revisa la sección de breakeven de inflación vs rendimientos nominales para enriquecer tu evidencia cuantitativa."

            st.session_state.session_answers["socratic_debate"] = {
                "selected_debate": selected_debate_key,
                "position": user_stance,
                "arguments": argument_text,
                "feedback": feedback_msg,
                "score": score_delta
            }
            st.success("Respuesta guardada con éxito en tu sesión.")

    if st.session_state.session_answers["socratic_debate"]["feedback"]:
        st.markdown(f"""
        <div class="pedagogical-alert">
            {st.session_state.session_answers['socratic_debate']['feedback']}
        </div>
        """, unsafe_allow_html=True)

# =============================================================================
# TAB 3: ESTUDIO DE CASO (Case Method - Estructura 5 Puntos UIA)
# =============================================================================
with tab_case:
    st.markdown("## 3. Estudio de Caso: Metodología Pedagógica UIA")
    st.markdown("""
    Este caso de estudio sigue estrictamente la estructura metodológica de 5 puntos de la Cátedra de Economía Aplicada.
    Analiza la situación y redacta tu dictamen técnico.
    """)

    st.markdown("""
    <div class="uia-card">
        <h3 style="color: #0d284f; margin-top: 0;">1) Título del Caso</h3>
        <p style="font-size: 1.15rem; font-weight: 700; color: #1e3a8a;">
            "El Cortocircuito de Liquidez de Marzo 2020: La Ilusión del Activo Libre de Riesgo frente al Shock de Efectivo"
        </p>
        
        <h3 style="color: #0d284f;">2) Objetivos de Aprendizaje</h3>
        <ul>
            <li>Comprender la diferencia crítica entre solvencia y liquidez inmediata en momentos de pánico financiero.</li>
            <li>Evaluar por qué los bonos del Tesoro, considerados activos libres de riesgo crediticio, se vendieron masivamente junto con las acciones.</li>
            <li>Diseñar alternativas de política monetaria evaluando las compensaciones (trade-offs) entre estabilidad financiera y monetización del déficit.</li>
        </ul>

        <h3 style="color: #0d284f;">3) Contexto del Caso</h3>
        <p>
            A mediados de marzo de 2020, ante la propagación global del COVID-19 y el colapso bursátil, ocurrió un fenómeno inédito:
            los bonos del Tesoro a largo plazo cayeron en precio al mismo tiempo que las acciones. El sector exterior vendió <b>$250,000 millones</b> en títulos del Tesoro en cuestión de días para conseguir dólares en efectivo.
            Fondos de cobertura con estrategias de paridad de riesgo apalancado se vieron forzados a liquidar.
            Los diferenciales de compra/venta (bid-ask spreads) para bonos <i>off-the-run</i> se dispararon y la profundidad del mercado se evaporó.
        </p>

        <h3 style="color: #0d284f;">4) Planteamiento del Problema o Desafío</h3>
        <p>
            <b>El Conflicto Central:</b> El mercado del Tesoro de EE.UU. (el pilar del sistema financiero global) dejó de funcionar eficazmente.
            Si el gobierno requería emitir billones para transferencias de emergencia por desempleo y la demanda privada se había secado,
            ¿debía la Reserva Federal convertirse en el comprador directo ilimitado a costa de monetizar el déficit fiscal?
        </p>
        <p><i>Preguntas orientadoras de reflexión:</i></p>
        <ol>
            <li>¿Por qué en una crisis extrema los inversores prefieren billetes de dólares en lugar de títulos del Tesoro que pagan intereses?</li>
            <li>¿Qué consecuencias a mediano plazo genera que el banco central compre $75,000 millones diarios de deuda de su propio gobierno?</li>
        </ol>
        
        <h3 style="color: #0d284f;">5) Guía de Investigación y Posicionamiento Estudiantil</h3>
        <p>
            Analiza el fragmento de las actas del FOMC de marzo/abril de 2020 provisto en la fuente. Redacta a continuación tu dictamen técnico
            evaluando el impacto sobre los intermediarios primarios y recomendando la postura de política adecuada.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col_c1, col_c2 = st.columns(2)
    with col_c1:
        diag_text = st.text_area(
            "A. Diagnóstico: ¿Por qué colapsó la liquidez en los bonos off-the-run a mediados de marzo 2020?",
            value=st.session_state.session_answers["case_study"]["liquidity_diagnosis"],
            height=130,
            placeholder="Analiza las ventas extranjeras ($250B), el apalancamiento de fondos de cobertura y la búsqueda urgente de dólares billete..."
        )
    with col_c2:
        pol_text = st.text_area(
            "B. Recomendación: ¿Cómo debió actuar la Fed y qué compensación de riesgos (trade-offs) asumió?",
            value=st.session_state.session_answers["case_study"]["policy_decision"],
            height=130,
            placeholder="Evalúa la compra masiva de $75B/día vs el riesgo de inflación a futuro y pérdida de independencia..."
        )

    if st.button("Guardar Dictamen del Estudio de Caso", key="btn_eval_case"):
        if len(diag_text.strip()) < 40 or len(pol_text.strip()) < 40:
            st.error("⚠️ Por favor completa ambos campos del estudio de caso con un desarrollo analítico suficiente.")
        else:
            kws = sum(1 for kw in ["liquidez", "off-the-run", "cobertura", "dólares", "75", "prestamista", "inflación", "monetización", "intervención"] if kw in (diag_text + pol_text).lower())
            score_case = min(100, 70 + (kws * 5))
            fb_case = f"📋 **Dictamen Registrado (Puntuación de Rigor: {score_case}/100):** Has demostrado comprensión sobre la mecánica de iliquidez y el rol de prestamista de última instancia de la Fed. La evidencia sobre intermediarios primarios fortalece sustancialmente tu análisis."
            
            st.session_state.session_answers["case_study"] = {
                "liquidity_diagnosis": diag_text,
                "policy_decision": pol_text,
                "portfolio_impact": "Completado y analizado",
                "feedback": fb_case,
                "score": score_case
            }
            st.success("Estudio de caso guardado exitosamente.")

    if st.session_state.session_answers["case_study"]["feedback"]:
        st.markdown(f"""
        <div class="pedagogical-alert">
            {st.session_state.session_answers['case_study']['feedback']}
        </div>
        """, unsafe_allow_html=True)

# =============================================================================
# TAB 4: SIMULADOR INTERACTIVO "ELIGE TU AVENTURA ECONÓMICA" (Merrill: Aplicación)
# =============================================================================
with tab_sim:
    st.markdown("## 4. Simulador Macroeconómico: Elige tu Propia Aventura")
    st.markdown("""
    Asume el rol de **Gobernador de la Reserva Federal y Miembro del FOMC**. Cada decisión que tomes
    ramificará la trayectoria económica y expondrá los dilemas reales vividos entre 2019 y 2020.
    Si cometes un error conceptual, el simulador te brindará retroalimentación pedagógica para reintentar.
    """)

    sim_steps_data = {
        1: {
            "title": "Escenario 1: Septiembre de 2019 — La Crisis del Mercado Repo",
            "context": "La tasa de interés del mercado de préstamos interbancarios garantizados (Repo) se dispara repentinamente al 10%. Los bancos comerciales no tienen suficiente efectivo disponible para financiar las crecientes emisiones de deuda del gobierno de EE.UU. El sistema de pagos está a punto de congelarse.",
            "options": [
                ("Opción 1A: No intervenir", "Dejar que el mercado libre de bonos ajuste las tasas de interés al alza para atraer capital privado internacional, sin emitir nueva moneda.", "error", "❌ **Callejón sin Salida Económico:** Al no intervenir, el sistema bancario colapsa por asfixia de liquidez. La deuda federal en expansión requiere compradores que el sector exterior ya no está dispuesto a proveer. Provocas una crisis crediticia innecesaria."),
                ("Opción 1B: Intervenir e iniciar monetización", "Iniciar compras de letras del Tesoro y repo de emergencia, creando reservas bancarias nuevas (expansión de balance) para proveer liquidez y absorber el excedente de deuda.", "correct", "✅ **Decisión Históricamente Coherente:** Esto fue exactamente lo que hizo la Fed a fines del T3 de 2019. Creó nuevos dólares para estabilizar el mercado repo, marcando el inicio de la monetización del déficit en plena fase de expansión económica.")
            ]
        },
        2: {
            "title": "Escenario 2: Mediados de Marzo de 2020 — El Pánico Pandémico y la Iliquidez de los Bonos",
            "context": "El COVID-19 paraliza la economía. Los mercados de renta variable caen en picada, pero sorpresivamente los bonos del Tesoro también se desploman y sus rendimientos se duplican. El sector exterior vende $250,000 millones y los diferenciales de compra/venta se abren de par en par. La liquidez desaparece.",
            "options": [
                ("Opción 2A: Actuar como Prestamista de Último Recurso Masivo", "Lanzar compras ilimitadas de títulos del Tesoro a un ritmo récord de hasta $75,000 millones al día, inyectando más de $1 billón en 3 semanas para licuar el mercado.", "correct", "✅ **Acierto Técnico:** Esta medida de emergencia restauró la liquidez en los bonos on-the-run y frenó en seco la espiral de rendimientos, evitando la quiebra en cadena de intermediarios primarios y fondos con apalancamiento."),
                ("Opción 2B: Esperar que el mercado de bonos encuentre su propio equilibrio", "Asumir que los bonos del Tesoro son seguros y que los compradores privados aparecerán atraídos por las mayores tasas nominales.", "error", "❌ **Fallo de Comprensión:** En un pánico extremo, la demanda de dólares billete superó con creces la disposición a mantener títulos ilíquidos. Sin la intervención de la Fed, el mercado del Tesoro estadounidense habría dejado de operar.")
            ]
        },
        3: {
            "title": "Escenario 3: Verano de 2020 — La Disonancia y las 'Ruedas de Entrenamiento'",
            "context": "La inflación esperada (breakeven) sube al 1.7%, pero la Fed mantiene los rendimientos a 10 años cerca del 0.6%. La Fed comienza a desacelerar sus compras semanales, intentando que el mercado privado comience a absorber más de $1 billón en nuevas emisiones sin asistencia.",
            "options": [
                ("Opción 3A: Mantener supervisión cercana y preparar Control de Curva (YCC)", "Reconocer que el mercado privado aún es frágil frente a emisiones gigantescas y evaluar formalmente topar los rendimientos mediante Yield Curve Control.", "correct", "✅ **Estrategia Acertada:** Como documentaron las actas de junio de 2020 y los informes de la Fed de St. Louis, la institución analizó las lecciones de la Segunda Guerra Mundial y de Japón/Australia para evitar que las subastas caóticas dispararan los costos de la deuda."),
                ("Opción 3B: Retirar totalmente las compras y subir tasas de interés", "Subir las tasas para compensar la inflación reportada que supera el 1.5%.", "error", "❌ **Grave Error Macroeconómico:** Con un desempleo de millones de personas y una recuperación frágil, subir tasas en agosto de 2020 habría abortado la recuperación fiscal y disparado el déficit por costos de servicio de deuda.")
            ]
        },
        4: {
            "title": "Escenario 4: Agosto de 2020 — Subastas Caóticas a 30 Años y el Repunte de Tipos",
            "context": "El rendimiento a 10 años sube un 36% en apenas 9 días (del 0.52% al 0.71%). La subasta de bonos a 30 años muestra una demanda excepcionalmente débil. El 'niño en la bicicleta' empieza a tambalearse.",
            "options": [
                ("Opción 4A: Intervención Estratégica con Orientación Futura", "Reafirmar que la Fed apoyará el mercado según sea necesario y tolerar un sobrepaso temporal de la meta de inflación del 2% para anclar las tasas reales negativas.", "correct", "✅ **Maestría Alcanzada:** Esta postura guió la política de la Fed en el simposio de Jackson Hole a fines de agosto de 2020 (Average Inflation Targeting), manteniendo las condiciones financieras acomodaticias a pesar del repunte de inflación."),
                ("Opción 4B: Negar cualquier intervención y culpar a los inversores", "Declarar que la Fed no tiene responsabilidad sobre el mercado secundario de deuda soberana.", "error", "❌ **Contradicción Institucional:** El mandato de estabilidad financiera y pleno empleo obliga a la Fed a garantizar el financiamiento fluido del Estado.")
            ]
        }
    }

    curr_step = st.session_state.sim_step
    step_data = sim_steps_data.get(curr_step, sim_steps_data[4])

    st.markdown(f"### 📍 {step_data['title']}")
    st.markdown(f"""
    <div class="uia-card" style="border-left: 5px solid #0d284f;">
        <p style="font-size: 1.05rem;">{step_data['context']}</p>
    </div>
    """, unsafe_allow_html=True)

    opt_choice = st.radio(
        "¿Qué decisión de política económica eliges implementar?",
        [opt[0] + ": " + opt[1] for opt in step_data["options"]],
        key=f"radio_step_{curr_step}"
    )

    if st.button("Ejecutar Decisión", key=f"btn_step_{curr_step}"):
        chosen_opt = step_data["options"][0] if "Opción 1A" in opt_choice or "Opción 2A" in opt_choice or "Opción 3A" in opt_choice or "Opción 4A" in opt_choice else step_data["options"][1]
        
        # Evaluar resultado
        if chosen_opt[2] == "correct":
            st.success(chosen_opt[3])
            st.session_state.session_answers["narrative_sim"]["step_choices"][f"Paso {curr_step}"] = {
                "decision": chosen_opt[0],
                "resultado": "Correcto",
                "explicacion": chosen_opt[3]
            }
            if curr_step < 4:
                st.session_state.sim_step = curr_step + 1
                st.rerun()
            else:
                st.balloons()
                st.session_state.session_answers["narrative_sim"]["final_status"] = "Completado con Éxito (4/4 Pasos)"
                st.session_state.session_answers["narrative_sim"]["score"] = 100
                st.session_state.session_answers["narrative_sim"]["feedback"] = "Dominio completo de la cronología y de los dilemas de monetización de déficit."
        else:
            st.error(chosen_opt[3])
            st.markdown("""
            <div class="struggle-alert">
                <b>Pausa Pedagógica (Productive Struggle):</b> Antes de avanzar, reflexiona sobre la relación causal.
                Recuerda que la Fed interviene no por capricho, sino porque la emisión de deuda superó la capacidad de absorción del mercado privado. ¡Vuelve a intentarlo!
            </div>
            """, unsafe_allow_html=True)

    if curr_step > 1:
        if st.button("🔄 Reiniciar Simulación", key="btn_reset_sim"):
            st.session_state.sim_step = 1
            st.session_state.session_answers["narrative_sim"]["step_choices"] = {}
            st.rerun()

# =============================================================================
# TAB 5: COMPROBACIÓN DE MAESTRÍA (Mastery Viva / Defensa Oral)
# =============================================================================
with tab_viva:
    st.markdown("## 5. Comprobación de Maestría: Simulación de Defensa Oral (Mastery Viva)")
    st.markdown("""
    En concordancia con el marco **Mastery Flip de Jon Bergmann**, la verdadera verificación de aprendizaje
    ocurre en el espacio sincrónico a través del **Human Check**: una defensa oral cara a cara con el docente.
    
    *Utiliza esta sección para estructurar tus respuestas antes de la sustentación.*
    """)

    st.markdown("""
    <div class="dark-card">
        <h4 style="color: #f59e0b; margin-top: 0;">🎯 Regla de Oro del Examen de Maestría (Método Feynman):</h4>
        <p style="margin-bottom: 0;">"Si no eres capaz de explicar un fenómeno macroeconómico complejo con analogías cotidianas y rigor analítico en menos de dos minutos sin apoyarte en un algoritmo, aún no has adquirido maestría."</p>
    </div>
    """, unsafe_allow_html=True)

    viva_q1 = st.text_area(
        "Pregunta 1: ¿Por qué tener tasas reales fuertemente negativas (-1.08%) perjudica a los ahorristas pero es la única salida matemática viable para un gobierno con deuda >100% del PIB?",
        value=st.session_state.session_answers["mastery_viva"]["q1_defense"],
        height=100,
        placeholder="Explica la devaluación silenciosa de la deuda frente a la inflación y la pérdida de poder adquisitivo del ahorro..."
    )

    viva_q2 = st.text_area(
        "Pregunta 2: ¿Por qué durante la QE de 2010-2014 las compras de la Fed hicieron SUBIR los rendimientos, mientras que en 2020 los mantuvieron BAJOS?",
        value=st.session_state.session_answers["mastery_viva"]["q2_defense"],
        height=100,
        placeholder="Contrasta la QE opcional de liquidez bancaria (65% deuda/PIB) con la monetización forzada de déficit fiscal pandémico..."
    )

    viva_q3 = st.text_area(
        "Pregunta 3: Desmitifica la disonancia entre los bonos del Tesoro y el Oro. ¿Cuál es el costo de oportunidad que conecta a ambos activos?",
        value=st.session_state.session_answers["mastery_viva"]["q3_defense"],
        height=100,
        placeholder="Analiza la correlación inversa entre tasas reales de interés y el atractivo de los metales preciosos como reserva de valor..."
    )

    viva_q4 = st.text_area(
        "Pregunta 4: ¿Qué precedente histórico de los años 1940 anticipa los riesgos de implementar un Control de la Curva de Rendimientos (YCC) hoy?",
        value=st.session_state.session_answers["mastery_viva"]["q4_defense"],
        height=100,
        placeholder="Menciona el tope del 2.5%, la multiplicación por diez del balance de la Fed y el Acuerdo Tesoro-Fed de 1951..."
    )

    self_eval = st.slider("Autoevaluación de Confianza para la Defensa Oral (1 = Inseguro, 5 = Dominio Total):", 1, 5, value=st.session_state.session_answers["mastery_viva"]["self_rating"])

    if st.button("Guardar Ensayo de Defensa Oral", key="btn_save_viva"):
        if not (viva_q1 and viva_q2 and viva_q3 and viva_q4):
            st.warning("⚠️ Te recomendamos contestar las cuatro preguntas para asegurar tu preparación integral para la clase sincrónica.")
        
        # Calcular puntaje viva
        filled_count = sum(1 for q in [viva_q1, viva_q2, viva_q3, viva_q4] if len(q.strip()) > 30)
        viva_score = filled_count * 25
        
        st.session_state.session_answers["mastery_viva"] = {
            "q1_defense": viva_q1,
            "q2_defense": viva_q2,
            "q3_defense": viva_q3,
            "q4_defense": viva_q4,
            "self_rating": self_eval,
            "score": viva_score
        }
        st.success(f"Respuestas guardadas. Nivel de preparación registrado: {viva_score}% de maestría documental.")

    # Rúbrica de evaluación oral
    with st.expander("📋 Rúbrica de Evaluación de la Defensa Oral Docente", expanded=False):
        st.markdown("""
        | Criterio | Nivel Inicial (1-2) | Nivel Competente (3-4) | Nivel Maestría (5) |
        | :--- | :--- | :--- | :--- |
        | **Rigor Conceptual** | Confunde rendimientos nominales y reales. | Diferencia nominal y real pero duda en breakevens. | Articula con fluidez el impacto de la tasa real negativa en deuda y activos. |
        | **Manejo de Evidencia** | No cita cifras de la lectura. | Recuerda compras de la Fed y shock de marzo. | Contrasta con precisión $75B/día, 55% de emisión y precedentes de 1940. |
        | **Pensamiento Crítico** | Repite fórmulas sin cuestionar la intervención. | Cuestiona la distorsión del mercado de bonos. | Evalúa los trade-offs de solvencia vs inflación y límites del banco central. |
        | **Claridad Feynman** | Lenguaje confuso y memorístico. | Explica con dificultad pero responde preguntas. | Utiliza analogías efectivas y responde con seguridad ante contrapreguntas. |
        """)

# =============================================================================
# TAB 6: RESUMEN CONSOLIDADO & EXPORTACIÓN
# =============================================================================
with tab_summary:
    st.markdown("## 6. Resumen de Desempeño y Exportación del Reporte")
    st.markdown("""
    A continuación se presenta el consolidado de tu sesión de trabajo sincrónica.
    Descarga tu reporte oficial en formato Markdown para entregarlo al profesor o presentarlo durante tu comprobación de maestría.
    """)

    student = st.session_state.student_name if st.session_state.student_name else "Estudiante no registrado"
    deb_data = st.session_state.session_answers["socratic_debate"]
    case_data = st.session_state.session_answers["case_study"]
    sim_data = st.session_state.session_answers["narrative_sim"]
    viva_data = st.session_state.session_answers["mastery_viva"]

    # Cálculo de Calificación Consolidada
    scores = [deb_data["score"], case_data["score"], sim_data["score"], viva_data["score"]]
    avg_score = sum(scores) / max(1, len(scores))

    c_s1, c_s2, c_s3 = st.columns(3)
    with c_s1:
        st.metric(label="Estudiante Evaluado", value=student)
    with c_s2:
        st.metric(label="Calificación Global Ponderada", value=f"{avg_score:.1f} / 100")
    with c_s3:
        status_label = "Dominio Sobresaliente 🏆" if avg_score >= 85 else ("En Desarrollo Positivo 📈" if avg_score >= 60 else "Requiere Mayor Profundización ⚠️")
        st.metric(label="Estado de Maestría", value=status_label)

    st.markdown("---")

    # Generación del Texto Markdown Consolidado
    report_content = f"""# REPORTE DE APRENDIZAJE Y COMPROBACIÓN DE MAESTRÍA
**Universidad Internacional de las Américas (U.I.A.)**  
**Cátedra:** Macroeconomía y Pensamiento Crítico  
**Sesión:** S6TBC - Disonancia del Mercado del Tesoro & Control de Curva  
**Metodología:** Mastery Flip (Jon Bergmann) & 4 Principios Didácticos (David Merrill)  
**Estudiante:** {student}  
**Calificación Global:** {avg_score:.1f} / 100  
**Dictamen:** {status_label}  

---

## 1. Módulo de Pensamiento Crítico: Debate Socrático
* **Controversia Seleccionada:** {deb_data['selected_debate']}
* **Postura Adoptada:** {deb_data['position']}
* **Argumentación del Estudiante:**
> {deb_data['arguments'] if deb_data['arguments'] else "Sin registrar"}
* **Retroalimentación Formativa Recibida:**
> {deb_data['feedback'] if deb_data['feedback'] else "Pendiente de evaluación"}
* **Puntaje Obtenido:** {deb_data['score']}/100

---

## 2. Estudio de Caso: Metodología Case Method (U.I.A.)
* **Título del Caso:** "El Cortocircuito de Liquidez de Marzo 2020: La Ilusión del Activo Libre de Riesgo"
* **Diagnóstico de Iliquidez y Venta Forzada:**
> {case_data['liquidity_diagnosis'] if case_data['liquidity_diagnosis'] else "Sin registrar"}
* **Recomendación de Política y Trade-offs:**
> {case_data['policy_decision'] if case_data['policy_decision'] else "Sin registrar"}
* **Evaluación del Caso:**
> {case_data['feedback'] if case_data['feedback'] else "Pendiente de evaluación"}
* **Puntaje Obtenido:** {case_data['score']}/100

---

## 3. Simulador Interactivo Macroeconómico
* **Estado Final del Recorrido:** {sim_data['final_status']}
* **Puntaje Obtenido:** {sim_data['score']}/100
* **Decisiones Tomadas en los Pasos:**
"""
    for step_k, step_v in sim_data.get("step_choices", {}).items():
        report_content += f"- **{step_k}:** {step_v['decision']} -> Resultado: {step_v['resultado']}\n"

    report_content += f"""
---

## 4. Ensayo Preparatorio para Defensa Oral (Mastery Viva)
* **Pregunta 1 (Tasas Reales Negativas y Deuda):**
> {viva_data['q1_defense'] if viva_data['q1_defense'] else "Sin registrar"}

* **Pregunta 2 (QE 2010-2014 vs Monetización 2020):**
> {viva_data['q2_defense'] if viva_data['q2_defense'] else "Sin registrar"}

* **Pregunta 3 (Disonancia Tesoro vs Oro):**
> {viva_data['q3_defense'] if viva_data['q3_defense'] else "Sin registrar"}

* **Pregunta 4 (Lecciones Históricas 1940 y Control de Curva):**
> {viva_data['q4_defense'] if viva_data['q4_defense'] else "Sin registrar"}

* **Autoevaluación de Confianza:** {viva_data['self_rating']} / 5  
* **Puntaje Preparatorio de Maestría:** {viva_data['score']}/100  

---

## 5. Matriz de Habilidades del Siglo XXI Trabajadas
1. **Pensamiento Crítico y Análisis de Contradicciones Macroeconómicas:** Contrastación entre señales de mercado libres e intervencionismo central.
2. **Alfabetización en Datos Financieros:** Interpretación de diferenciales de curva (10Y - 3M), rendimientos reales negativos e inflación de equilibrio.
3. **Resolución de Problemas Complejos:** Evaluación de compensaciones entre liquidez inmediata, solvencia soberana y estabilidad inflacionaria.
4. **Comunicación Rigurosa y Defensa Argumentativa:** Preparación formal de argumentos para sustentación oral cara a cara (Mastery Viva).

*Reporte generado automáticamente por la Plataforma Educativa UIA - Sesión Sincrónica Semana 6.*
"""

    st.markdown("### 📄 Vista Previa del Reporte Consolidado")
    st.text_area("Contenido del Reporte:", value=report_content, height=280)

    # Botón único de exportación y descarga
    file_safe_name = student.replace(" ", "_").lower() if student else "alumno"
    st.download_button(
        label="📥 Descargar Reporte Oficial de la Sesión (.md)",
        data=report_content.encode("utf-8"),
        file_name=f"reporte_sesion_{file_safe_name}.md",
        mime="text/markdown",
        key="btn_download_report"
    )
    st.caption("Guarda este archivo como respaldo de tu evidencia pedagógica y comprobación de maestría.")
