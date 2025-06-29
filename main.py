from funcoes import listar_eventos_participantes, buscar_participantes_por_codigo

def exibir_menu():
    print("==== Sitema de Gerenciamento de Eventos ====")
    print("1. Listar eventos e participantes")
    print("2. Buscar participante por código")
    print( "0. Sair")
    
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha um opção: ")
        
        if opcao == "1":
            listar_eventos_participantes()
        elif opcao == "2":
            buscar_participantes_por_codigo()
        elif opcao == "0":
            print("Saindo do Sistema...")
            break
        else:
            print("Opção inválida. Tente de novo.") 
 

# para executar o programa
if __name__ == "__main__": 
    main()      
        