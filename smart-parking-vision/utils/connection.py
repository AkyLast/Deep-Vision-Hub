import requests

BASE_URL = "http://127.0.0.1:5000"
TIMEOUT = (5, 20)

def connect():
    try:
        resp = requests.get(BASE_URL, timeout=TIMEOUT)
        _print_response(resp)
        return resp
    except requests.exceptions.RequestException as e:
        print("Erro ao conectar:", e)

def set_parking(data, name):
    url = f"{BASE_URL}/parkings/set_AllSlot"
    data_temp = {"rois": data, "parking_name": name}
    try:
        resp = requests.post(url, json=data_temp, timeout=TIMEOUT)
        _print_response(resp)
        return resp
    except requests.exceptions.RequestException as e:
        print("Erro:", e)

def set_slotParking(data, name):
    url = f"{BASE_URL}/parkings/set_slot"
    data_temp = {"id_roi": data, "parking_name": name}
    try:
        resp = requests.post(url, json=data_temp, timeout=TIMEOUT)
        _print_response(resp)
        return resp
    except requests.exceptions.RequestException as e:
        print("Erro:", e)


def get_parking():
    url = f"{BASE_URL}/status-parking"
    try:
        resp = requests.get(url, timeout=TIMEOUT)
        _print_response(resp)
        return resp
    except requests.exceptions.RequestException as e:
        print("Erro:", e)

def update_parking(parking, vaga_id, status):
    url = f"{BASE_URL}/parking/{parking}/{vaga_id}"  
    data_temp = {"parking": parking, "id": vaga_id, "status": status}
    try:
        resp = requests.patch(url, json=data_temp, timeout=TIMEOUT)
        _print_response(resp)
        return resp
    except requests.exceptions.RequestException as e:
        print("Erro ao tentar atualizar a vaga:", e)


def _print_response(resp):
    print("Status:", resp.status_code)
    if "application/json" in resp.headers.get("Content-Type", ""):
        try:
            print("Resposta JSON:", resp.json())
        except Exception:
            print("⚠️ Erro ao converter JSON. Conteúdo bruto:", resp.text)
    else:
        print("Resposta (texto):", resp.text)
