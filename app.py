from flask import Flask, render_template, abort

app = Flask(__name__)

# 暫時使用 List 儲存文章，不需要資料庫
posts = [
    {
        "id": 1,
        "title": "我的第一篇部落格文章",
        "author": "Alice",
        "content": "大家好！這是我的第一篇文章。\n歡迎來到我的部落格。"
    },
    {
        "id": 2,
        "title": "學習 Python Flask",
        "author": "Bob",
        "content": "Flask 是一個輕量級的 Python Web 框架。\n可以使用 Templates 呈現 HTML 頁面。"
    },
    {
        "id": 3,
        "title": "今天的學習心得",
        "author": "Charlie",
        "content": "今天學會了如何使用 Flask 傳遞資料到 HTML 模板。"
    }
]


# 首頁：顯示所有文章
@app.route("/")
def index():
    return render_template("index.html", posts=posts)


# 文章詳細頁面，例如 /post/1
@app.route("/post/<int:post_id>")
def detail(post_id):
    post = next(
        (p for p in posts if p["id"] == post_id),
        None
    )

    if post is None:
        abort(404)

    return render_template("detail.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)