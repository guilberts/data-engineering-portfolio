# ETL with PySpark (Simulation)

This project demonstrates a simplified **ETL pipeline** simulating an AWS Job using **PySpark**.  
It processes a small public dataset of movies, applies transformations, and writes results in **Parquet** format.

---

## ETL Steps
1. **Extract**: Load raw CSV dataset (`movies.csv`).  
2. **Transform**: Filter movies released after 2000 and enrich data with a rating category.  
3. **Load**: Save transformed output as Parquet (simulating S3/Glue Data Catalog).  

---

## 🗂 Project Structure
```sh
└── etl-pyspark-simulation/
    ├── README.md
    ├── data
    │   └── source
    ├── etl_job.py
    ├── requirements.txt
    └── tests
        ├── __pycache__
        └── test_etl.py


## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip

### Installation

Build etl-pyspark-simulation from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone ../etl-pyspark-simulation
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd etl-pyspark-simulation
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![pip][pip-shield]][pip-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [pip-shield]: https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white -->
	<!-- [pip-link]: https://pypi.org/project/pip/ -->

	**Using [pip](https://pypi.org/project/pip/):**

	```sh
	❯ pip install -r requirements.txt
	```

### Usage

Run the project with:

**Using [pip](https://pypi.org/project/pip/):**
```sh
python {entrypoint}
```

### Testing

Etl-pyspark-simulation uses the {__test_framework__} test framework. Run the test suite with:

**Using [pip](https://pypi.org/project/pip/):**
```sh
pytest
```

---

## Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---
