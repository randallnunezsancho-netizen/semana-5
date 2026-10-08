# 🏛️ Plataforma Educativa Interactiva: Disonancia del Mercado del Tesoro & Mastery Flip

[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35%2B-FF4B4B.svg)](https://streamlit.io/)
[![Institución](https://img.shields.io/badge/UIA-Universidad%20Internacional%20de%20las%20Am%C3%A9ricas-003366.svg)](https://www.uia.ac.cr/)
[![Pedagogía](https://img.shields.io/badge/Metodolog%C3%ADa-Mastery%20Flip%20%26%20Merrill-green.svg)](#marco-pedagógico)

---

## 📌 1. Descripción General del Proyecto y Propósito

Esta aplicación web interactiva ha sido diseñada para estudiantes de primer ingreso de la carrera de Economía de la **Universidad Internacional de las Américas (U.I.A.)**. Su propósito es transformar marcos teóricos y empíricos complejos de macroeconomía en una experiencia de aprendizaje activo orientada al desarrollo del **pensamiento crítico** y la **argumentación rigurosa**.

El núcleo analítico del proyecto está basado en el documento macroeconómico de Lyn Alden (*"Disonancia del mercado del tesoro"*, agosto de 2020), actas oficiales del Comité Federal de Mercado Abierto (FOMC) e investigación histórica de la Reserva Federal.

### El Problema Macroeconómico: La "Disonancia"
Históricamente, el mercado de bonos del Tesoro de EE.UU. ha sido catalogado como el *"dinero inteligente"*, anticipando recesiones sin falsos positivos a través de la inversión de la curva de rendimientos. Sin embargo, en 2020 la Reserva Federal intervino monetizando más del 50% de la emisión neta de deuda federal (adquiriendo más de **$2.2 billones** en meses tras la crisis repo de 2019 y el shock pandémico de 2020). 

Esta intervención masiva generó una **disonancia de mercado**: mientras las expectativas de inflación (breakeven) rebotaron con fuerza hacia el 1.7%, los rendimientos nominales a 10 años quedaron anclados artificialmente cerca del 0.6%, empujando las tasas de interés reales a niveles profundamente negativos (-1.08%) y alterando el costo de oportunidad de los activos de reserva como el oro y Bitcoin.

### El Marco Pedagógico
La herramienta combina de forma sinérgica:
1. **Los 4 Principios de Diseño Didáctico de David Merrill:** *Activación*, *Demostración*, *Aplicación* e *Integración*.
2. **El Enfoque Mastery Flip de Jon Bergmann:** Empleo de la tecnología y la IA como un *Motor Cognitivo* (Socratic Engine) que fomenta la *lucha productiva* (*productive struggle*), enraizado en *Raíces Analógicas* y validado mediante un *Human Check*: la preparación y ejecución de una **Defensa Oral cara a cara (Mastery Viva)** frente al docente.

---

## 🚀 2. Características Principales Implementadas

La plataforma está organizada modularmente en 6 áreas de trabajo sincrónico:

1. **📊 Demostración & Métricas Sincrónicas (Fase Demostrativa):**
   * Gráficos dinámicos e interactivos en **Plotly** que ilustran la disonancia entre rendimiento nominal a 10 años, expectativas de inflación (breakeven) y tasas reales negativas.
   * Gráfico comparativo de monetización de deuda: emisión neta total ($4.0 B) vs compras de la Fed ($2.2 B) vs absorción del mercado privado.
   * Analogías didácticas basadas en el texto: *"El niño en la bicicleta con rueditas"*, *"El balón de playa bajo el agua"* y *"El costo de oportunidad del oro"*.

2. **⚖️ Debate Socrático (Pensamiento Crítico y Dialéctica):**
   * Tres controversias macroeconómicas estructurales:
     * *Debate 1:* Señales distorsionadas por la Fed vs Mercado libre de bonos como dinero inteligente.
     * *Debate 2:* Deflación persistente por sobreendeudamiento vs Estanflación secular en la década de 2020.
     * *Debate 3:* Control Formal de la Curva de Rendimientos (YCC) al estilo de los años 40 vs Guía futura (*Forward Guidance*).
   * Selección obligatoria de postura y argumentación fundamentada con evaluación formativa automática.

3. **📑 Estudio de Caso (Metodología Case Method UIA en 5 Puntos):**
   * Caso estructurado: *"El Cortocircuito de Liquidez de Marzo 2020: La Ilusión del Activo Libre de Riesgo frente al Shock de Efectivo"*.
   * Componentes: 1) Título, 2) Objetivos de aprendizaje, 3) Contexto cuantitativo, 4) Desafío y preguntas orientadoras, 5) Guía de posicionamiento y dictamen técnico.

