class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    pouster = Pessoa(nome='Pouster')
    alice = Pessoa(pouster, nome='Alice')
    print(Pessoa.cumprimentar(alice))
    print(id(alice))
    print(alice.cumprimentar())
    print(alice.nome)
    print(alice.idade)
    for filho in alice. filhos:
        print(filho.nome)
    alice.sobrenome = 'ilha ramalho'
    del alice.filhos
    alice.olhos = 1
    del alice.olhos
    print(alice.__dict__)
    print(pouster.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(alice.olhos)
    print(pouster.olhos)
    print(id(Pessoa.olhos), id(alice.olhos), id(alice.olhos))
