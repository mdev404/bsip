from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # Menampilkan halaman utama (index.html)
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    # Mendapatkan data JSON dari frontend
    data = request.get_json()
    name = data.get('name', '')
    
    # Menyapa pengguna dengan nama yang dimasukkan
    if name:
        message = f"Hello, {name}! Selamat datang di Flask Web App!"
    else:
        message = "Nama tidak boleh kosong."
    
    # Mengirimkan respons dalam format JSON
    return jsonify({'message': message})

if __name__ == '__main__':
    # Menjalankan aplikasi Flask pada host lokal
    app.run(debug=True)
