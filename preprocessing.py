# -*- coding: utf-8 -*-
"""colab final year exp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O5pRG2DBEBMJAaTe-HnTZmGhB4ZFDYTf
"""

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive
drive.mount('/gdrive')
# %cd /gdrive

import cv2
!pip install PyWavelets
#import PyWavelets
import numpy as np 
import cv2 
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

import pywt
import pywt.data
from scipy import stats

import pandas as pd
dataset2 = pd.DataFrame(columns=['mean_r', 'mean_g', 'mean_b','med_r','med_g','med_b','var_r','var_g','var_b','skew_r','skew_g','skew_b','kurt_r','kurt_g','kurt_b','mean_r1', 'mean_g1', 'mean_b1','med_r1','med_g1','med_b1','var_r1','var_g1','var_b1','skew_r1','skew_g1','skew_b1','kurt_r1','kurt_g1','kurt_b1','mean_r2', 'mean_g2', 'mean_b2','med_r2','med_g2','med_b2','var_r2','var_g2','var_b2','skew_r2','skew_g2','skew_b2','kurt_r2','kurt_g2','kurt_b2','mean_r3', 'mean_g3', 'mean_b3','med_r3','med_g3','med_b3','var_r3','var_g3','var_b3','skew_r3','skew_g3','skew_b3','kurt_r3','kurt_g3','kurt_b3','camera'])

