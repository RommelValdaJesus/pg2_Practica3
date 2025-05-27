# API de Repuestos para Vehículos

## Descripción
Esta API permite gestionar proveedores, marcas, vehículos y repuestos. Facilita la administración de información sobre piezas automotrices y sus fabricantes, proporcionando endpoints para realizar operaciones CRUD.

## Diagrama de Modelos
Para generar el diagrama de modelos, usa el siguiente comando en Django Extensions:

```bash
python manage.py graph_models repuestos -o modelos.png 
```
## Documentación de la API
Esta API incluye una interfaz de documentación automática en localhost. Para acceder a la documentación interactiva, visita la siguiente URL una vez que el servidor esté en ejecución:
- Documentación automática: http://localhost:8000/docs/

En esta página, podrás visualizar todos los endpoints disponibles, sus métodos y ejemplos de uso, facilitando la integración y pruebas.


## Endpoints

## Proveedores
- GET /api/proveedores/ → Lista todos los proveedores.
- POST /api/proveedores/ → Crea un nuevo proveedor.
- GET /api/proveedores/{id}/ → Obtiene un proveedor por ID.
- PUT /api/proveedores/{id}/ → Actualiza un proveedor.
- DELETE /api/proveedores/{id}/ → Elimina un proveedor.

## Marcas
- GET /api/marcas/ → Lista todas las marcas.
- POST /api/marcas/ → Crea una nueva marca.
- GET /api/marcas/{id}/ → Obtiene una marca por ID.
- PUT /api/marcas/{id}/ → Actualiza una marca.
- DELETE /api/marcas/{id}/ → Elimina una marca.

## Vehículos
- GET /api/vehiculos/ → Lista todos los vehículos.
- POST /api/vehiculos/ → Crea un nuevo vehículo.
- GET /api/vehiculos/{id}/ → Obtiene un vehículo por ID.
- PUT /api/vehiculos/{id}/ → Actualiza un vehículo.
- DELETE /api/vehiculos/{id}/ → Elimina un vehículo.

## Repuestos
- GET /api/repuestos/ → Lista todos los repuestos.
- POST /api/repuestos/ → Crea un nuevo repuesto.
- GET /api/repuestos/{id}/ → Obtiene un repuesto por ID.
- PUT /api/repuestos/{id}/ → Actualiza un repuesto.
- DELETE /api/repuestos/{id}/ → Elimina un repuesto.


## Caso de Uso

1. Crear un proveedor:

```bash
curl -X POST "http://localhost:8000/api/proveedores/" \
-H "Content-Type: application/json" \
-d '{
    "nombre": "Repuestos ABC",
    "contacto": "Juan Pérez",
    "ubicacion": "Bolivia"
}'
```

2. Crear una marca:

```bash
curl -X POST "http://localhost:8000/api/marcas/" \
-H "Content-Type: application/json" \
-d '{
    "nombre": "Toyota",
    "pais_origen": "Japón"
}'
```

3. Crear un Vehiculo:

```bash
curl -X POST "http://localhost:8000/api/vehiculos/" \
-H "Content-Type: application/json" \
-d '{
    "modelo": "Corolla",
    "año": 2000,
    "marca": 1
}'
```

4. Agregar un repuesto al vehiculo:

```bash
curl -X POST "http://localhost:8000/api/repuestos/" \
-H "Content-Type: application/json" \
-d '{
    "nombre": "Filtro de aire",
    "descripcion": "Filtro para motor",
    "precio": 40,
    "proveedor": 1,
    "vehiculo": 1
}'
```