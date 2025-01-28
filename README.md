# ML Platform Test

This project is a machine learning platform for training and serving a model using FastAPI and Docker.

## Project Structure

```
.
├── app-ml
│   ├── app
│   │   ├── main.py
│   │   └── models
│   ├── train.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── docker-compose.yml
└── README.md
```

## Setup Instructions

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd ml-platform-test-master/app-ml
    ```

2. Build and run the Docker containers:
    ```sh
    docker-compose up --build
    ```

### Training the Model

The model is trained automatically when the Docker container starts. The training script is located in `train.py`.

### API Endpoints

Once the container is running, the FastAPI server will be available at `http://localhost:8000`. The following endpoints are available:

- `POST /predict`: Make a prediction using the trained model.
    - Request body:
        ```json
        {
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }
        ```
    - Response:
        ```json
        {
            "prediction": 0
        }
        ```

- `GET /model-info`: Get information about the trained model.
    - Response:
        ```json
        {
            "model_type": "<class 'sklearn.ensemble._forest.RandomForestClassifier'>",
            "model_params": {
                "bootstrap": true,
                "ccp_alpha": 0.0,
                "class_weight": null,
                "criterion": "gini",
                "max_depth": null,
                "max_features": "auto",
                "max_leaf_nodes": null,
                "max_samples": null,
                "min_impurity_decrease": 0.0,
                "min_samples_leaf": 1,
                "min_samples_split": 2,
                "min_weight_fraction_leaf": 0.0,
                "n_estimators": 100,
                "n_jobs": null,
                "oob_score": false,
                "random_state": 42,
                "verbose": 0,
                "warm_start": false
            }
        }
        ```

- `GET /health`: Health check endpoint.
    - Response:
        ```json
        {
            "status": "healthy"
        }
        ```

### Additional Information

- The model is saved in the `app/models` directory.
- The training script uses the Iris dataset from `sklearn.datasets`.
