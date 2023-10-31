from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<p>Hello, World!</p><a href="upload">Upload file</a>'

@app.route("/upload")
def upload_page():
    return '''
    <script>
    document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.upload_to_server');
    if (!form) return;

    form.addEventListener('submit', e => {
        e.preventDefault();
        const fileInput = form.querySelector('input[type="file"]');
        const file = fileInput.files[0];

        if (!file) {
        alert('Выберите файл для загрузки.');
        return;
        }

        fetch('http://127.0.0.1:5000/', { method: 'POST', body: new FormData(form) })
        .then(response => {
            if (response.status === 200) window.location.href = '/';
            else alert('Произошла ошибка при отправке файла.');
        })
        .catch(error => alert('Произошла ошибка при отправке файла: ' + error));
        });
    });
    </script>
    <form class=\"upload_to_server\">
        <input type=\"file\" />
        <input class=\"upload\" type=\"submit\" value=\"Загрузить на сервер\">
    </form>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0')