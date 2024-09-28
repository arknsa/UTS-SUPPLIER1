# models.py
from extensions import db
from datetime import datetime
from flask_login import UserMixin

class Pembelian(db.Model):
    __tablename__ = 'db_pembelian'

    id_pembelian = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_log = db.Column(db.Integer, db.ForeignKey('db_transaksi.id_log'))
    quantity = db.Column(db.Integer)
    total_harga_barang = db.Column(db.Numeric(10, 2))
    total_berat_barang = db.Column(db.Numeric(10, 2))
    jumlah = db.Column(db.Integer)
    no_resi = db.Column(db.String(255))
    harga_pengiriman = db.Column(db.Numeric(10, 2))
    tanggal_pembelian = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Relationship dengan Transaksi
    transaksi = db.relationship('Transaksi', back_populates='pembelian')

class Produk(db.Model):
    __tablename__ = 'db_produk'

    id_produk = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_produk = db.Column(db.String(255))
    kategori = db.Column(db.String(255))
    stock = db.Column(db.Integer)
    stock_minimum = db.Column(db.Integer)
    stock_maximum = db.Column(db.Integer)
    harga = db.Column(db.Numeric(10, 2))
    berat = db.Column(db.Numeric(10, 2))
    size = db.Column(db.String(50))
    width = db.Column(db.String(50))
    genre = db.Column(db.String(255))
    warna = db.Column(db.String(255))
    deskripsi = db.Column(db.Text)
    link_gambar_barang = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    suppliers = db.relationship('Supplier', secondary='db_supplier_produk', back_populates='products')
    transaksi = db.relationship('Transaksi', back_populates='produk')

class Supplier(db.Model):
    __tablename__ = 'db_supplier'

    id_supplier = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_supplier = db.Column(db.String(255))
    contact = db.Column(db.String(255))
    alamat_supplier = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    products = db.relationship('Produk', secondary='db_supplier_produk', back_populates='suppliers')
    transaksi = db.relationship('Transaksi', back_populates='supplier')

class SupplierProduk(db.Model):
    __tablename__ = 'db_supplier_produk'

    id_supplier = db.Column(db.Integer, db.ForeignKey('db_supplier.id_supplier'), primary_key=True)
    id_produk = db.Column(db.Integer, db.ForeignKey('db_produk.id_produk'), primary_key=True)

class Transaksi(db.Model):
    __tablename__ = 'db_transaksi'

    id_log = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_supplier = db.Column(db.Integer, db.ForeignKey('db_supplier.id_supplier'))
    id_produk = db.Column(db.Integer, db.ForeignKey('db_produk.id_produk'))
    id_retail = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    total_harga_barang = db.Column(db.Numeric(10, 2))
    total_berat_barang = db.Column(db.Numeric(10, 2))
    kota_asal = db.Column(db.String(255))
    kota_tujuan = db.Column(db.String(255))
    jumlah = db.Column(db.Integer)
    harga_pengiriman = db.Column(db.Numeric(10, 2))

    # Relationships
    supplier = db.relationship('Supplier', back_populates='transaksi')
    produk = db.relationship('Produk', back_populates='transaksi')
    pembelian = db.relationship('Pembelian', back_populates='transaksi')

class User(UserMixin, db.Model):
    __tablename__ = 'db_user'

    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    @property
    def id(self):
        return self.id_user

