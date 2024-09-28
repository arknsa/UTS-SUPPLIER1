from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from extensions import db 
from flask_sqlalchemy import SQLAlchemy
from models import Produk, Supplier, Transaksi, Pembelian, User  # Imported updated models
from datetime import datetime
from flask_login import LoginManager

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/uts_supplier1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


# Fungsi untuk memuat user berdasarkan id (dibutuhkan oleh Flask-Login)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user is None:
            flash('Username tidak ditemukan.', 'danger')
            return redirect(url_for('login'))

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Login berhasil!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Password salah.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')


# Route untuk logout
@app.route('/logout')
def logout():
    logout_user()
    flash('Anda telah logout!', 'success')
    return redirect(url_for('login'))

# Dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    try:
        return render_template('dashboard.html')
    except Exception as e:
        print(f"Error rendering dashboard: {e}")
        return "An error occurred.", 500


# Route untuk admin
@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html')

# Suppliers - Mengembalikan semua data supplier dalam format JSON
@app.route('/suppliers', methods=['GET'])
def suppliers():
    suppliers_info = Supplier.query.all()
    suppliers_list = [{
        "id_supplier": supplier.id_supplier,
        "nama_supplier": supplier.nama_supplier,
        "contact": supplier.contact,
        "alamat_supplier": supplier.alamat_supplier,
        "created_at": supplier.created_at.strftime('%Y-%m-%d %H:%M:%S')
    } for supplier in suppliers_info]

    return jsonify(suppliers_list)

@app.route('/products', methods=['GET'])
def products():
    try:
        all_products = Produk.query.all()
        if not all_products:
            return jsonify({"message": "No products found"}), 200
        
        products_list = [{
            "id_barang": product.id_produk,  # Use id_produk since that's the primary key in your model
            "nama_produk": product.nama_produk,
            "kategori": product.kategori,
            "stock": product.stock,
            "harga": float(product.harga),
            "berat": float(product.berat),
            "size": product.size,
            "width": product.width,
            "genre": product.genre,
            "warna": product.warna,
            "deskripsi": product.deskripsi,
            "link_gambar_barang": product.link_gambar_barang,
            "created_at": product.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": product.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        } for product in all_products]

        return jsonify(products_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route untuk menampilkan halaman Manage Product
@app.route('/manage_product')
@login_required
def manage_product():
    products = Produk.query.all()
    return render_template('manage_product.html', products=products)

# Route untuk menambah produk baru
@app.route('/add_product', methods=['GET', 'POST'])
@login_required
def add_product():
    if request.method == 'POST':
        # Ambil data dari form HTML
        nama_produk = request.form['nama_produk']
        kategori = request.form['kategori']
        stock = int(request.form['stock'])
        harga = float(request.form['harga'])
        berat = float(request.form['berat'])
        size = request.form['size']
        width = request.form['width']
        genre = request.form['genre']
        warna = request.form['warna']
        deskripsi = request.form['deskripsi']
        link_gambar_barang = request.form['link_gambar_barang']

        # Buat objek produk baru
        new_product = Produk(
            nama_produk=nama_produk,
            kategori=kategori,
            stock=stock,
            harga=harga,
            berat=berat,
            size=size,
            width=width,
            genre=genre,
            warna=warna,
            deskripsi=deskripsi,
            link_gambar_barang=link_gambar_barang
        )

        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('manage_product'))
    
    return render_template('add_product.html')

@app.route('/edit_product/<int:id_produk>', methods=['GET', 'POST'])
@login_required
def edit_product(id_produk):
    product = Produk.query.filter_by(id_produk=id_produk).first()

    if not product:
        flash('Produk tidak ditemukan', 'danger')
        return redirect(url_for('manage_product'))

    if request.method == 'POST':
        # Update data produk dengan data dari form
        product.nama_produk = request.form['nama_produk']
        product.kategori = request.form['kategori']
        product.stock = int(request.form['stock'])
        product.harga = float(request.form['harga'])
        product.berat = float(request.form['berat'])
        product.size = request.form['size']
        product.width = request.form['width']
        product.genre = request.form['genre']
        product.warna = request.form['warna']
        product.deskripsi = request.form['deskripsi']
        product.link_gambar_barang = request.form['link_gambar_barang']

        db.session.commit()
        flash('Produk berhasil diperbarui', 'success')
        return redirect(url_for('manage_product'))

    return render_template('edit_product.html', product=product)


# Route untuk menghapus produk
@app.route('/delete_product/<int:id_produk>', methods=['POST'])
@login_required
def delete_product(id_produk):
    product = Produk.query.filter_by(id_produk=id_produk).first()
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('manage_product'))

# Route untuk melihat detail produk
@app.route('/view_product/<int:id_produk>', methods=['GET'])
@login_required
def view_product(id_produk):
    product = Produk.query.filter_by(id_produk=id_produk).first()

    if not product:
        flash('Produk tidak ditemukan', 'danger')
        return redirect(url_for('manage_product'))

    return render_template('view_product.html', product=product)


# Orders - Buat pesanan baru
@app.route('/orders', methods=['POST'])
@login_required
def orders():
    data = request.get_json()
    list_barang = data.get('list_barang')

    # Validate list_barang
    if not list_barang:
        return jsonify({"error": "List barang tidak boleh kosong"}), 400

    # Perhitungan sederhana
    total_harga = len(list_barang.split(',')) * 1000
    total_berat = len(list_barang.split(',')) * 1

    # Buat nomor resi
    resi = f"RESI-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"

    # Simpan transaksi
    new_transaksi = Transaksi(
        id_retail=current_user.id_user,  # Assuming a user is linked to retail here
        total_harga_barang=total_harga,
        total_berat_barang=total_berat,
        kota_asal='Kota Asal',  # Placeholder for city data
        kota_tujuan='Kota Tujuan',  # Placeholder for city data
        jumlah=len(list_barang.split(',')),
        harga_pengiriman=0.0
    )
    db.session.add(new_transaksi)
    db.session.commit()

    return jsonify({
        "resi": resi,
        "message": "Pesanan berhasil dibuat",
        "total_harga": total_harga,
        "total_berat": total_berat
    }), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
