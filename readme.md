# Framework de Automatización de Pruebas

## Propósito del Proyecto
Este proyecto consiste en el desarrollo de un framework de automatización de pruebas en Python, integrando pruebas de UI con Selenium WebDriver y pruebas de API utilizando la librería Requests.
El objetivo es aplicar buenas prácticas de automatización, el patrón Page Object Model (POM) y generar reportes automáticos claros, reutilizables y fáciles de interpretar.

---

## Tecnologías Utilizadas
- Python 3
- Pytest
- Selenium WebDriver
- Requests
- Faker
- Git / GitHub
- Pytest HTML Report

---

## Tipos de Pruebas Implementadas

### Pruebas de UI (Selenium WebDriver)
- Login válido
- Login inválido (escenario negativo)
- Navegación por inventario
- Agregar productos al carrito
- Validación del carrito
- Prueba smoke (apertura del navegador)

Las pruebas de UI utilizan el patrón **Page Object Model (POM)** para separar la lógica de las pruebas de la lógica de interacción con la interfaz, facilitando el mantenimiento y la escalabilidad del proyecto.

---

### Pruebas de API (Requests)
- Pruebas sobre API pública (ReqRes)
- Métodos HTTP utilizados: GET, POST y DELETE
- Validación de códigos de estado HTTP
- Validación de estructura y contenido de las respuestas JSON
- Algunas pruebas se marcan como **SKIPPED** cuando se requiere API Key, manteniendo el flujo de ejecución estable

---

## Reportes, Logs y Evidencias

### Reporte HTML
El framework genera un reporte HTML detallado utilizando Pytest con el siguiente comando:

pytest -v --html=reports/report.html --self-contained-html

El reporte incluye:
- Lista de tests ejecutados
- Estado de cada test (PASSED / FAILED / SKIPPED)
- Tiempo de ejecución
- Información detallada de cada caso
- Evidencias visuales cuando ocurre un fallo

El archivo generado se encuentra en:
reports/report.html

---

### Capturas de Pantalla
- Las capturas se generan automáticamente cuando una prueba falla
- Se almacenan en el directorio:
reports/screens/
- El nombre del archivo incluye el nombre del test y la fecha/hora de ejecución para facilitar el análisis

---

### Ejecutar todas las pruebas
pytest -v

### Ejecutar una prueba específica
pytest tests/test_login.py -v

---

## Interpretación de Resultados
- PASSED: el test se ejecutó correctamente
- FAILED: ocurrió un error funcional o técnico (se genera automáticamente una captura de pantalla)
- SKIPPED: el test fue omitido por una condición controlada (por ejemplo, falta de API Key)

Los reportes HTML permiten identificar rápidamente los fallos, revisar evidencias y analizar el comportamiento del sistema bajo prueba.

---

## Manejo de Datos de Prueba
- Uso de @pytest.mark.parametrize para ejecutar pruebas con distintos conjuntos de datos
- Uso de la librería Faker para generación de datos dinámicos
- Separación clara entre datos de prueba y lógica de los tests

---

## Archivos y Carpetas Importantes
- tests/: contiene todos los casos de prueba
- pages/: implementación del Page Object Model
- utils/: utilidades y funciones auxiliares
- reports/: reportes HTML y evidencias
- reports/screens/: capturas automáticas en fallos

---

## Archivos Excluidos del Repositorio (.gitignore)
No deben subirse al repositorio los siguientes elementos:

.venv/
__pycache__/
.pytest_cache/
.idea/
.vscode/
*.log

---

## Conclusión
Este framework permite ejecutar pruebas automatizadas de UI y API de forma consistente, mantenible y escalable.
La estructura del proyecto facilita la incorporación de nuevas pruebas, la reutilización del código y la interpretación clara de los resultados, cumpliendo con los requisitos del proyecto final de automatización de pruebas.
