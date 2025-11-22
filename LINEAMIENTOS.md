# 📋 Lineamientos del Proyecto Final
## Guía Paso a Paso para el Desarrollo

---

## 🎯 Fase 1: Planificación y Definición (Semana 1)

### 📝 1.1 Formación de Equipos
- **Tamaño:** 3-4 integrantes máximo
- **Diversidad:** Combina diferentes fortalezas (programación, diseño, comunicación)
- **Registro:** Completa el formulario de registro de equipos

### 🌍 1.2 Selección de ODS y Problemática
- **Elige tu ODS:** Revisa los 17 Objetivos de Desarrollo Sostenible
- **Define el problema:** Identifica una problemática específica y medible
- **Justifica la relevancia:** ¿Por qué es importante este problema?
- **Scope local/global:** ¿Te enfocarás en Panamá, Latinoamérica, o global?

#### 💡 Ejemplos de Problemáticas por ODS:
- **ODS 3 (Salud):** Análisis de factores que influyen en la esperanza de vida
- **ODS 4 (Educación):** Identificación de brechas educativas por región
- **ODS 11 (Ciudades):** Análisis de la contaminación urbana y sus efectos
- **ODS 13 (Clima):** Visualización del cambio climático en Centroamérica

### 🔍 1.3 Búsqueda y Evaluación de Datos
- **Identifica fuentes:** Kaggle, World Bank, datos.gob, APIs públicas
- **Evalúa la calidad:** ¿Los datos están completos? ¿Son recientes?
- **Considera el tamaño:** ¿Puedes manejar el dataset con las herramientas que conoces?
- **Verifica la licencia:** ¿Puedes usar estos datos públicamente?

### 📋 1.4 Definición de Roles del Equipo
**Asigna responsabilidades claras:**
- **🗄️ Data Engineer:** Limpieza y preparación de datos
- **📊 Data Analyst:** Análisis exploratorio y estadísticas
- **🎨 Visualización Specialist:** Gráficos y dashboard
- **📢 Project Manager:** Coordinación y presentación

### 📄 1.5 Propuesta Inicial (Entregable)
**Documento de 1-2 páginas que incluya:**
- Nombre del proyecto y lema/slogan
- ODS seleccionado y justificación
- Problemática a resolver (¿qué?, ¿por qué?, ¿para quién?)
- Fuentes de datos identificadas
- Roles y responsabilidades del equipo
- Timeline básico del proyecto

---

## 🔧 Fase 2: Desarrollo y Análisis (Semana 2-3)

### 📊 2.1 Preparación de Datos
- **Carga de datos:** Usando pandas, lee tus datasets
- **Exploración inicial:** `.info()`, `.describe()`, `.head()`
- **Limpieza:** Manejo de valores nulos, duplicados, formatos
- **Transformación:** Creación de nuevas columnas, agrupaciones

```python
# Ejemplo de estructura básica
import pandas as pd
import numpy as np

# Carga de datos
df = pd.read_csv('datos/mi_dataset.csv')

# Exploración inicial
print(df.info())
print(df.describe())
print(df.isnull().sum())
```

### 📈 2.2 Análisis Exploratorio
- **Estadísticas descriptivas:** Media, mediana, distribuciones
- **Relaciones:** Correlaciones entre variables
- **Tendencias:** Análisis temporal si aplica
- **Segmentaciones:** Por regiones, categorías, etc.

### 🎨 2.3 Visualizaciones Iniciales
- **Gráficos básicos:** Barras, líneas, histogramas
- **Mapas:** Si tienes datos geográficos
- **Comparaciones:** Entre grupos, regiones, períodos
- **Distribuciones:** Boxplots, violin plots

### 🏗️ 2.4 Arquitectura de la Solución
**Documenta cómo funciona tu proyecto:**
```
[Datos] → [Limpieza] → [Análisis] → [Visualización] → [Dashboard]
   ↓           ↓           ↓            ↓              ↓
[CSV/API] → [Pandas] → [Estadísticas] → [Matplotlib] → [Streamlit]
```

---

## 💻 Fase 3: Implementación de la Solución (Semana 3-4)

### 🖥️ 3.1 Desarrollo del Dashboard/Aplicación
**Opciones tecnológicas:**

#### Option A: Dashboard con Streamlit (Recomendado)
```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Mi Proyecto ODS")
st.sidebar.selectbox("Filtrar por:", opciones)
# ... tu código aquí
```

#### Option B: Jupyter Notebook Interactivo
- Usa widgets de IPython para interactividad
- Combina markdown, código y visualizaciones
- Exporta como HTML para compartir

#### Option C: Aplicación Web con Flask
- Para equipos más avanzados
- Mayor flexibilidad de diseño
- Requiere más conocimiento de web

### 📱 3.2 Funcionalidades Esenciales
**Tu solución debe incluir:**
- **Filtros interactivos:** Por fecha, región, categoría
- **Visualizaciones dinámicas:** Que cambien según los filtros
- **Métricas clave:** KPIs importantes destacados
- **Interpretación:** Explicaciones de qué significan los datos

