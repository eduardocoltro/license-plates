class Veiculo:
    def __init__(self, placa, marca, modelo, proprietario, estado=None):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.proprietario = proprietario
        self.estado = estado

    def __str__(self):
        return '{} {} {}'.format(self.marca, self.modelo, self.proprietario)

    def __repr__(self):
        return '{} {} {}'.format(self.marca, self.modelo, self.proprietario)
    
    def lista(self, estado):
        self.estado = estado
        return [self.marca, self.modelo, self.proprietario, self.estado]
