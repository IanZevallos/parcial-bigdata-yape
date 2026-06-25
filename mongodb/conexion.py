from pymongo import MongoClient

# 🔵 1. URL de conexión (Atlas)
MONGO_URI = "mongodb+srv://<usuario>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority"

# 🔵 2. Conectar a MongoDB
client = MongoClient(MONGO_URI)

# 🔵 3. Crear/seleccionar base de datos
db = client["bigdata_s3_sunat"]

# 🔵 4. Crear colección
collection = db["empresas"]

print("✅ Conexión exitosa a MongoDB Atlas")
