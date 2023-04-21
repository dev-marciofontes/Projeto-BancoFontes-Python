# Projeto-BancoFontes-Python 

## Banco Fontes SA

O Banco Fontes SA é um programa em Python que simula operações bancárias básicas, como depósitos, saques e a visualização de extratos. O programa é uma aplicação de linha de comando simples e fácil de usar.

Este é um projeto simples e útil para quem deseja praticar seus conhecimentos em programação, especialmente em Python. Com ele, é possível aprender conceitos básicos de controle de fluxo, entrada e saída de dados, e manipulação de variáveis, além de se familiarizar com a linguagem de programação em si.

### [Versão 1.0 - 18/04/2023](https://github.com/dev-marciofontes/Projeto-BancoFontes-Python/blob/V1.0)

Na versão 1.0, as principais funcionalidades incluem:

- Depósito de valores
- Saque de valores (com limite de valor e quantidade de saques por dia)
- Visualização de extrato com as movimentações e saldo atual

Esta versão é uma aplicação simples e direta, com todas as operações realizadas em um único loop principal.

### [Versão 2.0 - 19/04/2023](https://github.com/dev-marciofontes/Projeto-BancoFontes-Python/blob/V2.0/)

A versão 2.0 inclui várias melhorias e novas funcionalidades em comparação com a versão 1.0:

- Refatoração do código, com a criação de funções para cada operação bancária, melhorando a organização e a legibilidade do código.
- Implementação de um menu de login, permitindo a criação de novas contas, listagem de contas, criação de novos usuários e autenticação de login.
- Várias contas e usuários podem ser criados e gerenciados.
- A autenticação de login é realizada com base no número da conta e senha, com um limite de tentativas.
- Mensagem de boas-vindas personalizada exibida após o login bem-sucedido.
- Acesso às operações bancárias somente após a autenticação bem-sucedida.

Com estas melhorias e novas funcionalidades, a versão 2.0 oferece uma experiência de usuário aprimorada e mais realista em comparação com a versão 1.0.

### [Versão 3.0 - 21/04/2023](https://github.com/dev-marciofontes/Projeto-BancoFontes-Python/blob/V3.0/)

A versão 3.0 inclui várias melhorias e foi aplicada a Orientação a Objetos em Python.

A versão orientada a objetos do sistema bancário foi refatorada para utilizar classes e objetos para representar entidades do sistema e organizar melhor o código.

Principais mudanças:

- Criação das classes Cliente, Conta, Transacao, Deposito, Saque e Historico
- Métodos de instância para realizar operações bancárias, tais como depositar, sacar e exibir extrato
- Uso de herança para definir tipos específicos de transações (Deposito e Saque)
- Encapsulamento dos dados e comportamentos relacionados em classes e objetos
- Refatoração do loop principal para trabalhar com os objetos e métodos das classes criadas
- A senha foi incorporada à classe Conta e o método sacar foi modificado para solicitar a senha antes de realizar a operação, garantindo maior segurança nas transações.