4. **🎮 Simulador Interactivo "Elige tu Propia Aventura Macroeconómica":**
   * Simulación por etapas asumiendo el rol de Gobernador del FOMC:
     * *Escenario 1:* Septiembre de 2019 (Pico del mercado Repo al 10%).
     * *Escenario 2:* Marzo de 2020 (Congelamiento de liquidez en bonos del Tesoro y compras de $75,000 M/día).
     * *Escenario 3:* Verano de 2020 (Ruedas de entrenamiento y debate de YCC).
     * *Escenario 4:* Agosto de 2020 (Subastas caóticas a 30 años y rebote del 36% en rendimientos).
   * Detección de callejones sin salida con retroalimentación correctiva sin revelar atajos.

5. **🗣️ Comprobación de Maestría (Mastery Viva / Defensa Oral):**
   * Cuatro preguntas inquisitivas diseñadas bajo el **Método Feynman** para evaluar comprensión profunda sin dependencia de algoritmos.
   * Rúbrica oficial de defensa oral (Rigor conceptual, Manejo de evidencia, Pensamiento crítico y Claridad expositiva).
   * Slider de autoevaluación de confianza estudiantil.

6. **📥 Resumen Consolidado & Exportación Oficial:**
   * Almacenamiento continuo acumulativo en `st.session_state`.
   * Cálculo de calificación ponderada global (0-100) y nivel de maestría alcanzado.
   * **Generador y descargador de reporte oficial en Markdown (`.md`)** listo para entrega académica.

---

## 💻 3. Requisitos Técnicos

* **Sistema Operativo:** Windows 10/11, macOS o Linux.
* **Lenguaje:** Python 3.10 o superior (probado y validado en Python 3.13.7).
* **Dependencias Clave:**
  * `streamlit >= 1.35.0`
  * `pandas >= 2.2.0`
  * `numpy >= 1.26.0`
  * `plotly >= 5.20.0`
  * `pypdf >= 4.0.0`

---

## 🛠️ 4. Instrucciones de Instalación Paso a Paso

### Paso 1: Clonar el Repositorio
```bash
git clone https://github.com/randallnunezsancho-netizen/semana-5.git
cd semana-5
git checkout dev
```

### Paso 2: Crear y Activar el Entorno Virtual

* **En Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
* **En macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### Paso 3: Instalar Dependencias
```bash
pip install -r requirements.txt
```

### Paso 4: Ejecutar la Aplicación Streamlit
```bash
streamlit run app.py
```
La aplicación abrirá automáticamente una pestaña en tu navegador en `http://localhost:8501`.

---

## 📖 5. Guía de Uso con Ejemplos Básicos

### Flujo de la Sesión Sincrónica:
1. **Identificación Inicial:**
   * En la barra lateral izquierda, ingresa tu nombre completo en el campo *"Nombre completo del estudiante"*.
2. **Exploración de la Demostración (Tab 1):**
   * Observa las series temporales de la disonancia (nominal vs breakeven vs real).
   * Pasa el cursor por los puntos clave (agosto 2020: tasa real en -1.08%).
3. **Participación en el Debate Socrático (Tab 2):**
   * Elige una de las 3 controversias disponibles.
   * Selecciona tu postura (ej. *Respaldar Postura A*).
   * Escribe al menos 2 premisas y 1 dato cuantitativo del documento y presiona *"Someter Argumentación a Evaluación Formativa"*.
4. **Dictamen del Caso de Estudio (Tab 3):**
   * Lee el contexto del shock de marzo de 2020.
   * Completa el diagnóstico de los diferenciales *off-the-run* y la recomendación de política.
   * Presiona *"Guardar Dictamen del Estudio de Caso"*.
