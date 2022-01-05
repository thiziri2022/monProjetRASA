# ------------------------------------- Description-------------------------------------------
# Après chaque message utilisateur. le modèle prédit une action que l'assistant doit effectuer.
# Ce fichier a été implementé à l'aide de https://rasa.com/docs/rasa/custom-actions
# --------------------------------------------------------------------------------------------

# ------------------------------------- Imports -------------------------------------------
from typing import Any, Text, Dict, List
# Tracker : maintient l'état du dialogue, représenté sous la forme d'un objet JSON répertoriant les événements de la session en cours.
from rasa_sdk import Action, Tracker 
from rasa_sdk.executor import CollectingDispatcher
import  actions.db_sqlite as db_sqlite
# -----------------------------------------------------------------------------------------

# --------------------------------------- Class -------------------------------------------
#Action qui recurére le planning de la section et du groupe 
class ActionSchedule(Action):

     def name(self) -> Text:
         return "action_schedule"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        section = tracker.get_slot('section')
        group = tracker.get_slot('group')

        print(db_sqlite.select_schedule(tracker.get_slot("section"),tracker.get_slot("group")))
        if (db_sqlite.select_schedule(tracker.get_slot("section"),tracker.get_slot("group"))==""):
                text="You have nothing then have fun ^_^"
        else:
                text="Your next schedule is {}".format(db_sqlite.select_schedule(tracker.get_slot("section"),tracker.get_slot("group")))

        dispatcher.utter_message(text)
	
        return []

#Action qui recurére le film selon la catégorie 
class ActionFilmCat(Action):

     def name(self) -> Text:
        return "action_film_categorie"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        categorie = tracker.get_slot('categorie')
        print(categorie)

        text=categorie+" films are :{}".format(db_sqlite.select_films(tracker.get_slot("categorie")))

        dispatcher.utter_message(text)

        return []

#Action qui recurére le film selon le réalisateur 
class ActionFilmReal(Action):

     def name(self) -> Text:
        return "action_film_realisateur"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        realisateur = tracker.get_slot('realisateur')
        print(realisateur)

        text="Films realized by "+realisateur+" are:{}".format(db_sqlite.select_films_by_rls(tracker.get_slot("realisateur")))

        dispatcher.utter_message(text)

        return []


#Action qui recurére le nombre de saison d'un série
class ActionSerieSaison(Action):

     def name(self) -> Text:
        return "action_series_saison"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        titre = tracker.get_slot('titre')
        print(titre)

        text="Number of saison in "+titre+" is :{} ".format(db_sqlite.select_nbr_saison(tracker.get_slot("titre")))
        dispatcher.utter_message(text)
        return []

#Action qui recurére une série selon la catégorie
class ActionSerieCat(Action):

     def name(self) -> Text:
        return "action_series_categorie"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        categorie = tracker.get_slot('categorie')
        print(categorie)

        text="The "+categorie+" serie you can watch are :{} ".format(db_sqlite.select_serie(tracker.get_slot("titre")))
        dispatcher.utter_message(text)

        return []

#Action qui recurére les informations de l'enseignant et lui envoie un mail
class ActionEnseignantNom(Action):

     def name(self) -> Text:
        return "action_enseignant_nom"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("----------- action_enseignant_nom --------------------")
        nom = tracker.get_slot('name')
        message = tracker.get_slot('message')
        print(nom)
        print(message)

        #print(db_sqlite.select_enseignant_nom(tracker.get_slot("nom")))
        res = db_sqlite.select_enseignant_nom(nom,message)

        text=" Les informations de l'enseignant :{}".format(res)

        dispatcher.utter_message(text)

        return []

#Action qui recurére la salle libre selon la date du jour 
class ActionSalleByDate(Action):

     def name(self) -> Text:
        return "action_salle_by_date"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        date = tracker.get_slot('date')
        print(date)
 
        res = db_sqlite.select_salle_libre_site(date)

        text = " Les salles libres selon le jour choisi sont:{}".format(res)

        dispatcher.utter_message(text)

        return []

#Action qui recurére le climat selon la date
class ActionWeather(Action):

     def name(self) -> Text:
        return "action_weather"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        date = tracker.get_slot('date')
        print(date)

        res = db_sqlite.select_weather(date)
        text = ""
        weather = format(res)
        if weather == "sunny":
                text = "it's a sunny day you can hang out"
        elif weather == "foggy":
             text = "it's a foggy day "
        elif weather == "rainy":
                text = "rainy day euhh Netflix and chill"
        elif weather == "cloudy":
                text = "cloudy day time to take a hot chocolat"

        dispatcher.utter_message(text)
        return []
