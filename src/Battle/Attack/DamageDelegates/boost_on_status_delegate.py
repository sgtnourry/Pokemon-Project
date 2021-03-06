from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate

class BoostDamageOnStatusDelegate(DamageDelegate):
    """ DAmagfe Delegate where damage is boosted on status """
    
    def coreDamage(self, user, target):
        """ Checks for damage and doubles the coreDamage if the target has a status """
        boostMod = 1
        
        if target.hasStatus():
            boostMod = 2
            
        damage = super(BoostDamageOnStatusDelegate, self).coreDamage(user, target)
            
        return boostMod*damage