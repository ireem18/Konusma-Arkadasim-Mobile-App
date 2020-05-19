# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 05:22:54 2020

@author: Lenovo
"""
import os
import pickle
import numpy as np
from python_speech_features import mfcc
import scipy.io.wavfile as wav
from hmmlearn import hmm

    
def trainmodel2 ( model, wavlist):
    X = np.array([])
    for wavfile in wavlist:
        path = os.path.join('C:/Users/Lenovo/Desktop/django-ionic/konusma_arkadasim-django/konusma_arkadasim_api/audio_hmm/train_audio_word', wavfile)
        (rate, sig) = wav.read(path)
        mfcc_feat = mfcc(sig,rate,nfft=4096)
        
        if len(X) == 0:
            X = mfcc_feat
        else:
            X = np.append(X, mfcc_feat,axis=0)
            
    modelHarf = hmm.GaussianHMM(n_components=6,covariance_type='diag',n_iter=1000)
    modelHarf.fit(X)
    
    
    hmmPath2 = os.path.join('C:/Users/Lenovo/Desktop/django-ionic/konusma_arkadasim-django/konusma_arkadasim_api/audio_hmm/hmm_word', model)
    file = open(hmmPath2,"wb")
    pickle.dump(modelHarf,file)
    file.close()
    
def main():
    
    trainmodel2 ('asker',['asker2.wav','asker3.wav','asker4.wav','asker5.wav','asker6.wav','asker7.wav','asker8.wav','asker9.wav']) 
    trainmodel2 ('haber',['haber.wav','haber2.wav','haber3.wav','haber4.wav','haber6.wav','haber7.wav','haber8.wav','haber9.wav'])
    trainmodel2 ('kafa',['kafa.wav','kafa2.wav','kafa3.wav','kafa4.wav','kafa6.wav','kafa7.wav','kafa8.wav','kafa9.wav'])
    trainmodel2 ('sevmek',['sevmek.wav','sevmek2.wav','sevmek3.wav','sevmek4.wav','sevmek6.wav','sevmek7.wav','sevmek8.wav','sevmek9.wav'])
    trainmodel2 ('ilce',['ilce.wav','ilce2.wav','ilce3.wav','ilce4.wav','ilce6.wav','ilce7.wav','ilce8.wav','ilce9.wav'])
    trainmodel2 ('yemek',['yemek.wav','yemek2.wav','yemek3.wav','yemek4.wav','yemek6.wav','yemek7.wav','yemek8.wav','yemek9.wav'])
    trainmodel2 ('yaris',['yaris.wav','yaris2.wav','yaris3.wav','yaris4.wav','yaris6.wav','yaris7.wav','yaris8.wav','yaris9.wav'])
    trainmodel2 ('hizli',['hizli.wav','hizli2.wav','hizli3.wav','hizli4.wav','hizli6.wav','hizli7.wav','hizli8.wav','hizli9.wav'])
    trainmodel2 ('irmak',['irmak.wav','irmak2.wav','irmak3.wav','irmak4.wav','irmak6.wav','irmak7.wav','irmak8.wav','irmak9.wav'])
    trainmodel2 ('cizgi',['cizgi.wav','cizgi2.wav','cizgi3.wav','cizgi4.wav','cizgi6.wav','cizgi7.wav','cizgi8.wav','cizgi9.wav'])
    trainmodel2 ('isim',['isim.wav','isim2.wav','isim3.wav','isim4.wav','isim6.wav','isim7.wav','isim8.wav','isim9.wav'])
    trainmodel2 ('pilot',['pilot.wav','pilot2.wav','pilot3.wav','pilot4.wav','pilot6.wav','pilot7.wav','pilot8.wav','pilot9.wav'])
    trainmodel2 ('olta',['olta.wav','olta2.wav','olta3.wav','olta4.wav','olta6.wav','olta7.wav','olta8.wav','olta9.wav'])
    trainmodel2 ('kosmak',['kosmak.wav','kosmak2.wav','kosmak3.wav','kosmak4.wav','kosmak6.wav','kosmak7.wav','kosmak8.wav','kosmak9.wav'])
    trainmodel2 ('pilot',['pilot.wav','pilot2.wav','pilot3.wav','pilot4.wav','pilot6.wav','pilot7.wav','pilot8.wav','pilot9.wav'])
    trainmodel2 ('ordek',['ordek.wav','ordek2.wav','ordek3.wav','ordek4.wav','ordek6.wav','ordek7.wav','ordek8.wav','ordek9.wav'])
    trainmodel2 ('gol',['gol.wav','gol2.wav','gol3.wav','gol4.wav','gol6.wav','gol7.wav','gol8.wav','gol9.wav'])
    trainmodel2 ('kotu',['kotu.wav','kotu2.wav','kotu3.wav','kotu4.wav','kotu6.wav','kotu7.wav','kotu8.wav','kotu9.wav'])
    trainmodel2 ('uzun',['uzun.wav','uzun2.wav','uzun3.wav','uzun4.wav','uzun6.wav','uzun7.wav','uzun8.wav','uzun9.wav'])
    trainmodel2 ('kuru',['kuru.wav','kuru2.wav','kuru3.wav','kuru4.wav','kuru6.wav','kuru7.wav','kuru8.wav','kuru9.wav'])
    trainmodel2 ('uludag',['uludag.wav','uludag2.wav','uludag3.wav','uludag4.wav','uludag6.wav','uludag7.wav','uludag8.wav','uludag9.wav'])
    trainmodel2 ('ruya',['ruya.wav','ruya2.wav','ruya3.wav','ruya4.wav','ruya6.wav','ruya7.wav','ruya8.wav','ruya9.wav'])
    trainmodel2 ('ucret',['ucret.wav','ucret2.wav','ucret3.wav','ucret4.wav','ucret6.wav','ucret7.wav','ucret8.wav','ucret9.wav'])
    trainmodel2 ('utu',['utu.wav','utu2.wav','utu3.wav','utu4.wav','utu6.wav','utu7.wav','utu8.wav','utu9.wav'])
    trainmodel2 ('cocuk',['cocuk.wav','cocuk2.wav','cocuk3.wav','cocuk4.wav','cocuk6.wav','cocuk7.wav','cocuk8.wav','cocuk9.wav'])
 
if __name__ == '__main__':
    main()

    
    
