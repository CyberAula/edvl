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

* Click "Import note". Pick a name and choose the "Select JSON File/IPYNB File" option

## Automatic subscription

* Open the notebook "Example2.zpln" in the directory ``notebook`` of this repository

* Run one by one each of the chunks

* After running the last chunk open a new terminal and run the script to create an entity in Orion: ```sh create_entity.sh``` (skip it if you have done it already)

* Simulate new data arriving to Orion ```sh simulated_data_entity.sh```

* See how in the notebook the minimum temperature each 10 seconds appears.

## Manual subscription

* Open the notebook "Example1.zpln" in the directory ``notebook`` of this repository

* Run one by one each of the chunks

* After running the last chunk open a new terminal and run the script to create an entity in Orion: ```sh create_entity.sh``` (skip it if you have done it already)

* Create the subscription to the entity, notifying the spark-worker of any change: ```sh subscribe.sh```

* Simulate new data arriving to Orion ```sh simulated_data_entity.sh```

* See how in the notebook the minimum temperature each 10 seconds appears.

* If you wish to skip Orion and simulate data arriving directly to Spark you can run ```sh simulated_notification.sh``` instead of the previous 3 scripts.

