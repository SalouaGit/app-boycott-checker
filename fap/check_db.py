import sqlite3

# Chemin de la base de données
db_path = '/var/www/fap/fap/products.db'

# Se connecter à la base de données
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Vérifier les données
c.execute("SELECT name, boycotted, description FROM products")
rows = c.fetchall()

# Afficher les données
for row in rows:
    print(f"Product: {row[0]}, Boycotted: {row[1]}, Description: {row[2]}")

conn.close()

