
class Game:
    """
    A single game which has its own timeline, events and players
    """
    def __init__(self, players:list) -> None:
        self.players = players
        self.targeting_graph = None

class Player:
    """
    The physical human player in the game.
    """
    def __init__(self, ID):
        self.ID = ID
        self.targeting = []
        self.targeted_by = []


















# #Initiates some classes
# class Game:
#     """
#     A single game which has its own timeline, events and players
#     """
#     def __init__(self, start_datetime, end_datetime, term) -> None:
#         self.start_datetime = start_datetime
#         self.end_datetime = end_datetime
#         self.term = term
#         self.players = []
#         self.police = []
#         self.characters = []
#         self.events = []
#         self.reports = []

#         self.wanted_list = []
#         self.inco_list = []

# class Player:
#     """
#     The physical human player in the game.
#     """
#     def __init__(self, ID,firstname:str, lastname:str, email:str, address:str, college:str, water_status, initial_character, notes = None):
#         self.ID = ID
#         self.firstname = firstname
#         self.lastname = lastname
#         self.email = email
#         self.address = address
#         self.college = college
#         self.water_status = water_status
#         self.notes = notes
#         self.characters = [initial_character]

#         self.targets = []


# class Character:
#     """
#     A character that exists in the game. Multiple characters can be assigned to a player
#     """

#     def __init__(self, pseudonym) -> None:
#         self.pseudonym = pseudonym
#         self.kills = 0
#         self.assists = 0
#         self.deaths = 0
#         self.points = 0
#         self.reports = []
#         self.police = False

# class Event:
#     """
#     An event in assassins, where kills, deaths, assists and other actions go down
#     """
#     def __init__(self, datetime, participants) -> None:
#         self.datetime = datetime
#         self.participants = participants
#         self.description = None


# class Report:
#     """
#     A piece of text that describes an event that has happened
#     """
#     def __init__(self) -> None:
#         pass
        

# class RealReport(Report):
#     """
#     A report that is truthful and short account of the events, for the Umpire's eyes
#     """
#     def __init__(self) -> None:
#         pass

# class FictionReport(Report):
#     """
#     A report that is fictional and posted to entertain
#     """
#     def __init__(self) -> None:
#         pass

