from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime,date
from typing import Union

from model import Base



class Financeiro(Base):
    __tablename__ = 'financeiro'

    id = Column("pk_financeiro", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    tipo_despesa = Column(String(50))
    tipo_pagamento = Column(String(50))
    data_vencimento = Column(String(12))
    valor = Column(Float)
    data_insercao = Column(DateTime, default=datetime.now())


def __init__(self, nome:str, tipo_despesa:str,tipo_pagamento:str, data_vencimento: str,valor:float,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Despesa 

        Arguments:
            nome: nome da despesa.
            tipo_pagamento: tipo de pagamento da despesa se ela é boleto, credito ou debito.
            tipo_despesa: tipo de despesa por exemplo: Lazer,alimento,etc.
            valor: valor da despesa foi comprado
            data_insercao: data de quando a despesa foi inserido à base
        """
        self.nome = nome
        self.tipo_despesa = tipo_despesa
        self.tipo_pagamento = tipo_pagamento
        self.data_vencimento = data_vencimento
        self.valor = valor

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
            

 