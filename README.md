# 遺伝的アルゴリズムによるシフトメイカー
 
アルバイトの従業員や学校のイベントなどのスタッフの情報を入力すると自動でシフト作成を行ってくれるウェブアプリです。
 
# デモ
 
アプリの一連の流れを紹介します。
 
![](https://cpp-learning.com/wp-content/uploads/2019/05/pyxel-190505-161951.gif)
 
この動画はユーザー登録からシフト作成が完了するまでの流れを説明するものです。
 
# 特徴
 
Pythonのライブラリの一つであるdeapの遺伝的アルゴリズムを使用したウェブアプリです。 [deap](https://github.com/DEAP/deap/blob/master/examples/ga/onemax.py)

また、[こちら](https://github.com/shouta-dev/nurse-scheduling-ga/blob/master/nurse_scheduling_by_ga.py)のソースコードも参考にさせて頂きました。
 
```python
import deap
```
[deap](https://github.com/DEAP/deap/blob/master/examples/ga/onemax.py)は遺伝的アルゴリズムだけでなく他にも様々な進化的計算のアルゴリズムが実装されているようです。
 
 
# 使用したライブラリやパッケージ
 
* Python 3.8.5
* django 3.1.3
* deap
* pandas
 
環境はWindows上で[Ubuntu](https://www.ubuntulinux.jp/)を使用したLinuxOsです。
 

# インストール
 
各パッケージは pip コマンドでインストールしました.
 
```bash
pip3 install django
pip3 install deap
pip3 install pandas
```
 
# アプリの使用
 

[こちら]()からデプロイしたアプリを使用できます。(動画冒頭のホーム画面に遷移します。)
サンプルアカウントは以下のものを使用してください。(10人程度の従業員情報を追加済みのアカウントです。)
***
ユーザー名：root  
パスワード：a


 
# ノート
 
* 上記の開発環境以外ではテストしていません。
* 遺伝的アルゴリズムを使用する都合上確実に理想のシフト表ができるとは限りません。
 
# 作成者
 
* 鈴木　悠春
* 小樽商科大学2年
 

ありがとうございました！
