class Atendimento:
    def __init__(self, id_atendimento, nome, servico, valor):
        self.id_atendimento = id_atendimento
        self.nome = nome
        self.servico = servico
        self.valor = valor

    def __str__(self):
        return f"ID: {self.id_atendimento} | Nome: {self.nome} | Serviço: {self.servico} | Valor: {self.valor}"

class GerenciadorDeAtendimentos:
    def __init__(self):
        self.atendimentos = []

    def adicionar_atendimento(self, nome, servico, valor):
        novo_id = len(self.atendimentos) + 1
        atendimento = Atendimento(novo_id, nome, servico, valor)
        self.atendimentos.append(atendimento)
        return atendimento

    def editar_atendimento(self, id_atendimento, nome=None, servico=None, valor=None):
        atendimento = self.buscar_por_id(id_atendimento)
        if atendimento is None:
            raise KeyError("Atendimento não encontrado.")
        if nome is not None:
            atendimento.nome = nome
        if servico is not None:
            atendimento.servico = servico
        if valor is not None:
            atendimento.valor = valor
        return atendimento

    def remover_atendimento(self, id_atendimento):
        atendimento = self.buscar_por_id(id_atendimento)
        if atendimento is None:
            raise KeyError("Atendimento não encontrado.")
        self.atendimentos.remove(atendimento)
        return atendimento

    def pesquisar_atendimentos(self, termo):
        termo = termo.lower()
        encontrados = []
        for atendimento in self.atendimentos:
            if termo in atendimento.nome.lower() or termo in atendimento.servico.lower():
                encontrados.append(atendimento)
        return encontrados

    def listar_atendimentos(self):
        return self.atendimentos

    def buscar_por_id(self, id_atendimento):
        for atendimento in self.atendimentos:
            if atendimento.id_atendimento == id_atendimento:
                return atendimento
        return None

    