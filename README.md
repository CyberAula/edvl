#  Educational Data Virtual Lab (EDVL) 

The **Educational Data Virtual Lab** (EDVL) is a component of the **ADA** project that will be used for the delivery of the practical and hands-on part of the Urban Mobility Data Science courses. 

It is based on  **Apache Zeppelin** and the European **FIWARE** platform, in which the specific components of Data Science applied to Urban Mobility will be integrated. 

**Apache Zeppelin** is a new and upcoming web-based notebook that enables data-driven, interactive data analytics and collaborative documents with SQL, Scala and more. It provides data exploration, visualization, sharing and collaboration features  and supports a plethora of languages and technologies.

**FIWARE** is a curated framework of open source components to accelerate the development of smart solutions, which enable the connection to IoT with Context Information Management and Big Data services in the Cloud. Furthermore, it provides standard APIs for data management and exchange, as well as harmonised data models.

## Requirements

* Docker and Docker-compose

## Installation

* Clone this project
```shell
git clone https://github.com/ging/edvl
cd edvl
```

* Run the whole scenario
```shell
docker-compose up
```

* Open the browser in http://localhost:8079 (credentials: admin/password1, user1/password2)


## Example notebooks

EDVL comes with a curated set of notebooks that can be use to get started in data science training. They are available in the ``notebook``directory. To run any of the notebooks you just need to:

* Click "Import note". Pick a name and choose the "Select JSON File/IPYNB File" option

* Choose the notebook that you want to explore from the ``notebook`` directory

* Open the notebook and run all of the chunks one by one in order.


Below is a description of the notebooks available.

### MongoDB with native visualizations

Notebook ``1. ExampleMongo.zpln`` showcases Apache Zeppelin's native visualizations when querying a Mongo database. It can be seen how data can be explored in an interactive way through many graphs and visualizations.

### SparkML

Stepping up from mere data exploration,  notebook ``2. ExampleSparkML.zpln`` shows how EDVL can be used for the complete lifecycle of machine learning, from data acquisition and storage provided by FIWARE Generic Enablers, to model training and prediction thanks to the SparkML library.

### MongoSpark with Scala

Instead of directly querying a Mongo database,  notebook ``3. ExampleMongoSpark.zpln`` shows how MongoSpark can be used to query data using the Scala language, and how the data retrieved can be ploted using web visualization libraries.

### Python Pandas

Apache Zeppelin supports one of the most common languages for data analysis (i.e., Python). In  notebook ``4. ExamplePandas.zpln``, a common workflow of analyzing a CSV file using Python Pandas is provided.

### Spark streaming

Not only batch analysis is supported, but also real-time. Thanks to Spark Streaming and the FIWARE Cosmos Spark Connector, data can be analyzed as soon as it arrives from the FIWARE Context Broker and plotted in real time using web visualization libraries (``5. ExampleStreamingPrint.zpln`` and ``6. ExampleStreamingGraph.zpln``). 

### Legacy Jupyter Notebook

Apache Zeppelin allows to import Jupyter Notebooks and reuse existing code. This way, users who are migrating from Jupyter can resume their work immediately. An example is provided in notebok ``7. Jupyter2Zeppelin.ipynb``
