from funcoes import listar_eventos_participantes, buscar_participantes_por_codigo, cadastrar_novo_participante, editar_participante, mostrar_estatisticas, remover_evento, remover_participante 

def exibir_menu():
    print("==== Sistema de Gerenciamento de Eventos ====")
    print("1. Listar eventos e participantes")
    print("2. Buscar participante por código")
    print("3. Cadastrar novo participante")
    print("4. Editar dados de um participante")
    print("5. Mostrar estatísticas dos eventos")
    print("6. Remover evento")
    print("7. Remover participante")

    print( "0. Sair")
    
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha um opção: ")
        
        if opcao == "1":
            listar_eventos_participantes()
        elif opcao == "2":
            buscar_participantes_por_codigo()
        elif opcao == "3":
            cadastrar_novo_participante()
        elif opcao == "4":
            editar_participante()
        elif opcao == "5":
            mostrar_estatisticas()
        elif opcao == "6":
            remover_evento()
        elif opcao == "7":
            remover_participante()
        elif opcao == "0":
            print("Saindo do Sistema...")
            break
        else:
            print("Opção inválida. Tente de novo.") 
 

# para executar o programa
if __name__ == "__main__": 
    main()      
        