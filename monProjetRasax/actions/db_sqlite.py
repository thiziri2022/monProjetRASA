import sqlite3
# ------------------------------------- Description -------------------------------------------
# Ce fichier python crée une base de donées via des rêquetes SQL grâce la bibliothèque Sqlite3
# Les fonctions permettent d'interagir avec la BDD et d'extraire des informations 
# Ces fonctions vont être appelée par des classes qui se trouvent dans actions.py
# ----------------------------------------------------------------------------------------------

# ------------------------------------- Base de données ----------------------------------------
# Fonction de création des tables de la BDD
def init_data():
 conn = sqlite3.connect('demo.db') 
 cursor = conn.cursor()
 print("Database created and Successfully Connected to SQLite")

# ------------------------------------- Table Schedule -------------------------------------------
 sql = "drop table if exists schedule;"
 cursor.execute(sql)

 sql="""CREATE TABLE schedule(
    section VARCHAR,
    grp VARCHAR,
    name VARCHAR,
    room VARCHAR,
    time VARCHAR
  )"""
 cursor.execute(sql)
 # Insertion des lignes dans la table schedule
 cursor.execute('''INSERT INTO schedule(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("M1","alternant","math","S2","11:00"))
 cursor.execute('''INSERT INTO schedule(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("M1","alternant","infra","S3","13:00"))
 cursor.execute('''INSERT INTO schedule(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("M1","classique","math","S2","11:00"))
 cursor.execute('''INSERT INTO schedule(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("M1","classique","web","S8","13:00"))
 cursor.execute('''INSERT INTO schedule(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("M2","alternant","IA","S5","11:00"))
 cursor.execute('''INSERT INTO schedule(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("M2","alternant","ingedoc","S7","13:00"))
 cursor.execute('''INSERT INTO schedule(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("M2","classique","anglais","S4","11:30"))
 cursor.execute('''INSERT INTO schedule(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("M2","classique","ecom","S6","13:30"))
 print("Table created successfully...")

# ------------------------------------- Table Room -------------------------------------------
 sql = "drop table if exists room;"
 cursor.execute(sql)

 sql="""CREATE TABLE room(
    location VARCHAR,
    nom_salle VARCHAR,
    jour VARCHAR,
    heure VARCHAR,
    cours VARCHAR

  )"""
 cursor.execute(sql)
 
 # Insertion des lignes dans la table Room
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours) VALUES (?, ?, ?, ?, ?)''', ("ceri","s1","sunday","11:00","web"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours) VALUES (?, ?, ?, ?, ?)''', ("ceri","s2","monday","13:00","security"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours) VALUES (?, ?, ?, ?, ?)''', ("ceri","s3","thursday","10:00","english"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours) VALUES (?, ?, ?, ?, ?)''', ("agrosciences","tp a119","sunday","13:00","Molecular biology"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours) VALUES (?, ?, ?, ?, ?)''', ("agrosciences","tp a118","monday","12:00","nutrissional aspects"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours) VALUES (?, ?, ?, ?, ?)''', ("agrosciences","tp a121","thursday","13:00","secondary metabolism"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours) VALUES (?, ?, ?, ?, ?)''', ("centre ville","101","sunday","8:30","public and digital services"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours) VALUES (?, ?, ?, ?, ?)''', ("centre ville","102","monday","14:30","robotization"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours) VALUES (?, ?, ?, ?, ?)''', ("centre ville","103","thursday","16:00","transformation of the world "))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours) VALUES (?, ?, ?, ?, ?)''', ("iut","gb salle 1","monday","13:30","business communication"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours) VALUES (?, ?, ?, ?, ?)''', ("iut","gb salle 2","sunday","11:30","sales basics"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours) VALUES (?, ?, ?, ?, ?)''', ("iut","gb salle 3","thursday","13:30","marketing"))
 print("Table created successfully...")

# ------------------------------------- Table Séries -------------------------------------------
 sql = "drop table if exists room;"
 cursor.execute(sql)

 sql="""CREATE TABLE room(
    location VARCHAR,
    nom_salle VARCHAR,
    jour VARCHAR,
    heure VARCHAR,
    cours VARCHAR,
    description VARCHAR

  )"""
 cursor.execute(sql)
 
 # Insertion des lignes dans la table
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours,description) VALUES (?, ?, ?, ?, ?, ?)''', ("ceri","s1","sunday","11:00 -> 13:00","web","dans 100 mètres au premier étage, à votre droite"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours,description) VALUES (?, ?, ?, ?, ?, ?)''', ("ceri","s2","monday","13:00 -> 16:00","security","dans le premier étage à votre gauche"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours,description) VALUES (?, ?, ?, ?, ?, ?)''', ("ceri","s3","thursday","10:00 -> 11:00 ","english","dans le premier étage au fond du couloir, à gauche"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours,description) VALUES (?, ?, ?, ?, ?, ?)''', ("agrosciences","tp a119","sunday","13:00 -> 15:00","Molecular biology","au fond du couloir du premier Hall, à votre droite"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours,description) VALUES (?, ?, ?, ?, ?, ?)''', ("agrosciences","tp a118","monday","12:00 -> 17:30 ","nutrissional aspects","en face de l'amphi Grand amphi"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours,description) VALUES (?, ?, ?, ?, ?, ?)''', ("agrosciences","tp a121","thursday","13:00 -> 16:00","secondary metabolism","au premier étage à votre gauche"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours,description) VALUES (?, ?, ?, ?, ?, ?)''', ("centre ville","101","sunday","8:30 -> 10:00","public and digital services","Premier étage à votre droite"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours,description) VALUES (?, ?, ?, ?, ?, ?)''', ("centre ville","102","monday","14:30 -> 17:30","robotization","Premier étage à votre gauche"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours,description) VALUES (?, ?, ?, ?, ?, ?)''', ("centre ville","103","thursday","16:00 -> 19:00","transformation of the world ","deuxieme étage, 50 mètres à votre gauche"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours,description) VALUES (?, ?, ?, ?, ?, ?)''', ("iut","gb salle 1","monday","13:30 -> 15:00","business communication","à gauche sur le même Hall de l'amphi Marie"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours,description) VALUES (?, ?, ?, ?, ?, ?)''', ("iut","gb salle 2","sunday","11:30 -> 13:00","sales basics","au fond du couloir du premier Hall, à votre droite"))
 cursor.execute('''INSERT INTO room(location,nom_salle,jour,heure,cours,description) VALUES (?, ?, ?, ?, ?, ?)''', ("iut","gb salle 3","thursday","13:30 -> 16:00","marketing","en face de l'amphi John McCarthy"))
 print("Table created successfully...")

# ------------------------------------- Table Enseignant -------------------------------------------
 sql = "drop table if exists Enseignant;"
 cursor.execute(sql)
 
 # Table Enseignant
 sql="""CREATE TABLE Enseignant(
    nom VARCHAR,
    mail VARCHAR,
    numero VARCHAR,
    cours VARCHAR
  )"""
 cursor.execute(sql)
 
 # Insertion statuses lignes statusans la table
 cursor.execute('''INSERT INTO Enseignant(nom,mail,numero,cours) VALUES (?, ?, ?, ?)''', ("Fabrice LEFEVRE","fabrice.lefevre@univ-avignon.fr","4507","Innovation"))
 cursor.execute('''INSERT INTO Enseignant(nom,mail,numero,cours) VALUES (?, ?, ?, ?)''', ("Romain RAFFIN","romain.raffin@univ-avignon.fr","3690","Multimédia"))
 cursor.execute('''INSERT INTO Enseignant(nom,mail,numero,cours) VALUES (?, ?, ?, ?)''', ("Yazekeal HAYEL","yazekeal.hayel@univ-avignon.fr","3498","Probabilités"))
 cursor.execute('''INSERT INTO Enseignant(nom,mail,numero,cours) VALUES (?, ?, ?, ?)''', ("Yannick ESTEVE","yannick.esteve@univ-avignon.fr","1209","Outil d'apprentissage"))
 cursor.execute('''INSERT INTO Enseignant(nom,mail,numero,cours) VALUES (?, ?, ?, ?)''', ("Corinne FREDOUILLE","corinne.fredouille@univ-avignon.fr","S7","Architecture WEB"))
 cursor.execute('''INSERT INTO Enseignant(nom,mail,numero,cours) VALUES (?, ?, ?, ?)''', ("Pierre JOURLIN","pierre.jourlin@univ-avignon.fr","3738","Assembleur"))
 cursor.execute('''INSERT INTO Enseignant(nom,mail,numero,cours) VALUES (?, ?, ?, ?)''', ("Damien JOURDAN","damien.jourdan@univ-avignon.fr","3634","Cloud"))
 cursor.execute('''INSERT INTO Enseignant(nom,mail,numero,cours) VALUES (?, ?, ?, ?)''', ("Zohra BELGAID","zohra.belgaid@alumni.univ-avignon.fr","2390","math"))
 print("Table create successfully...")

# ------------------------------------- Table Films -------------------------------------------
 sql_f = "drop table if exists films;"
 cursor.execute(sql_f)

 sql_f="""CREATE TABLE films(
    titre VARCHAR,
    categorie VARCHAR,
    realisateur VARCHAR,
    date_sortie VARCHAR
  )"""
 cursor.execute(sql_f)
 cursor.execute('''INSERT INTO films(titre,categorie,realisateur,date_sortie) VALUES (?, ?, ?, ?)''', ("Sherlock Holmes 3","enigme","Dexter Fletcher","22 december 2021"))
 cursor.execute('''INSERT INTO films(titre,categorie,realisateur,date_sortie) VALUES (?, ?, ?, ?)''', ("The Suicide Squad ","action","James Gunn","28 juillet 2021"))
 cursor.execute('''INSERT INTO films(titre,categorie,realisateur,date_sortie) VALUES (?, ?, ?, ?)''', ("The Last Duel","drama","Ridley Scott","13 octobre 2021"))
 cursor.execute('''INSERT INTO films(titre,categorie,realisateur,date_sortie) VALUES (?, ?, ?, ?)''', ("Stillwater ","drama"," Tom McCarthy"," 22 septembre 2021"))
 cursor.execute('''INSERT INTO films(titre,categorie,realisateur,date_sortie) VALUES (?, ?, ?, ?)''', ("Eiffel ","biopic","Martin Bourboulon ","13 octobre 2021"))
 cursor.execute('''INSERT INTO films(titre,categorie,realisateur,date_sortie) VALUES (?, ?, ?, ?)''', ("Avatar 2","aventure","James Cameron","12 decembre 2022"))
 cursor.execute('''INSERT INTO films(titre,categorie,realisateur,date_sortie) VALUES (?, ?, ?, ?)''', ("1984","science-fiction","Paul Greengrass","Ignored"))
 cursor.execute('''INSERT INTO films(titre,categorie,realisateur,date_sortie) VALUES (?, ?, ?, ?)''', ("Spider-Man: No Way Home","action","Jon Watts ","15 decembre 2021"))
 print("Table create successfully...")

# ------------------------------------- Table Séries -------------------------------------------
 sql_f = "drop table if exists series;"
 cursor.execute(sql_f)

 sql_f="""CREATE TABLE series(
    titre VARCHAR,
    categorie VARCHAR,
    nbr_saisons VARCHAR,
    nbr_episodes VARCHAR
  )"""
 cursor.execute(sql_f)
 cursor.execute('''INSERT INTO series(titre,categorie,nbr_saisons,nbr_episodes) VALUES (?, ?, ?, ?)''', ("maid","biopic","1","9"))
 cursor.execute('''INSERT INTO series(titre,categorie,nbr_saisons,nbr_episodes) VALUES (?, ?, ?, ?)''', ("how i meet your mother","comedy","7","168"))
 cursor.execute('''INSERT INTO series(titre,categorie,nbr_saisons,nbr_episodes) VALUES (?, ?, ?, ?)''', ("the original","action","4","92"))
 cursor.execute('''INSERT INTO series(titre,categorie,nbr_saisons,nbr_episodes) VALUES (?, ?, ?, ?)''', ("the good doctor","medical","5","83"))
 cursor.execute('''INSERT INTO series(titre,categorie,nbr_saisons,nbr_episodes) VALUES (?, ?, ?, ?)''', ("grey's anatomy","medical","18","388"))
 cursor.execute('''INSERT INTO series(titre,categorie,nbr_saisons,nbr_episodes) VALUES (?, ?, ?, ?)''', ("spinning out","Dance","1","12"))
 cursor.execute('''INSERT INTO series(titre,categorie,nbr_saisons,nbr_episodes) VALUES (?, ?, ?, ?)''', ("the office","comedy","9","201"))
 cursor.execute('''INSERT INTO series(titre,categorie,nbr_saisons,nbr_episodes) VALUES (?, ?, ?, ?)''', ("The Sinner","Action","4","32"))
 print("Table create successfully...")


# ------------------------------------- Table Méteo -------------------------------------------
 sql = "drop table if exists meteo;"
 cursor.execute(sql)

 sql_M = """CREATE TABLE meteo(
    jour VARCHAR,
    temp VARCHAR,
    temp_matin INT,
    temp_soir INT
  )"""
  
 cursor.execute(sql_M)
 cursor.execute('''INSERT INTO meteo(jour,temp,temp_matin,temp_soir) VALUES (?, ?, ?, ?)''', ("monday","rainy","14","3"))
 cursor.execute('''INSERT INTO meteo(jour,temp,temp_matin,temp_soir) VALUES (?, ?, ?, ?)''', ("tuesday","foggy","9","4"))
 cursor.execute('''INSERT INTO meteo(jour,temp,temp_matin,temp_soir) VALUES (?, ?, ?, ?)''', ("wendsday","foggy","9","4"))
 cursor.execute('''INSERT INTO meteo(jour,temp,temp_matin,temp_soir) VALUES (?, ?, ?, ?)''', ("thursday","cloudy","4","2"))
 cursor.execute('''INSERT INTO meteo(jour,temp,temp_matin,temp_soir) VALUES (?, ?, ?, ?)''', ("friday","sunny","17","13"))
 cursor.execute('''INSERT INTO meteo(jour,temp,temp_matin,temp_soir) VALUES (?, ?, ?, ?)''', ("saturday","foggy","9","4"))
 cursor.execute('''INSERT INTO meteo(jour,temp,temp_matin,temp_soir) VALUES (?, ?, ?, ?)''', ("sunday","sunny","18","14"))

 # Commit your changes in the database
 conn.commit()
 #Closing the connection
 conn.close()

# -------------------------------------------- Fonctions  --------------------------------------------------
def select_schedule(section,group):

  conn = sqlite3.connect('demo.db') 
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite")
 
  cursor.execute('''SELECT * FROM schedule WHERE section=? AND grp=?''',(section,group,))

  rows = cursor.fetchall()
  text =""
  for row in rows:
    print(row)
    text = row[2]+" in "+row[3]+" at "+row[4]

  #Closing the connection
  conn.close()
  
  return text


def select_enseignant_nom(nom,message):

  conn = sqlite3.connect('demo.db') 
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite")

  # Requete pour la séléction des informations de l'enseignant selon son nom
  cursor.execute('''SELECT * FROM Enseignant WHERE nom=? ''',(nom,))

  rows = cursor.fetchall()
  print(rows)

  text = list()
  ligne = ""
  addressMail = ""
  for row in rows:
    ligne = "L'addresse mail de l'enseignant "+row[0]+" est "+row[1]+", et son numéro de téléphone est le : "+row[2]+". Il enseigne le module "+row[3]
    # Liste de toutes les lignes
    text.append(ligne)
    addressMail = row[1]
  
  print (addressMail)
  sendMail(addressMail,message)

  conn.close()
  return text

def sendMail(addressMail,message):
  import smtplib
  from email.mime.multipart import MIMEMultipart
  from email.mime.text import MIMEText

  print(addressMail)
  print(message)
  msg = MIMEMultipart()
  msg['From'] = 'robot.nao@gmail.com'
  msg['To'] = addressMail
  msg['Subject'] = 'Message envoyé depuis NAO' 
  message = message
  msg.attach(MIMEText(message))
  mailserver = smtplib.SMTP('smtp.gmail.com', 587)
  mailserver.ehlo()
  mailserver.starttls()
  mailserver.ehlo()
  mailserver.login('robot.nao@gmail.com', 'aM3RmcrO67+kiMxod')
  mailserver.sendmail('robot.nao@gmail.com', addressMail, msg.as_string())
  mailserver.quit()

def select_enseignant_cours(cours):

  conn = sqlite3.connect('demo.db') 
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite")

  # Requete pour la séléction des informations de l'enseignant selon le cours
  cursor.execute('''SELECT * FROM Enseignant WHERE cours=? ''',(cours,))

  rows = cursor.fetchall()
  print(rows)

  text = list()
  ligne = ""
  for row in rows:
    ligne = "L'addresse mail de l'enseignant "+row[0]+" est "+row[1]+", et son numéro de téléphone est le : "+row[2]+". Il enseigne module "+row[3]
    # Liste de toutes les lignes
    text.append(ligne)
    #break

  #Closing the connection
  conn.close()
  
  return text


def select_films(categories):
  conn = sqlite3.connect('demo.db') 
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite")

  # Requete pour la séléction des films selon l'attribut "catégorie" donné
  cursor.execute('''SELECT * FROM films WHERE categorie=? ''',(categories,))

  rows = cursor.fetchall()
  print(rows)
  text = list()
  ligne = ""

  for row in rows:
    ligne = row[0]+" realized by "+row[2]
    text.append(ligne)

  #Closing the connection
  conn.close()
  return text

def select_films_by_rls(realisateur):
  conn = sqlite3.connect('demo.db') 
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite")

  cursor.execute('''SELECT * FROM films WHERE realisateur=? ''',(realisateur,))
  
  rows = cursor.fetchall()
  print(rows)

  text =""
  for row in rows:
    text=row[0]
    break

  #Closing the connection
  conn.close()
  return text

def select_serie(categorie):
  conn = sqlite3.connect('demo.db') 
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite")

  cursor.execute('''SELECT * FROM series WHERE categorie=? ''',(categorie,))
    
  rows = cursor.fetchall()
  print(rows)

  text =""
  for row in rows:
    text=row[0]
  #break

  #Closing the connection
  conn.close()
    
  return text

#nombre de saispon d'une serie donnée 
def select_nbr_saison(titre):
  conn = sqlite3.connect('demo.db') 
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite")

  cursor.execute('''SELECT * FROM series WHERE titre=? ''',(titre,))
    
  rows = cursor.fetchall()
  print(rows)

  text =""
  for row in rows:
    text=row[2]
    break

  #Closing the connection
  conn.close()
    
  return text

#Salle libre
def select_salle_libre(jour,heure,location):
  conn = sqlite3.connect('demo.db') 
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite")

  cursor.execute('''SELECT * FROM room WHERE jour=? AND heure=? AND location=? ''', (jour, heure,location))
    
  rows = cursor.fetchall()
  print(rows)

  text = ""
  for row in rows:
    text = "Les salles libres selon votre jour : " + row[2] + ", votre heure : " + row[3] + "et votre location : " + row[5]
    break

  #Closing the connection
  conn.close()
    
  return text

#Toutes les salles libres disponibles dans tous les sites
def select_salle_libre_site(jour):
  conn = sqlite3.connect('demo.db') 
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite")

  cursor.execute('''SELECT * FROM room WHERE jour=? ''',(jour,))
    
  rows = cursor.fetchall()
  print(rows)

  text =list()
  
  for row in rows:
    text.append(row[1])
  #Closing the connection
  conn.close()
    
  return text

# Fonction qui donne la météo
def select_weather(jour):
  conn = sqlite3.connect('demo.db') 
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite...")

  cursor.execute('''SELECT * FROM meteo WHERE jour=? ''',(jour,))
    
  rows = cursor.fetchall()
  print(rows)

  text = ""
  for row in rows:
    text = row[1]
    break

  #Closing the connection
  conn.close()
    
  return text

def print_data():

  conn = sqlite3.connect('demo.db') 
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite")
 
  cursor.execute('''SELECT * FROM series''')
  
  rows = cursor.fetchall()

  for row in rows:
    print(row)

  #Closing the connection
  conn.close()


# ------------------------------------- Phase Test ------------------------------------------------

if __name__ == "__main__":
 init_data()
 print("All data:")
 print_data()

 print(select_schedule("",""))

 print("Films selon categories")
 print(select_films("Action"))

 print("Films selon realisateurs")
 print(select_films_by_rls("James Gunn"))
 print("series are "+select_serie("action"))

 print("info ensiegnant selon le nom de l'enseignant")
 print(select_enseignant_nom("Zohra BELGAID","Hello"))

 print("info enseignant selon cours")
 print(select_enseignant_cours("Innovation"))

 print("Salle libre selon jour, heure et site :")
 print(select_salle_libre("sunday","11:00 -> 13:00","ceri"))

 print("Toutes les salles libres :")
 print(select_salle_libre_site("sunday"))
 
 print("Météo:")
 print(select_weather("sunday"))