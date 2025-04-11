from flask import Flask, request

app: Flask = Flask(__name__)

# /にアクセスがあった場合のルーティング
@app.route("/")
def index():
  return "<h1>これは掲示板のトップページです</h1>"


# /write にGETメソッドでアクセスがあった場合のルーティング
@app.route("/write", methods=["GET"])
def write_by_get_methodf():
  return """
    <html><body>
    <h1>これは掲示板の書き込みページです。</h1>
    <h3>書き込み内容</h3>
    <form action="/write" method="POST">
      <textarea name="msg" rows="5" cols="70"></textarea><br/><br/>
      <input type="submit" value="書き込み">
    </form>
    </body></html>
  """

#POSTメソッド
@app.route("/write", methods=["POST"])
def write_by_post_method():
  msg = request.form["msg"]
  return f"<h1>書き込みを受け付けました。内容：{msg}</h1>"


# /edit/message_id にアクセスがあった場合のルーティング
@app.route("/edit/<int:message_id>")
def edit(message_id):
  return f"<h1>これはID={message_id}の編集ページです。message_idは{type(message_id).__name__}型です。</h1>"

if __name__ == "__main__":
  app.run(debug=True)