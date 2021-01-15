# FIWARE Machine Learning - Supermarket example

* Clone this project
```shell
git clone https://github.com/ging/edvl-test
cd edvl-test
```

* Run the whole scenario
```shell
docker-compose up
```

* Open browser in http://localhost:8079

* Click on anonymous in top right corner and choose "Interpreters"

* Search for Spark and click "edit"

* Add the following in the "Artifact" field of the "Dependencies" section: ``/zeppelin/external-jars/orion.spark.connector-1.2.1.jar``

* Go back to main Zeppelin page by clicking on the logo and click "Import note". Pick a name and choose the "Select JSON File/IPYNB File" option

* Open the notebook "Example1.zpln" in the directory ``notebook`` of this repository

* Run one by one each of the chunks

* After running the last one open a new terminal and run the simulated notifications ```sh simulated_notification.sh```
