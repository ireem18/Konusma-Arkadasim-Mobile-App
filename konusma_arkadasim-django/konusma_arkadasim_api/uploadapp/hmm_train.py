# -*- coding: utf-8 -*-


import os
import pickle
import numpy as np
from python_speech_features import mfcc
import scipy.io.wavfile as wav

def trainmodel ( model, wavlist):
    X = np.array([])
    for wavfile in wavlist:
        path = os.path.join('../audio_hmm/train_audio', wavfile)
        (rate, sig) = wav.read(path)
        mfcc_feat = mfcc(sig,rate,nfft=4096)
        
        if len(X) == 0:
            X = mfcc_feat
        else:
            X = np.append(X, mfcc_feat,axis=0)
            
    modelHarf = hmm.GaussianHMM(n_components=6,covariance_type='diag',n_iter=1000)
    modelHarf.fit(X)
    
    hmmPath = os.path.join('../audio_hmm/hmm', model)
    file = open(hmmPath,"wb")
    pickle.dump(modelHarf,file)
    file.close()


def main ():
    trainmodel ('a',['a1.wav','a2.wav','a3.wav','a4.wav','a5.wav','a6.wav','a.wav','aa.wav','a7.wav','a8.wav','a_c.wav','a_s.wav','ac.wav'])
    trainmodel ('e',['e1.wav','e2.wav','e3.wav','e4.wav','e5.wav','e6.wav','e.wav','ee.wav','e_c.wav','e_s.wav','ec.wav'])
    trainmodel ('ı',['ı1.wav','ı2.wav','ı3.wav','ı4.wav','ı5.wav','ı6.wav','ı.wav','ıı.wav','ı_c.wav','ı_s.wav','ıc.wav'])
    trainmodel ('i',['i1.wav','i2.wav','i3.wav','i4.wav','i5.wav','i6.wav','i.wav','ii.wav','i_c.wav','i_s.wav','ic.wav'])
    trainmodel ('o',['o1.wav','o2.wav','o3.wav','o4.wav','o5.wav','o6.wav','o.wav','oo.wav','o_c.wav','o_s.wav','oc.wav'])
   #trainmodel ('oo',['oo1.wav','oo2.wav','oo3.wav','oo4.wav','oo5.wav','oo6.wav','oo.wav','oooo.wav'])
    trainmodel ('u',['u1.wav','u2.wav','u3.wav','u4.wav','u5.wav','u6.wav','u_c.wav','u_s.wav','uc.wav'])
    trainmodel ('ü',['ü1.wav','ü2.wav','ü3.wav','ü5.wav','ü6.wav','ü_c.wav','ü_s.wav','üc.wav'])
    

    
if __name__ == '__main__':
    main()

    




    
