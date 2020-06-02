class Atom:

    def __init__(self, symb, x, y, z, rayon):
        self._symb = symb
        self._x = x
        self._y = y
        self._z = z
        self._rayon = rayon

    
    def position(self):

        # Je sais plus c'est quoi la formule des coordonnées cartésiennes,
        # t'as juste à la mettre là :) :)
        return (_x, _y, _z)

    
    def getRayon(self):

        return self._rayon

    def separation(self, other):

        dist_x = (other._x - self._x)**2
        dist_y = (other._y - self._y)**2
        dist_z = (other._z - self._z)**2

        return (dist_x + dist_y + dist_z) ** 0.5

    def move_to(self, x, y, z):
        
        self._x = x
        self._y = y
        self._z = z

    def __repr__(self):
        return """
            {symbole}[x={x}, y={y}, z={z}, rayon={r}]
        """.strip().format(symbole=self._symb, x=self._x, y=self._y, z=self._z, r=self._rayon)


if __name__ == "__main__":

    at = Atom("H", 1, 1, 1, 5)

    print(at)