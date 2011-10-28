from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate

class LevelDelegate(DamageDelegate):
    """ Deals damage based on level """
    def __init__(self, parent, physical):
        """ Set physical """
        self.parent = parent
        self.physical = physical
        
    def calcDamage(self, actingSide, otherSide):
        """ Return the level of the user """
        return actingSide.currPokemon.level