for i in range(0,23):
    img = cv2.imread(f"canon5D ({i+1}).JPG") 
    dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    noise=img-dst
    b,g,r = cv2.split(noise)
    coeffs2_r = pywt.dwt2(r, 'haar')
    coeffs2_g = pywt.dwt2(g, 'haar')
    coeffs2_b = pywt.dwt2(b, 'haar')
    LLr, (LHr, HLr, HHr) = coeffs2_r
    LLg, (LHg, HLg, HHg) = coeffs2_g
    LLb, (LHb, HLb, HHb) = coeffs2_b
    mean_r = np.mean(LLr)
    mean_g = np.mean(LLg)
    mean_b = np.mean(LLb)
    med_r = np.median(LLr)
    med_g = np.median(LLg)
    med_b = np.median(LLb)
    var_r = np.var(LLr)
    var_g = np.var(LLg)
    var_b = np.var(LLb)
    skew_r = stats.skew(LHr, axis = None)
    skew_g = stats.skew(LHg, axis = None)
    skew_b = stats.skew(LHb, axis = None)
    kurt_r = stats.kurtosis(LHr, axis=None)
    kurt_g = stats.kurtosis(LHg, axis=None)
    kurt_b = stats.kurtosis(LHb, axis=None)
    mean_r1 = np.mean(LHr)
    mean_g1 = np.mean(LHg)
    mean_b1 = np.mean(LHb)
    med_r1 = np.median(LHr)
    med_g1 = np.median(LHg)
    med_b1 = np.median(LHb)
    var_r1 = np.var(LHr)
    var_g1 = np.var(LHg)
    var_b1 = np.var(LHb)
    skew_r1 = stats.skew(LHr, axis = None)
    skew_g1 = stats.skew(LHg, axis = None)
    skew_b1 = stats.skew(LHb, axis = None)
    kurt_r1 = stats.kurtosis(LHr, axis=None)
    kurt_g1 = stats.kurtosis(LHg, axis=None)
    kurt_b1 = stats.kurtosis(LHb, axis=None)
    mean_r2 = np.mean(HLr)
    mean_g2 = np.mean(HLg)
    mean_b2 = np.mean(HLb)
    med_r2 = np.median(HLr)
    med_g2 = np.median(HLg)
    med_b2 = np.median(HLb)
    var_r2 = np.var(HLr)
    var_g2 = np.var(HLg)
    var_b2 = np.var(HLb)
    skew_r2 = stats.skew(HLr, axis = None)
    skew_g2 = stats.skew(HLg, axis = None)
    skew_b2 = stats.skew(HLb, axis = None)
    kurt_r2 = stats.kurtosis(HLr, axis=None)
    kurt_g2 = stats.kurtosis(HLg, axis=None)
    kurt_b2 = stats.kurtosis(HLb, axis=None)
    mean_r3 = np.mean(HHr)
    mean_g3 = np.mean(HHg)
    mean_b3 = np.mean(HHb)
    med_r3 = np.median(HHr)
    med_g3 = np.median(HHg)
    med_b3 = np.median(HHb)
    var_r3 = np.var(HHr)
    var_g3 = np.var(HHg)
    var_b3 = np.var(HHb)
    skew_r3 = stats.skew(HHr, axis = None)
    skew_g3 = stats.skew(HHg, axis = None)
    skew_b3 = stats.skew(HHb, axis = None)
    kurt_r3 = stats.kurtosis(HHr, axis=None)
    kurt_g3 = stats.kurtosis(HHg, axis=None)
    kurt_b3 = stats.kurtosis(HHb, axis=None)
    #dataset in making
    dataset2 = dataset2.append({'mean_r':mean_r, 'mean_g':mean_g, 'mean_b':mean_b,'med_r':med_r,'med_g':med_g,'med_b':med_b,'var_r':var_r,'var_g':var_g,'var_b':var_b,'skew_r':skew_r,'skew_g':skew_g,'skew_b':skew_b,'kurt_r':kurt_r,'kurt_g':kurt_g,'kurt_b':kurt_b,'mean_r1':mean_r1, 'mean_g1':mean_g1, 'mean_b1':mean_b1,'med_r1':med_r1,'med_g1':med_g1,'med_b1':med_b1,'var_r1':var_r1,'var_g1':var_g1,'var_b1':var_b1,'skew_r1':skew_r1,'skew_g1':skew_g1,'skew_b1':skew_b1,'kurt_r1':kurt_r1,'kurt_g1':kurt_g1,'kurt_b1':kurt_b1,'mean_r2':mean_r2, 'mean_g2':mean_g2, 'mean_b2':mean_b2,'med_r2':med_r2,'med_g2':med_g2,'med_b2':med_b2,'var_r2':var_r2,'var_g2':var_g2,'var_b2':var_b2,'skew_r2':skew_r2,'skew_g2':skew_g2,'skew_b2':skew_b2,'kurt_r2':kurt_r2,'kurt_g2':kurt_g2,'kurt_b2':kurt_b2,'mean_r3':mean_r3, 'mean_g3':mean_g3, 'mean_b3':mean_b3,'med_r3':med_r3,'med_g3':med_g3,'med_b3':med_b3,'var_r3':var_r3,'var_g3':var_g3,'var_b3':var_b3,'skew_r3':skew_r3,'skew_g3':skew_g3,'skew_b3':skew_b3,'kurt_r3':kurt_r3,'kurt_g3':kurt_g3,'kurt_b3':kurt_b3,'camera':"Canon5D2"}, ignore_index=True)
    print(i)
    
