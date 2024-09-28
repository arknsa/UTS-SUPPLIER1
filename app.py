from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Transaksi, Pembelian, Supplier, Produk, User
import requests
import os

app = Flask(__name__)

# Konfigurasi MySQL
DB_USER = os.getenv('root')
DB_PASSWORD = os.getenv('')
DB_HOST = os.getenv('localhost')
DB_NAME = os.getenv('uts_supplier1')

# Konfigurasi SQLAlchemy untuk MySQL
DATABASE_URI = f"mysql+pymysql://root:@localhost/uts_supplier1"
engine = create_engine(DATABASE_URI)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

# Endpoint API distributor
DISTRIBUTOR_API = os.getenv('DISTRIBUTOR_API')

@app.route('/check_price', methods=['POST'])
def check_price():
    session = DBSession()
    data = request.json

    try:
        # Cek ongkir dari distributor
        ongkir_response = requests.post(f"{DISTRIBUTOR_API}/api/distributors6/orders/cek_ongkir", json={
            "id_log": data['id_log'],
            "kota_asal": data['kota_asal'],
            "kota_tujuan": data['kota_tujuan'],
            "quantity": data['quantity'],
            "berat": data['total_berat_barang']
        })
        ongkir_data = ongkir_response.json()

        # Membuat objek Transaksi baru
        new_transaction = Transaksi(
            id_supplier=data['id_supplier'],
            id_produk=data['id_produk'],
            id_retail=data['id_retail'],
            quantity=data['quantity'],
            total_harga_barang=data['total_harga_barang'],
            total_berat_barang=data['total_berat_barang'],
            kota_asal=data['kota_asal'],
            kota_tujuan=data['kota_tujuan'],
            jumlah=data['jumlah'],
            harga_pengiriman=ongkir_data['harga_pengiriman']
        )

        session.add(new_transaction)
        session.commit()

        return jsonify({
            "message": "Pemeriksaan harga berhasil",
            "transaction_id": new_transaction.id_log,
            "harga_pengiriman": ongkir_data['harga_pengiriman'],
            "lama_pengiriman": ongkir_data['lama_pengiriman']
        }), 200

    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400

    finally:
        session.close()

@app.route('/place_order', methods=['POST'])
def place_order():
    session = DBSession()
    data = request.json

    try:
        # Fetch the corresponding Transaksi
        transaction = session.query(Transaksi).filter_by(id_log=data['id_log']).first()
        if not transaction:
            return jsonify({"error": "Transaksi tidak ditemukan"}), 404

        # Melakukan pemesanan ke distributor
        order_response = requests.post(f"{DISTRIBUTOR_API}/api/distributors6/orders/fix_kirim", json={
            "id_log": data['id_log']
        })
        order_data = order_response.json()

        # Membuat objek Pembelian baru
        new_purchase = Pembelian(
            id_log=data['id_log'],
            quantity=transaction.quantity,
            total_harga_barang=transaction.total_harga_barang,
            total_berat_barang=transaction.total_berat_barang,
            jumlah=transaction.jumlah,
            no_resi=order_data['no_resi'],
            harga_pengiriman=order_data['harga_pengiriman']
        )

        session.add(new_purchase)
        session.commit()

        return jsonify({
            "message": "Pemesanan berhasil dilakukan",
            "purchase_id": new_purchase.id_pembelian,
            "no_resi": order_data['no_resi'],
            "lama_pengiriman": order_data['lama_pengiriman']
        }), 200

    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400

    finally:
        session.close()

