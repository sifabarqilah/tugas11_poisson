import math
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def kalkulator():
    table = []  # Tabel hasil perhitungan
    if request.method == "POST":
        try:
            # Mengambil input dari form
            lambda_value = float(request.form["lambda"])  # Rata-rata kedatangan (λ)
            interval = int(request.form["interval"])  # Interval waktu (misalnya jam)
            
            # Menghitung distribusi Poisson untuk beberapa nilai x (0 sampai interval)
            for x in range(interval + 1):  # Menghitung untuk x = 0 sampai interval
                peluang = (lambda_value ** x * math.exp(-lambda_value)) / math.factorial(x)
                persentase = peluang * 100
                
                # Pembulatan untuk hasil peluang dan persentase
                peluang_bulat = round(peluang, 5)  # Pembulatan peluang hingga 5 angka desimal
                persentase_bulat = round(persentase, 2)  # Pembulatan persentase hingga 2 angka desimal
                
                table.append((x, peluang_bulat, persentase_bulat))  # Menyimpan hasil perhitungan
        except Exception as e:
            print(f"Error: {e}")
            return render_template("index.html", error="Terjadi kesalahan dalam perhitungan.")
    
    # Mengirim hasil perhitungan ke tampilan
    return render_template("index.html", table=table)

# Rute untuk halaman About
@app.route("/about")
def about():
    return render_template("index.html", about_page=True)

if __name__ == "__main__":
    app.run(debug=True)
