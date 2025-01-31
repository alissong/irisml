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

## Application Description

This application provides a platform for training and serving a machine learning model using FastAPI and Docker. The model used in this example is a RandomForestClassifier trained on the Iris dataset from `sklearn.datasets`.

### Components

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **Docker**: A platform for developing, shipping, and running applications inside containers.
- **Scikit-learn**: A machine learning library for Python that provides simple and efficient tools for data mining and data analysis.

### Model Description

The model used in this application is a RandomForestClassifier from the `sklearn.ensemble` module. It is trained on the Iris dataset, which is a classic dataset in the field of machine learning. The dataset contains 150 samples of iris flowers, each with four features: sepal length, sepal width, petal length, and petal width. The goal is to classify the samples into three species of iris flowers: setosa, versicolor, and virginica.

## Setup Instructions

### Prerequisites

- Docker
- Docker Compose
- AWS Account with ECR (Elastic Container Registry) setup

### Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd ml-platform-test-master/app-ml
    ```

2. Configure the following GitHub secrets in your repository settings:
    - `AWS_ACCESS_KEY_ID`: Your AWS access key ID.
    - `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key.
    - `AWS_ACCOUNT_ID`: Your AWS account ID.
    - `IMAGE_URI`: The URI for your Docker image in ECR.

3. Build and run the Docker containers:
    ```sh
    docker-compose up --build
    ```

### Running the Container

You have two options to run the container:

1. **Locally**:
    ```sh
    docker-compose up --build
    ```

2. **Via ECR**:
    - Provision the infrastructure using Terraform from this repository: [infra-iris-ml](https://github.com/alissong/infra-iris-ml)
    - Push the Docker image to ECR and deploy to ECS as described in the CI/CD pipeline.

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

- `GET /version`: Get the current version of the API.
    - Response:
        ```json
        {
            "version": "1.0.1"
        }
        ```

### Additional Information

- The model is saved in the `app/models` directory.
- The training script uses the Iris dataset from `sklearn.datasets`.


### Contributing

We welcome contributions to this project! If you have any suggestions or improvements, please feel free to submit a pull request or open an issue. We encourage you to follow the best practices of the community when contributing.