@app.route('/check_status/<string:no_resi>', methods=['GET'])
def check_status(no_resi):
    try:
        status_response = requests.get(f"{DISTRIBUTOR_API}/api/status/{no_resi}")
        status_data = status_response.json()
        return jsonify(status_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint untuk supplier
@app.route('/suppliers', methods=['GET'])
def get_suppliers():
    session = DBSession()
    try:
        suppliers = session.query(Supplier).all()
        suppliers_info = [{
            "id_supplier": s.id_supplier,
            "nama_supplier": s.nama_supplier,
            "contact": s.contact,
            "alamat_supplier": s.alamat_supplier
        } for s in suppliers]
        return jsonify(suppliers_info), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        session.close()

@app.route('/products', methods=['GET'])
def get_products():
    session = DBSession()
    try:
        products = session.query(Produk).all()
        all_products = [{
            "id_produk": p.id_produk,
            "nama_produk": p.nama_produk,
            "kategori": p.kategori,
            "stock": p.stock,
            "harga": float(p.harga),
            "berat": float(p.berat)
        } for p in products]
        return jsonify(all_products), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        session.close()

@app.route('/orders', methods=['POST'])
def create_order():
    session = DBSession()
    data = request.json
    try:
        # Implementasi logika pemesanan di sini
        # Anda perlu menyesuaikan ini dengan kebutuhan spesifik Anda
        # Contoh sederhana:
        new_transaction = Transaksi(
            id_supplier=data['id_supplier'],
            id_produk=data['id_produk'],
            id_retail=data['id_retail'],
            quantity=data['quantity'],
            kota_tujuan=data['alamatpembeli'],
            # ... tambahkan field lain sesuai kebutuhan
        )
        session.add(new_transaction)
        session.commit()

        # Simulasi mendapatkan resi
        resi = f"RESI{new_transaction.id_log}"

        return jsonify({"resi": resi}), 200
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        session.close()

# Create a new product
@app.route('/products', methods=['POST'])
def create_product():
    session = DBSession()
    data = request.json
    try:
        new_product = Produk(
            nama_produk=data['nama_produk'],
            kategori=data['kategori'],
            stock=data['stock'],
            harga=data['harga'],
            berat=data['berat']
        )
        session.add(new_product)
        session.commit()
        return jsonify({
            "message": "Produk berhasil ditambahkan",
            "id_produk": new_product.id_produk
        }), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        session.close()

# Read all products
@app.route('/products', methods=['GET'])
def get_all_products():
    session = DBSession()
    try:
        products = session.query(Produk).all()
        return jsonify([{
            "id_produk": p.id_produk,
            "nama_produk": p.nama_produk,
            "kategori": p.kategori,
            "stock": p.stock,
            "harga": float(p.harga),
            "berat": float(p.berat)
        } for p in products]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        session.close()

# Read a specific product
@app.route('/products/<int:id_produk>', methods=['GET'])
def get_product(id_produk):
    session = DBSession()
    try:
        product = session.query(Produk).filter_by(id_produk=id_produk).first()
        if product:
            return jsonify({
                "id_produk": product.id_produk,
                "nama_produk": product.nama_produk,
                "kategori": product.kategori,
                "stock": product.stock,
                "harga": float(product.harga),
                "berat": float(product.berat)
            }), 200
        else:
            return jsonify({"message": "Produk tidak ditemukan"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        session.close()

# Update a product
@app.route('/products/<int:id_produk>', methods=['PUT'])
def update_product(id_produk):
    session = DBSession()
    data = request.json
    try:
        product = session.query(Produk).filter_by(id_produk=id_produk).first()
        if product:
            product.nama_produk = data.get('nama_produk', product.nama_produk)
            product.kategori = data.get('kategori', product.kategori)
            product.stock = data.get('stock', product.stock)
            product.harga = data.get('harga', product.harga)
            product.berat = data.get('berat', product.berat)
            session.commit()
            return jsonify({"message": "Produk berhasil diperbarui"}), 200
        else:
            return jsonify({"message": "Produk tidak ditemukan"}), 404
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        session.close()

# Delete a product
@app.route('/products/<int:id_produk>', methods=['DELETE'])
def delete_product(id_produk):
    session = DBSession()
    try:
        product = session.query(Produk).filter_by(id_produk=id_produk).first()
        if product:
            session.delete(product)
            session.commit()
            return jsonify({"message": "Produk berhasil dihapus"}), 200
        else:
            return jsonify({"message": "Produk tidak ditemukan"}), 404
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        session.close()

if __name__ == '__main__':
    app.run(debug=True)