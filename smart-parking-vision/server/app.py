from flask import Flask, jsonify, request
from utils.biuld import config_parking

app = Flask(__name__)

parking = []
status_parking = []

@app.route("/")
def home():
    status = {
        "Status": "Rodando",
        "Rotas": "TESTE"
    }
    return jsonify(status)

@app.route("/parkings/set_AllSlot", methods = ["POST"])
def create_parking():
    data = request.json
    rois, parking_name = data["rois"], data["parking_name"]
    for parking_i in parking:
        if parking_i.get(parking_name, 0):
            return {"mensagem": "Já Existe estacionameto com esse nom", "Parking": parking_name}, 400
    else:
        vagas = {
            parking_name: [
                {"id": i["id_roi"], "status": "Manitoring"}  
                for i in rois
            ]
        }
        parking.append(vagas)
        data, status_update = config_parking(status_parking, parking, force = True)
        if status_update:
            status_parking.extend(data)
    return {"mensagem": "Vagas criadas", "Dados": vagas}, 201

@app.route("/parkings/set_slot", methods = ["POST"])
def set_slot():
    data = request.json
    id_roi, parking_name = data["id_roi"], data["parking_name"]
    vagas = {
        parking_name: [
            {"id": id_roi, "status": "Manitoring"} 
        ]
    }
    parking.append(vagas)
    return {"mensagem": "Vagas criadas", "Dados": vagas}, 201

@app.route("/search-parking", methods = ["GET"])
def search():
    return jsonify(parking)

@app.route("/status-parking", methods = ["GET"])
def get_parking():
    data, status_update = config_parking(status_parking, parking)
    if status_update:
        status_parking.extend(data)
    return jsonify(status_parking)

@app.route("/parking/<parking>/<int:vaga_id>", methods=["PATCH"])
def atualizar_vaga(parking, vaga_id):
    data = request.json
    novo_status = data.get("status")
    print(data)
    print("Array:", status_parking)
    for vaga in status_parking:
        print(vaga)
        if vaga["parking"] == parking and vaga["id"] == vaga_id:
            vaga["status"] = novo_status
            return jsonify({"msg": "Vaga atualizada", "vaga": vaga})

    return jsonify({"error": "Vaga não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)

