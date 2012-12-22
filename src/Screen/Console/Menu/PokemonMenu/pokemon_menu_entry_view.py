from Screen.Console.Menu.MainMenu.menu_entry_view import MenuEntryView
from Screen.Console.HealthBar.health_bar_view import HealthBarView

class PokemonMenuEntryView(MenuEntryView):
    """ Represents an entry of a Pokemon in the menu """

    def __init__(self, entry):
        self.healthBar = HealthBarView(entry.getPokemon())
        MenuEntryView.__init__(self, entry)
        
    def draw(self, window):
        """ Draws the menu entry """
        format = self.getTerminalFormatting(self.entry.selected, window.terminal)
        pkmn = self.entry.getPokemon()
        return self.getEntryLines(window), self.getEntrySize(window)

    def getEntrySize(self, window):
        """ Return the entry size """
        return (window.getWidth()/2 - 2, window.getHeight()/3 - 2)

    def getEntryLines(self, window):
        """ Return entry lines """
        lines = []
        entrySize = self.getEntrySize(window)

        lines.append("")
        lines.append(self.getHeaderLine(window))
        lines.append(self.getPokemonNameLine(window))
        lines.append(self.getHealthLine(window))
        lines.append(self.getHealthBarLine(window))
        for i in range(entrySize[1]-5):
            lines.append(self.getLine("", window))
        lines.append(self.getHeaderLine(window))
        lines.append("")
        return lines
        
    def getHeaderLine(self, window):
        """ Returns the line for the header and footer of the entry """
        entrySize = self.getEntrySize(window)
        return "|{0}|".format("-"*(entrySize[0]-2))

    def getLine(self, text, window):
        """ Returns a line """
        entrySize = self.getEntrySize(window)
        spacer = " "*(entrySize[0]-2-len(text))
        format = self.getTerminalFormatting(self.entry.selected, window.terminal)
        return "|{0}{1}{2}{t.normal}|".format(format, text, spacer, t=window.terminal)

    def getPokemonNameLine(self, window):
        """ Returns the Pokemon Name and Species as a string """
        pkmn = self.entry.getPokemon()
        nameString = "{0} --- {1}".format(self.getFullString(pkmn.name), self.getFullString(pkmn.species))
        return self.getLine(nameString, window)

    def getHealthLine(self, window):
        """ Return the line with health stats """
        pkmn = self.entry.getPokemon()
        return self.getLine("{0}/{1}".format(pkmn.getCurrHP(), pkmn.getStat("HP")), window)

    def getHealthBarLine(self, window):
        """ Return the line with health bar """
        entrySize = self.getEntrySize(window)
        healthBarText = self.healthBar.draw(window, entrySize[0]-2)
        return self.getLine(healthBarText, window)

    def getFullString(self, string):
        """ Returns a string with the full 10 char limit """
        return (string + " "*10)[:10]

    def getTerminalFormatting(self, selected, terminal):
        """ Sets the Boldness of the entry """
        if selected:
            return terminal.reverse
        else:
            return ""