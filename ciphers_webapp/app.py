from flask import Flask, request, render_template
import cryptography_functions as cf

app = Flask(__name__)

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error_message = None
    if request.method == 'POST':
        cipher = request.form['cipher']
        text = request.form['text']
        key = request.form.get('key', '')
        action = request.form['action']

        if cipher == 'rail_fence':
            if not is_integer(key):
                error_message = 'The Rail Fence key must be an integer.'
            elif int(key) <= 1:
                error_message = 'The Rail Fence key must be greater than 1.'
            elif action not in ('Encrypt', 'Decrypt'):
                error_message = 'Invalid action selected.'
            else:
                try:
                    if action == 'Encrypt':
                        result = cf.rail_fence_encrypt(text, int(key))
                    else:
                        result = cf.rail_fence_decrypt(text, int(key))
                except Exception as e:
                    error_message = str(e)

        elif cipher == 'vigenere':
            if not key.isalpha():
                error_message = 'The Vigenere key must contain only alphabetic characters.'

            else:
                try:
                    result = cf.vigenere_cipher(text, key, encrypt=True if action == "Encrypt" else False)
                except Exception as e:
                    error_message = str(e)

    return render_template('index.html', result=result, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