for i in range(0,11):
    img = cv2.imread(f"canon80D ({i+1}).JPG") 
    dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    noise=img-dst
    b,g,r = cv2.split(noise)
    coeffs2_r = pywt.dwt2(r, 'haar')
    coeffs2_g = pywt.dwt2(g, 'haar')
    coeffs2_b = pywt.dwt2(b, 'haar')
    LLr, (LHr, HLr, HHr) = coeffs2_r
    LLg, (LHg, HLg, HHg) = coeffs2_g
    LLb, (LHb, HLb, HHb) = coeffs2_b
    mean_r = np.mean(LLr)
    mean_g = np.mean(LLg)
    mean_b = np.mean(LLb)
    med_r = np.median(LLr)
    med_g = np.median(LLg)
    med_b = np.median(LLb)
    var_r = np.var(LLr)
    var_g = np.var(LLg)
    var_b = np.var(LLb)
    skew_r = stats.skew(LHr, axis = None)
    skew_g = stats.skew(LHg, axis = None)
    skew_b = stats.skew(LHb, axis = None)
    kurt_r = stats.kurtosis(LHr, axis=None)
    kurt_g = stats.kurtosis(LHg, axis=None)
    kurt_b = stats.kurtosis(LHb, axis=None)
    mean_r1 = np.mean(LHr)
    mean_g1 = np.mean(LHg)
    mean_b1 = np.mean(LHb)
    med_r1 = np.median(LHr)
    med_g1 = np.median(LHg)
    med_b1 = np.median(LHb)
    var_r1 = np.var(LHr)
    var_g1 = np.var(LHg)
    var_b1 = np.var(LHb)
    skew_r1 = stats.skew(LHr, axis = None)
    skew_g1 = stats.skew(LHg, axis = None)
    skew_b1 = stats.skew(LHb, axis = None)
    kurt_r1 = stats.kurtosis(LHr, axis=None)
    kurt_g1 = stats.kurtosis(LHg, axis=None)
    kurt_b1 = stats.kurtosis(LHb, axis=None)
    mean_r2 = np.mean(HLr)
    mean_g2 = np.mean(HLg)
    mean_b2 = np.mean(HLb)
    med_r2 = np.median(HLr)
    med_g2 = np.median(HLg)
    med_b2 = np.median(HLb)
    var_r2 = np.var(HLr)
    var_g2 = np.var(HLg)
    var_b2 = np.var(HLb)
    skew_r2 = stats.skew(HLr, axis = None)
    skew_g2 = stats.skew(HLg, axis = None)
    skew_b2 = stats.skew(HLb, axis = None)
    kurt_r2 = stats.kurtosis(HLr, axis=None)
    kurt_g2 = stats.kurtosis(HLg, axis=None)
    kurt_b2 = stats.kurtosis(HLb, axis=None)
    mean_r3 = np.mean(HHr)
    mean_g3 = np.mean(HHg)
    mean_b3 = np.mean(HHb)
    med_r3 = np.median(HHr)
    med_g3 = np.median(HHg)
    med_b3 = np.median(HHb)
    var_r3 = np.var(HHr)
    var_g3 = np.var(HHg)
    var_b3 = np.var(HHb)
    skew_r3 = stats.skew(HHr, axis = None)
    skew_g3 = stats.skew(HHg, axis = None)
    skew_b3 = stats.skew(HHb, axis = None)
    kurt_r3 = stats.kurtosis(HHr, axis=None)
    kurt_g3 = stats.kurtosis(HHg, axis=None)
    kurt_b3 = stats.kurtosis(HHb, axis=None)
    #dataset in making
    dataset2 = dataset2.append({'mean_r':mean_r, 'mean_g':mean_g, 'mean_b':mean_b,'med_r':med_r,'med_g':med_g,'med_b':med_b,'var_r':var_r,'var_g':var_g,'var_b':var_b,'skew_r':skew_r,'skew_g':skew_g,'skew_b':skew_b,'kurt_r':kurt_r,'kurt_g':kurt_g,'kurt_b':kurt_b,'mean_r1':mean_r1, 'mean_g1':mean_g1, 'mean_b1':mean_b1,'med_r1':med_r1,'med_g1':med_g1,'med_b1':med_b1,'var_r1':var_r1,'var_g1':var_g1,'var_b1':var_b1,'skew_r1':skew_r1,'skew_g1':skew_g1,'skew_b1':skew_b1,'kurt_r1':kurt_r1,'kurt_g1':kurt_g1,'kurt_b1':kurt_b1,'mean_r2':mean_r2, 'mean_g2':mean_g2, 'mean_b2':mean_b2,'med_r2':med_r2,'med_g2':med_g2,'med_b2':med_b2,'var_r2':var_r2,'var_g2':var_g2,'var_b2':var_b2,'skew_r2':skew_r2,'skew_g2':skew_g2,'skew_b2':skew_b2,'kurt_r2':kurt_r2,'kurt_g2':kurt_g2,'kurt_b2':kurt_b2,'mean_r3':mean_r3, 'mean_g3':mean_g3, 'mean_b3':mean_b3,'med_r3':med_r3,'med_g3':med_g3,'med_b3':med_b3,'var_r3':var_r3,'var_g3':var_g3,'var_b3':var_b3,'skew_r3':skew_r3,'skew_g3':skew_g3,'skew_b3':skew_b3,'kurt_r3':kurt_r3,'kurt_g3':kurt_g3,'kurt_b3':kurt_b3,'camera':"canon80D"}, ignore_index=True)
    print(i)
    
    
