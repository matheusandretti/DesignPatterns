# Definição dos estados possíveis
CRIADO = "CRIADO"
EM_TRIAGEM = "EM_TRIAGEM"
EM_TRANSPORTE = "EM_TRANSPORTE"
SAIU_PARA_ENTREGA = "SAIU_PARA_ENTREGA"
ENTREGUE = "ENTREGUE"
EXTRAVIADO = "EXTRAVIADO"

# Definição de eventos
EVENTO_TRIAGEM = "triagem"
EVENTO_TRANSPORTE = "transporte"
EVENTO_ENTREGA = "entrega"
EVENTO_ENTREGUE = "confirmar_entrega"
EVENTO_EXTRAVIO = "extravio"

# Tabela de transições: {estado_atual: {evento: proximo_estado}}
transicoes = {
    CRIADO: {
        EVENTO_TRIAGEM: EM_TRIAGEM,
        EVENTO_EXTRAVIO: EXTRAVIADO
    },
    EM_TRIAGEM: {
        EVENTO_TRANSPORTE: EM_TRANSPORTE,
        EVENTO_EXTRAVIO: EXTRAVIADO
    },
    EM_TRANSPORTE: {
        EVENTO_ENTREGA: SAIU_PARA_ENTREGA,
        EVENTO_EXTRAVIO: EXTRAVIADO
    },
    SAIU_PARA_ENTREGA: {
        EVENTO_ENTREGUE: ENTREGUE,
        EVENTO_EXTRAVIO: EXTRAVIADO
    },
    ENTREGUE: {},
    EXTRAVIADO: {}
}

class Pacote:
    def __init__(self, codigo: str):
        self.codigo = codigo
        self.estado = CRIADO
        self.historico = [self.estado]

    def registrar_evento(self, evento: str):
        self.estado = transicoes[self.estado][evento]
        self.historico.append(self.estado)

    def rastrear(self):
        return f"Pacote {self.codigo} está em: {self.estado}"

    def linha_do_tempo(self):
        return f"Histórico do pacote {self.codigo}: {self.historico}"

pacote = Pacote("BR123456")

pacote.registrar_evento(EVENTO_TRIAGEM)
pacote.registrar_evento(EVENTO_TRANSPORTE)
pacote.registrar_evento(EVENTO_ENTREGA)
pacote.registrar_evento(EVENTO_ENTREGUE)

print(pacote.rastrear())
print(pacote.linha_do_tempo())
