# Projeto Banco Relacional e NoSQL

Este projeto consiste na implementação de uma aplicação que integra um banco de dados relacional utilizando SQLAlchemy e um banco de dados NoSQL com MongoDB.

## Parte 1 - Banco de Dados Relacional com SQLAlchemy

Nesta parte do projeto, desenvolvi uma API Flask-RESTful que se conecta a um banco de dados SQLite (ou MySql) utilizando SQLAlchemy. As tabelas do banco de dados relacional são 
modeladas com base no esquema fornecido, que inclui informações sobre clientes e contas. As classes em Python são criadas para representar as tabelas do banco de dados relacional. 
A API permite operações CRUD (Create, Read, Update, Delete).

### Principais Componentes

* Flask-RESTful: Extensão do Flask para criação de APIs RESTful em Python.
* SQLAlchemy: Biblioteca Python para interação com bancos de dados relacionais.
* Modelagem de Dados: Definição de modelos de dados como classes Python usando SQLAlchemy.
* Operações CRUD: Implementação das operações CRUD para manipulação de recursos.
* 
### features futuras:

* [ ] Autenticação de usuário
* [ ] Testes unitários 
* [ ] Validação dos dados de entrada mais robusto (Já é feita uma validação através de schemas)
## Parte 2 - Banco de Dados NoSQL com MongoDB

Na segunda parte do projeto, foi implementado um banco de dados NoSQL utilizando MongoDB. Aqui estão as etapas realizadas:

* Conexão ao MongoDB Atlas e criação de um banco de dados.
* Definição de uma coleção "bank" para armazenar documentos de clientes.
* Inserção de documentos com a estrutura mencionada.
* Escrita de instruções para recuperar informações com base nos pares de chave e valor.
