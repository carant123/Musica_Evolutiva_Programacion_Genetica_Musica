
from __future__ import print_function
from sqlite3 import connect

# Replace username with your own A2 Hosting account username:
conn = connect('test.db')
curs = conn.cursor()

curs.execute("SELECT * FROM evolutions;")
for population_size in curs.fetchall():
    print(population_size)

conn.close()