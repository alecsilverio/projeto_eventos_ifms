from eventos import (
    listar_eventos_participantes,    
    remover_evento, 
    cadastrar_evento,
    atualizar_tema_evento,
    buscar_eventos_por_tema,
    buscar_eventos_por_faixa_de_datas,
    agrupar_eventos_por_tema,
   
    ) 

from participantes import(
    buscar_participantes_por_codigo, 
    cadastrar_novo_participante, 
    editar_participante, 
    atualizar_email_participante,
    remover_participante,
    remover_participantes_duplicados,
    listar_eventos_por_participante,
    )

from estatisticas import (
    mostrar_estatisticas, 
    contar_eventos_por_tema,
    calcular_media_participantes_por_tema,
    indentificar_eventos_para_cancelamento,
    )
from certificados import gerar_certificados_participante

def exibir_menu():
    print("\n╔════════════════════════════════════════════════╗")
    print("║ 📆   -Sistema de Gerenciamento de Eventos-  📆 ║")
    print("╚════════════════════════════════════════════════╝")
    print("1. Listar eventos e participantes")
    print("2. Buscar participante por código")
    print("3. Cadastrar novo participante")
    print("4. Editar dados de um participante")
    print("5. Mostrar estatísticas dos eventos")
    print("6. Remover evento")
    print("7. Remover participante")
    print("8. Cadastrar novo evento")
    print("9. Atualizar tema de um evento")
    print("10. Atualizar e-mail de um participante")
    print("11. Remover participantes duplicados nos eventos")
    print("12. Buscar eventos por tema")
    print("13. Buscar eventos por faixa de data")
    print("14. Mostrar eventos por tema")
    print("15. Mostrar eventos por participante")
    print("16. Mostrar quantos eventos por tema")
    print("17. Ver a média de participação por tema")
    print("18. Ver eventos com baixa participação")
    print("19. Gerar certificado de participação")
    print( "0. Sair")
    
def main():
    remover_participantes_duplicados(silencioso = True)
    
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: \n")
        
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
        elif opcao =="8":
            cadastrar_evento()
        elif opcao == "9":
            atualizar_tema_evento()
        elif opcao == "10":
            atualizar_email_participante()
        elif opcao =="11":
            remover_participantes_duplicados()
        elif opcao == "12":
            buscar_eventos_por_tema()
        elif opcao == "13":
            buscar_eventos_por_faixa_de_datas()
        elif opcao == "14":
            agrupar_eventos_por_tema()
        elif opcao == "15":
            listar_eventos_por_participante()
        elif opcao == "16":
            contar_eventos_por_tema()
        elif opcao == "17":
            calcular_media_participantes_por_tema()
        elif opcao == "18":
            indentificar_eventos_para_cancelamento()
            
        elif opcao == "19":
            try:
                codigo = int(input("\nDigite o ID do participante:\n "))
                gerar_certificados_participante(
                    codigo,
                    "* Certificado gerado automaticamente pelo Sistema."
                )
            except ValueError:
                print("Digite um número válido.")
                
        elif opcao == "0":
            print("Saindo do Sistema...")
            print("\n")
            break
        else:
            print("Opção inválida. Tente de novo.") 

# para executar o programa
if __name__ == "__main__": 
    main()      
        
