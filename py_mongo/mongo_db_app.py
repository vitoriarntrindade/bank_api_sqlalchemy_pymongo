import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://vitoriarntrindade:Never.comes1@cluster0.2fufudf.mongodb.net/?retryWrites=true"
                         "&w=majority&appName=Cluster0")

db = client.bank

