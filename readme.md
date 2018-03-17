# AFD
Ani-Face Detecter for dlib

## 概要
アニメや漫画等の2次元画像の顔を検出するためのモデルです。  
dlibのsimple_object_detector向けに作成してあります。  
また、モデルは顔検出用のほかに目検出用も付属しています。 

## ファイル構成
detector_eye.svm -> 目検出用特徴量ファイル  
detector_face.svm -> 顔検出用特徴量ファイル  
sample.py -> サンプルスクリプト  

## 使い方
sample.pyを参考にしてください。  
`python3 sample.py (画像ファイル名)`で実行可能です。  
実行にはdlibとopencv-pythonが必要となるので、pipでインストールしてください。  
サンプルスクリプトでは、指定した画像ファイルから目の検出も行った高精度な顔検出を行います。  
ただ、目の検出によるチェックを行うと顔を拾わない場合があります。(下の例を参照)  
目の検出を止める場合は30～37行目をコメントアウトしてください。  
目の検出によるチェックを行わない場合、誤検出が若干増えます。  
用途によって切り替えてください。  

## 例
顔のみの検出の場合  
![detect](https://raw.githubusercontent.com/marron-akanishi/AFD/master/images/detect.jpg)  
目を含めた検出の場合  
![detect_with_eye](https://raw.githubusercontent.com/marron-akanishi/AFD/master/images/detect_with_eye.jpg)  

## その他
このファイルは[lbpcascade_animeface](https://github.com/nagadomi/lbpcascade_animeface/)より判定が厳しいです。  
また、顔として認識する範囲が顔ギリギリです。  
