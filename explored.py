'''

@author: Caleb
'''
class Explored(object):
    "Maintain an explored set.  Assumes that states are hashable"

    def __init__(self):
        "__init__() - Create an empty explored set"
        self.exploredSet = {}
        
    def exists(self, state):
        """exists(state) - Has this state already been explored?
        Returns True or False, state is hashable
        """
        if hash(state) in self.exploredSet:     #check for hash equality
            list = self.exploredSet[hash(state)]
            for s in list:
                if state == s:
                    #print("found a state inside")
                    return True                     #check for node equality
        return False
    
    def add(self, state):
        """add(state) - add given state to the explored set.  
        state must be hashable and we asssume that it is not already in set
        """
        
        # The hash function is a Python builtin that generates
        # a hash value from its argument.  Used this to create
        # a dictionary key.  Handle collisions by storing 
        # states that hash to the same key in a bucket list.
        # Note that when you access a Python dictionary by a
        # non existant key, it throws a KeyError

        if self.exists(state):
            list = self.exploredSet[hash(state)]
            list.append(state)
            self.exploredSet.update({hash(state): list})
        else:
            self.exploredSet.update({hash(state): [state]})


