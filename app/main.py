# Importa as bibliotecas necessárias
from fastapi import FastAPI  # Framework para construir APIs
from pydantic import BaseModel  # Biblioteca para validação de dados
import joblib  # Biblioteca para carregar o modelo treinado
import os  # Biblioteca para manipulação de caminhos de arquivos

# Cria a instância do FastAPI
app = FastAPI()

# Define o esquema de dados para a entrada da API
class IrisFeatures(BaseModel):
    sepal_length: float  
    sepal_width: float  
    petal_length: float  
    petal_width: float 

    # Exemplo de dados de entrada para a documentação da API
    class Config:
        schema_extra = {
            "example": {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2
            }
        }

# Carrega o modelo treinado
model_path = os.path.join(os.path.dirname(__file__), "models", "iris_model.joblib")  
model = joblib.load(model_path)  

# Endpoint para previsões
@app.post("/predict")
async def predict(features: IrisFeatures):
    # Converte os dados de entrada para o formato esperado pelo modelo
    data = [[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]]
    # Faz a previsão
    prediction = int(model.predict(data)[0])  
    return {"prediction": prediction}  

# Endpoint para informações sobre o modelo
@app.get("/model-info")
async def model_info():
    return {
        "model_type": str(type(model)),  
        "model_params": model.get_params()  
    }

# Endpoint de saúde (opcional, mas útil para monitoramento)
@app.get("/health")
async def health_check():
    return {"status": "healthy"}  