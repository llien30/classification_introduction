# Classification example by TensorFlow

分類問題のためのTensorFlowのコードです．

## 使用したデータセット
* [Chest Xray Dataset](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia) : for chest_xray.ipynb
* [Dog and Cat Dataset](https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip) : for dog_cat_classification.ipynb


### dog_cat_classification.ipynb

浅いネットワーク(畳み込み1層)と深いネットワーク(畳み込み5層)を作成し、その分類性能を比較しています．<br>
結果としては、30epochの段階でaccuracyが、<br>
浅いネットワーク : 61.6% <br>
深いネットワーク : 72.0% <br>
となりました．

### chest_xray.ipynb

ResNetのImageNetのpretrainingモデルを転移学習し、肺炎(Pneumonia)の肺と健康(Normal)な肺の2値分類を行っています．

#### make_dataset.py 
このコードを用いて、上記urlからダウンロードしたChest_xrayデータセットを整形することが可能です．
データセットのファイル構成は以下の通りです．

```
data _______ train ____ normal
        |            |_ pneumonia
        | __ test  ____ normal
                     |_ pneumonia
```

#### check_dataset.py
このコードを用いて、整形後のデータセットに対し、データの数を確認することができます．


## 参考にしたコード
[Tensorflow Tutorials](https://www.tensorflow.org/tutorials/images/classification)

