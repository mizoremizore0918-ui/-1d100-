from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/measure")
def measure():
    お風呂の温度 = random.randint(1, 100)

    if お風呂の温度 <= 10:
       結果= ("ほとんど氷水！体を熱した後に入ろう！")
    elif 10 < お風呂の温度 <= 20:
       結果= ("水風呂！サウナの後に入ろう！")
    elif 20 < お風呂の温度 <= 30:
       結果= ("ぬるめの水風呂！刺激が必要な人には足りないかも！")
    elif 30 < お風呂の温度 <= 36:
       結果= ("１晩放置したお風呂！追い炊きしよう！")
    elif 36 < お風呂の温度 <= 42:
       結果= ("ちょうどいい！快適だね！")
    elif 42 < お風呂の温度 <= 50:
       結果= ("ちょっと熱い！湯もみしよう！")
    elif 50 < お風呂の温度 <= 70:
       結果= ("熱すぎ！水をいれよう！ないけどね！")
    elif 70 < お風呂の温度 <= 90:
       結果= ("ほとんどサウナの温度！液体でやっちゃダメ！")
    elif 90 < お風呂の温度 <= 99:
       結果= ("もう少しで沸騰！火傷するかも！")
    else:
       結果= ("水の沸騰温度！危険！体をちゃんと冷ました後に入ろう！")

    return render_template(
        "result.html",
        温度=お風呂の温度,
        結果=結果
    )
if __name__ == "__main__":
    import os
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )