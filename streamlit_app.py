#Fórum de discussão simples para estudantes

forum = {}  # Chave: tópico, Valor: lista de mensagens

def criar_topico():
    topico = input("Digite o nome do tópico: ")
    if topico in forum:
        print("Tópico já existe!")
    else:
        forum[topico] = []
        print(f"Tópico '{topico}' criado com sucesso!")

def postar_mensagem():
    topico = input("Digite o tópico que deseja postar: ")
    if topico not in forum:
        print("Tópico não existe!")
        return
    mensagem = input("Digite sua mensagem: ")
    autor = input("Seu nome: ")
    forum[topico].append(f"{autor}: {mensagem}")
    print("Mensagem postada com sucesso!")

def ver_topicos():
    if not forum:
        print("Nenhum tópico disponível.")
    else:
        print("Tópicos disponíveis:")
        for t in forum:
            print(f"- {t}")

def ver_mensagens():
    topico = input("Digite o tópico que deseja ver: ")
    if topico not in forum:
        print("Tópico não existe!")
        return
    print(f"Mensagens do tópico '{topico}':")
    for msg in forum[topico]:
        print(f" {msg}")

def menu():
    while True:
        print("\n=== Fórum de Estudantes ===")
        print("1. Criar tópico")
        print("2. Postar mensagem")
        print("3. Ver tópicos")
        print("4. Ver mensagens de um tópico")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            criar_topico()
        elif escolha == "2":
            postar_mensagem()
        elif escolha == "3":
            ver_topicos()
        elif escolha == "4":
            ver_mensagens()
        elif escolha == "5":
            print("Saindo do fórum...")
            break
        else:
            print("Opção inválida!")

# Inicia o fórum
menu()
