import sqlite3
import turtle
import math
turtle.speed(0)

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

linescolors = {"Bakerloo":"#613113","Central":"#ff0000","Waterloo and City":"#7dd4ca","Victoria":"#00b2d1","Piccadilly":"#0926e3","Northern":"#000000","Metropolitan":"#611324","Jubilee":"#787878","Hammersmith and City":"#eda4dd","District":"#105c15","Docklands Light Railway":"#00b597","Circle":"#ffee00","Overground":"#ff8000"}

def getCoordinates(long,lat):
  dx = (-0.11748465009407572-long)*40000*math.cos((51.51389243681303+lat)*math.pi/360)/360
  dy = (51.51389243681303-lat)*40000/360
  return ((dy*-1)*15+86068.96608379924,(dx*-1)*15-77534.08586146026)
  
def draw(coordinate1,coordinate2,color):
  turtle.color(color)
  turtle.penup()
  turtle.goto(coordinate1)
  turtle.pendown()
  turtle.circle(5)
  turtle.goto(coordinate2)
  turtle.circle(5)

def drawLine(lineName):
  links = conn.execute("SELECT source_id,destination_id FROM links WHERE line = ?",[lineName]).fetchall()
  for link in links:
    coordinatesStart = conn.execute("SELECT latitude,longitude FROM stations WHERE id = ?", [link["source_id"]]).fetchone()
    coordinatesEnd = conn.execute("SELECT latitude,longitude FROM stations WHERE id = ?", [link["destination_id"]]).fetchone()
    draw(getCoordinates(coordinatesStart["longitude"],coordinatesStart["latitude"]),getCoordinates(coordinatesEnd["longitude"],coordinatesEnd["latitude"]),linescolors[lineName])



for key in linescolors:
  drawLine(key)

# drawLine("Northern")