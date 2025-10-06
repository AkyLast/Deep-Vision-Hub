import pandas as pd
import json

with open("config.json", "r") as file:
    DATA = json.load(file)

LOGS_PATH = DATA["logs_path"]

def load():
    try:
        df = pd.read_excel(LOGS_PATH)
    except Exception as e:
        print("Arquivo de logs não encontrado.", e)
        df = pd.DataFrame(columns=["DATA", "ID_VAGA", "ESTACIONAMENTO", "STATUS"])
    return df

def registrar_log(id_vaga, parking, status):
    status = "Saiu" if status else "Estacionou"
    df = load()
    try:
        date = pd.Timestamp.now()
        date_format = date.strftime("%d/%m/%Y %H:%M:%S")

        new_log = {
            "DATA": date_format,
            "ID_VAGA": id_vaga,
            "ESTACIONAMENTO": parking,
            "STATUS": status
        }
        df.loc[len(df)] = new_log
        df.to_excel(LOGS_PATH, index=False)
    except Exception as e:
        print("Erro ao registrar o log novo:", e)

def clear():
    df = pd.DataFrame(columns=["DATA", "ID_VAGA", "ESTACIONAMENTO", "STATUS"])
    df.to_excel(LOGS_PATH, index=False)