for i in range(0,26):
    img = cv2.imread(f"nikon800 ({i+1}).JPG") 
    dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    noise=img-dst
    b,g,r = cv2.split(noise)
    coeffs2_r = pywt.dwt2(r, 'haar')
    coeffs2_g = pywt.dwt2(g, 'haar')
    coeffs2_b = pywt.dwt2(b, 'haar')
    LLr, (LHr, HLr, HHr) = coeffs2_r
    LLg, (LHg, HLg, HHg) = coeffs2_g
    LLb, (LHb, HLb, HHb) = coeffs2_b
    mean_r = np.mean(LLr)
    mean_g = np.mean(LLg)
    mean_b = np.mean(LLb)
    med_r = np.median(LLr)
    med_g = np.median(LLg)
    med_b = np.median(LLb)
    var_r = np.var(LLr)
    var_g = np.var(LLg)
    var_b = np.var(LLb)
    skew_r = stats.skew(LHr, axis = None)
    skew_g = stats.skew(LHg, axis = None)
    skew_b = stats.skew(LHb, axis = None)
    kurt_r = stats.kurtosis(LHr, axis=None)
    kurt_g = stats.kurtosis(LHg, axis=None)
    kurt_b = stats.kurtosis(LHb, axis=None)
    mean_r1 = np.mean(LHr)
    mean_g1 = np.mean(LHg)
    mean_b1 = np.mean(LHb)
    med_r1 = np.median(LHr)
    med_g1 = np.median(LHg)
    med_b1 = np.median(LHb)
    var_r1 = np.var(LHr)
    var_g1 = np.var(LHg)
    var_b1 = np.var(LHb)
    skew_r1 = stats.skew(LHr, axis = None)
    skew_g1 = stats.skew(LHg, axis = None)
    skew_b1 = stats.skew(LHb, axis = None)
    kurt_r1 = stats.kurtosis(LHr, axis=None)
    kurt_g1 = stats.kurtosis(LHg, axis=None)
    kurt_b1 = stats.kurtosis(LHb, axis=None)
    mean_r2 = np.mean(HLr)
    mean_g2 = np.mean(HLg)
    mean_b2 = np.mean(HLb)
    med_r2 = np.median(HLr)
    med_g2 = np.median(HLg)
    med_b2 = np.median(HLb)
    var_r2 = np.var(HLr)
    var_g2 = np.var(HLg)
    var_b2 = np.var(HLb)
    skew_r2 = stats.skew(HLr, axis = None)
    skew_g2 = stats.skew(HLg, axis = None)
    skew_b2 = stats.skew(HLb, axis = None)
    kurt_r2 = stats.kurtosis(HLr, axis=None)
    kurt_g2 = stats.kurtosis(HLg, axis=None)
    kurt_b2 = stats.kurtosis(HLb, axis=None)
    mean_r3 = np.mean(HHr)
    mean_g3 = np.mean(HHg)
    mean_b3 = np.mean(HHb)
    med_r3 = np.median(HHr)
    med_g3 = np.median(HHg)
    med_b3 = np.median(HHb)
    var_r3 = np.var(HHr)
    var_g3 = np.var(HHg)
    var_b3 = np.var(HHb)
    skew_r3 = stats.skew(HHr, axis = None)
    skew_g3 = stats.skew(HHg, axis = None)
    skew_b3 = stats.skew(HHb, axis = None)
    kurt_r3 = stats.kurtosis(HHr, axis=None)
    kurt_g3 = stats.kurtosis(HHg, axis=None)
    kurt_b3 = stats.kurtosis(HHb, axis=None)
    #dataset in making
    dataset2 = dataset2.append({'mean_r':mean_r, 'mean_g':mean_g, 'mean_b':mean_b,'med_r':med_r,'med_g':med_g,'med_b':med_b,'var_r':var_r,'var_g':var_g,'var_b':var_b,'skew_r':skew_r,'skew_g':skew_g,'skew_b':skew_b,'kurt_r':kurt_r,'kurt_g':kurt_g,'kurt_b':kurt_b,'mean_r1':mean_r1, 'mean_g1':mean_g1, 'mean_b1':mean_b1,'med_r1':med_r1,'med_g1':med_g1,'med_b1':med_b1,'var_r1':var_r1,'var_g1':var_g1,'var_b1':var_b1,'skew_r1':skew_r1,'skew_g1':skew_g1,'skew_b1':skew_b1,'kurt_r1':kurt_r1,'kurt_g1':kurt_g1,'kurt_b1':kurt_b1,'mean_r2':mean_r2, 'mean_g2':mean_g2, 'mean_b2':mean_b2,'med_r2':med_r2,'med_g2':med_g2,'med_b2':med_b2,'var_r2':var_r2,'var_g2':var_g2,'var_b2':var_b2,'skew_r2':skew_r2,'skew_g2':skew_g2,'skew_b2':skew_b2,'kurt_r2':kurt_r2,'kurt_g2':kurt_g2,'kurt_b2':kurt_b2,'mean_r3':mean_r3, 'mean_g3':mean_g3, 'mean_b3':mean_b3,'med_r3':med_r3,'med_g3':med_g3,'med_b3':med_b3,'var_r3':var_r3,'var_g3':var_g3,'var_b3':var_b3,'skew_r3':skew_r3,'skew_g3':skew_g3,'skew_b3':skew_b3,'kurt_r3':kurt_r3,'kurt_g3':kurt_g3,'kurt_b3':kurt_b3,'camera':"nikon800"}, ignore_index=True)
    print(i)
    
