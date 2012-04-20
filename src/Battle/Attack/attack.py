from preconditions import PreconditionChecker
from resources.tags import Tags
from Battle.Attack.DamageDelegates.null_damage_delegate import NullDamageDelegate

class Attack:
    """ Represents an Attack """
    
    def __init__(self):
        self.hitDelegate = None
        self.damageDelegate = None
        self.speedDelegate = None
        
        self.effectDelegates = []
        
        
    def use(self, user, target):
        """ Uses the current attack Object in a Battle """
        messages = []
        stop = self.doPreconditions(user, target, messages)
        
        if not stop:
            messages += self.doAttack(user, target)
        
        return messages
        
    def doAttack(self, user, target):
        """  """
        messages = ["%s USED %s" % (user.getHeader(), self.name)]
        hit = self.doHit(user, target, messages)
        
        messages += self.doAttackLoop(user, target)
        
        return messages
        
    def doAttackLoop(self, user, target):
        """  """
        messages = []
        messages += self.doDamage(user, target)
        messages += self.doEffects(user, target)
        return messages
        
    # Attack Loop Functions
    def doPreconditions(self, user, target, messages):
        """ Checks preconditions to make sure the user isn't prevented from working """
        preconditionChecker = PreconditionChecker(user, target, self)
        stop, preMessages = preconditionChecker.checkPreConditions()
        messages += preMessages
        return stop
        
    def doHit(self, user, target, messages):
        """ Check if the user hits the target(s) """
        hit, hitMessages = self.hitDelegate.hit(user, target)
        if not hit:
            messages += hitMessages
            messages += self.applyEffectsOnMiss(user, target)
        return hit
        
    def doDamage(self, user, target):
        """ Does the attack's damage, returns that the loop should not stop """
        return self.damageDelegate.doDamage(user, target)
        
    def doEffects(self, user, target):
        """ Does the attack's effects, returns that the loop should not stop """
        messages = []

        if not self.preventEffects(user, target):
            for effect in self.effectDelegates:
                messages += effect.tryToApplyEffect(user, target)
        return messages
        
    # Helper Methods
    def addDelegate(self, delegateCategory, delegate):
        """ Adds a delegate to an Attack Object """
        if delegateCategory == Tags.effectDelegateTag:
            self.effectDelegates.append(delegate)
            return
        setattr(self, delegateCategory, delegate)
        
    def preventEffects(self, user, target):
        """ Return whether the effects are prevented """
        nullDamage = hasattr(self.damageDelegate, "isNull")
        canUse = user.getAbility().canUseEffects() and target.getAbility().canUseEffects()
        return not nullDamage and not canUse
        
    def applyEffectsOnMiss(self, user, target):
        """ Apply effects on miss """
        messages = []
        for effect in self.effectDelegates:
            if hasattr(effect, "applyOnMiss"):
                effectMessages = effect.applyEffect(user, target)
                messages = messages + effectMessages
            if hasattr(effect, "effectOnMiss"):
                effectMessages = effect.effectOnMiss(user, target)
                messages = messages + effectMessages
        return messages
        
    def isStatus(self):
        """ Returns if the Attack is a status attack """
        return isinstance(self.damageDelegate, NullDamageDelegate)
        