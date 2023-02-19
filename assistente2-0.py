# Importações
import webbrowser as database
import datetime
import wikipedia
import pyttsx3
import pywhatkit

# Programa
def main():
    maquina = pyttsx3.init()
    commando = input("Digite algo ou Site: ")
    if (commando == "https://www.youtube.com/"):
        print("Acessando YouTube...")
        maquina.say("Acessando YouTube...")
        maquina.runAndWait()
        database.open(commando)
        main()
    if (commando == "https://www.facebook.com/"):
        print("Acessando Facebook...")
        maquina.say("Acessando Facebook...")
        maquina.runAndWait()
        database.open(commando)
        main()
    if (commando == "https://www.linkedin.com/"):
        print("Acessando Linkedin...")
        maquina.say("Acessando Linkedin...")
        maquina.runAndWait()
        database.open(commando)
        main()
    if (commando == "https://www.google.com/"):
        print("Acessando Google...")
        maquina.say("Acessando Google...")
        maquina.runAndWait()
        database.open(commando)
        main()
    if (commando == "4"):
        exit()
    if (commando == "Que Horas São"):
        hora_atual = datetime.datetime.now().strftime('%H:%M:%S')
        print("Agora São: " + hora_atual)
        maquina.say("Agora São:" + hora_atual)
        maquina.runAndWait()
        main()
    if (commando == "Qual é o tempo de segundos"):
        segundos_minutos_atuais = datetime.datetime.now().strftime('%M:%S')
        print("Agora São: " + segundos_minutos_atuais)
        maquina.say("Agora São: " + segundos_minutos_atuais)
        maquina.runAndWait()
        main()
    if 'Procure por' in commando:
         procurar = commando.replace('Procure por', '')
         wikipedia.set_lang('pt')
         resultado = wikipedia.summary(procurar,2)
         print(resultado)
         maquina.say(resultado)
         maquina.runAndWait()
         main()
    if 'Toque' in commando:
        musica = commando.replace('Toque', '')
        resultado2 = pywhatkit.playonyt(musica)
        print("Tocando a Musica: " + resultado2)
        maquina.say("Tocando a Musica: " + musica)
        maquina.runAndWait()
        main()
    if 'Busque no YouTube por' in commando:
        pesquisa_youtube = commando.replace('Busque no YouTube por ', '')
        print('Pesquisando por: ' + pesquisa_youtube + " No Youtube")
        maquina.say('Pesquisando por: ' + pesquisa_youtube + " No Youtube")
        maquina.runAndWait()
        database.open("https://www.youtube.com/search?q=" + pesquisa_youtube)
        main()
    if 'Busque por' in commando:
        procure_resultado = commando.replace('Busque por ', '')
        print('Procurando por: ' + procure_resultado + ' No Google')
        maquina.say("Procurando por: " + procure_resultado + " No Google")
        maquina.runAndWait()
        database.open("https://www.google.com/search?q=" + procure_resultado)
        main()
    database.open(commando)

# Rodar o programa
main()
