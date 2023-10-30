import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

plataforma_tarefa_subtarefas = {
    "Criação das migrations": [
        "Criar migration para a tabela de Endereços",
        "Criar migration para a tabela de Empresas",
        "Criar migration para a tabela de Usuários",
        "Criar migration para a tabela de Feedbacks",
        "Criar migration para a tabela de Requisições",
        "Criar migration para a tabela de Local Requisitado",
        "Criar migration para a tabela de Origem do Usuário",
        "Criar migration para a tabela de Idas dos ônibus",
        "Criar migration para a tabela de Voltas dos ônibus",
        "Criar migration para a tabela de Ônibus",
        "Criar migration para a tabela de Rotas",
        "Criar migration para a tabela de Itinerários",
        "Revisar as migrations criadas",
        "Implementar código de roll back para as migrations"
    ],
    "Criação das factories": [
        "Criar factory para a tabela de Endereços",
        "Criar factory para a tabela de Empresas",
        "Criar factory para a tabela de Usuários",
        "Criar factory para a tabela de Feedbacks",
        "Criar factory para a tabela de Requisições",
        "Criar factory para a tabela de Local Requisitado",
        "Criar factory para a tabela de Origem do Usuário",
        "Criar factory para a tabela de Idas dos ônibus",
        "Criar factory para a tabela de Voltas dos ônibus",
        "Criar factory para a tabela de Ônibus",
        "Criar factory para a tabela de Rotas",
        "Criar factory para a tabela de Itinerários",
        "Gerar 50 dados de cada factory",
        "Seedar banco de dados"
    ],
    "Configuração da validação de dados": [
        "Criar validação de dados para inserções das tabelas",
        "Criar validação de dados para atualizações das tabelas",
        "Configurar validação de inserção de dados para todas as tabelas",
        "Configurar validação de atualização de dados para todas as tabelas"
    ],
    "Criação dos modelos do sistema": [
        "Criar o model para cada tabela do banco de dados",
        "Configurar nome das tabelas nos models",
        "Estabelecer a insistência o campo timestamp dos models",
        "Estabelecer relação entre os models",
        "Listar dados que serão daquele model"
    ],
    "Criação das rotas": [
        "Criar rota de Home",
        "Criar rota de Login e Cadastro",
        "Criar rota de Visualização de ônibus",
        "Criar rota de Visualização de Itinerários",
        "Criar rota de Painel de controle",
        "Agrupar rotas por controlador ou resource",
        "Nomear rotas adequadamente",
        "Aplicar middlewares nas rotas que precisam"
    ],
    "Criação dos controladores": [
        "Criar métodos padrões dos controladores que precisam",
        "Identificar necessidade de métodos padrões nos controladores",
        "Identificar métodos necessários e listar aqui",
        "Criar métodos necessários",
        "Implementar métodos necessários"
    ],
    "Definição dos requisitos de design": [
        "Identificar público alvo",
        "Escolher cores e fontes",
        "Escolher estrutura do website"
    ],
    "Criação dos componentes": [
        "Criar navbar",
        "Criar footer",
        "Criar formulário",
        "Criar botão"
    ],
    "Criação das views": [
        "Criar layout padrão para as views",
        "Aplicar layout nas views",
        "Criar view de Home",
        "Criar view de Login e Cadastro",
        "Criar view de Visualização de ônibus",
        "Criar view de Visualização de Itinerários",
        "Criar view de Painel de controle",
        "Implementar componentes no layout (caso haja algum)"
    ],
    "Realizar testes unitários": [
        "Testar cada método do sistema"
    ],
    "Definição dos gráficos e tabelas": [
        "Escolher quais gráficos serão usados",
        "Escolher quais tabelas serão usadas",
        "Listar componentes que serão usados",
        "Entender o funcionamento e necessidade de cada componente."
    ],
    "Inserção de dados reais": [
        "Trocar dados de teste por dados reias",
        "Corretamente inserir novos dados e dar fresh no banco de dados",
        "Executar testes e listar problemas encontrados pós troca de dados"
    ],
    "Revisão do código": [
        "Revisar lógica aplicada",
        "Revisar comentários escritos no código",
        "Revisar implementação das views",
        "Revisar banco de dados",
        "Revisar resultado de queries e validações de dados"
    ],
    "Implementação das views": [
        "Implementar parte funcional das views",
        "Aplicar CSS custom nas views",
        "Organizar estrutura seguindo o padrão Bootstrap",
        "Aplicar CSS nativo do Bootstrap nas views"
    ],
    "Implementação dos componentes": [
        "Implementar funcionalidades dos componentes",
        "Aplicar CSS customizado nos componentes se necessário"
    ],
    "Implementação dos gráficos do painel de controle": [
        "Tratar envio de dados para os gráficos e tabelas",
        "Implementar funcionalidades de inserção ou atualização de tabelas",
        "Implementar filtragem de dados dos gráficos e tabelas",
        "Implementar mostra dos dados nos gráficos"
    ],
    "Realizar testes com dados reais": [
        "Documentar resultados dos testes",
        "Avaliar os testes feitos",
        "Concertar possíveis problemas encontrados durante os testes feitos"
    ],
    "Criar testes automatizados": []
}
plataforma_tarefas = list(plataforma_tarefa_subtarefas.keys())

