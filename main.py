import random

def main():
    print("Bem Vindo ao programa de integração ao fã da Mahindra Racing! 🏎️🔋")
    
    # Lista para armazenar os feedbacks
    lista_feedbacks = []
    pontos = 0

    while True:
        print("\nMenu:")
        print("1. Adicionar feedback")
        print("2. Avaliar feedbacks")
        print("3. Mostrar estatísticas do feedback")
        print("4. Participar de uma enquete")
        print("5. Fazer um quiz")
        print("6. Ver pontuação")
        print("7. Sair")
        
        escolha = input("Selecione uma opção (1-7): ").strip()
        
        if escolha == '1':
            feedback = coletar_feedback()
            lista_feedbacks.append(feedback)
            pontos += 10  # Pontos por adicionar feedback
        elif escolha == '2':
            avaliar_feedback(lista_feedbacks)
        elif escolha == '3':
            mostrar_estatisticas(lista_feedbacks)
        elif escolha == '4':
            pontos += participar_enquete()
        elif escolha == '5':
            pontos += fazer_quiz()
        elif escolha == '6':
            mostrar_pontuacao(pontos)
        elif escolha == '7':
            print("Obrigado por utilizar o programa da Mahindra Racing. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, selecione uma opção de 1 a 7.")

# Coleta o feedback do usuário
def coletar_feedback():
    feedback = input("Por favor, digite seu feedback sobre as corridas de Fórmula E: ")
    return feedback

# Avalia o feedback e determina se é positivo ou negativo
def avaliar_feedback(lista_feedbacks):
    feedback_positivo = []
    feedback_negativo = []
    
    for feedback in lista_feedbacks:
        if 'bom' in feedback.lower() or 'ótimo' in feedback.lower() or 'incrível' in feedback.lower():
            feedback_positivo.append(feedback)
        else:
            feedback_negativo.append(feedback)
    
    print(f"\nFeedbacks Positivos - ({len(feedback_positivo)}):")
    for feedback in feedback_positivo:
        print(f"- {feedback}")
    
    print(f"\nFeedbacks Negativos - ({len(feedback_negativo)}):")
    for feedback in feedback_negativo:
        print(f"- {feedback}")

# Mostra estatísticas básicas sobre o feedback coletado
def mostrar_estatisticas(lista_feedbacks):
    total_feedbacks = len(lista_feedbacks)
    feedback_positivo = len([fb for fb in lista_feedbacks if 'bom' in fb.lower() or 'ótimo' in fb.lower() or 'incrível' in fb.lower()])
    feedback_negativo = total_feedbacks - feedback_positivo
    
    print(f"\nEstatísticas do Feedback:")
    print(f"Total de feedbacks: {total_feedbacks}")
    print(f"Feedbacks positivos: {feedback_positivo}")
    print(f"Feedbacks negativos: {feedback_negativo}")

# Participar de uma enquete
def participar_enquete():
    enquetes = [
        "Qual é o seu piloto favorito da Mahindra Racing?",
        "Qual foi a corrida mais emocionante até agora?",
        "O que você gostaria de ver mais nas corridas de Fórmula E?"
    ]
    enquete_escolhida = random.choice(enquetes)
    print(f"\nEnquete: {enquete_escolhida}")
    resposta = input("Digite sua resposta: ")
    print("Obrigado por participar da enquete!")
    return 5  # Pontos por participar da enquete

# Fazer um quiz
def fazer_quiz():
    perguntas = [
        "Qual ano a Mahindra Racing entrou na Fórmula E?",
        "Quantos títulos mundiais de Fórmula E a Mahindra Racing possui?",
        "Quem é o piloto principal da Mahindra Racing?"
    ]
    
    respostas = [
        "2014",
        "0",
        "Oliver Rowland"
    ]
    
    pergunta = random.choice(perguntas)
    index_pergunta = meu_index(perguntas, pergunta)
    print(f"\nQuiz: {pergunta}")
    resposta = input("Digite sua resposta: ")
    
    if resposta == respostas[index_pergunta]:
        print("Resposta correta! Você ganhou 10 pontos.")
        return 10
    else:
        print(f"Resposta errada. A resposta correta era: {respostas[index_pergunta]}.")
        return 0

# Mostrar pontuação
def mostrar_pontuacao(pontos):
    print(f"\nSua pontuação atual é: {pontos} pontos")

def meu_index(lista, buscar):
    for i in range(len(lista)):
        elem = lista[i]
        if elem == buscar:
            return i
    return False

# Rodar a função principal
if __name__ == "__main__":
    main()
