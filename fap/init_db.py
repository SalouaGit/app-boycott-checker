import sqlite3

# Chemin de la base de données
db_path = '/var/www/fap/fap/products.db'

# Se connecter à la base de données (ou la créer si elle n'existe pas)
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Créer la table products si elle n'existe pas déjà
c.execute('''
    CREATE TABLE IF NOT EXISTS products (
        name TEXT PRIMARY KEY,
        boycotted BOOLEAN,
        description TEXT
    )
''')

# Insérer des données initiales
initial_data = [
    ('coca cola', 1, 'An iconic carbonated beverage produced by The Coca-Cola Company. It comes in various variants and is popular worldwide.'),
    ('pepsi', 1, 'Pepsi is a major brand of carbonated beverages, competing with Coca-Cola. It is produced by PepsiCo and includes a range of flavors and products similar to Coca-Cola.'),
    ('aquafina', 1, 'A bottled water brand owned by PepsiCo. It\'s known for its purification process and global distribution.'),
    ('unilever', 1, 'A British-Dutch multinational company specializing in consumer goods, including food, beverages, personal care products, and household cleaning products.'),
    ('avon', 1, 'A direct selling company for beauty products, including makeup, skincare, and fragrances.'),
    ('laiko', 0, 'Laïko is a carbonated beverage available in a 1.5L size, distributed by Aswak Drive, offering various flavors including apple. It can be purchased online and picked up within an hour.'),
    ('glass', 0, 'Glass is a 100% Moroccan carbonated drink known for its delicious flavors and affordability, ensuring great taste and refreshment.'),
    ('sidi ali', 0, 'A Moroccan mineral water brand known for its purity and quality.'),
    ('isdin', 0, 'A Spanish company specializing in dermatological products and skincare. They offer a range of products for treating and preventing skin issues.')
]

c.executemany('INSERT OR IGNORE INTO products (name, boycotted, description) VALUES (?, ?, ?)', initial_data)

# Sauvegarder les modifications et fermer la connexion
conn.commit()
conn.close()

print(f"Base de données initialisée à {db_path}")
