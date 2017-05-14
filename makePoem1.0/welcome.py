import os
import hashlib, time
import answer,visual,translate,poem
from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename
from flask import send_from_directory
from watson_developer_cloud import VisualRecognitionV3

UPLOAD_FOLDER = 'photos'
ALLOWED_EXTENSIONS = set(['JPG', 'PNG', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

'''检查函数'''
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']#获得文件
        if file and allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            filename = hashlib.md5(('admin' + str(time.time())).encode("utf-8")).hexdigest()[:15] + ".jpg"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_url = url_for('uploaded_file',filename=filename)#获取图片地址
            local_urlbase = "G:\makePoem" + file_url
            local_url = open(local_urlbase,'rb')
            res = answer.Answer(local_url)
            ress = res.split('_')
            poem = str(ress[0])
            n = len(poem)
            poem_writer = res[n:]
            return render_template('show.html', pic_url=file_url, poem=poem, poem_writer=poem_writer)
    return render_template('index.html')

@app.route('/photos/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=5001, debug=True)
port = os.getenv('PORT', '5001')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port),debug=True)