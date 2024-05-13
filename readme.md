## Exercício Prático - Mock Object


### Objetivo:

Part 1

Implementar os testes de unidade da classe CustomStack desenvolvida de forma que a cobertura seja igual a 100% (usar ferramentas como o pytest-cov para analisar a cobertura).

Parte 2

A equipe da Caixa Econômica Federal, tem como objetivo desenvolver uma classe com responsabilidade de coletar todos os número sorteados da Mega Sena que estarão armazenados em um objeto CustomStack, conforme ordem do sorteio realizado, e ordená-los de forma ascendente.


### Clone do repositório 

```bash

git clone 
cd 
```

### Configurarando o Ambiente Virtual

Antes de instalar as dependências, configure um ambiente virtual para isolar as instalações. Se você estiver usando venv (recomendado para Python 3.3 e superiores):
Para usuários de Windows:

```bash

python -m venv venv
venv\Scripts\activate
```
Para usuários de macOS e Linux:

```bash

python3 -m venv venv
source venv/bin/activate
```
### Instalar Dependências

Com o ambiente virtual ativado, instale as dependências necessárias:

```bash

pip install -r requirements.txt
```

### Executando os Testes

Para verificar se tudo está funcionando como esperado, execute os testes com o seguinte comando:

```bash

pytest --cov=custom_stack tests/
```

Isso rodará todos os testes definidos no diretório tests e mostrará um relatório de cobertura do código.