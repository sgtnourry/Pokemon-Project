from resources.resource_manager import GetImagePath
from Screen.Pygame.Battle.Side.pokemon_stats_view import PokemonStatsView

from kao_gui.pygame.pygame_helper import GetTransparentSurface, load_image
from kao_gui.pygame.widgets.sized_widget import SizedWidget

class BattleSideView(SizedWidget):
    """ View for a battle side in a Pokemon Battle """
    
    def __init__(self, side, width, height):
        """ Initialize the Battle Side View """
        SizedWidget.__init__(self, width, height)
        self.side = side
        self.pokemonStatsView = PokemonStatsView(self.width*.4, self.height*.9,
                                                 self.side.pkmnInPlay[0], showHP=self.shouldShowHP())
        self.setPokemonImage()
        
    def update(self):
        """ Update the Battle Side View """
        self.setPokemonImage()
        
    def setPokemonImage(self):
        """ Set the pokemon Image """
        self.pokemonImage = load_image("{0}.png".format(self.getBasePokemonImageName()))
        
    def getBasePokemonImageName(self):
        """ Returns the base Pokemon Image Name """
        return GetImagePath("Pokemon/{0}".format(self.getPokemon().getDisplayImageBaseName()))
        
    def getPokemon(self):
        """ Returns the current Pokemon object """
        return self.side.pkmnInPlay[0].pkmn
        
    def shouldShowHP(self):
        """ Return if the Battle View should show the HP """
        return True 