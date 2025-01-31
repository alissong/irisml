# Importa as bibliotecas necessárias
import argparse  # Biblioteca para análise de argumentos da linha de comando
from sklearn.datasets import load_iris  # Função para carregar o dataset Iris
from sklearn.model_selection import train_test_split  # Função para dividir os dados em treino e teste
from sklearn.ensemble import RandomForestClassifier  # Modelo de classificação RandomForest
import joblib  # Biblioteca para salvar e carregar o modelo treinado
import os  # Biblioteca para manipulação de caminhos de arquivos

def train_model(dataset, model_class, params, save_path):
    # Carrega dados (genérico para qualquer dataset do sklearn)
    data = load_iris()  
    X, y = data.data, data.target  
    
    # Treina modelo
    model = model_class(**params) 
    model.fit(X, y)  
    
    # Salva modelo
    os.makedirs(os.path.dirname(save_path), exist_ok=True)  
    joblib.dump(model, save_path)  
    print(f"Modelo salvo em {save_path}")  

if __name__ == "__main__":
    parser = argparse.ArgumentParser()  
    parser.add_argument("--model_class", type=str, default="RandomForestClassifier", help="Classe do modelo (ex: RandomForestClassifier)")  
    parser.add_argument("--save_path", type=str, default="models/iris_model.joblib", help="Caminho para salvar o modelo") 
    parser.add_argument("--params", type=str, default='{"n_estimators": 100, "random_state": 42}', help="Parâmetros do modelo em JSON")  
    args = parser.parse_args()  
    
    # Converte string JSON para dicionário
    import json
    params = json.loads(args.params)  
    
    # Mapeia classes de modelo
    from sklearn.ensemble import RandomForestClassifier  
    model_class = eval(args.model_class) 
    
    train_model(load_iris(), model_class, params, args.save_path)