from flask import Flask, request, render_template, redirect, url_for
import os
import time
from parse import read_excel_file
from save_data import save_data

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/parse_exel_to_db/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'xls', 'xlsx'}

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        user_id = '1'
        filename = user_id + '_' + str(time.time()).split('.')[0] + '.xlsx'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        if read_excel_file(str('/parse_exel_to_db/uploads/' + filename)):
            save_data('/parse_exel_to_db/uploads/' + filename)
        return 'Файл успешно загружен!'
    else:
        return 'Недопустимый тип файла. Пожалуйста, загрузите файл с расширением .xlsx или .xls'


if __name__ == '__main__':
    app.run(debug=True)

