# Meu MVP

Este projeto faz parte do primeiro MVP curso de pós-graduação em Desenvolvimento de Full Stack do ano 2023, pela PUC - Rio.

A proposta do MVP é elaborar uma ideia que atenda um problema do mundo real, depois estrutura as ideias e criar um protótipo da entrega final.

O meu projeto de MVP atende um problema financeiro pessoal um sistema que controla todas despesas e renda do usuario. 
Que possibilita o cliente registar despesas ou entrada da renda.  

Projeto está separado em BackEnd e FrontEnd este repositório consta a aplicação do Backend que fica localizado todas as regras de negocios e API.

Para armazenamento desde dados utilizei banco de dados SQLite que atende demanda inicial do prototipo.

--

## Como executar

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte.

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000](http://localhost:5000) no navegador para verificar o status da API em execução.

Aluno: Victor Mesquita Xavier