for i in range(0,16):
    img = cv2.imread(f"SonyA7 ({i+1}).JPG") 
    dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    noise=img-dst
    b,g,r = cv2.split(noise)
    coeffs2_r = pywt.dwt2(r, 'haar')
    coeffs2_g = pywt.dwt2(g, 'haar')
    coeffs2_b = pywt.dwt2(b, 'haar')
    LLr, (LHr, HLr, HHr) = coeffs2_r
    LLg, (LHg, HLg, HHg) = coeffs2_g
    LLb, (LHb, HLb, HHb) = coeffs2_b
    mean_r = np.mean(LLr)
    mean_g = np.mean(LLg)
    mean_b = np.mean(LLb)
    med_r = np.median(LLr)
    med_g = np.median(LLg)
    med_b = np.median(LLb)
    var_r = np.var(LLr)
    var_g = np.var(LLg)
    var_b = np.var(LLb)
    skew_r = stats.skew(LHr, axis = None)
    skew_g = stats.skew(LHg, axis = None)
    skew_b = stats.skew(LHb, axis = None)
    kurt_r = stats.kurtosis(LHr, axis=None)
    kurt_g = stats.kurtosis(LHg, axis=None)
    kurt_b = stats.kurtosis(LHb, axis=None)
    mean_r1 = np.mean(LHr)
    mean_g1 = np.mean(LHg)
    mean_b1 = np.mean(LHb)
    med_r1 = np.median(LHr)
    med_g1 = np.median(LHg)
    med_b1 = np.median(LHb)
    var_r1 = np.var(LHr)
    var_g1 = np.var(LHg)
    var_b1 = np.var(LHb)
    skew_r1 = stats.skew(LHr, axis = None)
    skew_g1 = stats.skew(LHg, axis = None)
    skew_b1 = stats.skew(LHb, axis = None)
    kurt_r1 = stats.kurtosis(LHr, axis=None)
    kurt_g1 = stats.kurtosis(LHg, axis=None)
    kurt_b1 = stats.kurtosis(LHb, axis=None)
    mean_r2 = np.mean(HLr)
    mean_g2 = np.mean(HLg)
    mean_b2 = np.mean(HLb)
    med_r2 = np.median(HLr)
    med_g2 = np.median(HLg)
    med_b2 = np.median(HLb)
    var_r2 = np.var(HLr)
    var_g2 = np.var(HLg)
    var_b2 = np.var(HLb)
    skew_r2 = stats.skew(HLr, axis = None)
    skew_g2 = stats.skew(HLg, axis = None)
    skew_b2 = stats.skew(HLb, axis = None)
    kurt_r2 = stats.kurtosis(HLr, axis=None)
    kurt_g2 = stats.kurtosis(HLg, axis=None)
    kurt_b2 = stats.kurtosis(HLb, axis=None)
    mean_r3 = np.mean(HHr)
    mean_g3 = np.mean(HHg)
    mean_b3 = np.mean(HHb)
    med_r3 = np.median(HHr)
    med_g3 = np.median(HHg)
    med_b3 = np.median(HHb)
    var_r3 = np.var(HHr)
    var_g3 = np.var(HHg)
    var_b3 = np.var(HHb)
    skew_r3 = stats.skew(HHr, axis = None)
    skew_g3 = stats.skew(HHg, axis = None)
    skew_b3 = stats.skew(HHb, axis = None)
    kurt_r3 = stats.kurtosis(HHr, axis=None)
    kurt_g3 = stats.kurtosis(HHg, axis=None)
    kurt_b3 = stats.kurtosis(HHb, axis=None)
    #dataset in making
    dataset2 = dataset2.append({'mean_r':mean_r, 'mean_g':mean_g, 'mean_b':mean_b,'med_r':med_r,'med_g':med_g,'med_b':med_b,'var_r':var_r,'var_g':var_g,'var_b':var_b,'skew_r':skew_r,'skew_g':skew_g,'skew_b':skew_b,'kurt_r':kurt_r,'kurt_g':kurt_g,'kurt_b':kurt_b,'mean_r1':mean_r1, 'mean_g1':mean_g1, 'mean_b1':mean_b1,'med_r1':med_r1,'med_g1':med_g1,'med_b1':med_b1,'var_r1':var_r1,'var_g1':var_g1,'var_b1':var_b1,'skew_r1':skew_r1,'skew_g1':skew_g1,'skew_b1':skew_b1,'kurt_r1':kurt_r1,'kurt_g1':kurt_g1,'kurt_b1':kurt_b1,'mean_r2':mean_r2, 'mean_g2':mean_g2, 'mean_b2':mean_b2,'med_r2':med_r2,'med_g2':med_g2,'med_b2':med_b2,'var_r2':var_r2,'var_g2':var_g2,'var_b2':var_b2,'skew_r2':skew_r2,'skew_g2':skew_g2,'skew_b2':skew_b2,'kurt_r2':kurt_r2,'kurt_g2':kurt_g2,'kurt_b2':kurt_b2,'mean_r3':mean_r3, 'mean_g3':mean_g3, 'mean_b3':mean_b3,'med_r3':med_r3,'med_g3':med_g3,'med_b3':med_b3,'var_r3':var_r3,'var_g3':var_g3,'var_b3':var_b3,'skew_r3':skew_r3,'skew_g3':skew_g3,'skew_b3':skew_b3,'kurt_r3':kurt_r3,'kurt_g3':kurt_g3,'kurt_b3':kurt_b3,'camera':"sonyA7"}, ignore_index=True)
    print(i)

