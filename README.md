# Filmeverwaltung
## Dies ist ein Script in Python das dazu dient die eigene Filme Sammlung in einer Datenbank zu speichern

Was genau benötigt wird um das Script auszuführen ist in der requirements.txt aufgeführt.
Außerdem benötigt man eine Datenbank auf die man zugreifen kann.
____

### Datenbank Verbindung

Damit das Programm richtig läuft muss eine Datenbank Verbindung herstellt werden. Die Daten der Datenbank Verbindung können unter Linux in die .bashrc geschrieben werden im Home verzeichniss oder unter Windows als Globale Enviroment Variable gespeichert werden.
Alternativ können auch die Werte SQLIP, SQLUsername, SQLPassword und SQLDatabase mit den entsprechenden Daten verändert werden.

Das Script öffnen könnt ihr unter Linux mit einem Konsolen Befehl ```python test_mysql_connection```

Das Script für die Datenbank Verbindung sieht wie folgt aus:
```python
import mysql.connector
import os

SQLIP = str(os.environ["SQLIP"])
SQLUsername = str(os.environ['SQL_USERNAME'])
SQLPassword = str(os.environ['SQL_PASSWORD'])
SQLDatabase = str(os.environ['SQL_DATABASE'])

def create_connection():
    connection = mysql.connector.connect(
host=SQLIP,
user=SQLUsername,
password=SQLPassword,
database=SQLDatabase # ggf. anpassen
)
    return connection

try:
    conn = create_connection()
    print("Verbindung zur MySQL-Datenbank Erfolgreich")
    conn.close()
except mysql.connector.Error as err:
    print(f"Fehler: {err}")
```

### Enviroment Variables

Wie man die Enviroment Variablen setzen kann, ist sonst auch in der env_variables.sh zu sehen.
Dieses Script kann man mithilfe von ```vim env_variables.sh``` öffnen.
Um es ausführbar zu machen muss man sonst die Datei Berechtigung unter Linux ändern mithilfe ```chmod 744 env_variables.sh```

Das Script von env_variables.sh ist wie folgt:
```bash
#!/bin/bash
export SQLIP="172.18.87.187"
export SQL_USERNAME="python-admin"
export SQL_PASSWORD="Kekse1234!"
export SQL_DATABASE="Filmverwaltungsystem"
echo $SQLIP
echo $SQL_USERNAME
echo $SQL_PASSWORD
echo $SQL_DATABASE
```
