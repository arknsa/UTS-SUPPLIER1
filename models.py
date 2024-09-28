from sqlalchemy import Column, Integer, String, Numeric, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Pembelian(Base):
    __tablename__ = 'db_pembelian'

    id_pembelian = Column(Integer, primary_key=True, autoincrement=True)
    id_log = Column(Integer, ForeignKey('db_transaksi.id_log'))
    quantity = Column(Integer)
    total_harga_barang = Column(Numeric(10, 2))
    total_berat_barang = Column(Numeric(10, 2))
    jumlah = Column(Integer)
    no_resi = Column(String(255))
    harga_pengiriman = Column(Numeric(10, 2))
    tanggal_pembelian = Column(DateTime, default=datetime.utcnow)

    transaksi = relationship("Transaksi", back_populates="pembelian")

class Produk(Base):
    __tablename__ = 'db_produk'

    id_produk = Column(Integer, primary_key=True, autoincrement=True)
    id_barang = Column(Integer)
    nama_produk = Column(String(255))
    kategori = Column(String(255))
    stock = Column(Integer)
    stock_minimum = Column(Integer)
    stock_maximum = Column(Integer)
    harga = Column(Numeric(10, 2))
    berat = Column(Numeric(10, 2))
    size = Column(String(50))
    width = Column(String(50))
    genre = Column(String(255))
    warna = Column(String(255))
    deskripsi = Column(Text)
    link_gambar_barang = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    suppliers = relationship("Supplier", secondary="db_supplier_produk", back_populates="products")
    transaksi = relationship("Transaksi", back_populates="produk")

class Supplier(Base):
    __tablename__ = 'db_supplier'

    id_supplier = Column(Integer, primary_key=True, autoincrement=True)
    nama_supplier = Column(String(255))
    contact = Column(String(255))
    alamat_supplier = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)

    products = relationship("Produk", secondary="db_supplier_produk", back_populates="suppliers")
    transaksi = relationship("Transaksi", back_populates="supplier")

class SupplierProduk(Base):
    __tablename__ = 'db_supplier_produk'

    id_supplier = Column(Integer, ForeignKey('db_supplier.id_supplier'), primary_key=True)
    id_produk = Column(Integer, ForeignKey('db_produk.id_produk'), primary_key=True)

class Transaksi(Base):
    __tablename__ = 'db_transaksi'

    id_log = Column(Integer, primary_key=True, autoincrement=True)
    id_supplier = Column(Integer, ForeignKey('db_supplier.id_supplier'))
    id_produk = Column(Integer, ForeignKey('db_produk.id_produk'))
    id_retail = Column(Integer)
    quantity = Column(Integer)
    total_harga_barang = Column(Numeric(10, 2))
    total_berat_barang = Column(Numeric(10, 2))
    kota_asal = Column(String(255))
    kota_tujuan = Column(String(255))
    jumlah = Column(Integer)
    harga_pengiriman = Column(Numeric(10, 2))

    supplier = relationship("Supplier", back_populates="transaksi")
    produk = relationship("Produk", back_populates="transaksi")
    pembelian = relationship("Pembelian", back_populates="transaksi")

class User(Base):
    __tablename__ = 'db_user'

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255))
    password = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)