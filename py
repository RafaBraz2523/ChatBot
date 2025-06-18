import datetime
import webbrowser  # 🔍 Para abrir o navegador automaticamente

# Nome do usuário
nome = input("Chatbot: Olá! Qual é o seu nome?\nVocê: ")
print(f"Chatbot: Muito prazer, {nome}! Pode começar. (Digite 'sair' para encerrar)")

# Tabela de respostas com palavras-chave
respostas = {
    "oi": f"Oi, {nome}! Como posso te ajudar?",
    "olá": f"Oi, {nome}! Como posso te ajudar?",
    "seu nome": "Sou um chatbot criado em Python para fins educacionais.",
    "meu nome": f"Seu nome é {nome}, certo?",
    "capital brasil": "A capital do Brasil é Brasília.",
    "tudo bem": "Estou ótimo! E você?",
    "hora": f"Agora são {datetime.datetime.now().strftime('%H:%M:%S')}.",
    "data": f"Hoje é {datetime.datetime.now().strftime('%d/%m/%Y')}.",
    "programar": "Programar é uma das habilidades mais valiosas hoje em dia!",
    "python": "Python é ótimo para automação, IA, e muito mais.",
    "idade": "Eu não tenho idade, sou apenas um código 😄",

    # Novas perguntas
    "clima": "Eu não consigo acessar o clima em tempo real, mas espero que esteja um bom dia aí!",
    "futebol": "Futebol é uma paixão nacional! Qual time você torce?",
    "filme": "Gosto muito de filmes de ficção científica. E você, qual é o seu favorito?",
    "música": "A música anima qualquer momento! Qual estilo você mais gosta?",
    "piada": "Por que o jacaré tirou o filho da escola? Porque ele réptil de ano! 😂",
    "inteligência artificial": "Inteligência Artificial é a capacidade de máquinas imitarem a inteligência humana.",
    "faculdade": "Estudar é essencial! Continue firme na sua jornada acadêmica.",

    "ajuda": (
        "Você pode me perguntar sobre:\n"
        "- Seu nome\n"
        "- Hora e data\n"
        "- Capital do Brasil\n"
        "- Programação, Python e IA\n"
        "- Clima, futebol, filmes, música, piadas\n"
        "- Compras e muito mais!"
    ),
    "menu": (
        "Você pode me perguntar sobre:\n"
        "- Seu nome\n"
        "- Hora e data\n"
        "- Capital do Brasil\n"
        "- Programação, Python e IA\n"
        "- Clima, futebol, filmes, música, piadas\n"
        "- Compras e muito mais!"
    ),
    "tchau": f"Tchau, {nome}! Foi um prazer conversar com você!",
    "adeus": f"Tchau, {nome}! Foi um prazer conversar com você!"
}

# Função de resposta
def responder(pergunta):
    pergunta = pergunta.lower()

    # Amanhã
    if "amanhã" in pergunta or "amanha" in pergunta:
        dias_semana = {
            "Monday": "segunda-feira",
            "Tuesday": "terça-feira",
            "Wednesday": "quarta-feira",
            "Thursday": "quinta-feira",
            "Friday": "sexta-feira",
            "Saturday": "sábado",
            "Sunday": "domingo"
        }
        amanha = datetime.datetime.now() + datetime.timedelta(days=1)
        dia_semana_en = amanha.strftime('%A')
        dia_semana_pt = dias_semana[dia_semana_en]
        return f"Amanhã será {dia_semana_pt}, {amanha.strftime('%d/%m/%Y')}."

    # 🏆 Detecta nomes de times de futebol
    times = [
        "flamengo", "corinthians", "palmeiras", "são paulo", "vasco",
        "grêmio", "internacional", "cruzeiro", "atlético mineiro",
        "botafogo", "fluminense", "bahia", "fortaleza", "santos"
    ]
    for time in times:
        if time in pergunta:
            return f"Ah, você torce para o {time.title()}? Grande time!"

    # 🛒 Detecta intenção de comprar algo
    if "quero comprar" in pergunta:
        produto = pergunta.split("quero comprar")[-1].strip()
        if produto == "":
            return "O que você quer comprar?"
        url_busca = f"https://www.google.com/search?q=melhor+preço+{produto.replace(' ', '+')}"
        webbrowser.open(url_busca)
        return f"Abri para você uma busca pelos melhores preços de {produto}!"

    # Verifica se há palavra-chave no dicionário
    for chave in respostas:
        if chave in pergunta:
            return respostas[chave]

    return "Desculpe, não entendi. Tente outra pergunta."

# Loop principal
while True:
    user_input = input(f"{nome}: ")

    if user_input.lower() == "sair":
        print(f"Chatbot: Tchau, {nome}!")
        break

    resposta = responder(user_input)

    print("Chatbot:", resposta)

    # Salva histórico da conversa
    with open("historico_conversa.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}: {user_input}\nChatbot: {resposta}\n")

