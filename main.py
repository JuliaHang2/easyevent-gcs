```python
# Pseudocódigo para o Sistema EasyEvent

class Evento:
    def __init__(self, id, nome, descricao, data, hora, local, capacidade):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.data = data
        self.hora = hora
        self.local = local
        self.capacidade = capacidade
        self.participantes_inscritos = []

    def adicionar_participante(self, participante):
        if len(self.participantes_inscritos) < self.capacidade:
            self.participantes_inscritos.append(participante)
            return True
        else:
            return False # Evento lotado

    def remover_participante(self, participante):
        if participante in self.participantes_inscritos:
            self.participantes_inscritos.remove(participante)
            return True
        else:
            return False

class Participante:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

class SistemaEasyEvent:
    def __init__(self):
        self.eventos = {}
        self.usuarios = {}

    def cadastrar_evento(self, evento):
        self.eventos[evento.id] = evento
        print(f"Evento \'{evento.nome}\' cadastrado com sucesso.")

    def editar_evento(self, id_evento, novos_dados):
        if id_evento in self.eventos:
            evento = self.eventos[id_evento]
            for chave, valor in novos_dados.items():
                setattr(evento, chave, valor)
            print(f"Evento \'{evento.nome}\' atualizado com sucesso.")
        else:
            print("Evento não encontrado.")

    def excluir_evento(self, id_evento):
        if id_evento in self.eventos:
            del self.eventos[id_evento]
            print("Evento excluído com sucesso.")
        else:
            print("Evento não encontrado.")

    def inscrever_participante_em_evento(self, id_participante, id_evento):
        if id_evento in self.eventos and id_participante in self.usuarios:
            evento = self.eventos[id_evento]
            participante = self.usuarios[id_participante]
            if evento.adicionar_participante(participante):
                print(f"Participante \'{participante.nome}\' inscrito no evento \'{evento.nome}\'")
            else:
                print(f"Não foi possível inscrever \'{participante.nome}\' Evento \'{evento.nome}\' lotado.")
        else:
            print("Evento ou participante não encontrado.")

    def emitir_certificado(self, id_participante, id_evento):
        # Lógica para emissão de certificado digital
        print(f"Certificado emitido para o participante {id_participante} no evento {id_evento}.")

    def enviar_notificacao(self, id_participante, mensagem):
        # Lógica para envio de notificação por e-mail
        print(f"Notificação enviada para o participante {id_participante}: {mensagem}")

    def consultar_eventos(self):
        print("\n--- Eventos Cadastrados ---")
        for evento_id, evento in self.eventos.items():
            print(f"ID: {evento.id}, Nome: {evento.nome}, Local: {evento.local}, Data: {evento.data}, Vagas: {evento.capacidade - len(evento.participantes_inscritos)}")
        print("--------------------------")

# Exemplo de Uso:
sistema = SistemaEasyEvent()

# Criar eventos
evento1 = Evento(1, "Semana Acadêmica", "Palestras e workshops", "2026-07-10", "09:00", "Auditório A", 100)
evento2 = Evento(2, "Hackathon", "Maratona de programação", "2026-08-01", "14:00", "Laboratório de TI", 50)

sistema.cadastrar_evento(evento1)
sistema.cadastrar_evento(evento2)

# Criar participantes
participante1 = Participante(101, "João Silva", "joao.silva@email.com")
participante2 = Participante(102, "Maria Souza", "maria.souza@email.com")
sistema.usuarios[participante1.id] = participante1
sistema.usuarios[participante2.id] = participante2

# Consultar eventos
sistema.consultar_eventos()

# Inscrever participantes
sistema.inscrever_participante_em_evento(participante1.id, evento1.id)
sistema.inscrever_participante_em_evento(participante2.id, evento1.id)
sistema.inscrever_participante_em_evento(participante1.id, evento2.id)

# Consultar eventos novamente para ver vagas
sistema.consultar_eventos()

# Emitir certificado e enviar notificação (simulado)
sistema.emitir_certificado(participante1.id, evento1.id)
sistema.enviar_notificacao(participante1.id, "Sua inscrição na Semana Acadêmica foi confirmada!")
```
