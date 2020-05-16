import librosa
from pydub import AudioSegment

file_path='C:/Users/Lenovo/Desktop/django-ionic/konusma_arkadasim-django/konusma_arkadasim_api/media/'
def wav_split(fileName, seconds, ad):
    readWav = AudioSegment.from_wav(fileName)
    for i in seconds:
        t1 = (i - 1) * 500
        t2 = (i + 1) * 500
        print("t1 : ", t1)
        print("t2 : ", t2)
        newWav = readWav[t1:t2]
        newWav.export(str(file_path)+'split_audio/' + ad + '-' + str(i) + '.wav', format='wav')
    y, sr = librosa.load(fileName)
    split_interval = librosa.effects.split(y, top_db=1000, hop_length=10000)
    print(split_interval)
