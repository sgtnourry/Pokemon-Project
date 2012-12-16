from Menu.box_menu import BoxMenu
from Menu.menu_entry import MenuEntry

class AttackMenu(BoxMenu):
    """ Represents the Battle's Attack Menu """

    def __init__(self, userPkmn):
        """ Create the Action Menu for the given Pokemon """
        self.pkmn = userPkmn
        BoxMenu.__init__(self)
    
    def addEntries(self):
        """ Add entries to the Menu """
        self.action = None
        self.entries = [MenuEntry("Attack 1", self.tempEntryCallback),
                        MenuEntry("Attack 2", self.tempEntryCallback),
                        MenuEntry("Attack 3", self.tempEntryCallback),
                        MenuEntry("Attack 4", self.tempEntryCallback)]


    def tempEntryCallback(self):
        """ Temporary Call back function for Action menu Entries """