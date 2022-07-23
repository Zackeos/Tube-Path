import sqlite3
import json

def dict_factory(cursor,row):
  d = {}
  for idx,col in enumerate(cursor.description):
    d[col[0]] = row[idx]
  return d

conn = sqlite3.connect("tube.db")
conn.row_factory = dict_factory
conn.execute("""CREATE TABLE IF NOT EXISTS stations (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            longitude DOUBLE NOT NULL,
            latitude DOUBLE NOT NULL
            )""")
conn.execute("""CREATE TABLE IF NOT EXISTS links (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            source_id INTEGER NOT NULL,
            destination_id INTEGER NOT NULL,
            distance INTEGER NOT NULL,
            line TEXT NOT NULL 
            )""")
conn.commit()

# with open('info.json') as json_file:
#     links = json.load(json_file)

# with open("Stations.txt","r") as f:
#   stations = f.readlines()
# stationyes = [station.strip().split("#") for station in stations]
# for s in range(len(stationyes)):
#   stationyes[s][1],stationyes[s][2] = float(stationyes[s][1]),float(stationyes[s][2]) 
# # print(stationyes)

# for x in stationyes:
#   conn.execute("INSERT INTO stations(name, longitude, latitude) VALUES (?,?,?)",[x[0], x[1], x[2]])
# conn.commit()
# for link in links:
#   source = link[0]
#   dest = link[1]
#   dist = link[2]
#   line = link[3]
#   conn.execute("INSERT INTO links(source_id,destination_id,distance,line) VALUES (?,?,?,?)",[source,dest,dist,line])
# conn.commit()
