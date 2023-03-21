# Desarrollo

Esta etapa abarca los sprint 3, 4 y 5.

# Discusión inicial de diseño

Nosotros planteamos 2 arquitecturas, una utilizando Flask (o FastAPI) en Python como back-end. 
- En esta arquitectura referenciamos los recursos de Azure SQL y Azure Data Lake desde esta API, diferenciando la ejecución de Cliente y Proveedor dentro de la propia API. La desventaja es que no se hace tanto enfoque en Azure Data Factory ya que no existe, sino que se usan recursos de Azure para la base de datos consultada.  
![Arquitectura con API](https://i.imgur.com/vZPEPRA.png)
- La segunda arquitectura aprovecha más los recursos de Azure, no tenemos un API propio sino que usamos la API REST de Azure Data Factory, el mayor inconveniente con esta arquitectura es que es necesario un Pipeline para Cliente y un Pipeline para Proveedor dentro de Datafactory, lo que dificulta la escalabilidad, además de que los tiempos de respuesta de Datafactory son mucho más lentos que el procesamiento en un servidor dedicado de una API y la simultaneidad de clientes ¿ Crearía varios pipelines ejecutándose en simultaneo?  
![Arquitectura intentando utilizar pipelines](https://i.imgur.com/Te8qktO.png)
- El front-end es invariable en ambas arquitecturas.

Finalmente nos quedamos con la primera arquitectura, lo cual resultó ser un acierto debido a inconvenientes que surgieron después para otros grupos, los cuales no se presentaron en nuestro caso. La razón por la que elegimos esta fue porque era más sencilla de implementar y más rápida al ejecutarse.

# Inicialización del entorno

Para inicializar el entorno se desarrolló un pipeline sencillo que creaba las tablas nuevas a utilizar y las rellenaba. Luego éstas se copiaban a CSVs.  

![Pipeline inicializador](https://i.imgur.com/Ircrc17.png)  
![Tablas necesarias](https://i.imgur.com/7GkGNoO.png)

# Características de la API

- Desarrollada en FastAPI.
- Accedemos a la información del Data Lake a través del Azure Data Lake File System (adlfs).
- Nos conectamos a la base de datos en Azure SQL a través del conector pyodbc.
- Distintos endpoints (rutas) para poder consultar múltiples recursos según distintos criterios/objetivos.
- Devolvemos el contenido en formato JSON para poder ser consultado fácilmente por distintos recursos (ej: frontend).

# Ejecución

Para ejecutar se necesita un config.json, se adjunta un config.example.json de muestra

## Levantar servidor en DOCKER
docker build -t fastapi-image .

docker run -d --name softtek-api-container -p 8000:8000 fastapi-image