for i in range(0,23):
    img = cv2.imread(f"canon5D ({i+1}).JPG") 
    dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    noise=img-dst
    b,g,r = cv2.split(noise)
    coeffs2_r = pywt.dwt2(r, 'haar')
    coeffs2_g = pywt.dwt2(g, 'haar')
    coeffs2_b = pywt.dwt2(b, 'haar')
    LLr, (LHr, HLr, HHr) = coeffs2_r
    LLg, (LHg, HLg, HHg) = coeffs2_g
    LLb, (LHb, HLb, HHb) = coeffs2_b
    mean_r = np.mean(LLr)
    mean_g = np.mean(LLg)
    mean_b = np.mean(LLb)
    med_r = np.median(LLr)
    med_g = np.median(LLg)
    med_b = np.median(LLb)
    var_r = np.var(LLr)
    var_g = np.var(LLg)
    var_b = np.var(LLb)
    skew_r = stats.skew(LLr, axis = None)
    skew_g = stats.skew(LLg, axis = None)
    skew_b = stats.skew(LLb, axis = None)
    kurt_r = stats.kurtosis(LLr, axis=None)
    kurt_g = stats.kurtosis(LLg, axis=None)
    kurt_b = stats.kurtosis(LLb, axis=None)
    #dataset in making
    dataset2 = dataset2.append({'mean_r':mean_r, 'mean_g':mean_g, 'mean_b':mean_b,'med_r':med_r,'med_g':med_g,'med_b':med_b,'var_r':var_r,'var_g':var_g,'var_b':var_b,'skew_r':skew_r,'skew_g':skew_g,'skew_b':skew_b,'kurt_r':kurt_r,'kurt_g':kurt_g,'kurt_b':kurt_b,'camera':"Canon5D2"}, ignore_index=True)
    print(i)

