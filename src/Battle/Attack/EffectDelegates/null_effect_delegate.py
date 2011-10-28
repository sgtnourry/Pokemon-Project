
class NullEffectDelegate:
    """ An empty Effect Delegate for attacks with no effect """
    
    def applyEffect(self, actingSide, otherSide):
        return