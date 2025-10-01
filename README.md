## 🚀 ETL with PySpark (Simulation)

This project demonstrates a **simplified ETL** pipeline simulating an AWS job using **PySpark**.  
It processes a small public movie dataset, applies transformations, and writes the results in **Parquet** format.

---

## 📌 ETL Steps
1. **Extract** → Load the raw dataset in CSV format (`movies.csv`).  
2. **Transform** → Filter movies released after 2000 and enrich the data with a rating category.  
3. **Load** → Save the transformed output in Parquet format (simulating S3/Glue Data Catalog).

---

## 🗂 Estrutura do Projeto

```sh
etl-pyspark-simulation/
├── README.md
├── data
│   └── source
├── etl_job.py
├── requirements.txt
└── tests
    ├── __pycache__/
    └── test_etl.py
```
### Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip

### Installation

Build etl-pyspark-simulation from the source and install dependencies:

1. **Clone the repository:**
   ```sh
   ❯ git clone ../etl-pyspark-simulation
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd etl-pyspark-simulation
    ```

3. **Install the dependencies:**

    ```sh
    ❯ pip install -r requirements.txt
    ```

### Usage

Run the project with:

**Using:**
```sh
python {entrypoint}
```

### Testing:

Etl-pyspark-simulation uses the {__test_framework__} test framework. Run the test suite with:

**Using:**

```sh
pytest
```
