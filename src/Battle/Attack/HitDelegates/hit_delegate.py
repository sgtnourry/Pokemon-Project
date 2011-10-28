import random

class HitDelegate(object):
    """ Represents an Attack's ability to hit an opponent """
    accMods = [1.0, 4/3.0, 5/3.0, 2.0, 7/3.0, 8/3.0, 9,
                    1/3.0, 3/8.0, .428, 1/2.0, 3/5.0, 3/4.0]
  
    def __init__(self, parent, toHit, message):
        """ Build a core hit Delegate """
        self.parent = parent
        self.chanceToHit = toHit
        self.message = message
    
    
    def hit(self, actingSide, otherSide):
        """ Returns whether or not an attack hit its target """
        return not self.dodging(otherSide) and self.core(actingSide, otherSide), [self.message]
        
        
    def core(self, actingSide, otherSide):
        """ Calculates a random #, compares to chanceToHit to determine if it
        lands or not """
        accMod = HitDelegate.accMods[actingSide.statMods["ACC"]]
        evasMod = HitDelegate.accMods[-1*otherSide.statMods["EVAS"]]
        toHit = self.chanceToHit*accMod*evasMod
        return random.randint(0, 99) < toHit
        
    def dodging(self, otherSide):
            """ Returns if the opp is dodging """
            return otherSide.dodge is not None 