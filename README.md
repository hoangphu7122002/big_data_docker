# Hadoop Spark JupyterHub Environment

A development environment integrating Hadoop, Spark, and JupyterHub using Docker containers.

## Project Structure

```
.
├── DAC/                    # User notebooks and data directory
│   └── dataset.csv
├── docker-compose.yml      # Main Docker Compose configuration
├── Dockerfile.jupyterhub   # JupyterHub Dockerfile
├── hadoop.env             # Hadoop environment variables
├── hadoop_data/           # Hadoop data directory
│   └── dataset.csv
├── jupyterhub_config.py   # JupyterHub configuration
└── jupyterhub_data/       # JupyterHub shared data
```

## Components

### Hadoop Services
- NameNode (ports: 9870, 9000)
- DataNode
- ResourceManager
- NodeManager
- HistoryServer

### Spark Services
- Spark Master (ports: 8080, 7077)
- Spark Worker 1 (port: 8081)
- Spark Worker 2 (port: 8082)

### Development Environment
- JupyterHub (port: 8000)

## Prerequisites

- Docker Engine
- Docker Compose

## Quick Start

1. Start the environment:
```bash
docker-compose --profile docker_hadoop_phu up -d
```

2. Check services status:
```bash
docker-compose ps
```

3. Access web interfaces:
   - Hadoop NameNode: http://localhost:9870
   - Spark Master: http://localhost:8080
   - JupyterHub: http://localhost:8000

4. Stop the environment:
```bash
docker-compose --profile docker_hadoop_phu down
```

## Working with Spark in JupyterHub

Example code to read CSV from HDFS using PySpark:

```python
from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Read CSV") \
    .master("spark://spark-master:7077") \
    .config("spark.driver.memory", "1g") \
    .config("spark.executor.memory", "1g") \
    .getOrCreate()

# Read CSV from HDFS
df = spark.read.csv("hdfs://namenode:9000/user/root/input/dataset.csv", header=True, inferSchema=True)

# Display data
df.show()

# Close SparkSession
spark.stop()
```

## Docker Configuration

### Volumes
- `hadoop_namenode`: NameNode data
- `hadoop_datanode`: DataNode data
- `hadoop_historyserver`: History server data
- `spark_data`: Spark shared data
- `jupyterhub_data`: JupyterHub shared data

### Network
- `hadoop_network_phu`: Bridge network for all services

## Important Notes

- Ensure required ports are not in use by other applications
- Check service logs if issues occur: `docker-compose logs [service_name]`
- The `.gitignore` file is configured to exclude temporary files and data directories

## Files Ignored by Git

```
# Python
__pycache__/
*.py[cod]
*$py.class
.Python
.env
.venv
.cache

# Jupyter
.ipynb_checkpoints
.jupyter
.local
DAC/.*

# Data and logs
data/
logs/
*.log

# Docker volumes
jupyterhub_data/
hadoop_namenode/
hadoop_datanode/
hadoop_historyserver/

# IDE
.idea/
.vscode/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```
