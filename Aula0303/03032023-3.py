class Carro:
    kind = 'automovel'
    def __init__(self, color: str, model: str, id: str):
        self.color = color
        self.model = model
        self.id = id

    def ligar(self):
        print('Vrrruuum')

    def print_carro(self):
        print(f'Seu carro é {self.color}, modelo {self.model} e placa {self.id}')

carro1 = Carro('Corsa','preto','ABC2023')
carro2 = Carro('Corola','branco','TUI3475')
carro3 = Carro('Gol','prata','SPC2018')
carro4 = Carro('Vectra','azul','BDS32039')
carro5 = Carro('Onibus','vermelho','JIK4745')
        
carro1.ligar()
print('=-'*30)

carro2.print_carro()
print('=-'*30)

carro5.print_carro()
print('=-'*30)

carro1.print_carro()
print('=-'*30)

carro3.print_carro()
print('=-'*30)

