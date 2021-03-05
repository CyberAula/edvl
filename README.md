# EDVL

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
