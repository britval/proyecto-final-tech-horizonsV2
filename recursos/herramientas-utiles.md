# Herramientas y Recursos Útiles
## Guía Completa para el Desarrollo del Proyecto Final

---

## Herramientas de Análisis de Datos

### Python - Core Libraries
- **Pandas** - Manipulación y análisis de datos
  - [Documentación oficial](https://pandas.pydata.org/docs/)
  - [Pandas Tutorial - 10 minutes](https://pandas.pydata.org/docs/user_guide/10min.html)
  - **Tip:** Usa `.info()`, `.describe()`, `.head()` para explorar datasets

- **NumPy** - Operaciones numéricas y arrays
  - [Documentación oficial](https://numpy.org/doc/)
  - [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html)

- **Matplotlib** - Visualización básica
  - [Documentación oficial](https://matplotlib.org/stable/contents.html)
  - [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/index.html)
  - **Tip:** Usa `plt.style.use('ggplot')` para mejores estilos

- **Seaborn** - Visualización estadística
  - [Documentación oficial](https://seaborn.pydata.org/)
  - [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
  - **Tip:** Perfecto para boxplots, heatmaps y distribuciones

---

## Herramientas de Visualización Interactiva

### Plotly
- **¿Para qué usarlo?** Gráficos interactivos profesionales
- [Documentación](https://plotly.com/python/)
- [Plotly Express Tutorial](https://plotly.com/python/plotly-express/)
- **Mejores usos:** Dashboards, mapas, gráficos 3D
- **Instalación:** `pip install plotly`

```python
import plotly.express as px
fig = px.scatter(df, x='columna1', y='columna2', color='categoria')
fig.show()
```

### Folium (Para Mapas)
- **¿Para qué usarlo?** Mapas interactivos
- [Documentación](https://python-visualization.github.io/folium/)
- **Mejores usos:** Datos geográficos, heat maps, marcadores
- **Instalación:** `pip install folium`

---

## Plataformas de Dashboard

### Streamlit (Recomendado)
- **¿Por qué elegirlo?** Fácil de usar, perfecto para principiantes
- [Documentación oficial](https://docs.streamlit.io/)
- [Get Started Tutorial](https://docs.streamlit.io/library/get-started)
- [Galería de ejemplos](https://streamlit.io/gallery)

**Ventajas:**
- Sintaxis simple
- Integración automática con Pandas/Plotly
- Deploy fácil en Streamlit Cloud
- Widgets interactivos built-in

**Comandos esenciales:**
```python
import streamlit as st

st.title("Mi Dashboard")
st.selectbox("Filtro:", opciones)
st.plotly_chart(figura)
st.dataframe(df)
```

### Dash
- **¿Cuándo usarlo?** Para dashboards más complejos y customizables
- [Documentación oficial](https://dash.plotly.com/)
- **Mejor para:** Equipos con más experiencia en web

---

## Fuentes de Datos

### Datos de Panamá
- **INEC (Instituto Nacional de Estadística):** https://www.inec.gob.pa/
  - Censos, encuestas de hogares, estadísticas vitales
- **Contraloría General de la República:** https://www.contraloria.gob.pa/
  - Datos económicos, presupuestos, estadísticas oficiales
- **MEDUCA (Ministerio de Educación):** https://www.meduca.gob.pa/
  - Estadísticas educativas, matrícula, infraestructura

### Datos Internacionales
- **World Bank Open Data:** https://data.worldbank.org/
  - Indicadores de desarrollo, pobreza, educación, salud
- **Our World in Data:** https://ourworldindata.org/
  - Datos sobre progreso mundial, muy bien visualizados
- **Kaggle Datasets:** https://www.kaggle.com/datasets
  - Datasets curados para práctica

---

## Herramientas de Colaboración

### Control de Versiones
- **GitHub** (Obligatorio)
  - [GitHub Guide](https://guides.github.com/activities/hello-world/)
  - **Comandos básicos:**
    ```bash
    git add .
    git commit -m "Mensaje descriptivo"
    git push origin main
    ```

### Desarrollo Colaborativo
- **Google Colab** 
  - [Colab Tips](https://colab.research.google.com/)
  - **Tip:** Usa comentarios para dividir trabajo
  - **Conectar con GitHub:** Para sincronizar notebooks

---

## Deploy y Compartir

### Streamlit Cloud (Recomendado)
- **¿Qué es?** Hosting gratuito para apps Streamlit
- [Streamlit Cloud](https://streamlit.io/cloud)
- **Ventajas:** Deploy automático desde GitHub, gratis

**Pasos:**
1. Sube tu código a GitHub
2. Conecta Streamlit Cloud con tu repo
3. ¡Tu app está online!

---

## Templates de Código Útiles

### Template Básico de Carga de Datos
```python
import pandas as pd
import streamlit as st

@st.cache_data
def load_data(file_path):
    """Carga y procesa los datos iniciales"""
    try:
        df = pd.read_csv(file_path)
        df = df.dropna()  # Limpieza básica
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        st.error(f"Error cargando datos: {e}")
        return None

# Uso
df = load_data('mi_dataset.csv')
if df is not None:
    st.success("Datos cargados exitosamente!")
    st.dataframe(df.head())
```

### Template de Métricas
```python
def mostrar_metricas(df, columna_numerica):
    """Muestra métricas principales"""
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total", f"{df[columna_numerica].sum():,.0f}")
    
    with col2:
        st.metric("Promedio", f"{df[columna_numerica].mean():.1f}")
    
    with col3:
        st.metric("Máximo", f"{df[columna_numerica].max():,.0f}")
    
    with col4:
        st.metric("Mínimo", f"{df[columna_numerica].min():,.0f}")
```

---

## Checklist de Herramientas Mínimas

### Para Análisis de Datos:
- Pandas (obligatorio)
- Matplotlib o Plotly (obligatorio)
- NumPy (recomendado)
- Seaborn (recomendado)

### Para Dashboard:
- Streamlit (recomendado) o Dash
- Plotly (para interactividad)

### Para Colaboración:
- GitHub (obligatorio)
- Google Colab o Jupyter (obligatorio)

### Para Deploy:
- Streamlit Cloud (recomendado)
- GitHub Pages (para sitios estáticos)

---

## Recomendaciones por Tipo de Proyecto

### Si tu proyecto es principalmente análisis estadístico:
**Stack recomendado:**
- **Análisis:** Pandas + NumPy + SciPy
- **Visualización:** Matplotlib + Seaborn
- **Presentación:** Jupyter Notebook bien documentado

### Si tu proyecto necesita interactividad:
**Stack recomendado:**
- **Análisis:** Pandas + NumPy
- **Visualización:** Plotly + Streamlit
- **Deploy:** Streamlit Cloud

### Si tu proyecto tiene componente geográfico:
**Stack recomendado:**
- **Análisis:** Pandas + GeoPandas
- **Visualización:** Folium + Plotly
- **Dashboard:** Streamlit con mapas

---

## Quick Commands Reference

### Pandas Essentials
```python
# Exploración
df.head(), df.tail(), df.info(), df.describe()
df.shape, df.columns, df.dtypes

# Limpieza
df.dropna(), df.fillna(value)
df.drop_duplicates()

# Filtrado
df[df['col'] > value]
df.query('col > @value')

# Agrupación
df.groupby('col').agg({'col2': 'mean', 'col3': 'sum'})
```

### Plotly Quick Charts
```python
# Charts básicos
px.bar(df, x='col1', y='col2')
px.line(df, x='fecha', y='valor')
px.scatter(df, x='x', y='y', color='categoria')
px.histogram(df, x='valor')
```

### Streamlit Quick Widgets
```python
# Inputs
st.selectbox('Label:', options)
st.multiselect('Label:', options)
st.slider('Label:', min_val, max_val)

# Outputs
st.metric('Label', value)
st.dataframe(df)
st.plotly_chart(fig)
```

---

## Recursos de Ayuda

### ¿Dónde Buscar Ayuda?
1. **Errores de sintaxis:** Stack Overflow
2. **Dudas de Pandas:** Pandas documentation
3. **Problemas de Streamlit:** Streamlit forums
4. **Ayuda del curso:** Discord/Slack del programa

### Documentación Favorita
- **Pandas:** https://pandas.pydata.org/docs/user_guide/
- **Plotly:** https://plotly.com/python/
- **Streamlit:** https://docs.streamlit.io/

---

**¡Con estas herramientas y recursos estás listo para crear un proyecto increíble!**

*Recuerda: La mejor herramienta es la que tu equipo puede usar efectivamente. ¡Empieza simple y mejora gradualmente!*
