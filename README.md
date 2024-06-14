# Mahindra Racing Fan Integration Program 🏎️🔋

Este projeto Python foi desenvolvido para aumentar a visibilidade da Fórmula E e da Mahindra Racing, permitindo que os fãs interajam através de feedbacks, enquetes e quizzes, ganhando pontos por suas participações.

## Funcionalidades 🔧

- **Adicionar Feedback**: Os usuários podem adicionar seus feedbacks sobre as corridas de Fórmula E.
- **Avaliar Feedbacks**: O sistema categoriza os feedbacks como positivos ou negativos.
- **Mostrar Estatísticas do Feedback**: Exibe estatísticas básicas sobre os feedbacks coletados.
- **Participar de Enquetes**: Os usuários podem participar de enquetes relacionadas à Fórmula E.
- **Fazer um Quiz**: Os usuários respondem a perguntas sobre a Mahindra Racing e ganham pontos por respostas corretas.
- **Ver Pontuação**: Os usuários podem ver sua pontuação atual.

## Dependências 🖇️

Certifique-se de ter o Python instalado na sua máquina. Este script não possui dependências externas adicionais.

## Instalação 💾

1. Clone o repositório:
    ```bash
    git clone https://github.com/mahindraracing/python-sprint.git
    cd python-sprint
    ```
2. Execute o script:
    ```bash
    python main.py
    ```

## Como Utilizar 💡

1. Ao rodar o script, você será apresentado ao menu principal.
2. Selecione uma opção do menu para adicionar feedback, avaliar feedbacks, mostrar estatísticas, participar de enquetes, fazer um quiz, ver sua pontuação ou sair do programa.
3. Siga as instruções na tela para interagir com o programa.

## Explicação das Funções 💬

### Função Principal `main()`
- **Descrição**: Inicializa o programa e exibe o menu principal.
- **Bloco de Código**:
    ```python
    import random

    def main():
        print("Bem Vindo ao programa de integração ao fã da Mahindra Racing! 🏎️🔋")
        
        # Lista para armazenar os feedbacks
        lista_feedbacks = []
        # Lista para armazenar os pontos do usuário
        pontos = 0

        # Loop para o menu
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
            
            # Escolhas
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
    ```

### Função `coletar_feedback()`
- **Descrição**: Coleta o feedback do usuário.
- **Retorno**: Feedback fornecido pelo usuário.
- **Bloco de Código**:
    ```python
    def coletar_feedback():
        feedback = input("Por favor, digite seu feedback sobre as corridas de Fórmula E: ")
        return feedback
    ```

### Função `avaliar_feedback(lista_feedbacks)`
- **Descrição**: Avalia os feedbacks e categoriza como positivos ou negativos.
- **Parâmetros**: `lista_feedbacks` - Lista de feedbacks coletados.
- **Bloco de Código**:
    ```python
    def avaliar_feedback(lista_feedbacks):
        feedback_positivo = []
        feedback_negativo = []
        
        # Uso de palavras chaves para feedback positivo ou negativo
        for feedback in lista_feedbacks:
            if 'bom' in feedback.lower() or 'ótimo' in feedback.lower() or 'incrível' in feedback.lower():
                feedback_positivo.append(feedback)
            else:
                feedback_negativo.append(feedback)
        
        # Mostrar feedbacks
        print(f"\nFeedbacks Positivos - ({len(feedback_positivo)}):")
        for feedback in feedback_positivo:
            print(f"- {feedback}")
        
        print(f"\nFeedbacks Negativos - ({len(feedback_negativo)}):")
        for feedback in feedback_negativo:
            print(f"- {feedback}")
    ```

### Função `mostrar_estatisticas(lista_feedbacks)`
- **Descrição**: Mostra estatísticas básicas sobre os feedbacks coletados.
- **Parâmetros**: `lista_feedbacks` - Lista de feedbacks coletados.
- **Bloco de Código**:
    ```python
    def mostrar_estatisticas(lista_feedbacks):
        # Analisa a quantidade de estatísticas
        total_feedbacks = len(lista_feedbacks)
        feedback_positivo = len([fb for fb in lista_feedbacks if 'bom' in fb.lower() or 'ótimo' in fb.lower() or 'incrível' in fb.lower()])
        feedback_negativo = total_feedbacks - feedback_positivo
        
        # Mostrar quantidade de estatísticas
        print(f"\nEstatísticas do Feedback:")
        print(f"Total de feedbacks: {total_feedbacks}")
        print(f"Feedbacks positivos: {feedback_positivo}")
        print(f"Feedbacks negativos: {feedback_negativo}")
    ```

### Função `participar_enquete()`
- **Descrição**: Apresenta uma enquete ao usuário e coleta sua resposta.
- **Retorno**: Pontos ganhos por participar da enquete.
- **Bloco de Código**:
    ```python
    def participar_enquete():
        # Enquetes
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
    ```

### Função `fazer_quiz()`
- **Descrição**: Apresenta uma pergunta de quiz ao usuário e verifica a resposta.
- **Retorno**: Pontos ganhos pela resposta correta.
- **Bloco de Código**:
    ```python
    def fazer_quiz():
        # Lista de perguntas
        perguntas = [
            "Qual ano a Mahindra Racing entrou na Fórmula E?",
            "Quantos títulos mundiais de Fórmula E a Mahindra Racing possui?",
            "Quem é o piloto principal da Mahindra Racing?"
        ]

        # Lista de respostas
        respostas = [
            "2014",
            "0",
            "Oliver Rowland"
        ]
        
        pergunta = random.choice(perguntas)
        index_pergunta = meu_index(perguntas, pergunta)
        print(f"\nQuiz: {pergunta}")
        resposta = input("Digite sua resposta: ")
        
        # Verificar resposta
        if resposta == respostas[index_pergunta]:
            print("Resposta correta! Você ganhou 10 pontos.")
            return 10 # Retorna 10 pontos caso resposta for correta
        else:
            print(f"Resposta errada. A resposta correta era: {respostas[index_pergunta]}.")
            return 0 # Retorna 0 pontos caso resposta for errada
    ```

### Função `mostrar_pontuacao(pontos)`
- **Descrição**: Exibe a pontuação atual do usuário.
- **Parâmetros**: `pontos` - Pontuação atual do usuário.
- **Bloco de Código**:
    ```python
    def mostrar_pontuacao(pontos):
        print(f"\nSua pontuação atual é: {pontos} pontos")
    ```

### Função `meu_index(lista, buscar)`
- **Descrição**: Encontra o índice de um item em uma lista.
- **Parâmetros**: `lista` - Lista de itens. `buscar` - Item a ser encontrado.
- **Retorno**: Índice do item ou `False` se não encontrado.
- **Bloco de Código**:
    ```python
    def meu_index(lista, buscar):
        for i in range(len(lista)):
            elem = lista[i]
            if elem == buscar:
                return i
        return False
    ```

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Sinta-se à vontade para contribuir com este projeto e ajudar a aumentar a visibilidade da Fórmula E e da Mahindra Racing! 🏎️🔋
