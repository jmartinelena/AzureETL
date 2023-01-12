# 
## Instalacion de `Java` y `Scala`:

> Si no tienes instalado el jdk de java:
```bash
sudo apt update
sudo apt install openjdk=11.0.17 
java --version
```
 `Output:`
```bash
openjdk 11.0.17 2022-10-18
OpenJDK Runtime Environment (build 11.0.17+8-post-Ubuntu-1ubuntu222.04)
OpenJDK 64-Bit Server VM (build 11.0.17+8-post-Ubuntu-1ubuntu222.04, mixed mode, sharing)
```
> Instalar Scala:  
```bash
sudo apt install scala
scala -version
```
`Output:`
```bash
Scala code runner version 2.11.12 -- Copyright 2002-2017, LAMP/EPFL
```

## Instalar `Apache Spark`
 
>Descargar la última versión.

[link](https://archive.apache.org/dist/spark/spark-3.3.1/)

```bash
cd /tmp
wget https://archive.apache.org/dist/spark/spark-3.3.1/spark-3.3.1-bin-hadoop3.tgz 
```

> Extraiga el archivo descargado y muévalo al `/opt` directorio, renombrado como `spark` e elimina de archivos temporales el relese.
```bash
tar -xvzf spark-3.3.1-bin-hadoop3.tgz 
sudo mv spark-3.3.1-bin-hadoop3.tgz /opt/spark
sudo rm -r spark-3.3.1-bin-hadoop3.tgz 
```
>Cree variables de entorno para poder ejecutar y ejecutar `Spark`:
```bash
nano ~/.bashrc
```
>Agregue las líneas en la parte inferior del archivo y guárdelo.
```bash
export SPARK_HOME=/opt/spark

export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
```
>Ejecute los siguientes comandos para aplicar los cambios de su entorno.
```bash
source ~/.bashrc
```
# Inicie Apache `Spark`.
>En este punto, Apache Spark está instalado y listo para usar. 
> Ejecute los siguientes comandos para iniciarlo.
```bash
cd /opt/spark

./sbin/start-master.sh
```
>Inicie el proceso de trabajo de Spark ejecutando los siguientes comandos.
```
./sbin/start-slave.sh spark://localhost:7077
```
>Puede reemplazar el host localhost con el nombre de host del servidor o la dirección IP.
```
http://localhost:8080
```

>Si deseas conectarse a Spark a través de su shell de comandos, ejecute los siguientes comandos:
```
./sbin/spark-shell
```
## Path de data:
> Ahora Moveremos la careta data al lugar indicado: seguramente te encuentras en el `path:`  /opt/spark:
> Pocisionate en la carpeta donde esta data Osea:

```
cd --
cd Documents/notebooks
```
>Es posible que veas la carpeta data:
>Ahora mueve esa carpeta a: `opt/spark/spark-warehouse.`

```
mv data ../../../../opt/spark/spark-warehouse
```
>Ahora  vuelve a: `opt/spark`:
```
cd /opt/spark
```
>Analiza el directorio, veras las carpeta `csv` dentro de `spark-warehouse.` con todos los archivos a tranformar. asegurate que se encuentre dicha carpeta. recuerda la carpeta csv dentro de   `spark-warehouse.`.

```
ls -l
```


## Run `ETL` 
>Run Spark App si el clon fuen en Documents.

```
./bin/spark-submit \
                --master spark://localhost:7077 \
                 $HOME/Documents/notebooks/cicd-etl/job/tasks/etl.py

```
>En mi caso solo para el archivo VentasInternet.csv:
```
./bin/spark-submit \
                --master spark://fede:7077 \
                 $HOME/Documents/notebooks/cicd-etl/job/tasks/etl.py VentasInternet.csv

```
> Si quiere ejecutar todas las tranformaciones con el siguiente comando:

```
./bin/spark-submit --master spark://fede:7077 \
                    $HOME/Documents/notebooks/cicd-etl/job/tasks/etl.py\
                     VentasInternet.csv \
                     Categoria.csv \
                     FactMine.csv \
                     Producto.csv \
                     Mine.csv

```
> Recuerda tienes que estar parado en el directorio ```/opt/spark ```y tener la carpeta de ```csv``` proveniente de ```data``` en 
```spark-warehouse```.
> Tiempo de ejucion total: ```36.316101``` ms.  tranquilo bucaremos mayor eficiencia.
>Resultado:
```
Schema de Ventas Internet
root
 |-- Cod_Producto: integer (nullable = true)
 |-- Cod_Cliente: integer (nullable = true)
 |-- Cod_Territorio: integer (nullable = true)
 |-- NumeroOrden: string (nullable = true)
 |-- Cantidad: integer (nullable = true)
 |-- PrecioUnitario: double (nullable = true)
 |-- CostoUnitario: double (nullable = true)
 |-- Impuesto: double (nullable = true)
 |-- Flete: double (nullable = true)
 |-- FechaOrden: timestamp (nullable = true)
 |-- FechaEnvio: timestamp (nullable = true)
 |-- FechaVencimiento: timestamp (nullable = true)
 |-- Cod_Promocion: integer (nullable = true)


```
>Visualizamos tabla TableSortedByDescCode

```
+------------+-----------+--------------+-----------+--------+--------------+-------------+--------+-------+-------------------+-------------------+-------------------+-------------+
|Cod_Producto|Cod_Cliente|Cod_Territorio|NumeroOrden|Cantidad|PrecioUnitario|CostoUnitario|Impuesto|  Flete|         FechaOrden|         FechaEnvio|   FechaVencimiento|Cod_Promocion|
+------------+-----------+--------------+-----------+--------+--------------+-------------+--------+-------+-------------------+-------------------+-------------------+-------------+
|         606|      14161|             8|    SO70009|       1|        539.99|     343.6496| 43.1992|13.4998|2013-11-03 00:00:00|2013-11-10 00:00:00|2013-11-15 00:00:00|            1|
|         606|      25927|             9|    SO70858|       1|        539.99|     343.6496| 43.1992|13.4998|2013-11-15 00:00:00|2013-11-22 00:00:00|2013-11-27 00:00:00|            1|
|         606|      25508|             8|    SO70011|       1|        539.99|     343.6496| 43.1992|13.4998|2013-11-03 00:00:00|2013-11-10 00:00:00|2013-11-15 00:00:00|            1|
|         606|      25707|             9|    SO69632|       1|        539.99|     343.6496| 43.1992|13.4998|2013-10-29 00:00:00|2013-11-05 00:00:00|2013-11-10 00:00:00|            1|
|         606|      28375|            10|    SO70012|       1|        539.99|     343.6496| 43.1992|13.4998|2013-11-03 00:00:00|2013-11-10 00:00:00|2013-11-15 00:00:00|            1|
|         606|      28399|            10|    SO69647|       1|        539.99|     343.6496| 43.1992|13.4998|2013-10-29 00:00:00|2013-11-05 00:00:00|2013-11-10 00:00:00|            2|
|         606|      25944|             9|    SO70165|       1|        539.99|     343.6496| 43.1992|13.4998|2013-11-05 00:00:00|2013-11-12 00:00:00|2013-11-17 00:00:00|            1|
|         606|      23739|             4|    SO69711|       1|        539.99|     343.6496| 43.1992|13.4998|2013-10-30 00:00:00|2013-11-06 00:00:00|2013-11-11 00:00:00|            1|
|         606|      25937|             9|    SO70225|       1|        539.99|     343.6496| 43.1992|13.4998|2013-11-06 00:00:00|2013-11-13 00:00:00|2013-11-18 00:00:00|            2|
|         606|      29294|             9|    SO69373|       1|        539.99|     343.6496| 43.1992|13.4998|2013-10-28 00:00:00|2013-11-04 00:00:00|2013-11-09 00:00:00|            2|
|         606|      23835|             4|    SO70237|       1|        539.99|     343.6496| 43.1992|13.4998|2013-11-06 00:00:00|2013-11-13 00:00:00|2013-11-18 00:00:00|            1|
|         606|      23505|             4|    SO69856|       1|        539.99|     343.6496| 43.1992|13.4998|2013-11-01 00:00:00|2013-11-08 00:00:00|2013-11-13 00:00:00|            1|
|         606|      25939|             9|    SO70310|       1|        539.99|     343.6496| 43.1992|13.4998|2013-11-07 00:00:00|2013-11-14 00:00:00|2013-11-19 00:00:00|            1|
|         606|      28425|            10|    SO69861|       1|        539.99|     343.6496| 43.1992|13.4998|2013-11-01 00:00:00|2013-11-08 00:00:00|2013-11-13 00:00:00|            1|
|         606|      25713|             9|    SO70375|       1|        539.99|     343.6496| 43.1992|13.4998|2013-11-08 00:00:00|2013-11-15 00:00:00|2013-11-20 00:00:00|            1|
|         606|      23847|             1|    SO69933|       1|        539.99|     343.6496| 43.1992|13.4998|2013-11-02 00:00:00|2013-11-09 00:00:00|2013-11-14 00:00:00|            1|
|         606|      23586|             4|    SO70442|       1|        539.99|     343.6496| 43.1992|13.4998|2013-11-09 00:00:00|2013-11-16 00:00:00|2013-11-21 00:00:00|            1|
|         606|      23854|             4|    SO70512|       1|        539.99|     343.6496| 43.1992|13.4998|2013-11-10 00:00:00|2013-11-17 00:00:00|2013-11-22 00:00:00|            1|
|         606|      23857|             1|    SO70809|       1|        539.99|     343.6496| 43.1992|13.4998|2013-11-14 00:00:00|2013-11-21 00:00:00|2013-11-26 00:00:00|            2|
|         606|      25504|             8|    SO70518|       1|        539.99|     343.6496| 43.1992|13.4998|2013-11-10 00:00:00|2013-11-17 00:00:00|2013-11-22 00:00:00|            1|
+------------+-----------+--------------+-----------+--------+--------------+-------------+--------+-------+-------------------+-------------------+-------------------+-------------+


```


```
+------------+-----------+--------------+-----------+--------+--------------+-------------+--------+------+-------------------+-------------------+-------------------+-------------+--------------+
|Cod_Producto|Cod_Cliente|Cod_Territorio|NumeroOrden|Cantidad|PrecioUnitario|CostoUnitario|Impuesto| Flete|         FechaOrden|         FechaEnvio|   FechaVencimiento|Cod_Promocion|Ingresos_Netos|
+------------+-----------+--------------+-----------+--------+--------------+-------------+--------+------+-------------------+-------------------+-------------------+-------------+--------------+
|         528|      12097|             6|    SO65573|       1|          4.99|       1.8663|  0.3992|0.1248|2013-09-02 00:00:00|2013-09-09 00:00:00|2013-09-14 00:00:00|            1|        3.1237|
|         535|      26198|             4|    SO65574|       1|         24.99|       9.3463|  1.9992|0.6248|2013-09-02 00:00:00|2013-09-09 00:00:00|2013-09-14 00:00:00|            1|       15.6437|
|         536|      11276|             6|    SO65575|       1|         29.99|      11.2163|  2.3992|0.7498|2013-09-02 00:00:00|2013-09-09 00:00:00|2013-09-14 00:00:00|            1|       18.7737|
|         528|      11276|             6|    SO65575|       1|          4.99|       1.8663|  0.3992|0.1248|2013-09-02 00:00:00|2013-09-09 00:00:00|2013-09-14 00:00:00|            1|        3.1237|
|         536|      15413|             6|    SO65576|       1|         29.99|      11.2163|  2.3992|0.7498|2013-09-02 00:00:00|2013-09-09 00:00:00|2013-09-14 00:00:00|            1|       18.7737|
|         528|      15413|             6|    SO65576|       1|          4.99|       1.8663|  0.3992|0.1248|2013-09-02 00:00:00|2013-09-09 00:00:00|2013-09-14 00:00:00|            1|        3.1237|
|         214|      15413|             6|    SO65576|       1|         34.99|      13.0863|  2.7992|0.8748|2013-09-02 00:00:00|2013-09-09 00:00:00|2013-09-14 00:00:00|            1|       21.9037|
|         234|      15413|             6|    SO65576|       1|         49.99|      38.4923|  3.9992|1.2498|2013-09-02 00:00:00|2013-09-09 00:00:00|2013-09-14 00:00:00|            1|       11.4977|
|         478|      13303|             6|    SO65577|       1|          9.99|       3.7363|  0.7992|0.2498|2013-09-02 00:00:00|2013-09-09 00:00:00|2013-09-14 00:00:00|            1|        6.2537|
|         478|      21292|             1|    SO65578|       1|          9.99|       3.7363|  0.7992|0.2498|2013-09-02 00:00:00|2013-09-09 00:00:00|2013-09-14 00:00:00|            1|        6.2537|
|         478|      22340|             4|    SO65579|       1|          9.99|       3.7363|  0.7992|0.2498|2013-09-02 00:00:00|2013-09-09 00:00:00|2013-09-14 00:00:00|            1|        6.2537|
|         472|      19636|             1|    SO65580|       1|          63.5|       23.749|    5.08|1.5875|2013-09-02 00:00:00|2013-09-09 00:00:00|2013-09-14 00:00:00|            1|       39.7510|
|         473|      24322|             6|    SO65582|       1|          63.5|       23.749|    5.08|1.5875|2013-09-02 00:00:00|2013-09-09 00:00:00|2013-09-14 00:00:00|            1|       39.7510|
|         528|      16369|             1|    SO65584|       1|          4.99|       1.8663|  0.3992|0.1248|2013-09-02 00:00:00|2013-09-09 00:00:00|2013-09-14 00:00:00|            1|        3.1237|
|         485|      16369|             1|    SO65584|       1|         21.98|       8.2205|  1.7584|0.5495|2013-09-02 00:00:00|2013-09-09 00:00:00|2013-09-14 00:00:00|            1|       13.7595|
|         528|      16501|             1|    SO65585|       1|          4.99|       1.8663|  0.3992|0.1248|2013-09-02 00:00:00|2013-09-09 00:00:00|2013-09-14 00:00:00|            1|        3.1237|
|         528|      22730|             6|    SO65586|       1|          4.99|       1.8663|  0.3992|0.1248|2013-09-02 00:00:00|2013-09-09 00:00:00|2013-09-14 00:00:00|            1|        3.1237|
|         485|      14841|             8|    SO65587|       1|         21.98|       8.2205|  1.7584|0.5495|2013-09-02 00:00:00|2013-09-09 00:00:00|2013-09-14 00:00:00|            1|       13.7595|
|         472|      14841|             8|    SO65587|       1|          63.5|       23.749|    5.08|1.5875|2013-09-02 00:00:00|2013-09-09 00:00:00|2013-09-14 00:00:00|            1|       39.7510|
|         528|      14691|             7|    SO65588|       1|          4.99|       1.8663|  0.3992|0.1248|2013-09-02 00:00:00|2013-09-09 00:00:00|2013-09-14 00:00:00|            1|        3.1237|
+------------+-----------+--------------+-----------+--------+--------------+-------------+--------+------+-------------------+-------------------+-------------------+-------------+--------------+

>


```
>
```
+------------+---------------------+-------------------+
|Cod_Producto|Ingreso_Neto_Promedio|Suma_Ingresos_Netos|
+------------+---------------------+-------------------+
|         471|              39.7510|          6678.1680|
|         540|              20.4076|         17509.7208|
|         580|             618.4800|        152146.0800|
|         588|             349.7116|         44763.0848|
|         481|               5.6277|          1677.0546|
|         472|              39.7510|          7910.4490|
|         322|             285.9519|          4861.1823|
|         362|             943.2882|        189600.9282|
|         321|             296.2834|         16295.5870|
|         375|             860.8787|        121383.8967|
|         593|             256.7721|         10014.1119|
|         597|             245.4103|         12025.1047|
|         530|               3.1237|          4648.0656|
|         368|             924.5636|        133137.1584|
|         385|             394.7883|         27240.3927|
|         596|             245.4103|         11779.6944|
|         587|             349.7116|         51757.3168|
|         332|             285.9519|          5147.1342|
|         577|             459.6992|         44590.8224|
|         384|             407.4102|         81074.6298|
+------------+---------------------+-------------------+



```

>Categoria:
```
+-------------+----------------+
|Cod_Categoria|Nombre_Categoria|
+-------------+----------------+
|            1|       Bicicleta|
|            2|      Componente|
|            3|          Prenda|
|            4|       Accesorio|
+-------------+----------------+


```


>Schema Producto:

```
root
 |-- Cod_Producto: integer (nullable = true)
 |-- Producto: string (nullable = true)
 |-- Cod_SubCategoria: integer (nullable = true)
 |-- Color: string (nullable = true)

root
 |-- Cantidad_CodProducto: long (nullable = false)

root
 |-- Cantidad_CodProducto: integer (nullable = false)



```
>FactMine
```
+------------------+
|Suma_TotalOreMined|
+------------------+
|         166599.51|
+------------------+

```
>Schema Mine:

```
Master
root
 |-- TruckID: integer (nullable = true)
 |-- Truck: string (nullable = true)
 |-- ProjectID: integer (nullable = true)
 |-- Country: string (nullable = true)
 |-- OperatorID: integer (nullable = true)
 |-- FirstName: string (nullable = true)
 |-- LastName: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- TotalOreMined: double (nullable = true)
 |-- TotalWasted: double (nullable = true)
 |-- Date: timestamp (nullable = true)
```
```
Transformada
    root
    |-- Country: string (nullable = true)
    |-- FirstName: string (nullable = true)
    |-- LastName: string (nullable = true)
    |-- Age: integer (nullable = true)
```
```
Transformada
    root
    |-- Country: string (nullable = true)
    |-- Suma_TotalWasted: double (nullable = true)

```

>### Hadoop Config

```


```
>### Hadoop Commandos

<br />

**Comandos utilizados Hadoop**

<details>
<summary>Comandos </summary>


<br />


`hdfs dfs -mkdir /user/fede/input/csv` = Crea un directorio `csv`. 

`hdfs dfs -ls /` = Muestra el directorio. 

`hdfs dfs -put csv /user/fede/input` = Empuja la carpeta de archivo csv a la carpeta Input.

>output:
`-rw-r--r--   1 fede supergroup    1598678 2023-01-12 19:01 /user/fede/input/csv` 

`hdfs dfs -ls /user/fede/input` = Muestra las carpetas en el directorio. 

`hdfs dfs -cp /user/fede/input/csv/Mine.csv /user/fede/Output/landing` = Mueve el archivo Mine.csv al ente directorio landing. 

`hdfs dfs -rm /user/fede/input/csv/Mine.csv` = Remueve el archivo Mine.csv de la carpeta csv.



<br />

**Testing and releasing**
<br />

```
git tag -a v<0.0.3> -m "Release tag for version <0.0.3>"
git push origin --tags
```
