# DataOps
A template for DataOps projects.

Data extracted from: https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017

## Create DataOps Development Environment

1) Clone Project

    ```bash
    git clone https://github.com/CharlieHex/DataOps.git
    ```

2) Setup Spark Container

    ```docker
    # Start containers in detached mode
    docker-compose up -d

    # View logs to ensure running
    docker-compose logs
    ```

2) Activate Python Virtual Environment

    1) Install Virtualenv
    
        * venv is included in Python 3.3 and above
            ```bash
            python --version
            ```
        * Install Python Virtual Environment
            ```bash
            pip install virtualenv
            ```
    2) Create a Virtual Environment

        ```Bash
        # Navigate to your project directory
        cd /path/to/your/DataOps/project

        # Create a virtual environment named 'venv'
        python -m venv venv
        ```

    3) Activate the Virtual Environment

        Windows
        
            .\venv\Scripts\activate

        Linux

            source venv/bin/activate

    4) Install Project Dependancies

        ```bash
        pip install -r requirements.txt
        ```

3) Run Python script or issue arguments via the command line

    * Script

        ```bash
        python main.py
        ```

    * Command Line

        1) Type "python" and hit enter. This opens the Python Interpreter.
        
        2) Import pyspark library
            ```python
            from pyspark.sql import SparkSession
            ```
        3) Start a spark session (local master 2/ no workers)
            ```python
            spark = SparkSession.builder \
                .appName("Example Application") \
                .master("local[*]") \
                .getOrCreate()
            ```
        4) Issue Commands
            ```python
            data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
            columns = ["Name", "Age"]
            df = spark.createDataFrame(data, columns)
            df.show()
            ```