tcc_tarefa_subtarefas = {
    "Planejamento inicial": [
        "Coletar todos os documentos já redigidos",
        "Listar documentos desatualizados",
        "Atualizar documentos desatualizados",
        "Definir horários e responsáveis por tarefa",
        "Adicionar mais tarefas caso necessário"
    ],
    "Divisão da equipe": [
        "Divisão do grupo em duas equipes",
        "Separar tarefas para cada equipe/pessoa 01"
    ],
    "Criação do repositório no Github": [
        "Criar repositório no Github",
        "Definir repositório como privado",
        "Convidar participantes para o repositório",
        "Definir regras de acesso do repositório",
        "Configurar .gitignore",
        "Adicionar README"
    ],
    "Parte escrita": [
        "Encontrar template pra parte escrita",
        "Pesquisar exemplos de escritas TCC",
        "Redigir Introdução",
        "Adicionar referencias que justificam as ideias da introdução",
        "Redigir Objetivos do trabalho",
        "Adicionar referencias que justificam as ideias do objetivo do trabalho",
        "Redigir Visão do sistema",
        "Descrever planejamento tecnologias e objetivos da plataforma ou sistema",
        "Escrever campo para citar informações relevantes",
        "Começar banco de dados, explicar o proposito do banco para o sistema e abstração feita",
        "Escrever campo para citar informações relevantes",
        "Redigir Justificativa",
        "Listar todas as referências seguindo a norma ABNT",
        "Redigir Análise dos resultados",
        "Redigir Conclusão"
    ],
    "Apresentação mundo SENAI": [
        "Preparar slide",
        "Preparar roteiro"
    ],
    "Slide de apresentação": [
        "Estruturar ordem das informações",
        "Listar informações que serão usadas no Slide",
        "Pesquisar dicas e exemplos de inspiração",
        "Escolher fontes e cores",
        "Escolher elementos gráficos que serão usados nos slides",
        "Revisar e refatorar slide"
    ],
    "Preparação para apresentação": [
        "Criar roteiro de apresentação",
        "Garantir que todos estão em sintonia com o assunto",
        "Usar IA para criar perguntas sobre nosso TCC",
        "Estudar perguntas feitas pela IA e o assunto do TCC",
        "Dividir 'falas'"
    ],
    "Revisão geral": [
        "Revisar código do sistema",
        "Revisar slide de apresentação",
        "Revisar parte escrita",
        "Revisar manual do usuário",
        "Realizar testes no sistema",
        "Fazer um test-drive do funcionamento do sistema",
        "Corrigir bugs que podem aparecer",
        "Revisar conhecimento da equipe no assunto",
        "Realizar uma roda de conversa sobre o TCC (Isso foi um baita aventura, não foi?)"
    ]
}
tcc_tarefas = list(tcc_tarefa_subtarefas.keys())

manual_tarefa_subtarefas = {
    "Reunião 02": [],
    "Termo de abertura": [],
    "Escolher fontes e cores": [],
    "Criar wireframes para o manual": [],
    "Estruturar o layout do manual": [],
    "Definir estrutura das informações": [],
    "Revisar manual": [],
    "Coletar imagens e vídeos que serão usados no manual": [],
    "Redigir versão 1 do manual": [
        "Texto de introdução do sistema para os usuarios",
        "Texto de introdução do sistema para as empresas",
        "Criar layout da tela padrão"
    ],
    "Texto de introdução do sistema para os usuarios": [],
    "Texto de introdução do sistema para as empresas": [],
    "Criar layout da tela padrão": [],
    "Implementar funcionalidades especificas do manual": [],
    "Identificar e corrigir problemas": [],
    "Executar testes de usabilidade": [],
    "Reunião 01": [
        "Definir Objetivos do manual"
    ],
    "Definir Objetivos do manual": [],
    "Redigir manual escrito": [],
    "Criação do repositório do GitHub": [],
    "Criar arquivo CSS customizado com nossa paleta de cores": [],
    "Definir telas do manual de usuários": [
        "Definir informações que serão mostradas em cada tela"
    ],
    "Definir telas do manual de empresas": [
        "Definir informações que serão mostradas em cada tela"
    ]
}
manual_tarefas = list(manual_tarefa_subtarefas.keys())

