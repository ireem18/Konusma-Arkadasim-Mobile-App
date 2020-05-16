# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 05:24:42 2020

@author: Lenovo
"""


import os
import pickle
import sys
from python_speech_features import mfcc
import scipy.io.wavfile as wav

def loadModels():

    global model_haber,model_asker,model_kafa,model_yemek,model_sevmek,model_ilce;
    global model_yaris,model_hizli,model_irmak,model_cizgi,model_isim,model_pilot;
    global model_olta,model_kosmak,model_cocuk,model_ordek,model_gol,model_kotu;
    global model_uzun,model_kuru,model_uludag,model_ruya,model_ucret,model_utu;


    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'haber')
    file = open(hmmPath2,"rb")
    model_haber = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'asker')
    file = open(hmmPath2,"rb")
    model_asker = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'kafa')
    file = open(hmmPath2,"rb")
    model_kafa = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'sevmek')
    file = open(hmmPath2,"rb")
    model_sevmek = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'yemek')
    file = open(hmmPath2,"rb")
    model_yemek = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'ilce')
    file = open(hmmPath2,"rb")
    model_ilce = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'yaris')
    file = open(hmmPath2,"rb")
    model_yaris = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'hizli')
    file = open(hmmPath2,"rb")
    model_hizli = pickle.load(file)
    file.close()
    
    hmmPath = os.path.join('../audio_hmm/hmm_word', 'irmak')
    file = open(hmmPath2,"rb")
    model_irmak = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'cizgi')
    file = open(hmmPath2,"rb")
    model_cizgi = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'isim')
    file = open(hmmPath2,"rb")
    model_isim = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'pilot')
    file = open(hmmPath2,"rb")
    model_pilot = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'olta')
    file = open(hmmPath2,"rb")
    model_olta = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'kosmak')
    file = open(hmmPath2,"rb")
    model_kosmak = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'cocuk')
    file = open(hmmPath2,"rb")
    model_cocuk = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'ordek')
    file = open(hmmPath2,"rb")
    model_ordek = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'gol')
    file = open(hmmPath2,"rb")
    model_gol = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'kotu')
    file = open(hmmPath2,"rb")
    model_kotu = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'uzun')
    file = open(hmmPath2,"rb")
    model_uzun = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'kuru')
    file = open(hmmPath2,"rb")
    model_kuru = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'uludag')
    file = open(hmmPath2,"rb")
    model_uludag = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'ruya')
    file = open(hmmPath2,"rb")
    model_ruya = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'ucret')
    file = open(hmmPath2,"rb")
    model_ucret = pickle.load(file)
    file.close()
    
    hmmPath2 = os.path.join('../audio_hmm/hmm_word', 'utu')
    file = open(hmmPath2,"rb")
    model_utu = pickle.load(file)
    file.close()
    

    
def testWav(file):
    (rate,sig) = wav.read(file)
    mfcc_feat_test = mfcc(sig,rate,nfft=4096)

      
    modelSkorHaber = model_haber.score(mfcc_feat_test)
    modelSkorAsker = model_asker.score(mfcc_feat_test)
    modelSkorKafa = model_kafa.score(mfcc_feat_test)
    modelSkorSevmek = model_sevmek.score(mfcc_feat_test)
    modelSkorYemek = model_yemek.score(mfcc_feat_test)
    modelSkorIlce = model_ilce.score(mfcc_feat_test)
    modelSkorYaris = model_yaris.score(mfcc_feat_test)
    modelSkorHizli = model_hizli.score(mfcc_feat_test)
    modelSkorIrmak = model_irmak.score(mfcc_feat_test)
    modelSkorCizgi = model_cizgi.score(mfcc_feat_test)
    modelSkorIsim = model_isim.score(mfcc_feat_test)
    modelSkorPilot = model_pilot.score(mfcc_feat_test)
    modelSkorOlta = model_olta.score(mfcc_feat_test)
    modelSkorKosmak = model_kosmak.score(mfcc_feat_test)
    modelSkorCocuk = model_cocuk.score(mfcc_feat_test)
    modelSkorOrdek = model_ordek.score(mfcc_feat_test)
    modelSkorGol = model_gol.score(mfcc_feat_test)
    modelSkorKotu = model_kotu.score(mfcc_feat_test)
    modelSkorUzun = model_uzun.score(mfcc_feat_test)
    modelSkorKuru = model_kuru.score(mfcc_feat_test)
    modelSkorUludag = model_uludag.score(mfcc_feat_test)
    modelSkorRuya = model_ruya.score(mfcc_feat_test)
    modelSkorUcret = model_ucret.score(mfcc_feat_test)
    modelSkorUtu = model_utu.score(mfcc_feat_test)
    
    
    t = max(modelSkorHaber,modelSkorAsker, modelSkorKafa,modelSkorSevmek,modelSkorYemek,modelSkorIlce, modelSkorYaris,modelSkorHizli,
        modelSkorIrmak,modelSkorCizgi,modelSkorIsim,modelSkorPilot,modelSkorOlta,modelSkorKosmak,
        modelSkorCocuk,modelSkorOrdek,modelSkorGol,modelSkorKotu,modelSkorUzun,modelSkorKuru,
        modelSkorUludag,modelSkorRuya,modelSkorUcret,modelSkorUtu)

    
    if (t == modelSkorHaber): return 'haber'
    if (t == modelSkorAsker): return 'asker'
    if (t == modelSkorKafa): return 'kafa'
    if (t == modelSkorSevmek): return 'sevmek'
    if (t == modelSkorYemek): return 'yemek'
    if (t == modelSkorIlce): return 'ilce'
    if (t == modelSkorYaris): return 'yaris'
    if (t == modelSkorHizli): return 'hizli'  
    if (t == modelSkorIrmak): return 'irmak'   
    if (t == modelSkorCizgi): return 'cizgi'   
    if (t == modelSkorIsim): return 'isim'    
    if (t == modelSkorPilot): return 'pilot'
    if (t == modelSkorOlta): return 'olta'
    if (t == modelSkorKosmak): return 'kosmak'
    if (t == modelSkorCocuk): return 'cocuk'
    if (t == modelSkorOrdek): return 'ordek'
    if (t == modelSkorGol): return 'gol'    
    if (t == modelSkorKotu): return 'kotu'   
    if (t == modelSkorUzun): return 'uzun'
    if (t == modelSkorUludag): return 'uludag'
    if (t == modelSkorRuya): return 'ruya'
    if (t == modelSkorUcret): return 'ucret'
    if (t == modelSkorUtu): return 'utu'

    
if __name__ == '__main__':
    loadModels()
    dogru=0
    yanlis=0
    yanlis_dizi=[]
    fileName = 'C:/Users/Lenovo/Desktop/TEZ/tezz/tez_siniflandirici/ses/kelime'
    kelime = ['asker','sevmek','uludag','gol','isim','kafa','olta','haber']
    for element in kelime:
       testFile = fileName+'/'+element+'.wav'
       sonuc = testWav(testFile)
       if (str(element)  == sonuc):
           print(" kelime : "+sonuc)
           dogru+=1
       else:
           print("yanliş tahmin edildi !! \t doğrusu : "+str(element)+"\t tahmin edilen : "+sonuc)
           yanlis+=1
           yanlis_dizi.append(str(element))
    
 
            
            
 #print(testWav(testFile))
        