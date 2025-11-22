import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Configuración de la página
st.set_page_config(
    page_title="EduData Latinoamérica - Dashboard",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
        font-weight: bold;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .ods-badge {
        background: linear-gradient(90deg, #e74c3c, #3498db);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 2rem;
        font-weight: bold;
        display: inline-block;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Función para cargar datos
@st.cache_data
def load_data():
    """Carga y procesa los datos de educación"""
    try:
        df = pd.read_csv('ejemplo-dashboard/data/educacion_latinoamerica.csv')
        return df
    except FileNotFoundError:
        st.error("No se encontró el archivo de datos. Asegúrate de ejecutar generate_data.py primero.")
        return None

# Función para calcular métricas principales
def calculate_metrics(df_filtered):
    """Calcula métricas principales del dataset filtrado"""
    total_estudiantes = df_filtered['Población_Estudiantil'].sum()
    tasa_promedio = df_filtered['Tasa_Matriculación'].mean()
    desercion_promedio = df_filtered['Tasa_Deserción'].mean()
    inversion_promedio = df_filtered['Inversión_Per_Capita_USD'].mean()
    
    return {
        'total_estudiantes': total_estudiantes,
        'tasa_promedio': tasa_promedio,
        'desercion_promedio': desercion_promedio,
        'inversion_promedio': inversion_promedio
    }

# Función para crear gráfico de tendencias
def create_trend_chart(df_filtered):
    """Crea gráfico de tendencias de matriculación por año"""
    trend_data = df_filtered.groupby(['Año', 'Nivel_Educativo'])['Tasa_Matriculación'].mean().reset_index()
    
    fig = px.line(
        trend_data,
        x='Año',
        y='Tasa_Matriculación',
        color='Nivel_Educativo',
        title='Tendencia de Matriculación por Nivel Educativo',
        markers=True
    )
    
    fig.update_layout(
        xaxis_title='Año',
        yaxis_title='Tasa de Matriculación (%)',
        legend_title='Nivel Educativo',
        hovermode='x unified'
    )
    
    return fig

# Función para crear gráfico de comparación países
def create_country_comparison(df_filtered, metric):
    """Crea gráfico de barras comparando países"""
    metric_names = {
        'Tasa_Matriculación': 'Tasa de Matriculación (%)',
        'Tasa_Deserción': 'Tasa de Deserción (%)',
        'Inversión_Per_Capita_USD': 'Inversión Per Cápita (USD)'
    }
    
    country_data = df_filtered.groupby('País')[metric].mean().sort_values(ascending=False)
    
    fig = px.bar(
        x=country_data.values,
        y=country_data.index,
        orientation='h',
        title=f'Comparación por País: {metric_names[metric]}',
        labels={'x': metric_names[metric], 'y': 'País'}
    )
    
    fig.update_layout(
        showlegend=False,
        height=400
    )
    
    return fig

# Función para crear gráfico de dispersión
def create_scatter_plot(df_filtered):
    """Crea gráfico de dispersión inversión vs matriculación"""
    fig = px.scatter(
        df_filtered,
        x='Inversión_Per_Capita_USD',
        y='Tasa_Matriculación',
        color='País',
        size='Población_Estudiantil',
        hover_data=['Año', 'Nivel_Educativo', 'Región'],
        title='Relación: Inversión Per Cápita vs Tasa de Matriculación'
    )
    
    fig.update_layout(
        xaxis_title='Inversión Per Cápita (USD)',
        yaxis_title='Tasa de Matriculación (%)'
    )
    
    return fig

# Función para crear heatmap
def create_heatmap(df_filtered):
    """Crea heatmap de correlaciones"""
    # Preparar datos numéricos
    numeric_cols = ['Tasa_Matriculación', 'Tasa_Deserción', 'Inversión_Per_Capita_USD', 'Población_Estudiantil']
    corr_data = df_filtered[numeric_cols].corr()
    
    fig = px.imshow(
        corr_data,
        text_auto=True,
        aspect="auto",
        title="Matriz de Correlaciones entre Variables"
    )
    
    return fig

# APLICACIÓN PRINCIPAL
def main():
    # Header principal
    st.markdown('<p class="main-header"> EduData Latinoamérica</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Dashboard de Análisis Educativo para el ODS 4: Educación de Calidad</p>', unsafe_allow_html=True)
    
    # Badge ODS
    st.markdown('<div class="ods-badge"> ODS 4: Educación de Calidad</div>', unsafe_allow_html=True)
    
    # Cargar datos
    df = load_data()
    if df is None:
        st.stop()
    
    # Sidebar - Filtros
    st.sidebar.markdown("## Filtros de Análisis")
    
    # Filtro de años
    years_available = sorted(df['Año'].unique())
    year_range = st.sidebar.slider(
        "Seleccionar rango de años:",
        min_value=min(years_available),
        max_value=max(years_available),
        value=(min(years_available), max(years_available))
    )
    
    # Filtro de países
    countries_available = sorted(df['País'].unique())
    selected_countries = st.sidebar.multiselect(
        "Seleccionar países:",
        countries_available,
        default=countries_available
    )
    
    # Filtro de región
    regions_available = df['Región'].unique()
    selected_regions = st.sidebar.multiselect(
        "Seleccionar regiones:",
        regions_available,
        default=regions_available
    )
    
    # Filtro de nivel educativo
    levels_available = df['Nivel_Educativo'].unique()
    selected_levels = st.sidebar.multiselect(
        "Seleccionar niveles educativos:",
        levels_available,
        default=levels_available
    )
    
    # Aplicar filtros
    df_filtered = df[
        (df['Año'] >= year_range[0]) &
        (df['Año'] <= year_range[1]) &
        (df['País'].isin(selected_countries)) &
        (df['Región'].isin(selected_regions)) &
        (df['Nivel_Educativo'].isin(selected_levels))
    ]
    
    if df_filtered.empty:
        st.warning("No hay datos que coincidan con los filtros seleccionados.")
        st.stop()
    
    # Calcular métricas
    metrics = calculate_metrics(df_filtered)
    
    # Mostrar métricas principales
    st.markdown("## Métricas Principales")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Total Estudiantes",
            f"{metrics['total_estudiantes']:,.0f}",
            help="Suma total de población estudiantil en los filtros seleccionados"
        )
    
    with col2:
        st.metric(
            "Tasa Promedio de Matriculación",
            f"{metrics['tasa_promedio']:.1f}%",
            help="Promedio de tasas de matriculación"
        )
    
    with col3:
        st.metric(
            "Tasa Promedio de Deserción",
            f"{metrics['desercion_promedio']:.1f}%",
            help="Promedio de tasas de deserción escolar"
        )
    
    with col4:
        st.metric(
            "Inversión Promedio Per Cápita",
            f"${metrics['inversion_promedio']:.0f}",
            help="Inversión promedio en educación per cápita"
        )
    
    st.markdown("---")
    
    # Gráficos principales
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(create_trend_chart(df_filtered), use_container_width=True)
    
    with col2:
        metric_option = st.selectbox(
            "Seleccionar métrica para comparación:",
            ['Tasa_Matriculación', 'Tasa_Deserción', 'Inversión_Per_Capita_USD']
        )
        st.plotly_chart(create_country_comparison(df_filtered, metric_option), use_container_width=True)
    
    # Segunda fila de gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(create_scatter_plot(df_filtered), use_container_width=True)
    
    with col2:
        st.plotly_chart(create_heatmap(df_filtered), use_container_width=True)
    
    # Sección de insights
    st.markdown("---")
    st.markdown("## 💡 Insights Principales")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### Tendencias Positivas
        - La matriculación en educación primaria muestra mejora constante
        - Los países con mayor inversión per cápita tienden a tener mejores tasas de matriculación
        - La brecha urbano-rural se está reduciendo gradualmente
        """)
    
    with col2:
        st.markdown("""
        ### Desafíos Identificados
        - La deserción en educación secundaria sigue siendo alta
        - Existe una correlación negativa entre deserción y matriculación
        - Las zonas rurales aún enfrentan mayores desafíos de acceso
        """)
    
    with col3:
        st.markdown("""
        ### Recomendaciones
        - Aumentar la inversión en infraestructura rural
        - Implementar programas de retención para secundaria
        - Fortalecer programas de becas y apoyo económico
        """)
    
    # Información del proyecto
    st.markdown("---")
    st.markdown("## Información del Proyecto")
    
    with st.expander("Acerca de este dashboard"):
        st.markdown("""
        **Proyecto:** EduData Latinoamérica - Dashboard de Análisis Educativo
        
        **ODS Objetivo:** ODS 4 - Educación de Calidad
        
        **Problemática:** Análisis del acceso y calidad educativa en países de Centroamérica para identificar 
        brechas y oportunidades de mejora en la educación.
        
        **Tecnologías utilizadas:**
        - Python, Pandas, Streamlit, Plotly
        
        **Equipo de desarrollo:**
        - Data Analyst: [Tu nombre]
        - Data Engineer: [Tu nombre]  
        - Visualization Specialist: [Tu nombre]
        - Project Manager: [Tu nombre]
        
        **Fuente de datos:** Datos simulados basados en tendencias reales de organismos internacionales
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("**Hecho por el equipo Tech Horizons** | Contacto: equipo@techhorizons.com")

if __name__ == "__main__":
    main()
