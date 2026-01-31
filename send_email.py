import os
import sys
import smtplib
import email.message
from dotenv import load_dotenv
from get import get_last_id, check_word
from insert import insert_new_word
from get_word import get_random_word, get_word
from get_phrase import get_definition

def main():
    print('🔹 Iniciando programa...')

    # Carregar o banco
    try:
        id = get_last_id()
        int_id = int(id) + 1
        print(f'✅ Banco OK — ID retornado: {int_id}')
    except Exception as e:
        print('❌ ERRO no banco:', e)
        sys.exit(1)

    # Preparar o e-mail

    # Carregar o env
    
    load_dotenv()

    sender_password = os.getenv('EMAIL_PASSWORD')
    if not sender_password:
        print('❌ ERRO: EMAIL_PASSWORD não carregada do .env')
        sys.exit(1)

    sender_email = os.getenv('EMAIL_ADDRESS')
    if not sender_email:
        print('❌ ERRO: EMAIL_ADDRESS não carregada do .env')
        sys.exit(1)
    
    #print('✅ .env carregado')

    receiver_email = ['jvlabremachado@id.uff.br','beatriz.cavalcante1674@gmail.com']
    subject = f'New English word for you to learn today - Day {int_id}'

    try:
        while True:
            word = get_random_word() if get_random_word() != None else get_word()
            
            #print(f'Palavra obtida: {word}') #Verificação de qual palavra está retornando
            #word = 'conversation' #Teste para deixar o loop travado em uma palavra específica, a fim de testar o banco

            if not check_word(word): # irá verificar se a palavra já está no banco de dados
                break

        results = get_definition(word)
        #print(f'✅ Palavra e definições obtidas: {word}')

    except Exception as e:
        print('❌ ERRO ao obter palavra ou definição:', e)
        sys.exit(1)

    definitions_text = ""
    examples_text = ""

    for i, (definition, example) in enumerate(results, start=1):
        if i != 1:
            definitions_text += f"                      Definition {i}: {definition}.\n"
            examples_text += f"                      Example {i}: {example}.\n"
        else:
            definitions_text += f"          Definition {i}: {definition}.\n"
            examples_text += f"          Example {i}: {example}.\n"

    body = f"""
        Hello, we are learning word ID: {int_id}#!!

        Here is the new word of the day: {word} 🥳🥳🥳

        It means:

            {definitions_text}

        Examples of usage:

            {examples_text}

        Keep learning and have fun! 🚀📚
    """
    for i in range(len(results)):
        j = 0
        insert_new_word(word, results[i][j], results[i][j + 1])

    # Teste 3 — SMTP + envio
    for e_mail in receiver_email:
        try:
            msg = email.message.EmailMessage()
            msg['From'] = sender_email
            msg['To'] = e_mail
            msg['Subject'] = subject
            msg.set_content(body)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(sender_email, sender_password)
                print('✅ Login no Gmail OK')
                smtp.send_message(msg)

            print('📧 E-mail enviado com sucesso!')
            print(f'🔹 Enviado para o {e_mail}')
            
        except smtplib.SMTPAuthenticationError:
            print('❌ Falha de autenticação: verifique App Password do Gmail')
            sys.exit(1)
            
        except Exception as e:
            print(f'❌ ERRO_SMTP: {e}')
            sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
