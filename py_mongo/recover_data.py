import pymongo.collection
from py_mongo.mongo_db_app import db


def recover_all_docs(client_doc: pymongo.collection.Collection):
    """

    :param client_doc: objeto do tipo Collection

    :return: Retorna todos os documentos da Collection

    """
    for doc in client_doc.find():
        return doc


def recover_doc_by_key(key_and_value: dict):
    """
    :param key_and_value: {"chave": "valor"}

    :return: O primeiro elemento encontrado  contendo o valor

    """
    return db.clients_data.find_one(key_and_value)

