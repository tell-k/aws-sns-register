import os
import time
import csv

import boto3
from dotenv import load_dotenv, find_dotenv

# .env ファイルを読み込んで環境変数にセット
load_dotenv(find_dotenv())

# このファイルを起点としてCSVのパスを組み立て
here = os.path.dirname(__file__)
CSV_PATH = os.path.join(here, 'data', 'telephone.csv')

# 環境変数(.env) から必要となる情報を取得
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
TOPIC_ARN = os.environ.get('TOPIC_ARN')


def main():

    # CSVファイルの存在チェック
    if not os.path.exists(CSV_PATH):
        print('CSVファイル {} がありません。'.format(CSV_PATH))
        return

    client = boto3.client(
        'sns',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

    # CSVファイルのオープン
    with open(CSV_PATH, mode='r', encoding='utf-8') as fp:
        reader = csv.reader(fp)

        next(reader)  # 1行目を読み飛ばし

        # 2行目からループで回す(reader = iterable)
        for row in reader:
            tel_number = row[1]

            # 日本の電話番号であれば '+81' を先頭につける
            tel_number = '+81' + str(tel_number)

            # SNSトピックに電話番号を登録(Subscribe)
            response = client.subscribe(
                TopicArn=TOPIC_ARN,
                Protocol='sms',
                Endpoint=tel_number
            )

            # 登録がうまくいったら、Subscribe OKとメッセージを出す
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                print('Subscribe OK {}'.format(tel_number))
            else:
                print('Subscribe NG {}'.format(tel_number))

            # APIに負荷を掛けないようように1秒スリープさせる
            time.sleep(1)

    print('Finish subscribing sns topic.')


if __name__ == '__main__':
    main()
