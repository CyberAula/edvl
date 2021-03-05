#  Educational Data Virtual Lab (EDVL) 

The Educational Data Virtual Lab (EDVL) is a component of the ADA project that will be used for the delivery of the practical and hands-on part of the Urban Mobility Data Science courses. 
It is based on the European FIWARE platform, in which the specific components of Data Science applied to Urban Mobility will be integrated. 
Users will be able to analyze open data sets (anonymized) and also real data from companies.


* Clone this project
```shell
git clone https://github.com/ging/edvl
cd edvl
```

* Run the whole scenario
```shell
docker-compose up
```

## Spark Streaming example with Scala

* Open browser in http://localhost:8079

* Click "Import note". Pick a name and choose the "Select JSON File/IPYNB File" option

* Open the notebook "ExampleStreamingGraph.zpln" in the directory ``notebook`` of this repository

* In a terminal, simulate new data arriving to Orion  by running```sh simulated_data_entity.sh```

* Run one by one each of the chunks in the notebook to see how  the temperature updates in the graph


## MongoSpark example with Scala

* Open browser in http://localhost:8079

* Click "Import note". Pick a name and choose the "Select JSON File/IPYNB File" option

* Open the notebook "ExampleMongo.zpln" in the directory ``notebook`` of this repository

* Run one by one each of the chunks in the notebook to list and plot the data from the database

## PySpark batch example with pandas

* Open browser in http://localhost:8079

* Click "Import note". Pick a name and choose the "Select JSON File/IPYNB File" option

* Open the notebook "ExamplePlotCSV.zpln" in the directory ``notebook`` of this repository

* Run one by one each of the chunks in the notebook to perform descriptive statistics and create simple visualizations of the data
