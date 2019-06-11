from work import Work

def get_work(work_name):
    for work in all_works:
        if work.name == work_name:
            return work
    return None

def get_all_works():
    return all_works

work1 = Work(id=1,
            name="ホームページ",
            image="homePage.JPG",
            description="このサイト．flaskを使って初めて制作したものです",
            date="2019年4月5日")

work2 = Work(id=2,
            name="CANDLE",
            image="candle.jpg",
            description="災害時の被害状況をGoogleMapを使って共有し，避難意識を向上させることを目的としたWebアプリ．開発途中なのでたびたび仕様が変更されています",
            date="2019年3月5日",
            url="https://wsapp.cs.kobe-u.ac.jp/candle")

work3 = Work(id=3,
            name="Todo front",
            image="todo.png",
            description="フロントエンドとバックエンドを切り離した設計の練習",
            date="2019年3月20日",
            github="https://github.com/pk-Musan/todo-front")

work4 = Work(id=4,
              name="make10",
              image="make10.png",
              description="Gitを用いた共同開発の練習として開発したもので，提示された4つの数字をそれぞれ一回ずつ使い，四則演算を用いて10を作る速さを競うWebアプリです．制作の際にはフロントを担当しました．",
              date="2019年5月18日",
              github="https://github.com/rokuyon/make10_project")

work5 = Work(id=5,
             name="Uちゃんねる",
             image="u-channel.jpg",
             description="Gitを用いた共同開発とVue.jsの練習用に開発している掲示板．チャンネルは日本の大学それぞれに用意する予定で，その大学に関する話題で盛り上がれる場を提供したいと考えています",
             date="2019年6月11日",
             github="https://github.com/pk-Musan/u-channel-front")

all_works = [work1, work2, work3, work4, work5]