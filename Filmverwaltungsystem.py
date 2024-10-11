# Dies ist ein CRUD Script um ein Filmverwaltungssystem zu erstelle
from test_mysql_connection import create_connection

# Funktion um einen Film hinzuzufügen
def add_movie():
    connection = create_connection()
    cursor = connection.cursor()
    title = input("Bitte gib den Film an den du zu deiner Liste hinzufügen willst\n")
    director = input("Wer war der Regisseur von dem Film?\n")
    genre = input("Welchem Genre gehört der Film an?\n")
    releaseyear = int(input("In welchem Jahr wurde der Film veröffentlicht?\n"))
    rating = float(input("Mit welchem Rating versiehst du den Film? Bitte gebe eine Nachkommazahl mit einem . als trennung an.\n"))
    cursor.execute('''
        INSERT INTO movies (title, director, genre, releaseyear, rating)
        VALUES (%s, %s, %s, %s, %s)
        ''', (title, director, genre, releaseyear, rating,))
    connection.commit()
    print(f"Der Film {title} vom Regisseur {director} aus dem Genre {genre} aus dem Jahr {releaseyear} wurde mit einer Wertung von {rating} deiner Filmsammlung hinzugefügt")
    cursor.close()
    connection.close()

# Funktion um die Filmliste anzuzeigen
def show_movies():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM movies')
    movielist = cursor.fetchall()
    for i in movielist:
        print(f"Nummer: {i[0]}, Titel: {i[1]}, Regisseur: {i[2]}, Genre: {i[3]}, Erscheinungsjahr: {i[4]}, Bewertung: {i[5]}")
    cursor.close()
    connection.close()

# Funktion um die Filmliste upzudaten
def update_movie():
    while True:
        show_movies()
        movie_id = input("Welchen Film möchten Sie updaten? Bitte gib die ID an.\n")
        print("----- Film Liste Updaten -----")
        print("1. Title")
        print("2. Director")
        print("3. Genre")
        print("4. Erscheinungsdatum")
        print("5. Rating")
        print("6. Alles")
        print("7. Updaten beenden")
        print("-----")
        choice = input("Was möchtest du Updaten?\n")

        if choice == "1":
            connection = create_connection()
            cursor = connection.cursor()
            new_title = input("Wie soll der neue Title heißen?\n")
            cursor.execute('''
                UPDATE movies SET title = %s WHERE id = %s
                ''', (new_title, movie_id))
            connection.commit()
            print(f"Der neue Titel vom Film mit der ID {movie_id} lautet {new_title}.")
            cursor.close()
            connection.close()
        
        elif choice == "2":
            connection = create_connection()
            cursor = connection.cursor()
            new_director = input("Wer ist der neue Director des Films?\n")
            cursor.execute('''
                UPDATE movies SET direcotr = %s WHERE id = %s
            ''', (new_director, movie_id))
            connection.commit()
            print(f"Sie haben Erfolgreich den Director vom Film mit der Nummer {movie_id} geändert in {new_director}.")
            cursor.close()
            connection.close()

        elif choice == "3":
            connection = create_connection()
            cursor = connection.cursor()
            new_genre = input("Wie lautet das neue Genre?\n")
            cursor.execute('''
                UPDATE movies SET genre = %s WHERE id = %s
            ''', (new_genre, movie_id))
            connection.commit()
            print(f"Sie haben Erfolgreich das Genre vom Film mit der Nummer {movie_id} geändert in {new_genre}.")
            cursor.close()
            connection.close()

        elif choice == "4":
            new_year = int(input("Wie lautet das neue Erscheinungsdatum?\n"))
            cursor.execute('''
                UPDATE movies SET releaseyear = %s WHERE id = %s
            ''', (new_year, movie_id))
            connection.commit()
            print(f"Sie haben Erfolgreich das Erscheinungsjahr vom Film mit der Nummer {movie_id} geändert in {new_year}.")
            cursor.close()
            connection.close()

        elif choice == "5":
            connection = create_connection()
            cursor = connection.cursor()
            new_rating = float(input("Wie hoch ist die neue Bewertung des Films?\n"))
            cursor.execute('''
                UPDATE movies SET rating = %s WHERE id = %s
            ''', (new_rating, movie_id))
            connection.commit()
            print(f"Sie haben Erfolgreich das Rating vom Film mit der Nummer {movie_id} geändert in {new_rating}.")
            cursor.close()
            connection.close()

        elif choice == "6":
            connection = create_connection()
            cursor = connection.cursor()
            new_title = input("Wie soll der Film nun heißen?\n")
            new_director = input("Wie soll die neue Director lauten?\n")
            new_genre = input("Wie lautet das neue Genre?\n")
            new_year = int(input("Wie lautet das neue Erscheinungsdatum?\n"))
            new_rating = float(input("Wie Stufen Sie den Film nun ein?\n"))
            cursor.execute('''
                UPDATE movies SET title = %s, director = %s, genre = %s, releaseyear = %s, rating = %s WHERE id = %s
            ''', (new_title, new_director, new_genre, new_year, new_rating, movie_id))
            connection.commit()
            cursor.close()
            connection.close()

        elif choice == "7":
            print("Das Update Programm wird beendet.")
            break

        else:
            print("Bitte wählen Sie nur zwischen 1, 2, 3, 4, 5, 6,  oder 7 aus.")

def delete_movie():
    connection = create_connection()
    cursor = connection.cursor()
    movie_name = input("Welchen Film möchtest du aus deiner Liste löschen? Bitte gib den Namen ein.\n")
    cursor.execute('''
        DELETE FROM movies WHERE name = %s
        ''', (movie_name))
    connection.commit()
    print(f"Der Film {movie_name} wurde aus deiner Filmliste entfernt.")
    cursor.close()
    connection.close()

def search_movie():
    kriterium = input("Nach welchem Kriterium möchtest du suchen?\n")
    wert = input("Nach was möchtest du Suchen?\n")
    connection = create_connection()
    cursor = connection.cursor()
    sql = f"SELECT * FROM movies WHERE {kriterium} = %s"
    cursor.execute(sql, (wert,))
    result = cursor.fetchall()
    for i in result:
        print(f"Nummer: {i[0]}, Titel: {i[1]}, Regisseur: {i[2]}, Genre: {i[3]}, Erscheinungsjahr: {i[4]}, Bewertung: {i[5]}")
    cursor.close()
    connection.close()

def main():
    while True:
        print("----- Dein Filmverwaltungsystem -----")
        print("1. Einen Film hinzufügen")
        print("2. Deine Filmliste anzeigen lassen")
        print("3. Deine Filmliste Aktualisieren (Updaten)")
        print("4. Einen Film aus deiner Liste löschen")
        print("5. Nach einem bestimmten Film suchen")
        print("6. Das Programm beenden")
        print("-----")
        choice = input("Was möchtest du tun?\n")

        if choice == "1":
            add_movie()

        elif choice == "2":
            show_movies()

        elif choice == "3":
            update_movie()

        elif choice == "4":
            delete_movie()

        elif choice == "5":
            search_movie()

        elif choice == "6":
            print("Das Programm wird beendet. Auf Wiedersehen!")
            break

        else:
            print("Bitte gib nur 1, 2, 3, 4, 5 oder 6 ein.")

if __name__ == "__main__":
    main()
