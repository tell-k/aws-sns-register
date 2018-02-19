AWS SNS Topicに携帯電話番号(SMS)を登録するサンプル
========================================================

概要
---------------------------

* CSVファイルを解析
* 解析したデータの中から電話番号を抽出
* その電話番号を該当のSNSトピックに登録する(boto3使用)

.env ファイルの用意
--------------------------

* 機密情報はgithubリポジトリにはコミットしない
* ローカルで自分しかわからないようにしておく
* 事前に下記三つの情報を用意する

::

 AWS_ACCESS_KEY_ID=xxxx
 AWS_SECRET_ACCESS_KEY=xxxx
 TOPIC_ARN=arn:aws:sns:xxxx

CSVの設置
--------------------------

``data/telephone.csv`` を設置

フォーマット

* 1行目は列名
* 2列目に電話番号

::

 例)

 name,tel,created_at
 tell-k,090xxxxxxxx,2018-02-01
 tell-k,090xxxxxxxx,2018-02-01
 tell-k,090xxxxxxxx,2018-02-01

セットアップ + 実行
--------------------------

::

 $ python3 -m venv venv
 $ source venv/bin/activate
 (venv) $ pip install -r requirements.txt
 (venv) $ python main.py


メモ
--------------------------

* SNSトピックに電話番号(SMS)を登録する時は、日本のであれば 「+81」が必要になる

  * 09012345678 -> +8109012345678


* SNSトピックに対しては重複して電話番号を登録できない。

  * トピックと電話番号は 1対1の関係になる
  * = つまりプログラムで重複排除する必要なし

参考
--------------------------

* http://boto3.readthedocs.io/en/latest/reference/services/sns.html
* https://dev.classmethod.jp/cloud/publish_to_sns_using_boto3/
