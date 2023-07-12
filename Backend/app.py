from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError
from datetime import datetime

from model import Session, Financeiro
from logger import logger
from schema.error import *
from schema.financeiro import *
from flask_cors import CORS

info = Info(title="API Controle Financeiro", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
financeiro_tag = Tag(name="Financeiro", description="Adição, visualização e remoção de transações financeiras à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/financeiro', tags=[financeiro_tag],
          responses={"200": FinanceiroViewSchema, "409": ErrorSchema, "400": ErrorSchema})


def add_financeiro(form: FinanceiroSchema):
    """Adiciona um nova transação financeira à base de dados

    Retorna uma representação das despesa.
    """
    financeiro = Financeiro(
        nome = form.nome,
        tipo_despesa = form.tipo_despesa,
        tipo_pagamento = form.tipo_pagamento,
        data_vencimento = form.data_vencimento,
        valor = form.valor
        )
    logger.debug(f"Adicionando Financeiro de nome: '{financeiro.nome}'")
    try:

        session = Session()

        session.add(financeiro)

        session.commit()
        logger.debug(f"Adicionado Financeiro de nome: '{financeiro.nome}'")
        return apresenta_financeiro(financeiro), 200

    except IntegrityError as e:

        error_msg = "Transação de mesmo nome já foi salvo na base :/"
        logger.warning(f"Erro ao adicionar Financeiro '{financeiro.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:

        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar Financeiro '{financeiro.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/financeiros', tags=[financeiro_tag],
         responses={"200": ListagemFinanceirosSchema, "404": ErrorSchema})


def get_financeiros():
    """Faz a busca por todas transações já cadastrados

    Retorna uma representação da listagem de Financeiros.
    """

    logger.debug(f"Coletando Financeiros ")

    session = Session()

    financeiros = session.query(Financeiro).all()

    if not financeiros:
        return {"financeiros": []}, 200
    else:
        logger.debug(f"%d rodutos econtrados" % len(financeiros))
        print(financeiros)
        return apresenta_financeiros(financeiros), 200


@app.get('/financeiro', tags=[financeiro_tag],
         responses={"200": FinanceiroViewSchema, "404": ErrorSchema})


def get_financeiro(query: FinanceiroBuscaSchema):
    """Faz a busca por uma descrição de transação a partir do id do Financeiro

    Retorna uma representação das transações.
    """

    financeiro_nome_desc = query.nome
    logger.debug(f"Coletando dados sobre Financeiro #{financeiro_nome_desc}")

    session = Session()

    financeiro = session.query(Financeiro).filter(Financeiro.nome == financeiro_nome_desc).first()

    if not financeiro:

        error_msg = "Financeiro não encontrado na base :/"
        logger.warning(f"Erro ao buscar Financeiro '{financeiro_nome_desc}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Financeiro econtrado: '{financeiro.nome}'")

        return apresenta_financeiro(financeiro), 200


@app.delete('/financeiro', tags=[financeiro_tag],
            responses={"200": FinanceiroDelSchema, "404": ErrorSchema})


def del_Financeiro(query: FinanceiroBuscaSchema):
    """Deleta uma transação financeiro a partir do nome de financeiro informado

    Retorna uma mensagem de confirmação da remoção.
    """
    financeiro_nome = unquote(unquote(query.nome))
    print(financeiro_nome)
    logger.debug(f"Deletando dados sobre Financeiro #{financeiro_nome}")

    session = Session()

    count = session.query(Financeiro).filter(Financeiro.nome == financeiro_nome).delete()
    session.commit()

    if count:

        logger.debug(f"Deletado Financeiro #{financeiro_nome}")
        return {"mesage": "Financeiro removido", "id": financeiro_nome}
    else:

        error_msg = "Financeiro não encontrado na base :/"
        logger.warning(f"Erro ao deletar Financeiro #'{financeiro_nome}', {error_msg}")
        return {"mesage": error_msg}, 404


