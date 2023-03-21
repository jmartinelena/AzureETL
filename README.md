# Índice
- [Integrantes](#integrantes)
- [Modalidad](#modalidad)
- [Parte 1](#parte-1)
  - [Introduccion](#introducción)
  - [Objetivos](#objetivos)
  - [Assets](#assets)
- [Parte 2](#parte-2)
  - [Introducción](#introducción-1)
- [Navegación](#navegación)

# Integrantes

Integrantes del GRUPO 1:
-  Carlos Eduardo Denett
-  Cecilia Marcela Espada 
-  Federico Pfund
-  **Juan Martín Elena**
-  Agustín Fernández
-  Patricio Perrone

# Modalidad:

Marco scrum en equipos de 3 y 5 de personas, con un tablero de gestión en Trello y la definición del Backlog del Producto. 

# Parte 1
## Introducción

Te contratan como Arquitecto Cloud para una startup de IT dedicada a la consultoría y asesoría en temáticas orientadas a analítica de datos.  Marcela, project manager de tu equipo, te comparte el pedido de que un cliente de la organización (Tech Consulting Group) necesita realizar un proceso de ETL sobre una base de datos que se encuentra de forma “on - premise” dentro de su compañía.

El pedido de la empresa consiste esencialmente en desarrollar una canalización de datos (pipeline) utilizando diferentes servicios de Azure, los cuales incluyen el almacenamiento, procesamiento y orquestación de datos. Como requerimiento excluyente del proyecto, es necesario que todo el flujo de datos se ejecute sobre la nube de Azure dado que es el proveedor que actualmente posee contratado la organización.

La base de datos a utilizar se llama: dbRetail y se encuentra compuesta por diferentes tablas de negocio como ser: Resulta importante destacar que el formato de la base de datos es de tipo .bacpac.

Con esta implementación, se busca realizar diferentes transformaciones sobre las tablas propuestas para automatizar el proceso de ingesta, transformación y carga de datos. Con la aplicación de esta tecnología, Tech Consulting Group, lograra incrementar la productividad de sus procesos, al automatizar una tarea repetitiva que con lleva en la perdida de tiempo valioso para el negocio.

## Objetivos

Crearemos una canalización que permita:
<ul>
<li>Almacenar la base de datos dentro del motor de Azure SQL.</li>
<li>Ingestar una tabla desde el servicio de Data Factory.</li>
<li>Configurar los diferentes Linked Services requeridos para el proyecto.</li>
<li>Integrar el servicio de Databricks para la realización de un ETL con Data Factory.</li>
<li>Cargar la tabla transformada dentro de un Data Lake a través del proceso de ETL.</li>
</ul>

## Transformaciones

Transformaciones:

<ol>
<li>En la tabla “Categoria” renombrar el campo Categoria a Nombre_Categoria.</li>
<li>En la tabla “FactMine” obtener el total de la columna: TotalOreMined.</li>
<li>En la tabla “Mine” seleccionar únicamente las columnas: Country, FirstName,LastName y Age.</li>
<li>En la tabla “Mine” obtener el total de la columna: TotalWasted agrupado por el atributo Country.</li>
<li>En la tabla “Producto” realizar un conteo de la cantidad de productos disponibles utilizando el campo: Cod_Producto.</li>
<li>En la tabla “Producto” mostrar de forma descendiente la información ordenada por el campo: Cod_Producto.</li>
<li>En la tabla “Subcategoria” realizar un filtro por el Cod_Categoria = 3.</li>
<li>En la tabla “VentasInternet” generar una columna llamada Ingresos Netos, que se obtenga de multiplicar los atributos: (Cantidad * PrecioUnitario) – CostoUnitario.</li>
<li>En la tabla “VentasInternet” mostrar el promedio y suma total de la columna: Ingresos Netos por Cod_Producto.</li>
</ol>

## Assets
La base de datos a utilizar para el proyecto, podrás encontrarla en el siguiente <a href="https://github.com/laylascheli/alkemy_proyecto_aceleracion_practica">repositorio de GitHub</a>

# Parte 2

# Introducción
Luego de la ingesta de datos, Tech Consulting Group quiere que haya una asociación entre los productos y su sucursal correspondiente, para poder hacer un inventario de los productos en stock.

Al poder disponibilizar la información desde Datalake, la empresa quiere que esta pueda visualizarse para sus clientes y proveedores, por lo que desean usar una página (opcional) con dos tipos de acceso:

Cliente: Acceso anónimo, podrán hacer consultas por categoría, subcategoría o producto de la siguiente forma:
- Si la búsqueda no contiene producto, los resultados se desplegaran mostrando productos y total de stock.
- Si la búsqueda contiene producto, los resultados se desplegaran mostrando las sucursales y el stock que hay en cada una.
- Simular una compra.

Proveedor: Acceso con credenciales. Ingresará la información de los productos y la cantidad
- Internamente los productos se repartirán a todas las sucursales proporcionalmente a la cantidad de ventas de la sucursal, con un mínimo de "1" producto según disponibilidad, esto quiere decir que si hay 3 productos y 10 sucursales, el producto se repartirá al top 3 de las sucursales.
- Agregar nuevos productos.

# Navegación

- [Rama martin](https://github.com/jmartinelena/AzureETL/tree/martin): pipelines de Azure Data Factory (ambas versiones de la parte 1).
- [Rama api](https://github.com/jmartinelena/AzureETL/tree/api): API en FastAPI hecha para la parte 2.
- [Rama sprintreviews](https://github.com/jmartinelena/AzureETL/tree/sprintreviews): presentaciones de cada sprint en formato pdf (originalmente hechas en Google Slides).
