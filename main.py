from pytube import YouTube
import moviepy.editor as mp
import re
import os

link = input("Digite o link do vídeo que você quer baixar: ")
path = input("Digite o a pasta que o vídeo deverá ser salvo: ")
yt = YouTube(link)
mode = str(input("Você quer baixar em .mp3, ou .mp4 (Digite mp3, ou mp4)? "))


def BaixarVideo(link, pasta):
    print("Tìtulo: ", link.title)
    print("Número de Views: ", link.views)
    print("Duração do vídeo: ", link.length, " segundos.")
    print("Avaliação do vídeo: ", link.rating)

    ys = link.streams.get_highest_resolution()

    print("Baixando...")
    ys.download(path)
    print("Finalizado com sucesso!")


def BaixarAudio(link, pasta):
    print("Baixando...")
    ys = yt.streams.filter(only_audio=True).first().download(pasta)
    print("Download Completo!")
    print("Convertendo arquivo...")
    for file in os.listdir(pasta):
        if re.search("mp4", file):
            mp4_path = os.path.join(pasta, file)
            mp3_path = os.path.join(pasta, os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)
    print("Conversão Concluída!")


if mode == "mp4":
    BaixarVideo(yt, path)

if mode == "mp3":
    BaixarAudio(yt, path)