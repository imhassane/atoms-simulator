from atom import Atom


class Molecule:

    def __init__(self):

        self._atomes = []
        self._liaisons = []

    
    def ajouteAtome(self, nouveau):
        self._atomes.append(nouveau)


    def etablitLiaison(self, a1, a2):

        if a1.position() != a2.position():

            dist = a1.separation(a2)
            if dist > a1.getRayon() and dist > a2.getRayon():
                self._liaisons.append((a1, a2))

            else:
                print("Liaison chimique impossible")

        else:
            print("Liaision chimique impossible")



if __name__ == "__main__":

    molecule = Molecule()

    a1 = Atom("H", 1, 1, 1, 5)
    a2 = Atom("B", 5, 3, 4, 5)

    molecule.etablitLiaison(a1, a2)

    print("Molécule ajoutée")