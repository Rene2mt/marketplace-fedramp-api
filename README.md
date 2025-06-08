# FedRAMP Marketplace API

This project provides a FastAPI-based web API for accessing information about cloud service offerings (CSOs) listed in the [FedRAMP Marketplace](https://marketplace.fedramp.gov/). The API fetches and serves live data from the official FedRAMP marketplace JSON source, allowing users to query products, retrieve product details, and check authorization status.

## Purpose

The goal of this app is to make it easy for developers and organizations to programmatically access up-to-date FedRAMP marketplace data, enabling integration with other tools, dashboards, or automation workflows.

---

## Setup Instructions

This project is designed to run in a Dev Container for a consistent development environment.

### Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop) installed on your machine.
- [Visual Studio Code](https://code.visualstudio.com/) with the following extensions:
  - [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
  - [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

### Getting Started

1. **Open the Project in VS Code**
   - Open the folder containing this repository in VS Code.

2. **Reopen in Dev Container**
   - Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`).
   - Run the command: `Dev Container: Reopen in Container`.

3. **Install Python Dependencies**
   - The dev container will automatically install dependencies listed in `requirements.txt` (if present).
   - If you add new dependencies, run:
     ```sh
     pip3 install -r requirements.txt
     ```

4. **Run the Application**
   - Start the FastAPI app using the Run and Debug view or by pressing `F5`.
   - Alternatively, run:
     ```sh
     uvicorn main:app --reload
     ```
   - The API will be available at `http://localhost:5000`.

---

## API Endpoints & Examples

### 1. Root Endpoint

- **GET /**  
  Returns a welcome message.

  **Example:**

    curl -X 'GET' \
    'http://localhost:5000/' \
    -H 'accept: application/json'

  **Response:**

    {
      "message": "Welcome to the FedRAMP Marketplace API. Available endpoints: /products, /products/{id}, /status/{id}."
    }

### 2. Get All Products

- **GET /products**  
  Retrieves a list of all products in the FedRAMP Marketplace.

  **Example:**

    curl -X 'GET' \
    'http://localhost:5000/products' \
    -H 'accept: application/json'

  **Response:**

    [
      {
        "id": "123",
        "name": "Product A",
        "provider": "Provider X",
        "status": "Active"
      },
      {
        "id": "456",
        "name": "Product B",
        "provider": "Provider Y",
        "status": "Inactive"
      }
    ]

### 3. Get Product Details

- **GET /products/{id}**  
  Retrieves detailed information about a specific product.

  **Example:**

    curl -X 'GET' \
    'http://localhost:5000/products/123' \
    -H 'accept: application/json'

  **Response:**

    {
      "id": "123",
      "name": "Product A",
      "provider": "Provider X",
      "status": "Active",
      "description": "Detailed description of Product A.",
      "documentation": "URL to product documentation."
    }

### 4. Check Authorization Status

- **GET /status/{id}**  
  Checks the authorization status of a specific product.

  **Example:**

    curl -X 'GET' \
    'http://localhost:5000/status/123' \
    -H 'accept: application/json'

  **Response:**

    {
      "id": "123",
      "status": "Authorized",
      "last_updated": "2023-10-01"
    }

---

## Development Notes

- This project uses [FastAPI](https://fastapi.tiangolo.com/) for the web framework.
- Data is fetched from the FedRAMP Marketplace JSON source and cached for performance.
- Automatic testing is set up using [pytest](https://pytest.org/).

### Running Tests

To run the tests for this project, use the following command:

```sh
pytest
```

### Code Formatting

Code formatting is enforced using [Black](https://black.readthedocs.io/en/stable/). To format the code, run:

```sh
black .
```

### Linting

Linting is performed using [Flake8](https://flake8.pycqa.org/en/latest/). To lint the code, run:

```sh
flake8 .
```

---

## Troubleshooting

- If you encounter issues with dependencies, ensure that you have the correct version of Python installed (3.8 or later).
- For Docker-related issues, ensure that Docker is running and you have enough resources allocated (CPU, memory).
- If the API does not start, check the output logs for any error messages and resolve the issues accordingly.

---

## Acknowledgements

- This project is inspired by the need for transparent and accessible information about cloud services in the FedRAMP Marketplace.
- Special thanks to the contributors and the open-source community for their valuable tools and libraries.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
