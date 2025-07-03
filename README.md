# 🚀 Kafka + PySpark + NASA API Streaming Project

Thius project shows real-time data inggestion using Apache Kafka, Pyspark scalable and fault-tolerant stream proces, data was source from NASA Public API (APOD and inSight). Originally it was created during an internship and now i just wanted to update the documentation.


📌 Features

    -Fetching daily data from NASA’s APOD and InSight APIs from https://api.nasa.gov/
    -Produces messages into two Kafka topics.
    -Consumes those topics using Apache Spark streaming.
    -Streams and stores the results in HDFS, partitioned by data source and the environment.
    -Supports both APOD and Mars Weather (InSight) pipelines.




📁 Project Structure

    > producer.py                  # Kafka producer logic
    > consumer.py                  # PySpark consumer that reads from Kafka and writes to HDFS
    > nasa_api_client.py           # NASA API fetcher and message dispatcher
    > directory_creation_script.sh # HDFS directory creation script
    > README.md                    # Project documentation


🔄 Data Flow Overview

    1. nasa_api_client.py fetches data from NASA's APIs and sends it to Kafka.

    2. Kafka receives and stores messages in two topics:

        2.1 api.analyst_data.apod_edvin

        2.2 api.analyst_data.insight_edvin

    3. consumer.py uses Spark Structured Streaming to read data from Kafka and writes it to:

        3.1 interns/test/landing/... directories in HDFS

    4. HDFS is organized by environment (test/prod), topic, and data layer (landing/base/analytical/error).



🧪 How to Run

    Pre-launch: Get your API key from: https://api.nasa.gov/ (APOD & Insight) and insert it in "nasa_api_client.py"
    
    Step 1: Create HDFS directories
    Run the setup script:
    bash directory_creation_script.sh
    
    Step 2: Start Spark Consumer
    Submit the consumer script using Spark:
    spark-submit --deploy-mode cluster --master yarn consumer.py

    Step 3: Send NASA API Data
    python nasa_api_client.py


    Troubleshoot check logs:
    yarn logs -applicationId <your_app_id>


🛠 Technologies Used:

    -Python 3
    -Apache Kafka
    -Apache Spark
    -HDFS
    -NASA API (APOD & InSight)


🙋‍♂️ Author
-Edvin Volcok
