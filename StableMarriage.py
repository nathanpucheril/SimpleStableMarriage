# x_pref and y_pref are dictionaries with key : value of the form
# element: list of elements preferences
# return: two dictionary of bindings of preferences
#         {y : x} , {x : y}
def StablePairing(x_pref, y_pref):
    pairings = {}
    hasBeenProposedTo = set()

    def propose(x, y):
        hasBeenProposedTo.add(y)
        if not pairings.has_key(y):
            pairings[y] = x
        else:
            x_old = pairings[y]
            if does_prefer_X(y, x_old, x):
                pairings[y] = x
                (x_pref[x_old]).remove(y)
            else:
                x_pref[x].remove(y)

    def does_prefer_X(y, x_old, x_new):
        y_preferences = y_pref[y]
        for x in y_preferences:
            if x == x_new:
                return True
            elif x == x_old:
                return False
        return False


    while(not(len(hasBeenProposedTo) == len(y_pref))):
        for x in x_pref:
            y = (x_pref[x])[0]
            propose(x, y)
    return pairings, {v: k for k, v in pairings.items()}



# x_pref = {"A": ["a", "b", "c", "d"], "B": ["b", "a", "c", "d"], "C": ["a", "d", "c", "b"],"D": ["d", "c", "a", "b"] }
# y_pref = {"a": ["A", "B", "C", "D"], "b": ["D", "C", "B", "A"], "c": ["A", "B", "C", "D"],"d": ["C", "D", "A", "B"] }

x = {1: ['a' ,'b'], 2: ['b', 'a']}
y = {'a': [2,1], 'b': [2, 1]}
print(StablePairing(x, y))