5. **Decisiones en el Simulador (Tab 4):**
   * Evalúa cada dilema cronológico. Si eliges una opción económicamente inconsistente, lee la advertencia de *Lucha Productiva* y rectifica tu decisión.
6. **Preparación para la Defensa Oral (Tab 5):**
   * Redacta tus argumentos Feynman para las 4 preguntas de comprobación cara a cara con el docente.
7. **Descarga de Evidencia (Tab 6):**
   * Revisa tu calificación global y haz clic en **"📥 Descargar Reporte Oficial de la Sesión (.md)"** para guardar tu informe final.

---

## 📁 6. Estructura del Proyecto

```text
semana-5/
├── .gitignore                                         # Exclusiones de Git (venv, cachés, temporales)
├── app.py                                             # Código fuente principal de la aplicación Streamlit
├── funcionalidades.txt                                # Especificaciones didácticas y funcionales del proyecto
├── Logo-transparente UIA.png                           # Identidad visual de la Universidad Internacional de las Américas
├── MasteryFlip-A_Guide_to_the_Future_of_Educcation.pdf # Marco pedagógico de Jon Bergmann (Mastery Flip & AI)
├── requirements.txt                                   # Lista de paquetes de Python requeridos
├── substack.com-Los 4 principios del diseño didáctico.pdf # Marco didáctico de David Merrill
├── 2020 08 - Disonancia del mercado del tesoro.pdf    # Lectura macroeconómica central de Lyn Alden
└── README.md                                          # Documentación técnica y pedagógica del repositorio
```

---

## 📊 7. Interpretación de Resultados de Manera Pedagógica

| Indicador Macroeconómico | Valor Observado (Ago 2020) | Significado Económico Real | Impacto Didáctico para el Estudiante |
| :--- | :---: | :--- | :--- |
| **Rendimiento Nominal 10Y** | `0.52% - 0.71%` | Tasa que el Tesoro paga formalmente al inversor por prestar dinero a 10 años. | Muestra el anclaje artificial generado por las compras masivas de la Fed. |
| **Breakeven de Inflación** | `1.60% - 1.75%` | Expectativa del mercado sobre la tasa de inflación promedio de la próxima década. | Demuestra que los inversores privados ya descontaban el impacto monetario y fiscal. |
| **Tasa de Interés Real** | `-1.08%` *(Mínimo)* | Rendimiento neto descontando la inflación (`Tasa Real = Nominal - Inflación`). | **La Trampa de los Bonos:** Prestar dinero al Estado garantizaba una pérdida matemática de poder de compra. |
| **Costo de Oportunidad del Oro** | Muy bajo / Negativo | Rendimiento perdido por mantener un activo sin cupón. | Explica por qué el oro alcanzó máximos históricos por encima de los $2,000/oz en agosto de 2020. |
| **Monetización de Deuda** | `>55%` de emisión neta | Creación de nuevas reservas bancarias para financiar el gasto público. | Conecta la teoría cuantitativa del dinero con la expansión del balance central. |

### Rúbrica de la Comprobación de Maestría (Mastery Viva)
El reporte final clasifica el desempeño del estudiante en tres niveles:
* **Requiere Mayor Profundización (< 60 puntos):** Respuestas mecánicas o memorísticas que no articulan causas y efectos macroeconómicos.
* **En Desarrollo Positivo (60 - 84 puntos):** Buen manejo conceptual; diferencia nominal y real, pero requiere fortalecer el contraste de evidencias cuantitativas.
* **Dominio Sobresaliente (85 - 100 puntos):** Capacidad de aplicar el Método Feynman, sintetizar analogías cotidianas, evaluar compensaciones de política monetaria y defender posturas bajo presión dialéctica.

---

## 📜 8. Licencia y Nota Educativa

### Nota Educativa Institucional
> **Aviso Académico:** Este proyecto ha sido desarrollado exclusivamente con fines **académicos y pedagógicos** para la Cátedra de Economía de la **Universidad Internacional de las Américas (U.I.A.)**. Los simuladores, modelos y análisis contenidos en este software están diseñados como herramientas formativas para el aula universitaria y **no constituyen asesoramiento financiero, crediticio ni de inversión profesional**.

### Licencia
Este proyecto se distribuye bajo la licencia **MIT License**. Consulta el archivo de código para mayores detalles de reutilización académica.
