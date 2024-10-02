# DiretoAí


O **DiretoAí** é uma aplicação simples desenvolvida em Python para cadastrar e gerenciar restaurantes. O projeto foi criado durante com intuito de gerar uma interface dinâmica para cadastrar, listar e alterar o estado de atividade dos restaurantes. Cada restaurante cadastrado começa com o status inativo, conforme a regra de negócio.

## Funcionalidades

- **Cadastro de Restaurantes**: Permite cadastrar restaurantes com nome e categoria. Todos os restaurantes começam com o status de "inativo".
- **Listagem de Restaurantes**: Lista todos os restaurantes cadastrados com nome, categoria e estado (ativado/desativado).
- **Alteração de Estado**: Possibilita ativar ou desativar um restaurante.
- **Sair da aplicação**: Opção para finalizar a aplicação de forma segura.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para implementação da aplicação.
- **Biblioteca `os`**: Usada para limpar a tela e melhorar a interface da linha de comando.
- **Estrutura de Controle**: Utiliza `match case` para seleção de opções no menu.
- **Programação Funcional**: Estrutura baseada em funções modulares para cada operação.

## Requisitos de Negócio

- Todo restaurante criado começa com o **status inativo**.
- As opções disponíveis no menu são:
  - Cadastrar um novo restaurante
  - Listar todos os restaurantes
  - Alterar o estado (ativar/desativar) de um restaurante
  - Sair da aplicação

## Como Executar

1. Verifique se o python esta instalado na sua máquina.


2. Clone o repositório:
   ```bash
   git clone https://github.com/GuilhermeEnrique18/DiretoAi-.git

3. Abra a pasta no editor de texto da sua preferência.

## Demonstração
Quando a aplicação é iniciada, o usuário verá o menu principal com as opções:

```python
1. Cadastrar restaurante
2. Listar restaurante
3. Alternar estado do restaurante
4. Sair

```

### Exemplo de Cadastro de Restaurante:
Ao selecionar a opção "1", você será instruído a inserir o nome e a categoria do restaurante. Após o cadastro, o restaurante estará na lista com o status inativo.

### Exemplo de Listagem:
Selecionando a opção "2", será exibida uma tabela com todos os restaurantes cadastrados, incluindo nome, categoria e estado.

### Exemplo de Alteração de Estado:
Na opção "3", você pode alternar o estado de um restaurante, ativando ou desativando-o com base no nome informado.

## Melhorias Futuras
Apesar de ser uma aplicação simples, o projeto "DiretoAí" abre espaço para muitas melhorias, como:

- Integração com um banco de dados para armazenamento persistente.
- Interface gráfica para facilitar o uso.
- Filtros de pesquisa para buscar restaurantes por categoria ou estado.
