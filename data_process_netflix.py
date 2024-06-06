import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv("netflix_data.csv")

genre = netflix_df['genre'].fillna('Uncategorized').tolist()

    # Définir les genre les plus populaires de Netflix grace à un histogramme
# Dictionnaire pour stocker le nombre de productions dans chaque genre
genre_nb = {}
for g in genre:
    if g in genre_nb:
        genre_nb[g] += 1
    else:
        genre_nb[g] = 1

# Convertir le dictionnaire en deux listes pour l'affichage
genres = list(genre_nb.keys())
nb = list(genre_nb.values())

# Histogramme des genres
plt.barh(genres, nb, color='skyblue')
plt.xlabel('Nombre de productions')
plt.ylabel('Genres')
plt.title('Répartition des genres sur Netflix')
plt.show()
plt.barh(genres, nb, color='skyblue')
plt.xlabel('Nombre de productions [Attention échelle logarithmique !]')
plt.ylabel('Genres')
plt.title('Répartition des genres sur Netflix')
plt.xscale('log')
plt.xticks([1,10,100,1000], ['1','10','100','1000'])
plt.show()

    #Parmi les genres les plus populaires certains sont ils plus liés à certaines époques ?

genre_populaire = []
for g in genre_nb:
    if genre_nb[g] > 300:
        genre_populaire.append(g)

annee = netflix_df['release_year'].fillna('Unknown').tolist()

#Dictionnaire de décompte des productions par genre par année
nb_genre_par_annee = {}
for i, a in enumerate(annee):
    if genre[i] in genre_populaire:
        if a not in nb_genre_par_annee.keys():
            nb_genre_par_annee[a] = []
            for g in genre_populaire:
                nb_genre_par_annee[a].append(g)
                nb_genre_par_annee[a].append(0)
        elif a in nb_genre_par_annee.keys():
            if genre[i] in nb_genre_par_annee[a]:         
                nb_genre_par_annee[a][int(nb_genre_par_annee[a].index(str(genre[i])))+1] +=1

#convertir le dictionnaire en DataFrame pour préparer le graphique
genre_par_annee_df = pd.DataFrame.from_dict(nb_genre_par_annee, orient='index', columns=[
    'Dramas', 'Dramas_nb', 'Action', 'Action_nb', 'Documentaries', 'Documentaries_nb',
    'Comedies', 'Comedies_nb', 'Children', 'Children_nb'])
sort = genre_par_annee_df.sort_index()
genre_par_annee_df = sort[['Dramas_nb', 'Action_nb', 'Documentaries_nb', 'Comedies_nb', 'Children_nb']]


#une liste de couleurs : dramas, action, documentaries, comedies, children
colors = ['grey', 'red', 'green', 'blue', 'yellow']


#Graphique en barres empilées
genre_par_annee_df.plot(kind='bar', stacked=True, color=colors)
plt.xlabel('Année')
plt.ylabel('Nombre de productions')
plt.title('Nombre de productions par genre par année en ligne sur Netflix')
plt.legend(['Drames', 'Action', 'Documentaires', 'Comédies', 'Pour les enfants'], loc='upper left')
plt.show()