### 🎯 3.3 Enfoque en el Impacto
**Responde estas preguntas en tu solución:**
- ¿Qué insights descubriste?
- ¿Cómo estos insights pueden generar cambio?
- ¿Quién se beneficiaría de esta información?
- ¿Qué acciones concretas recomiendas?

---

## 📚 Fase 4: Documentación y Presentación (Semana 4)

### 📖 4.1 Documentación del Código
- **README.md:** Explicación clara de cómo ejecutar el proyecto
- **Comentarios:** En funciones complejas
- **Docstrings:** Para funciones principales
- **Requirements.txt:** Lista de dependencias

### 🎤 4.2 Preparación de la Presentación
**Estructura sugerida (10-15 minutos):**

1. **Introducción (2 min)**
   - Presentación del equipo y roles
   - Nombre y lema del proyecto

2. **Problemática (3 min)**
   - ODS seleccionado y justificación
   - ¿Por qué es importante este problema?
   - ¿A quién afecta?

3. **Metodología (3 min)**
   - Datos utilizados y fuentes
   - Proceso de análisis
   - Herramientas empleadas

4. **Resultados (5 min)**
   - Demo en vivo del dashboard/aplicación
   - Insights principales descubiertos
   - Visualizaciones más impactantes

5. **Impacto y Conclusiones (2 min)**
   - ¿Cómo tu solución puede generar cambio?
   - Recomendaciones basadas en datos
   - Próximos pasos y mejoras

6. **Preguntas (2-3 min)**
   - Espacio para Q&A

### 🎥 4.3 Elementos Visuales de la Presentación
- **Slides claras:** Máximo 10-12 slides
- **Gráficos grandes:** Que se vean desde atrás del salón
- **Demo preparada:** Ensaya tu demostración
- **Backup plan:** Ten screenshots si falla la demo

---

## ✅ Entregables Finales

### 📦 4.4 Repositorio de GitHub
**Debe contener:**
- [ ] Código fuente completo y funcional
- [ ] Datasets utilizados (o enlaces a las fuentes)
- [ ] README.md con instrucciones de instalación
- [ ] Notebooks con análisis exploratorio
- [ ] Aplicación/dashboard funcionando
- [ ] Documentación técnica

### 📊 4.5 Presentación
- [ ] Slides de la presentación (PDF o PPT)
- [ ] Demo en vivo funcionando
- [ ] Video de backup (opcional pero recomendado)

### 📝 4.6 Reporte Final (Opcional)
- Documento de 2-3 páginas resumiendo:
  - Objetivos y metodología
  - Principales hallazgos
  - Limitaciones del estudio
  - Recomendaciones para investigación futura

---

## 🚨 Criterios de Evaluación Detallados

### 📊 Técnico (40%)
- **Calidad del código** (15%): Limpio, comentado, funcional
- **Análisis de datos** (15%): Uso correcto de pandas, estadísticas
- **Visualizaciones** (10%): Claras, informativas, estéticamente agradables

### 🌍 Impacto Social (30%)
- **Relevancia del problema** (15%): Importancia y urgencia
- **Alineación con ODS** (10%): Conexión clara y justificada
- **Propuesta de solución** (5%): Realismo y viabilidad

### 👥 Trabajo en Equipo (20%)
- **Distribución de roles** (10%): Clara y equilibrada
- **Uso de GitHub** (5%): Commits regulares de todos
- **Colaboración** (5%): Evidencia de trabajo conjunto

### 🎤 Presentación (10%)
- **Claridad comunicativa** (5%): Fácil de entender
- **Profesionalismo** (3%): Preparación y confianza
- **Manejo del tiempo** (2%): Respeto por los tiempos

---

## 🆘 Recursos de Apoyo

### 📞 ¿Dónde Buscar Ayuda?
- **Dudas técnicas:** Discord/Slack del curso
- **Problemas de datos:** Oficina virtual los viernes
- **Issues de GitHub:** Para problemas específicos del proyecto
- **Tutorías de equipo:** Agenda una sesión si tu equipo está atascado

### 📚 Documentación Útil
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Documentation](https://plotly.com/python/)
- [GitHub Guide](https://guides.github.com/)

### 🌟 Consejos de Éxito
1. **Empieza simple:** Un dashboard básico que funciona > uno complejo que no funciona
2. **Itera temprano:** Haz versiones simples y mejóralas gradualmente
3. **Comunica regularmente:** Reúnanse al menos 2 veces por semana
4. **Usa GitHub:** Commite frecuentemente, no esperes al final
5. **Práctica la presentación:** Al menos 3 ensayos completos
6. **Ten un plan B:** Para cuando la tecnología falle

---

**¡Tu proyecto puede hacer la diferencia! 🌟**

*Recuerda: No se trata solo de mostrar datos, sino de contar una historia que inspire acción.*