# Entrar no site do trello
driver = webdriver.Edge()
driver.get('https://trello.com/b/nmUvjDF5/tcc-geral')


def login_to_trello():
    # Encontrar link de login
    link_login = driver.find_element(By.XPATH, "//button[@data-testid='request-access-login-button']")

    # Clicar no link de login
    link_login.click()
    time.sleep(3)

    # Encontrar o campo de e-mail e o botão de continuação
    email_field = driver.find_element(By.XPATH, "//input[@id='user']")
    continue_button = driver.find_element(By.XPATH, "//input[@id='login']")

    # Preencher o campo de e-mail
    email_field.send_keys("antonio.neto12@ba.estudante.senai.br")
    time.sleep(1)

    # Clicar no botão de continuação
    continue_button.click()
    time.sleep(3)

    # Encontrar o campo de senha e o botão de login final
    password_field = driver.find_element(By.XPATH, "//input[@name='password']")
    login_final_button = driver.find_element(By.XPATH, "//button[@id='login-submit']")

    # Preencher o campo de senha
    password_field.send_keys("marcosDE22")

    # Clicar no botão de login final
    login_final_button.click()


# Efetua login no trello
login_to_trello()

# Aguarda 10 segunos
time.sleep(10)

# Cria uma espera customizada
wait = WebDriverWait(driver, 10)

# Encontrar botão de criação de novo card
create_new_card_button = driver.find_element(By.XPATH,
                                             "//h2[text()='To Do']/following::a[@data-testid='list-add-card-button']")
# Clicar no botão de criação de novo card
create_new_card_button.click()

# Pra cada super-tarefa
for tarefa in tcc_tarefas:
    # Obter novamente o elemento do campo de texto após adicionar um cartão
    card_title_textarea = driver.find_element(By.XPATH, "//textarea[@data-testid='list-card-composer-textarea']")

    # Colar o nome da tarefa no textarea
    card_title_textarea.send_keys(tarefa)
    time.sleep(0.5)
    # Precionar ENTER
    card_title_textarea.send_keys(Keys.ENTER)
    time.sleep(0.5)

    time.sleep(2)  # ...

    if len(tcc_tarefa_subtarefas[tarefa]) > 0:
        # Localize o card com base no título
        new_card = driver.find_element(By.XPATH, f"//span[contains(text(), '{tarefa}')]/ancestor::a")
        # Clicar no card
        new_card.click()
        # Localizar botão de criação de checklist
        create_checklist_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Checklist']")))
        # Clicar no botão de criar novo checklist
        create_checklist_button.click()

        time.sleep(2)  # ...

        # Localizar o campo de inserção de nome do checklist
        checklist_name_field = driver.find_element(By.XPATH, "//input[@id='id-checklist']")
        # Colar nome do checklist
        checklist_name_field.send_keys("Subtarefas")

        # Localize o botão para adicionar o checklist e clique nele
        add_checklist_button = driver.find_element(By.XPATH, "//input[@value='Add']")
        add_checklist_button.click()

        time.sleep(2)

        # Para cada sub-tarefa dentro da super-tarefa
        for subtarefa in tcc_tarefa_subtarefas[tarefa]:
            # Localizar campo de inserção do nome da subtarefa
            subtask_field = driver.find_element(By.XPATH, "//textarea[@placeholder='Add an item']")
            # Colar o nome da subtarefa
            subtask_field.send_keys(subtarefa)
            time.sleep(0.5)
            # Apertar ENTER
            subtask_field.send_keys(Keys.ENTER)
            time.sleep(1)
        # Localizar botão de fecharo card aberto
        close_card = driver.find_element(By.XPATH,
                                         "//a[@class='icon-md icon-close dialog-close-button js-close-window']")
        # Clicar no botão de fechar o card
        close_card.click()
        time.sleep(1)

        # Encontrar botão de criação de novo card
        create_new_card_button = driver.find_element(By.XPATH,
                                                     "//h2[text()='To Do']/following::a[@data-testid='list-add-card-button']")
        # Clicar no botão de criação de novo card
        create_new_card_button.click()
    else:
        continue

print('hello')

time.sleep(40)

driver.quit()
