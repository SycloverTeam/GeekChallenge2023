from flask import Flask, request, render_template, render_template_string,send_from_directory
import re
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/secr3ttt', methods=['GET', 'POST'])
def secr3t():

    name = request.args.get('klf', '')
    template = f'''
       <html>
           <body>
               <h1>找到secr3t了，但是找不到flag你还是个klf</h1>
               <h1>%s</h1>         
           </body>
       </html>
       <img src=\"https://image-obsidian-1317327960.cos.ap-chengdu.myqcloud.com/obisidian-blog/8.jpg\" alt="g">
       <!--klf?-->
       <!-- klf还想要flag？没那么容易 -->

       '''
    bl = ['_', '\\', '\'', '"', 'request', "+", 'class', 'init', 'arg', 'config', 'app', 'self', 'cd', 'chr',
          'request', 'url', 'builtins', 'globals', 'base', 'pop', 'import', 'popen', 'getitem', 'subclasses', '/',
          'flashed', 'os', 'open', 'read', 'count', '*', '43', '45', '38', '124', '47', '59', '99', '100', 'cat', '~',
          ':', 'not', '0', 'length', 'index', '-', 'ord', '37', '94', '96', '48', '49', '50', '51', '52', '53', '54',
          '55', '56', '57',
          '58', '59', '[', ']', '@', '^', '#']
    for i in bl:
        if i in name:
            return render_template('klf.html')
            #return "真是klf！！！回去多学学啦"

    pattern = r"\s*\)\s*\)"
    match = re.search(pattern, name)
    pattern2 = r"\s*\)\s*(,)?\s*\)"
    match2 = re.search(pattern2, name)
    pattern3 = r"\s*\)\s*\)\s*\|"
    match3 = re.search(pattern3, name)
    pattern4 = r"\s*,\s*\)\s*\)\s*\|"
    match4 = re.search(pattern4, name)

    pattern_mo = r"\d+\s*%\s*\d+|[a-zA-Z]+\s*%\s*[a-zA-Z]+"
    matche_mo = re.search(pattern_mo, name)

    if match:
        if match2.group(1):
            return render_template('klf.html')
        elif match4:
            return render_template('klf.html')
        elif match3:
            return render_template_string(template % name)
        else:
            return render_template('klf.html')

    # 输出匹配的结果
    if matche_mo :
        return render_template('klf.html')


    a=render_template_string(template % name)
    if "{" in a:
        return a + render_template('win.html')
    return  a
@app.route('/robots.txt', methods=['GET'])
def robots():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'robots.txt', mimetype='text/plain')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7888, debug=False)
