# Importa as bibliotecas necessárias
from fastapi import FastAPI, HTTPException  # Framework para construir APIs e exceções HTTP
from pydantic import BaseModel  # Biblioteca para validação de dados
import joblib  # Biblioteca para carregar o modelo treinado
import os  # Biblioteca para manipulação de caminhos de arquivos
import logging  # Biblioteca para logging

# Configura o logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
        json_schema_extra = {  # Updated from schema_extra to json_schema_extra
            "example": {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2
            }
        }

# Carrega o modelo treinado
model_path = "/app/models/iris_model.joblib"  # Update the model path
try:
    model = joblib.load(model_path)  
except Exception as e:
    model = None
    logger.error(f"Erro ao carregar o modelo: {e}")

# Endpoint para previsões
@app.post("/predict")
async def predict(features: IrisFeatures):
    logger.info("Recebendo dados para previsão")
    if model is None:
        logger.error("Modelo não carregado")
        raise HTTPException(status_code=500, detail="Modelo não carregado")
    try:
        # Converte os dados de entrada para o formato esperado pelo modelo
        data = [[
            features.sepal_length,
            features.sepal_width,
            features.petal_length,
            features.petal_width
        ]]
        # Faz a previsão
        prediction = int(model.predict(data)[0])
        logger.info(f"Previsão realizada com sucesso: {prediction}")
        return {"prediction": prediction}
    except Exception as e:
        logger.error(f"Erro ao fazer a previsão: {e}")
        raise HTTPException(status_code=400, detail=f"Erro ao fazer a previsão: {e}")

# Endpoint para informações sobre o modelo
@app.get("/model-info")
async def model_info():
    logger.info("Recebendo solicitação de informações do modelo")
    if model is None:
        logger.error("Modelo não carregado")
        raise HTTPException(status_code=500, detail="Modelo não carregado")
    try:
        model_info = {
            "model_type": str(type(model)),
            "model_params": model.get_params()
        }
        logger.info(f"Informações do modelo retornadas com sucesso: {model_info}")
        return model_info
    except Exception as e:
        logger.error(f"Erro ao obter informações do modelo: {e}")
        raise HTTPException(status_code=400, detail=f"Erro ao obter informações do modelo: {e}")

# Endpoint de saúde (opcional, mas útil para monitoramento)
@app.get("/health")
async def health_check():
    logger.info("Recebendo solicitação de verificação de saúde")
    return {"status": "healthy"}

# Endpoint para obter a versão da API
@app.get("/version")
async def get_version():
    logger.info("Recebendo solicitação de versão da API")
    return {"version": "1.0.1"}  # Atualize a versão conforme necessário