# Instrucciones para Ejecutar el Dashboard de Ejemplo
## EduData Latinoamérica - Dashboard Educativo

---

## Prerequisitos

Antes de ejecutar el dashboard, asegúrate de tener:
- Python 3.7 o superior instalado
- Git instalado (para clonar el repositorio)
- Terminal o línea de comandos funcionando

---

## Instalación Paso a Paso

### Descarga los Archivos
```bash
# Si tienes git instalado:
git clone [URL_DEL_REPOSITORIO]
cd proyecto-final-tech-horizons

# O descarga el ZIP y extrae los archivos
```

### Navega a la Carpeta del Ejemplo
```bash
cd ejemplo-dashboard
```

### Genera los Datos de Ejemplo
```bash
# Desde la carpeta raíz del proyecto:
python generate_data.py
```

Este comando creará el archivo `ejemplo-dashboard/data/educacion_latinoamerica.csv` con datos simulados.

### Instala las Dependencias
```bash
pip install -r requirements.txt
```

**Si tienes problemas con pip, prueba:**
```bash
# Para usuarios de Mac con M1/M2:
pip install --upgrade pip
pip install -r requirements.txt

# Para usuarios de Windows:
python -m pip install -r requirements.txt

# Si tienes conflictos, crea un entorno virtual:
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Ejecutar el Dashboard

### Iniciar la Aplicación
```bash
streamlit run dashboard.py
```

### Abrir en el Navegador
- El dashboard se abrirá automáticamente en tu navegador predeterminado
- Si no se abre automáticamente, ve a: `http://localhost:8501`
- Deberías ver la interfaz del dashboard **EduData Latinoamérica**

---

## Cómo Usar el Dashboard

### Sidebar - Controles de Filtrado:
1. **Rango de años:** Slider para seleccionar período temporal
2. **Países:** Multiselect para elegir países específicos
3. **Regiones:** Filtro urbano/rural
4. **Niveles educativos:** Primaria, secundaria, universidad

### Área Principal - Visualizaciones:
1. **Métricas principales:** Números resumen en la parte superior
2. **Tendencias temporales:** Gráfico de líneas por nivel educativo
3. **Comparación países:** Gráfico de barras horizontales
4. **Correlaciones:** Scatter plot inversión vs matriculación
5. **Heatmap:** Matriz de correlaciones entre variables

### Insights Destacados:
- Revisa la sección "Insights Principales" al final del dashboard
- Observa cómo los filtros cambian las visualizaciones dinámicamente
- Experimenta con diferentes combinaciones de filtros

---

## Solución de Problemas Comunes

### Error: "ModuleNotFoundError"
**Problema:** No están instaladas las dependencias
```bash
# Solución:
pip install streamlit pandas plotly numpy
```

### Error: "FileNotFoundError: educacion_latinoamerica.csv"
**Problema:** No se ejecutó el script de generación de datos
```bash
# Solución:
cd ..  # Volver a la carpeta raíz
python generate_data.py
cd ejemplo-dashboard
streamlit run dashboard.py
```

### Error: "Address already in use"
**Problema:** Puerto 8501 está ocupado
```bash
# Solución - usar otro puerto:
streamlit run dashboard.py --server.port 8502
```

### Dashboard se ve mal o no carga gráficos
**Problema:** Browser cache o compatibilidad
- **Solución 1:** Refrescar la página (Ctrl+F5 o Cmd+Shift+R)
- **Solución 2:** Abrir en modo incógnito
- **Solución 3:** Probar con otro navegador (Chrome recomendado)

### Dashboard muy lento
**Problema:** Computadora con pocos recursos
- **Solución:** Reducir el tamaño del dataset en `generate_data.py`
- Cambiar `years = list(range(2015, 2024))` por `years = list(range(2020, 2024))`

---

## Personalización del Ejemplo

### Modificar los Datos:
1. **Edita `generate_data.py`:**
   - Cambia países, años, o variables
   - Ajusta los rangos de valores simulados
   - Añade nuevas columnas de datos

2. **Regenera los datos:**
   ```bash
   python generate_data.py
   ```

### Modificar el Dashboard:
1. **Edita `dashboard.py`:**
   - Cambia colores en la sección CSS
   - Añade nuevos tipos de gráficos
   - Modifica la estructura de la página

2. **Reinicia el servidor:**
   ```bash
   # Ctrl+C para parar, luego:
   streamlit run dashboard.py
   ```

---

## Estructura de Archivos

```
ejemplo-dashboard/
│
├── dashboard.py           # Aplicación principal de Streamlit
├── requirements.txt       # Lista de dependencias
├── data/                  # Carpeta de datos
│   └── educacion_latinoamerica.csv  # Dataset generado
│
../generate_data.py         # Script para generar datos (carpeta raíz)
```

---

## Características del Dashboard de Ejemplo

### Funcionalidades Implementadas:
- **Carga de datos con cache** para mejor performance
- **Filtros interactivos** que actualizan todas las visualizaciones
- **Métricas dinámicas** que cambian según filtros
- **4 tipos de visualizaciones** diferentes
- **Responsive design** que se adapta a diferentes pantallas
- **Manejo de errores** con mensajes informativos
- **Documentación integrada** con información del proyecto

### Tecnologías Demostradas:
- **Streamlit:** Framework de dashboard
- **Pandas:** Manipulación de datos
- **Plotly:** Visualizaciones interactivas
- **Python:** Lógica de la aplicación

---

## Cómo Adaptar para tu Proyecto

### Cambiar el Tema:
- Modifica la sección CSS para tu paleta de colores
- Cambia el título y descripción del proyecto
- Actualiza la información del ODS

### Adaptar los Datos:
- Reemplaza `educacion_latinoamerica.csv` con tu dataset
- Modifica las columnas en `load_data()` y las funciones de análisis
- Actualiza los nombres de variables en todo el código

### Personalizar Visualizaciones:
- Cambia los tipos de gráficos según tus datos
- Añade nuevas métricas relevantes para tu problema
- Modifica los filtros según las dimensiones de tus datos

### Actualizar Contenido:
- Cambia la sección de insights por tus hallazgos reales
- Actualiza la información del equipo
- Modifica las recomendaciones según tu análisis

---

## Ideas para Mejorar

### Funcionalidades Avanzadas que Podrías Añadir:
- **Descarga de datos filtrados** como CSV
- **Gráficos de mapas** si tienes datos geográficos
- **Predicciones simples** con scikit-learn
- **Comparación lado a lado** de diferentes períodos
- **Alertas automáticas** cuando ciertos umbrales se cruzan

### Mejoras de UX/UI:
- **Tema oscuro/claro** toggle
- **Animaciones** en las transiciones de gráficos
- **Tooltips explicativos** para conceptos técnicos
- **Breadcrumbs** para navegación
- **Export a PDF** de reportes

---

## ¿Necesitas Ayuda?

### Recursos Útiles:
- **Documentación de Streamlit:** https://docs.streamlit.io/
- **Galería de Plotly:** https://plotly.com/python/
- **Pandas Cheat Sheet:** https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

### Comunidad:
- **Stack Overflow:** Para errores específicos
- **Streamlit Forum:** https://discuss.streamlit.io/
- **Discord/Slack del curso:** Para ayuda inmediata

---

**¡Felicitaciones por ejecutar tu primer dashboard!**

*Este es solo el comienzo. Ahora adapta este ejemplo para crear tu propio proyecto de impacto social.*
