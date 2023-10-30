# campo de texto //textarea[@placeholder='Insira um título para este cartão...']
# botão //li[@data-list-id='6534256421c3983094ef5ccb']//div[@data-testid='list-footer']//button

from selenium import webdriver
import pandas as pd

tarefas_pai = [
    "Planejamento inicial",
    "Divisão da equipe",
    "Criação do repositório no Github",
    "Manual do usuário",
    "Parte escrita",
    "Apresentação mundo SENAI",
    "Criação das migrations",
    "Criação das factories",
    "Configuração da validação de dados",
    "Criação dos modelos do sistema",
    "Criação das rotas",
    "Criação dos controladores",
    "Definição dos requisitos de design",
    "Criação dos componentes",
    "Criação das views",
    "Realizar testes unitários",
    "Definição dos gráficos e tabelas",
    "Inserção de dados reais",
    "Revisão do código",
    "Implementação das views",
    "Implementação dos componentes",
    "Implementação dos gráficos do painel de controle",
    "Realizar testes com dados reais",
    "Criar testes automatizados",
    "Slide de apresentação",
    "Preparação para apresentação",
    "Revisão geral"
]

# Guardar apenas os nomes das tarefas do arquivo .csv
tarefas = pd.read_csv('tarefas-tcc.csv')
nomes_tarefas = tarefas['Name']


for nome in nomes_tarefas:
    print(nome)




# Abrir o site do Trello no board de TCC

# Clicar no botão de adicionar cartão
# Para cada nome na lista de tarefas
# Colar o nome no campo de texto
# Apertar enter
