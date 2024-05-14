from py_mongo.mongo_db_app import db

client_docs = [{
    "id_client"
    "name": "vitória",
    "cpf": "0202020",
    "address": "Rua Belém, 132",
    "id_account": "1",
    "type_account": "current_account",
    "agency_number": "100",
    "account_balance": 5000.00

},
    {
        "id_client"
        "name": "guilherme",
        "cpf": "44596321",
        "address": "Rua Domingos de Moraes, 132",
        "id_account": "2",
        "type_account": "current_account",
        "agency_number": "200",
        "account_balance": 8000.00

    }
]

client_doc = db.clients_data

client_docs_ids = client_doc.insert_many(client_docs).inserted_ids


