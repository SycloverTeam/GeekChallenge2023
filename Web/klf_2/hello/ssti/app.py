from flask import Flask, request, render_template, render_template_string,send_from_directory
import re
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/secr3ttt', methods=['GET', 'POST'])
def secr3t():
    klf = request.args.get('klf', '')
    template = f'''
       <html>
           <body>
               <h1>别找了，这次你肯定是klf</h1>     
           </body>
           <img src="https://image-obsidian-1317327960.cos.ap-chengdu.myqcloud.com/obisidian-blog/0071088CAC91D2C42C4D31053A7E8D2B731D69.jpg" alt="g">
            <h1>%s</h1>   
       </html>
       <!--klf?-->
       <!-- 别想要flag？klf -->

       '''
    bl = ['_', '\\', '\'', '"', 'request', "+", 'class', 'init', 'arg', 'config', 'app', 'self', 'cd', 'chr',
      'request', 'url', 'builtins', 'globals', 'base', 'pop', 'import', 'popen', 'getitem', 'subclasses', '/',
      'flashed', 'os', 'open', 'read', 'count', '*', '38', '124', '47', '59', '99', '100', 'cat', '~',
      ':', 'not', '0', '-', 'ord', '37', '94', '96', '[',']','index','length']#'43', '45',
    for i in bl:
        if i in klf:
            return render_template('klf.html')

    a = render_template_string(template % klf)
    if "{" in a:
        return  a + render_template('win.html')

    return a



@app.route('/robots.txt', methods=['GET'])
def robots():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'robots.txt', mimetype='text/plain')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7889, debug=False)
