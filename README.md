# DataOps
A template for DataOps projects.

Data extracted from: https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017

Create DataOps Development Environment

1) Clone Project

    git clone https://github.com/CharlieHex/DataOps.git

2) Setup Spark Container

    docker-compose up

2) Activate Python Virtual Environment

    1) Install Virtualenv
    
        * venv is included in Python 3.3 and above

        pip install virtualenv

    2) Create a Virtual Environment

        Bash
        
        # Navigate to your project directory
        cd /path/to/your/project

        # Create a virtual environment named 'venv'
        python -m venv venv

    3) Activate the Virtual Environment

        Windows
        
            Bash

            .\venv\Scripts\activate

        Linux

            Bash

            source venv/bin/activate

    4) Install Project Dependancies

        pip install -r requirements.txt


3) Run Python script or issue arguments via the command line

    Script

    python main.py

    Command Line
    1) Type "python" and hit enter. This opens the Python Interpreter.
    2) Import pyspark library

        from pyspark.sql import SparkSession
    
    3) Start a spark session (local master 2/ no workers)

        spark = SparkSession.builder \
        .appName("Example Application") \
        .master("local[*]") \
        .getOrCreate()

    4) Issue Commands

        data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
        columns = ["Name", "Age"]
        df = spark.createDataFrame(data, columns)
        df.show()