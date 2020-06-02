from atom import Atom


class Molecule:

    def __init__(self):

        _atomes = []
        _liasions = []

    
    def ajouteAtom(self, nouveau):
        self._atomes.append(nouveau)


    def etablitLiaison(self, a1, a2):

        if a1.position() != a2.position():

            dist = a1.separation(a2):
            if dist > a1.rayon() && dist > a2.rayon():
                self._liaisons.append((a1, a2))
                
            else:
                print("Liaison chimique impossible")

        else:
            print("Liaision chimique impossible")

