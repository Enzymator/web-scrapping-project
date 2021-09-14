from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os
import pymongo

app = Flask(__name__)
#app.config["MONGO_URI"] = "mongodb://localhost:27017/api_py"
#app.config["MONGO_URI"] = "mongodb://mongo/api_py"
# mongo_host = os.environ["MONGO_HOST"]
# mongo_port = os.environ["MONGO_PORT"]
# mongo_host = "localhost"
# mongo_port = "27017"

# app.config["MONGO_URI"] = f"mongodb://{mongo_host}:{mongo_port}/api_python"

# mongo = PyMongo(app)

myclient = pymongo.MongoClient("mongodb://localhost:27017/api_python")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


@app.route("/ajoutvol", methods=["POST"])
def ajouter_vol():
    # new_user = request.get_json()
    mydict = { "name": "John", "address": "Highway 37" }

    x = mycol.insert_one(mydict)
    return jsonify({'ok': True, 'message': 'user added'}), 200



@app.route("/", methods=["GET"])
def racince():
    return "Salut Esperance"


@app.route("/bonjour", methods=["GET"])
def bonjour():
    return "bonjour"




# @app.route("/ajoutvol", methods=["POST"])
# def ajouter_vol():
#     # new_user = request.get_json()
#     new_vol = {
#         "numero": "43"
#     }
#     mongo.db.demo.insert_one(new_vol)
#     return jsonify({'ok': True, 'message': 'user added'}), 200

# @app.route("/api/utilisateurs", methods=["GET"])
# def afficher_alluser():
#     results = []
#     for i in mongo.db.utilisateurs.find():
#         results.append({'nom' : i['nom'], 'prenom' : i['prenom']})
#     return jsonify({'result' : results})

# @app.route("/api/utilisateurs/nom/<nom>", methods=["GET"])
# def chercher_nom(nom):
#     results = []
#     for r in mongo.db.utilisateurs.find({"nom" : nom}):
#         results.append({'nom' : r['nom'], 'prenom' : r['prenom']})
#     return jsonify({'result' : results})

# @app.route("/api/utilisateurs/<id>", methods=["GET"])
# def chercher_id(id):
#     results = []
#     r = mongo.db.utilisateurs.find_one({"_id" : ObjectId(id)})
#     results.append({'nom' : r['nom'], 'prenom' : r['prenom']})
#     return jsonify({'result' : results})

# @app.route("/api/utilisateurs", methods=["POST"])
# def ajouter_utilisateur():
#     new_user = request.get_json()
#     mongo.db.utilisateurs.insert_one(new_user)
#     return jsonify({'ok': True, 'message': 'user added'}), 200
    

# @app.route("/api/utilisateurs/nom/<nom>", methods=["DELETE"])
# def supprimer_utilisateur(nom):
#     mongo.db.utilisateurs.delete_one({"nom": nom})
#     return jsonify({'ok': True, 'message': 'user deleted'}), 204

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

#"host="0.0.0.0" ouvre le localhost