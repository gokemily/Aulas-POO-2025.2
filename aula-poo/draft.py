class Towel:
    def __init__(self, color: str, size: str): # construtor
        self.color: str = color # atributos
        self.size: str = size
        self.wetness: int = 0
    
    def dry(self, amount: int) -> None:
        self.wetness += amount
        if self.wetness >= self.isMaxWetness():
            self.wetness = self.isMaxWetness()
            print("toalha encharcada")

    def isDry(self):
        return self.wetness == 0

    def wringOut(self):
        self.wetness = 0

    def isMaxWetness(self) -> int:
        if self.size == "P": # early return
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0 # default return

    def __str__(self) -> str: # toString
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"
def main():
    towel: Towel = Towel(size="", color="")
    while True:
        line = input()
        arg : list[str] = line.split(" ")

        if arg[0] == "end":
            break
        elif arg[0] == "new":
            towel: Towel = Towel(color=arg[1], size=arg[2])
        elif arg[0] == "show":
            print(towel)
        elif arg[0] == "wet":
            towel.wetness = int(arg[1])
            print("Umidade da toalha alterada")
        elif arg[0] == "wringOut":
            towel.wetness = 0git
            print("Toalha torcida até a ultima gota")
        else:
            print("comando nao encontrado")

main()