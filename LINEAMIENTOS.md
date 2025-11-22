# Lineamientos del Proyecto Final
## Guía Paso a Paso para el Desarrollo

---

## Fase 1: Planificación y Definición (22-Nov)

### 1.1 Formación de Equipos
- **Tamaño:** 6-7 integrantes máximo

### 1.2 Selección de ODS y Problemática
- **Elige tu ODS:** Revisa los 17 Objetivos de Desarrollo Sostenible
- **Define el problema:** Identifica una problemática específica y medible
- **Justifica la relevancia:** ¿Por qué es importante este problema?
- **Scope:** ¿Te enfocarás en Panamá, Latinoamérica, etc.?

#### Ejemplos de Problemáticas por ODS:
- **ODS 4 (Educación):** Identificación de brechas educativas por región

### 1.3 Búsqueda y Evaluación de Datos
- **Identifica fuentes:** Kaggle, World Bank, datos.gob, APIs públicas
- **Evalúa la calidad:** ¿Los datos están completos? ¿Son recientes?
- **Considera el tamaño:** ¿Puedes manejar el dataset con las herramientas que conoces?
- **Verifica la licencia:** ¿Puedes usar estos datos públicamente?

### 1.4 Definición de Roles del Equipo
**Asigna responsabilidades claras:**
- **Rol:** responsabilidad

### 1.5 Propuesta Inicial (Entregable)
**Documento de 1-2 páginas que incluya:**
- Nombre del proyecto y lema/slogan
- ODS seleccionado y justificación
- Problemática a resolver (¿qué?, ¿por qué?, ¿para quién?)
- Fuentes de datos identificadas
- Roles y responsabilidades del equipo
- Timeline básico del proyecto

---

## Fase 2: Desarrollo y Análisis (25/27-Nov)

### 2.1 Preparación de Datos
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

### 2.2 Análisis Exploratorio
- **Estadísticas descriptivas:** Media, mediana, distribuciones
- **Relaciones:** Correlaciones entre variables
- **Tendencias:** Análisis temporal si aplica
- **Segmentaciones:** Por regiones, categorías, etc.

### 2.3 Visualizaciones Iniciales
- **Gráficos básicos:** Barras, líneas, histogramas
- **Mapas:** Si tienes datos geográficos
- **Comparaciones:** Entre grupos, regiones, períodos
- **Distribuciones:** Boxplots, violin plots

### 2.4 Arquitectura de la Solución
**Documenta cómo funciona tu proyecto:**
```
[Datos] → [Limpieza] → [Análisis] → [Visualización] → [Dashboard]
   ↓           ↓           ↓            ↓              ↓
[CSV/API] → [Pandas] → [Estadísticas] → [Matplotlib] → [Streamlit]
```

---

## Fase 3: Implementación de la Solución (27-Nov / 02-Dic)

### 3.1 Desarrollo del Dashboard/Aplicación
**Opciones tecnológicas a discreción del grupo:**

#### Option A: Dashboard con Streamlit
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

### 3.2 Funcionalidades Esenciales
**Tu solución debe incluir:**
- **Filtros interactivos:** Por fecha, región, categoría
- **Visualizaciones dinámicas:** Que cambien según los filtros
- **Métricas clave:** KPIs importantes destacados
- **Interpretación:** Explicaciones de qué significan los datos

### 3.3 Enfoque en el Impacto
**Responde estas preguntas en tu solución:**
- ¿Qué insights descubriste?
- ¿Cómo estos insights pueden generar cambio?
- ¿Quién se beneficiaría de esta información?
- ¿Qué acciones concretas recomiendas?

---

## Fase 4: Documentación y Presentación (04-Dic)

### 4.1 Documentación del Código
- **README.md:** Explicación clara del proyecto (cómo ejecutar el proyecto en caso de ser necesario)
- **Comentarios:** En funciones complejas
- **Docstrings:** Para funciones principales
- **Requirements.txt:** Lista de dependencias

### 4.2 Preparación de la Presentación (Vídeo)
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

### 4.3 Elementos Visuales de la Presentación
- **Slides claras:** Máximo 10-12 slides
- **Gráficos grandes:** Que se puedan apreciar en el vídeo
- **Demo preparada:** Ensaya tu demostración

---

## Entregables Finales

### 4.4 Repositorio de GitHub 
   Nota: Puede mandar un archivo zip de no utilizar Github, pero puede perder puntos.
**Debe contener:**
- Código fuente completo y funcional
- Datasets utilizados (o enlaces a las fuentes)
- README.md con instrucciones de instalación
- Notebooks con análisis exploratorio
- Aplicación/dashboard funcionando
- Documentación técnica

### 4.5 Presentación
- Slides de la presentación (PDF o PPT)
- Vídeo de presentación del grupo

### 4.6 Reporte Final (Opcional)
- Documento de 2-3 páginas resumiendo:
  - Objetivos y metodología
  - Principales hallazgos
  - Limitaciones del estudio
  - Recomendaciones para investigación futura

---

## Criterios de Evaluación Detallados

### Técnico (40%)
- **Fase inicial del proyecto (ODS)**:
      - ODS seleccionado correctamente y justificado
	   - Preguntas de investigación bien planteadas (3 a 5)	
	   - Repositorio inicial en GitHub (estructura base + README)	
	   - Identidad del equipo	
- **Análisis de datos en pandas**:
   - Limpieza, exploración, manejo de nulos, filtros, agrupaciones, interpretaciones y calidad técnica del análisis.
- **Visualizaciones + Dashboard**:	
   - Mínimo 4 gráficos, calidad visual, orden, estilo coherente, interpretación y valor para responder preguntas del ODS.

### Impacto Social (30%)
- **Relevancia del problema**: 
   - Claridad de la problemática social
   - Impacto social y aplicabilidad
- **Alineación con ODS**:
   -  Pertinencia del ODS seleccionado
- **Propuesta de solución**: 
   - Relevancia y coherencia de la solución propuesta
   - Conclusiones basadas en datos
   - Originalidad y profundidad
	
### Trabajo en Equipo (20%)
- **Asistencia grupal**: 
   - Promedio de asistencia del grupo a clases 1–24.
- **Entrega de trabajos de clase**:
   - Entrega de actividades previas (mini notebooks, ejercicios, etc.).
- **Documentación y organización**: 
   - Notebook ordenado, limpio y documentado
	- Markdown bien usado
	- Comentarios en el código
	- Organización del repositorio de GitHub

### Presentación (10%)
**Presentación Final**:
   - Claridad de la narrativa
	- Explicación del proceso completo
	- Visuales y storytelling efectivo
	- Coherencia con el análisis
	- Participación equilibrada del equipo
- **Manejo del tiempo**: Respeto por los tiempos

---

## Recursos de Apoyo

### ¿Dónde Buscar Ayuda?
- **Dudas técnicas:** Grupos de Whatsapp del curso

### Documentación Útil
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Documentation](https://plotly.com/python/)
- [GitHub Guide](https://guides.github.com/)

### Consejos de Éxito
1. **Empieza simple:** Un dashboard básico que funciona > uno complejo que no funciona
2. **Itera temprano:** Haz versiones simples y mejóralas gradualmente
3. **Usa GitHub:** Commite frecuentemente, no esperes al final

---

**¡Tu proyecto puede hacer la diferencia!**

*Recuerda: No se trata solo de mostrar datos, sino de contar una historia que inspire acción.*
