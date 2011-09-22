import sqlite3 as sqlite

def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value = '0'
    return float(value)

def createDbFromFile():
    conn = sqlite.connect('food.db')
    curs = conn.cursor()
    
    curs.execute('''
    CREATE TABLE food(
        id        TEXT    PRIMARY KEY,
        desc      TEXT,
        water     FLOAT,
        kcal      FLOAT,
        protein   FLOAT,
        fat       FLOAT,
        ash       FLOAT,
        carbs     FLOAT,
        fiber     FLOAT,
        sugar     FLOAT
    )
    ''')
    field_count=10
    
    query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'
    
    for line in open('ABBREV.txt'): #get a copy of this file from http://www.mediafire.com/?k658spp8bdpuayp
        fields = line.split('^')
        vals = [convert(f) for f in fields[:field_count]]
        curs.execute(query, vals)
        
    conn.commit()
    conn.close()
    
createDbFromFile()