dataset2

for i in range(0,11):
    img = cv2.imread(f"canon80D ({i+1}).JPG") 
    dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    noise=img-dst
    b,g,r = cv2.split(noise)
    coeffs2_r = pywt.dwt2(r, 'haar')
    coeffs2_g = pywt.dwt2(g, 'haar')
    coeffs2_b = pywt.dwt2(b, 'haar')
    LLr, (LHr, HLr, HHr) = coeffs2_r
    LLg, (LHg, HLg, HHg) = coeffs2_g
    LLb, (LHb, HLb, HHb) = coeffs2_b
    mean_r = np.mean(LLr)
    mean_g = np.mean(LLg)
    mean_b = np.mean(LLb)
    med_r = np.median(LLr)
    med_g = np.median(LLg)
    med_b = np.median(LLb)
    var_r = np.var(LLr)
    var_g = np.var(LLg)
    var_b = np.var(LLb)
    skew_r = stats.skew(LLr, axis = None)
    skew_g = stats.skew(LLg, axis = None)
    skew_b = stats.skew(LLb, axis = None)
    kurt_r = stats.kurtosis(LLr, axis=None)
    kurt_g = stats.kurtosis(LLg, axis=None)
    kurt_b = stats.kurtosis(LLb, axis=None)
    #dataset in making
    dataset2 = dataset2.append({'mean_r':mean_r, 'mean_g':mean_g, 'mean_b':mean_b,'med_r':med_r,'med_g':med_g,'med_b':med_b,'var_r':var_r,'var_g':var_g,'var_b':var_b,'skew_r':skew_r,'skew_g':skew_g,'skew_b':skew_b,'kurt_r':kurt_r,'kurt_g':kurt_g,'kurt_b':kurt_b,'camera':"canon80D"}, ignore_index=True)
    print(i)
    
