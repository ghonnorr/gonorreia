import telebot

CHAVE_API = "6866667364:AAEagLpHzDi4pDtooRAzDOIsBVHgdLizg4Y"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    bot.send_message(mensagem.chat.id, 'Cliquei na opção 1!')

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, 'Cliquei na opção 2!')

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, 'Cliquei na opção 3!')


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar, content_types=['text'])
def responder(mensagem):
    texto = '''
    Bem-vindo ao lado oposto da sociedade, escolha uma opção para começar (clique em um dos itens abaixo):
        /opcao1 grupo do canal exclusivo
        /opcao2 saber mais sobre nós
        /opcao3 provas da nossa veracidade
    Responder qualquer outra coisa não vai funcionar, clique em alguma das opções
    '''
    bot.reply_to(mensagem, texto)

bot.polling()
