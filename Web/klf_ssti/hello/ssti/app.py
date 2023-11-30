from flask import Flask, request, render_template, render_template_string,send_from_directory
import re
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/hack', methods=['GET', 'POST'])
def secr3t():
    name = request.args.get('klf', '')
    template = f'''
       <html>
           <body>
               <h1>啊不，klf原来是这个意思，不可能女神不可能骂我的！</h1>
               <h1>我不信，就算是klf我也绝对比你们这群klf好，就算是klf我也是最好的那个，这样女神就会回头看我了呜呜呜</h1>
               <h1>%s</h1>        
           </body>
       </html>
       <!--klf?-->
       <!-- 想要flag？那你得知道klf是什么意思吧，你个klf -->

       '''
    template1 = f'''
       <html>
           <body>
               <h1>啊不，klf原来是这个意思，不可能女神不可能骂我的！</h1>
               <h1>我不信，就算是klf我也绝对比你们这群klf好，就算是klf我也是最好的那个，这样女神就会回头看我了呜呜呜</h1>        
           </body>
       </html>
       <!--klf?-->
       <!-- 想要flag？那你得知道klf是什么意思吧，你个klf -->

       '''
    render_template_string(template % name)
    if name:
        return render_template('klf.html')

    return render_template_string(template1)

@app.route('/robots.txt', methods=['GET'])
def robots():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'robots.txt', mimetype='text/plain')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7899, debug=False)
