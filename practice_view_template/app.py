from datetime import datetime

from flask import Flask, render_template, request

# 掲示板の１つ１つのメッセージを示すクラス

class Message: 
  def __init__(self, id: str, user_name: str, contents: str):
    self.id = id
    self.user_name = user_name
    self.contents =contents


# グローバル変数の宣言
app: Flask = Flask(__name__)
login_user_name: str = "myan"
message_list :list[Message] = [
  Message(202504110203, "myan", "ハロー有明応答願う"),
  Message(202504120305, "藤原基央", "みゃんくん愛しているよ"),
  Message(202504120555, "江戸川コナン", "真実はいつも1つ!"),
]


# / にアクセスがあった場合のルーティング
@app.route("/")
def index():
  #GETメソッドのフォームの値を取得
  search_word: str = request.args.get("search_word")


  #searchパラメータの有無
  if search_word is None:
    return render_template(
      "top.html", login_user_name=login_user_name, message_list=message_list
      )
  else:
    filtered_message_list: list[Message] = [
      x for x in message_list if search_word in x.contents
    ]
    return render_template(
      "top.html",
      login_user_name=login_user_name,
      message_list=filtered_message_list,
      search_word=search_word

    )
  

#/writeにアクセスがあった場合のルーティング
@app.route("/write", methods=["POST", "GET"])
def write():
  if request.method == "GET":
    return render_template("write.html", login_user_name=login_user_name)
  
  elif request.method == "POST":
    id: str = datetime.now().strftime("%Y%m%d%H%M%S")
    contents: str = request.form.get("contents")
    user_name: str = request.form.get("user_name")


    # 新しいMessageクラスインスタンスを生成

  # message_listに追加して、top.htmlを表示
  if contents:
    message_list.insert(0, Message(id, user_name, contents))
  return render_template(
    "top.html",
    login_user_name=login_user_name,
    message_list=message_list,
  )


if __name__ == "__main__":
  app.run(debug=True)