for i in range(0,26):
    img = cv2.imread(f"nikon800 ({i+1}).JPG") 
    dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    noise=img-dst
    b,g,r = cv2.split(noise)
    coeffs2_r = pywt.dwt2(r, 'haar')
    coeffs2_g = pywt.dwt2(g, 'haar')
    coeffs2_b = pywt.dwt2(b, 'haar')
    LLr, (LHr, HLr, HHr) = coeffs2_r
    LLg, (LHg, HLg, HHg) = coeffs2_g
    LLb, (LHb, HLb, HHb) = coeffs2_b
    mean_r = np.mean(LLr)
    mean_g = np.mean(LLg)
    mean_b = np.mean(LLb)
    med_r = np.median(LLr)
    med_g = np.median(LLg)
    med_b = np.median(LLb)
    var_r = np.var(LLr)
    var_g = np.var(LLg)
    var_b = np.var(LLb)
    skew_r = stats.skew(LLr, axis = None)
    skew_g = stats.skew(LLg, axis = None)
    skew_b = stats.skew(LLb, axis = None)
    kurt_r = stats.kurtosis(LLr, axis=None)
    kurt_g = stats.kurtosis(LLg, axis=None)
    kurt_b = stats.kurtosis(LLb, axis=None)
    #dataset in making
    dataset2 = dataset2.append({'mean_r':mean_r, 'mean_g':mean_g, 'mean_b':mean_b,'med_r':med_r,'med_g':med_g,'med_b':med_b,'var_r':var_r,'var_g':var_g,'var_b':var_b,'skew_r':skew_r,'skew_g':skew_g,'skew_b':skew_b,'kurt_r':kurt_r,'kurt_g':kurt_g,'kurt_b':kurt_b,'camera':"nikon800"}, ignore_index=True)
    print(i)
    
for i in range(0,16):
    img = cv2.imread(f"SonyA7 ({i+1}).JPG") 
    dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    noise=img-dst
    b,g,r = cv2.split(noise)
    coeffs2_r = pywt.dwt2(r, 'haar')
    coeffs2_g = pywt.dwt2(g, 'haar')
    coeffs2_b = pywt.dwt2(b, 'haar')
    LLr, (LHr, HLr, HHr) = coeffs2_r
    LLg, (LHg, HLg, HHg) = coeffs2_g
    LLb, (LHb, HLb, HHb) = coeffs2_b
    mean_r = np.mean(LLr)
    mean_g = np.mean(LLg)
    mean_b = np.mean(LLb)
    med_r = np.median(LLr)
    med_g = np.median(LLg)
    med_b = np.median(LLb)
    var_r = np.var(LLr)
    var_g = np.var(LLg)
    var_b = np.var(LLb)
    skew_r = stats.skew(LLr, axis = None)
    skew_g = stats.skew(LLg, axis = None)
    skew_b = stats.skew(LLb, axis = None)
    kurt_r = stats.kurtosis(LLr, axis=None)
    kurt_g = stats.kurtosis(LLg, axis=None)
    kurt_b = stats.kurtosis(LLb, axis=None)
    #dataset in making
    dataset2 = dataset2.append({'mean_r':mean_r, 'mean_g':mean_g, 'mean_b':mean_b,'med_r':med_r,'med_g':med_g,'med_b':med_b,'var_r':var_r,'var_g':var_g,'var_b':var_b,'skew_r':skew_r,'skew_g':skew_g,'skew_b':skew_b,'kurt_r':kurt_r,'kurt_g':kurt_g,'kurt_b':kurt_b,'camera':"sonyA7"}, ignore_index=True)
    print(i)

dataset2

df2y = dataset2["camera"]
df2 = dataset2.drop(['camera'], axis = 1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df2,df2y, test_size = 0.2)

from sklearn.linear_model import LogisticRegression

log_reg = LogisticRegression(multi_class = 'multinomial', max_iter = 1000)

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score as acc
from mlxtend.feature_selection import SequentialFeatureSelector as sfs

sfs1 = sfs(log_reg,
           k_features=2,
           forward=True,
           floating=False,
           verbose=2,
           cv=10)

sfs1 = sfs1.fit(X_train, y_train)

log_reg.fit(X_train,y_train)

pred = log_reg.predict(X_test)

from sklearn.metrics import accuracy_score





dataset2.to_csv('noise_final_1.csv', index = True, header = True)



from google.colab import files

#with open('example.txt', 'w') as f:
  #f.write('some content')

files.download('noise_final_1.csv')

