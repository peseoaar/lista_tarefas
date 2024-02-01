# adicionar sistema de id com tabela hash igual no video dos favoritos
def mostrar_tarefas():
    with open('lista_tarefas.txt','r') as arquivo_r:
        ler = arquivo_r.read()
        print("\n",ler,"\n")
        def opcao_mostrar():
            opcao = int(input("(1)voltar ao menu (2)sair: "))
            if opcao==1:
                menu()
            elif opcao==2:
                exit
            else:
                print("\n Opcao inexixtente!")
                opcao_mostrar()
        opcao_mostrar()

def adicionar_tarefas():
    with open('lista_tarefas.txt','r+') as arquivo_a:
        ctd_linha = arquivo_a.readlines()
    

        if len(ctd_linha) > 0:
            id_maior=0
            for linha in ctd_linha[1:]:  
                id_split = linha.split(";")[0].strip()
                if id_split.isdigit():
                    id_aux = int(id_split)
                    if id_aux > id_maior:
                        id_maior = id_aux
                
            id = str(id_maior + 1)
        else:
            id = '1'
        
        tarefa = str(input("Tarefa: "))
        prioridade = int(input("Prioridade (1~3): "))
        arquivo_a.write("\n {};       {}        {}".format(id, prioridade, tarefa))
       
        def opcao():  
            opcao = int(input("(1)Continuar adicionando (2)Voltar ao Menu: "))
            if opcao == 1:
                adicionar_tarefas()
            elif opcao == 2:
                menu()
            else:
                print("\nOpcao inexistente!\n")
                opcao()
        
        print("\nTarefa adicionada a lista\n")
        opcao()
        
    
def excluir_tarefas():
    id_digitado = int(input("Id da tarefa a ser excludia:"))
    
    novas_linhas = []

    with open("lista_tarefas.txt","r+") as excluir_r:
            
        def opcao_excluir(): 
            opcao = int(input("[1]continuar excluindo [2]voltar ao menu: "))
            if opcao == 1:
                return excluir_tarefas()
            elif opcao == 2:
                return menu()
            else:
                print("Opcao nao existente!")
                opcao_excluir()

        linhas = excluir_r.readlines()
        count=0
        for linha in linhas[1:]:
            id_split = linha.split(";")[0].strip()

            if id_split.isdigit():
                id = int(id_split)
                if id == id_digitado:
                    count+=1
                else:
                    novas_linhas.append(linha) # se nao for o id, volta com as linhas que pegou para o lugar delas
        if count == 1:
            with open("lista_tarefas.txt","w") as excluir_w:
                excluir_w.write(linhas[0])
                for linha in novas_linhas:
                    excluir_w.write(linha)
                print("Tarefa excluida com sucesso!")
                opcao_excluir()
        elif count == 0:
            print("Tarefa nao encontrada!")
            opcao_excluir()
                
                
def menu():
    print("\n------LISTA DE TAREFAS------\n")
    print("1 - Mostrar Tarefas\n2 - Adicionar Tarefa\n3 - Excluir Tarefa\n4 - Sair\n")
    escolha_menu = int(input("Escolha uma opcao: "))
    match escolha_menu:
        case 1:
            mostrar_tarefas()
        case 2:
            adicionar_tarefas()
        case 3:
            excluir_tarefas()
        case 4:
            exit()
menu()



