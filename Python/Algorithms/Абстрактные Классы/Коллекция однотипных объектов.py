from abc import ABC

class ANamed(ABC):
    name = ""

class Flower(ANamed):
    pass

class City(ANamed):
    pass

class Star(ANamed):
    pass

rose = Flower()
rose.name = "Rose"

rome = City()
rome.name = "Rome"

sirius = Star()
sirius.name = "Sirius"

rows = [rose, rome, sirius]
names = ", ".join([r.name for r in rows])

# namse is Rose, Rome, Sirius

print(names)