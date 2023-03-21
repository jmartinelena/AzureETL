# Desarrollo

Esta etapa del proyecto abarca el sprint 1 y 2.

## Arquitectura inicial

Inicialmente optamos por una arquitectura en la que nos conectábamos a la base de datos desde Databricks, leíamos las tablas, las cargábamos en dataframes de PySpark, realizábamos las transformaciones y luego estas se cargaban en tablas nuevas dentro de la base de datos. Además, este trabajo en Databricks estaba distribuido en múltiples notebooks - uno por cada transformación, y eran ejecutados desde un notebook padre. 

![Arquitectura inicial](https://i.imgur.com/hgtnn1E.png)

- En este diseño Databricks lee las tablas desde Azure SQL y escribe hacia el mismo los cambios generando nuevas tablas.
- Como ventaja este diseño permitía ejecutar cada transformación por separado o en conjunto llamándolas consecutivamente en otro módulo.
- Sumado a eso nos permitía agregar nuevas transformaciones y nuevas tablas sin depender de las ya existentes.
- Copy data de SQL a DATA LAKE (exportación final)
- La desventaja que promovió el cambio de diseño es el gran consumo de recursos que generaba la recurrente interacción con Azure SQL.
- Otra desventaja es que tenía un tiempo de ejecución mayor (alrededor de 5 minutos comparado con los 2 actuales)

## Arquitectura final

- En este diseño Databricks lee el blob storage con los archivos CSV generados con un copy data desde SQL y escribe en el datalake archivos CSV
- Al cargar tablas csv estáticas tanto en blob storage como datalake se tiene un menor uso de recursos y por ende un menor costo
- Copy data de SQL a BLOB STORAGE (preparación de tablas csv para ser leídas por databricks)
- Mucho más rápido que el pipeline anterior (~2 min vs ~5 min)
- Pero al usar un notebook único se pierde un poco la modularidad de las transformaciones
- Al no usar SQL la información no persiste y no sería posible que los datos de las tablas se actualicen en tiempo real como si lo harían si estuvieran cargados en SQL

![Arquitectura final](https://i.imgur.com/XlPdt83.png)

El pipeline en Azure Data Factory para esta arquitectura era el siguiente:  
![Pipeline final](https://i.imgur.com/NT2P4uM.png)

Este consistía en los siguientes pasos:
1. Ir a buscar la información de acceso para el blob storage y data lake (generados por el script de automatización en PowerShell) para pasárselas posteriormente a Databricks como parámetro.
2. Verificar la existencia de los CSV en el blob storage, de no existir crearlos a través de un Copy Data de SQL a CSV.
3. Traer las tablas CSV y guardar sus nombres en un array.
4. Pasar el array con las tablas y la información de acceso a Databricks mediante parámetros.
5. Ejecutar el notebook único donde se leen los CSV originales, se los carga en dataframes de PySpark, se ejecutan las transformaciones y se exportan esos dataframes a nuevos CSV en el datalake.
