from flask import Flask

# render_template 是幹嘛的？
# 它會去找 templates/ 資料夾裡的 HTML 檔案
# 然後把那個網頁渲染（render）出來給使用者看
# 所以你必須放一個叫 "xxx".html 的檔案在 templates 裡 (注意有"s")
from flask import render_template


app = Flask(__name__)


# 他的瀏覽器跳轉的邏輯是: 
# 當使用者輸入('???')時，電腦如果有找到@app.route('???')裡面的???網址時，電腦會執行下面def xxx():裡面的程式碼

# @ 跟 def 是雙胞胎，用來告訴 Flask，當使用者連到網站的某個網址時，就執行後面的定義式
@app.route('/')
def home():
    return render_template('home.html')   # <<< 這裡用"home.html"示範


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
