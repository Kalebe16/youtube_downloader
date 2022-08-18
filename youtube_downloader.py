from pytube import YouTube
from time import sleep
import os
import requests
from youtube_dl import YoutubeDL
import webbrowser


def check_internet():
    ''' verifica se o pc está conectado na internet '''
    os.system('cls') or None 
    url = 'https://www.google.com'
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except:
        return False


def baixar_audio(link):
    ''' baixa o arquivo no formato de audio'''
    try:
        audio_downloader = YoutubeDL({'format':'bestaudio'})
        audio_downloader.extract_info(link)
        
        print("\nDownload concluído!")
        sleep(2)
        
    except: 
        os.system('cls') or None 
        print("\nLink inválido, verifique se colou o link corretamente...")
        sleep(2)
        executar_programa()


def baixar_video(link):
    ''' baixa o arquivo no formato de video'''

    try:
        youtube = YouTube(link)
        print("\nBaixando...")

        '''
        for stream in youtube.streams:  
            print(stream)
        
        '''
        youtube.streams.get_highest_resolution().download()
        print("\nDownload concluído!")
        sleep(2)
        
    except: 
        os.system('cls') or None 

        print("\nLink inválido, verifique se colou o link corretamente...")
        sleep(2)
        executar_programa()


def abrir_link():
    ''' Abre o link do meu site'''
    meu_site = "https://kalebeportfolio.netlify.app/"
    webbrowser.open(meu_site)


def menu_informacoes():
    os.system('cls') or None 
    tipo_informações = input("Digite o numero correspondente a ação:\n\n 1- Desenvolvedor\n 2- Ajuda\n\n>> Tecle ENTER para VOLTAR ao menu anterior <<")
    
    if tipo_informações == "1":
        abrir_link()
        menu_informacoes()
    elif tipo_informações == "2":
        os.system('cls') or None 
        print("Desenvolvido por KALEBE CHIMANSKI DE ALMEIDA\n\n- Os downloads serão feitos na mesma pasta em que este programa se encontra, escolha uma pasta de fácil acesso em seu computador e então mova este programa para a pasta escolhida, dessa forma todos os seus downloads estarão disponiveis por lá")
        input("\n>> Tecle ENTER para VOLTAR ao menu anterior <<")
        menu_informacoes()
    else:
        executar_programa()


def executar_programa():
    ''' função principal '''
    os.system('cls') or None # limpa a tela do terminal

    tipo_download = input("Digite o numero correspondente a ação:\n\n 1- Baixar video\n 2- Baixar audio\n 3- Sobre o app\n")

    if tipo_download == "1":
        link = str(input("\nCole aqui o link do video que deseja baixar: "))
        baixar_video(link)
    elif tipo_download == "2":
        link = str(input("\nCole aqui o link do video que deseja baixar: "))
        baixar_audio(link)
    elif tipo_download == "3":
        menu_informacoes()
    else:
        executar_programa()



# ordem de execução do programa:
if not check_internet():
    os.system('cls') or None 
    print("Sem internet :( \nConecte-se a uma rede wifi para utilizar o aplicativo")
    sleep(3)
    print("\n\nSaindo...")
    sleep(2.5)

else:    
    executar_programa()



    
