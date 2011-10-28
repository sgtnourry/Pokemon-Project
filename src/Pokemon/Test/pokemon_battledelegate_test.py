from Pokemon.pokemon import Pokemon

import unittest

class takeDamage(unittest.TestCase):
    """ Tests logic for a Pokemon taking damage"""
    
    def  setUp(self):
        """ Build the Trainer and Pokemon lists for use in tests """
        self.poke = Pokemon("BULBASAUR")
        
    def noFaint(self):
        """ Test a Pokemon takes damage appropriately """
        self.poke.battleDelegate.currHP = 2
        self.poke.battleDelegate.takeDamage(1)
        assert self.poke.battleDelegate.currHP == 1, \
                "HP Should decrease by the damage taken"
        
    def faintPerfect(self):
        """ Test a Pokemon faints when it takes damage equal to its health """
        self.poke.battleDelegate.currHP = 1
        self.poke.battleDelegate.takeDamage(self.poke.battleDelegate.currHP)
        assert self.poke.battleDelegate.currHP == 0, \
                "When taking damage equivalent to the Pokemon's health the \
                Pokemon should have no health"
        assert self.poke.isFainted(), "A Pokemon with 0 HP should be fainted"
        
    def faintOver(self):
        """ Test a Pokemon has zero health when taking more damage than it has health """
        self.poke.battleDelegate.currHP = 1
        self.poke.battleDelegate.takeDamage(self.poke.battleDelegate.currHP+1)
        assert self.poke.battleDelegate.currHP == 0, \
                "When taking damage greater than the Pokemon's health the \
                Pokemon should have no health"
        assert self.poke.isFainted(), "A Pokemon with 0 HP should be fainted"

# Collect all test cases in this class
testcasesTakeDamage = ["noFaint", "faintPerfect", "faintOver"]
suiteTakeDamage = unittest.TestSuite(map(takeDamage, testcasesTakeDamage))

##########################################################

class heal(unittest.TestCase):
    """ Tests logic for healing a Pokemon """
    
    def  setUp(self):
        """ Build the Trainer and Pokemon lists for use in tests """
        self.poke = Pokemon("BULBASAUR")
        
    def notToFull(self):
        """ Test a Pokemon gains health when not at full"""
        self.poke.battleDelegate.currHP = self.poke.battleDelegate.stats["HP"] -10
        self.poke.battleDelegate.heal(5)
        assert self.poke.battleDelegate.currHP == self.poke.battleDelegate.stats["HP"] -5, \
                "HP Should increase by the amount healed"
        
    def pastFull(self):
        """ Test a Pokemon can't heal past full """
        self.poke.battleDelegate.currHP = self.poke.battleDelegate.stats["HP"] -10
        self.poke.battleDelegate.heal(self.poke.battleDelegate.stats["HP"])
        assert self.poke.battleDelegate.currHP == self.poke.battleDelegate.stats["HP"], \
                "Pokemon should not be able to be healed past its max HP"

# Collect all test cases in this class
testcasesHeal = ["notToFull", "pastFull"]
suiteHeal = unittest.TestSuite(map(heal, testcasesHeal))

##########################################################
# Collect all testcases in this file
suites = [suiteTakeDamage, suiteHeal]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()