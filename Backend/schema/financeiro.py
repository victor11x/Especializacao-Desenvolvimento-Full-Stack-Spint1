from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from model.financeiro import Financeiro


class FinanceiroSchema(BaseModel):
    """ Define como um nova transação financeira a ser inserido deve ser representado
    """
    nome: str = "Conta da Internet"
    tipo_despesa:str = "Escritorio Home Office"
    tipo_pagamento:str = "Boleto"
    data_vencimento:str = "DD/MM/YYYY"
    valor: float = 126.90
    

class FinanceiroBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome da transação.
    """
    nome: str = "Digite nome da despesa"


class ListagemFinanceirosSchema(BaseModel):
    """ Define como uma listagem de transações que será retornada.
    """
    financeiros:List[FinanceiroSchema]


def apresenta_financeiros(financeiros: List[Financeiro]):
    """ Retorna uma representação da transação financeira seguindo o schema definido em
        financeiroViewSchema.
    """
    result = []
    for financeiro in financeiros:
        result.append({
            "nome": financeiro.nome,
            "tipo_despesa": financeiro.tipo_despesa,
            "tipo_pagamento": financeiro.tipo_pagamento,
            "data_vencimento": financeiro.data_vencimento,
            "valor": financeiro.valor,
        })

    return {"financeiros": result}


class FinanceiroViewSchema(BaseModel):
    """ Define como um transação será retornado: descrição da transação de entrada e saída (entrada seria renda e despesa seria uma saída).
    """
    id: int = 1    
    nome: str = "Conta da Internet"
    tipo_despesa = "Escritorio Home Office"
    tipo_pagamento = "Boleto"
    data_vencimento = "23/05/2023"
    valor: float = 126.90    


class FinanceiroDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_financeiro(financeiro: Financeiro):
    """ Retorna uma representação do financeiro seguindo o schema definido em
        financeiroViewSchema.
    """
    return {
        "id": financeiro.id,
        "nome": financeiro.nome,
        "tipo_despesa": financeiro.tipo_despesa,
        "tipo_pagamento": financeiro.tipo_pagamento,
        "data_vencimento": financeiro.data_vencimento,        
        "valor": financeiro.valor
        
    }