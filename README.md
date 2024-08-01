
## Description

The `escape-room-lab` project is designed to assist with prepping. This project uses Docker to manage its environment and dependencies, ensuring consistency across different setups.

## Directory Structure

- **Dockerfile**: Contains the instructions to build the Docker image for the project.
- **docker-compose.yml**: Docker Compose file to define and run multi-container Docker applications.
- **README.md**: The main documentation file for the project.
- **data/**: Directory containing data files.
  - **data.csv**
  - **data2.csv** 
- **scripts/**: Directory containing Python scripts for data manipulation.
  - **data_copy.py**: Script to copy data csv files data_copy.py does.
  - **postgres_data_manipulation.py**: Script for postgres_data_manipulation.py does.

## Setup

1. Clone the repository:
    ```bash
    git clone [repository URL]
    cd escape-room-lab
    ```

2. Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```

## Usage

Follow pdf

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.
