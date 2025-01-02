# Hadoop Docker Cluster

A production-ready Hadoop cluster using Docker containers, supporting various Hadoop components and easy deployment.

## Overview

This project provides a Docker-based environment with the following components:

### Hadoop Ecosystem
- Namenode
- Datanode
- Resource Manager
- Node Manager
- History Server

### Apache Spark
- Spark Master
- 2 Spark Workers
- Spark History Server

### Development Environment
- JupyterHub with PySpark support

## Prerequisites

- Docker Engine
- Docker Compose
- Make (optional, for running example jobs)

## Quick Start

### Using Docker Compose

1. Start the cluster:
```bash
docker-compose up -d
```

2. Run the example wordcount job:
```bash
make wordcount
```

### Using Docker Swarm

Deploy the cluster in swarm mode:
```bash
docker stack deploy -c docker-compose-v3.yml hadoop
```

## Accessing Web Interfaces

After deployment, the following web interfaces are available:

### Hadoop Services
| Service | URL | Description |
|---------|-----|-------------|
| Namenode | `http://localhost:9870` | HDFS management and overview |
| Resource Manager | `http://localhost:8088` | YARN resource management |
| History Server | `http://localhost:8188` | MapReduce job history |
| Datanode | `http://localhost:9864` | Individual datanode information |
| Node Manager | `http://localhost:8042` | YARN node management |

### Spark Services
| Service | URL | Description |
|---------|-----|-------------|
| Spark Master | `http://localhost:8080` | Spark master web UI |
| Spark Worker 1 | `http://localhost:8081` | First worker node |
| Spark Worker 2 | `http://localhost:8082` | Second worker node |
| Spark History Server | `http://localhost:18081` | Spark job history |

### Development Environment
| Service | URL | Description |
|---------|-----|-------------|
| JupyterHub | `http://localhost:8000` | Web-based Python/Spark development environment |

## Configuration

### Environment Variables

Configuration is managed through environment variables in `hadoop.env`. The system supports configuration for various Hadoop components:

- Core configurations (`CORE_CONF_*`)
- HDFS configurations (`HDFS_CONF_*`)
- YARN configurations (`YARN_CONF_*`)
- MapRed configurations (`MAPRED_CONF_*`)

Example configuration:
```
CORE_CONF_fs_defaultFS=hdfs://namenode:8020
YARN_CONF_yarn_log___aggregation___enable=true
```

### Spark Configuration

Spark is configured with the following settings:
- Master URL: `spark://spark-master:7077`
- 2 worker nodes
- History server for job monitoring
- Integrated with HDFS for storage

### JupyterHub Configuration

JupyterHub is configured with:
- PySpark integration
- Direct connection to Spark master
- HDFS access
- Persistent storage for notebooks in `./DAC` directory

### Configuration Files

The environment variables map to these configuration files:
- `/etc/hadoop/core-site.xml`
- `/etc/hadoop/hdfs-site.xml`
- `/etc/hadoop/yarn-site.xml`
- `/etc/hadoop/mapred-site.xml`
- `/etc/hadoop/httpfs-site.xml`
- `/etc/hadoop/kms-site.xml`

## Notes

- For special characters in configuration parameters, use triple underscores. Example: `yarn_log___aggregation___enable` translates to `yarn.log-aggregation-enable`
- The cluster uses `wait_for_it` script to ensure proper startup sequence
- All services run in separate containers for better isolation and scalability
- Spark workers automatically connect to the Spark master
- JupyterHub data is persisted in the specified volumes

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is licensed under the MIT License.

## Project Structure

```
.
├── base/                  # Base Hadoop configuration
├── datanode/             # Datanode service configuration
├── namenode/             # Namenode service configuration
├── historyserver/        # History server configuration
├── resourcemanager/      # Resource manager configuration
├── nodemanager/          # Node manager configuration
├── DAC/                  # JupyterHub notebooks directory
├── data/                 # Data directory for HDFS
├── jupyterhub_config/    # JupyterHub configuration
├── jupyterhub_data/      # JupyterHub data
├── docker-compose.yml    # Main compose file
├── hadoop.env           # Hadoop environment variables
└── README.md            # This file
```

## Ignored Files and Directories

The following files and directories are ignored by Git:

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
