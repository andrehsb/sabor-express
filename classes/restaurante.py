from classes.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome}  {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome}  {restaurante.categoria}  {restaurante.ativo}  {restaurante.media_avaliacoes}')

    @property
    def ativo(self):
        return 'ativado' if self._ativo else 'deativado'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, coment, nota):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(coment, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return ''
        else:
            return round(sum(avaliacao._nota for avaliacao in self._avaliacao)/len(self._avaliacao), 1)
