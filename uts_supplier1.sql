-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 28, 2024 at 01:05 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `uts_supplier1`
--

-- --------------------------------------------------------

--
-- Table structure for table `db_pembelian`
--

CREATE TABLE `db_pembelian` (
  `id_pembelian` int(11) NOT NULL,
  `id_log` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `total_harga_barang` decimal(10,2) DEFAULT NULL,
  `total_berat_barang` decimal(10,2) DEFAULT NULL,
  `jumlah` int(11) DEFAULT NULL,
  `no_resi` varchar(255) DEFAULT NULL,
  `harga_pengiriman` decimal(10,2) DEFAULT NULL,
  `tanggal_pembelian` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `db_produk`
--

CREATE TABLE `db_produk` (
  `id_produk` int(11) NOT NULL,
  `id_barang` int(11) DEFAULT NULL,
  `nama_produk` varchar(255) DEFAULT NULL,
  `kategori` varchar(255) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL,
  `stock_minimum` int(11) DEFAULT NULL,
  `stock_maximum` int(11) DEFAULT NULL,
  `harga` decimal(10,2) DEFAULT NULL,
  `berat` decimal(10,2) DEFAULT NULL,
  `size` varchar(50) DEFAULT NULL,
  `width` varchar(50) DEFAULT NULL,
  `genre` varchar(255) DEFAULT NULL,
  `warna` varchar(255) DEFAULT NULL,
  `deskripsi` text DEFAULT NULL,
  `link_gambar_barang` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `db_produk`
--

INSERT INTO `db_produk` (`id_produk`, `id_barang`, `nama_produk`, `kategori`, `stock`, `stock_minimum`, `stock_maximum`, `harga`, `berat`, `size`, `width`, `genre`, `warna`, `deskripsi`, `link_gambar_barang`, `created_at`, `updated_at`) VALUES
(1, 111, 'Genio Ban Luar 20 x 1.75 157', 'Ban Luar', 100, 10, 150, 60000.00, 0.61, '20 x 1.75', '1.75', 'kawat', 'hitam', 'Genio Ban Luar 20 x 1.75 157 berukuran 20 yang cocok menggantikan ban luar sepeda dengan ukuran 20 x 1.75. Fitur: ukuran 20 inci, bahan rubber, jenis ban wire, traction yang baik.', 'https://icubic-space.sgp1.digitaloceanspaces.com/app/public/ss/lib/pro/img/2024/09/genio-ban-luar-20-x-175-157-1-1726038482.jpg', '2024-09-28 10:37:16', '2024-09-28 10:37:16'),
(2, 112, 'CST Ban Luar 700 x 35C S-Sumo', 'Ban Luar', 80, 8, 120, 345000.00, 0.62, '700 x 35C', '35', 'kawat', 'hitam', 'CST Ban Luar 700 x 35C S-Sumo berukuran 700c yang cocok menggantikan ban luar sepeda dengan ukuran 700 x 35c. Fitur: ukuran 700c, bahan rubber, jenis ban wire, traction yang baik.', 'https://icubic-space.sgp1.digitaloceanspaces.com/app/public/ss/lib/pro/img/2024/09/img-8346jpg1jpgedit-1725353921.jpg', '2024-09-28 10:37:16', '2024-09-28 10:37:16'),
(3, 113, 'CST Ban Luar 700 x 28C C740', 'Ban Luar', 90, 9, 130, 160000.00, 0.43, '700 x 28C', '28', 'kawat', 'hitam', 'CST Ban Luar 700 x 28C C740 berukuran 700c yang cocok menggantikan ban luar sepeda dengan ukuran 700 x 28c. Fitur: ukuran 700, bahan rubber, jenis ban wire, traction yang baik.', 'https://icubic-space.sgp1.digitaloceanspaces.com/app/public/ss/lib/pro/img/2024/08/cst-ban-luar-700-x-28c-c740-1-1724748689.jpg', '2024-09-28 10:37:16', '2024-09-28 10:37:16'),
(4, 114, 'CST Ban Luar 700 x 23C Black Road', 'Ban Luar', 70, 7, 110, 160000.00, 0.42, '700 x 23C', '23', 'kawat', 'hitam', 'CST Ban Luar 700 x 23C Black Road berukuran 700c yang cocok menggantikan ban luar sepeda dengan ukuran 700 x 23c. Fitur: ukuran 700, bahan rubber, jenis ban wire, traction yang baik.', 'https://icubic-space.sgp1.digitaloceanspaces.com/app/public/ss/lib/pro/img/2024/08/cst-ban-luar-700-x-23c-black-road-1-1724748063.jpg', '2024-09-28 10:37:16', '2024-09-28 10:37:16'),
(5, 115, 'CST Ban Luar 700 x 25C C1818 Recourse', 'Ban Luar', 85, 8, 120, 230000.00, 0.31, '700 x 25C', '25', 'kawat', 'hitam', 'CST Ban Luar 700 x 25C C1818 Recourse berukuran 700c yang cocok menggantikan ban luar sepeda dengan ukuran 700 x 25c. Fitur: ukuran 700, bahan rubber, jenis ban wire, traction yang baik.', 'https://icubic-space.sgp1.digitaloceanspaces.com/app/public/ss/lib/pro/img/2024/08/cst-ban-luar-700-x-25c-c1818-recourse-1-1724747542.jpg', '2024-09-28 10:37:16', '2024-09-28 10:37:16'),
(6, 116, 'CST Ban Luar 20 x 1.75 C1959 Coffee Skinwall', 'Ban Luar', 75, 7, 110, 250000.00, 0.39, '20 x 1.75', '1.75', 'kawat', 'hitam', 'CST Ban Luar 20 x 1.75 C1959 Coffee Skinwall berukuran 20 yang cocok menggantikan ban luar sepeda dengan ukuran 20 x 1.75. Fitur: ukuran 20 inci, bahan rubber, jenis ban wire, traction yang baik.', 'https://icubic-space.sgp1.digitaloceanspaces.com/app/public/ss/lib/pro/img/2024/08/cst-ban-luar-20-x-175-c1959-coffee-skinwall-1-1724747458.jpg', '2024-09-28 10:37:16', '2024-09-28 10:37:16'),
(7, 117, 'Schwalbe Ban Luar 16 x 1.35 349 One Skinwall', 'Ban Luar', 60, 6, 100, 798000.00, 0.25, '16 x 1.35', '1.35', 'kawat', 'hitam', 'Schwalbe Ban Luar 16 x 1.35 349 One Skinwall berukuran 16 yang cocok menggantikan ban luar sepeda dengan ukuran 16 x 1.35. Fitur: ukuran 16 inci, bahan rubber, jenis ban kevlar, traction yang baik.', 'https://icubic-space.sgp1.digitaloceanspaces.com/app/public/ss/lib/pro/img/2024/08/schwalbe-ban-luar-16-x-135-349-one-skinwall-1722581805.jpg', '2024-09-28 10:37:16', '2024-09-28 10:37:16'),
(8, 118, 'Pro Action Ban Luar 16 x 1 3/8 Skinwall', 'Ban Luar', 95, 9, 140, 100000.00, 0.42, '16 x 1.375', '1.375', 'kawat', 'hitam', 'Pro Action Ban Luar 16 x 1 3/8 Skinwall berukuran 16 yang cocok menggantikan ban luar sepeda dengan ukuran 16 x 1 3/8. Fitur: ukuran 16 inci, bahan rubber, jenis ban wire, traction yang baik.', 'https://icubic-space.sgp1.digitaloceanspaces.com/app/public/ss/lib/pro/img/2024/07/pro-action-ban-luar-16-x-1-38-skinwall-1-1721015834.jpg', '2024-09-28 10:37:16', '2024-09-28 10:37:16'),
(9, 119, 'Vittoria Ban Luar 700 x 23C Topazio Pro', 'Ban Luar', 50, 5, 90, 370000.00, 0.25, '700 x 23C', '23', 'kawat', 'hitam', 'Vittoria Ban Luar 700 x 23C Topazio Pro berukuran 700c yang cocok menggantikan ban luar sepeda dengan ukuran 700 x 23. Fitur: ukuran 700c, bahan rubber, jenis ban kevlar, traction yang baik.', 'https://icubic-space.sgp1.digitaloceanspaces.com/app/public/ss/lib/pro/img/2024/07/vittoria-ban-luar-700-x-23c-topazio-pro-1-1720782259.jpg', '2024-09-28 10:37:16', '2024-09-28 10:37:16'),
(10, 1110, 'Genio Ban Luar 26 x 1.95', 'Ban Luar', 100, 10, 150, 80000.00, 1.02, '26 x 1.95', '1.95', 'kawat', 'hitam', 'Genio Ban Luar 26 x 1.95 berukuran 26 yang cocok menggantikan ban luar sepeda dengan ukuran 26 x 1.95. Fitur: ukuran 26 inci, bahan rubber, jenis ban wire, traction yang baik.', 'https://icubic-space.sgp1.digitaloceanspaces.com/app/public/ss/lib/pro/img/2024/02/genio-ban-luar-26-x-195-1-1707115715.jpg', '2024-09-28 10:37:16', '2024-09-28 10:37:16'),
(11, 121, 'CST Ban Dalam 700 x 35-43 FV 60mm', 'Ban Dalam', 85, 8, 120, 110000.00, 0.40, '700 x 35-43', '35', 'Presta', 'hitam', 'CST Ban Dalam 700 x 35-43 FV 60mm adalah ban dalam sepeda yang terbuat dari bahan rubber yang elastis. Ban dalam ini memiliki panjang pentil sekitar 60mm. Fitur: ukuran 700 x 35-43, bahan rubber, panjang pentil 60mm, FV (French Valve) atau Presta.', 'https://icubic-space.sgp1.digitaloceanspaces.com/app/public/ss/lib/pro/img/2024/08/cst-ban-dalam-700-x-35-43-fv-60mm-1-1724751679.jpg', '2024-09-28 10:37:16', '2024-09-28 10:37:16'),
(12, 122, 'CST Ban Dalam 700 x 19/23 FV 48mm', 'Ban Dalam', 65, 6, 110, 75000.00, 0.20, '700 x 19/23', '23', 'Presta', 'hitam', 'CST Ban Dalam 700 x 19/23 FV 48mm adalah ban dalam sepeda yang terbuat dari bahan rubber yang elastis. Ban dalam ini memiliki panjang pentil sekitar 48mm. Fitur: ukuran 700 x 19/23, bahan rubber, panjang pentil 48mm, FV (French Valve) atau Presta.', 'https://icubic-space.sgp1.digitaloceanspaces.com/app/public/ss/lib/pro/img/2024/08/cst-ban-dalam-700-x-1923-fv-48mm-1-1724746592.jpg', '2024-09-28 10:37:16', '2024-09-28 10:37:16');

-- --------------------------------------------------------

--
-- Table structure for table `db_supplier`
--

CREATE TABLE `db_supplier` (
  `id_supplier` int(11) NOT NULL,
  `nama_supplier` varchar(255) DEFAULT NULL,
  `contact` varchar(255) DEFAULT NULL,
  `alamat_supplier` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `db_supplier_produk`
--

CREATE TABLE `db_supplier_produk` (
  `id_supplier` int(11) NOT NULL,
  `id_produk` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `db_transaksi`
--

CREATE TABLE `db_transaksi` (
  `id_log` int(11) NOT NULL,
  `id_supplier` int(11) DEFAULT NULL,
  `id_produk` int(11) DEFAULT NULL,
  `id_retail` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `total_harga_barang` decimal(10,2) DEFAULT NULL,
  `total_berat_barang` decimal(10,2) DEFAULT NULL,
  `kota_asal` varchar(255) DEFAULT NULL,
  `kota_tujuan` varchar(255) DEFAULT NULL,
  `jumlah` int(11) DEFAULT NULL,
  `harga_pengiriman` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `db_user`
--

CREATE TABLE `db_user` (
  `id_user` int(11) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `db_pembelian`
--
ALTER TABLE `db_pembelian`
  ADD PRIMARY KEY (`id_pembelian`),
  ADD KEY `id_log` (`id_log`);

--
-- Indexes for table `db_produk`
--
ALTER TABLE `db_produk`
  ADD PRIMARY KEY (`id_produk`);

--
-- Indexes for table `db_supplier`
--
ALTER TABLE `db_supplier`
  ADD PRIMARY KEY (`id_supplier`);

--
-- Indexes for table `db_supplier_produk`
--
ALTER TABLE `db_supplier_produk`
  ADD PRIMARY KEY (`id_supplier`,`id_produk`),
  ADD KEY `id_produk` (`id_produk`);

--
-- Indexes for table `db_transaksi`
--
ALTER TABLE `db_transaksi`
  ADD PRIMARY KEY (`id_log`),
  ADD KEY `id_supplier` (`id_supplier`),
  ADD KEY `id_produk` (`id_produk`);

--
-- Indexes for table `db_user`
--
ALTER TABLE `db_user`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `db_pembelian`
--
ALTER TABLE `db_pembelian`
  MODIFY `id_pembelian` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `db_produk`
--
ALTER TABLE `db_produk`
  MODIFY `id_produk` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `db_supplier`
--
ALTER TABLE `db_supplier`
  MODIFY `id_supplier` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `db_transaksi`
--
ALTER TABLE `db_transaksi`
  MODIFY `id_log` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `db_user`
--
ALTER TABLE `db_user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `db_pembelian`
--
ALTER TABLE `db_pembelian`
  ADD CONSTRAINT `db_pembelian_ibfk_1` FOREIGN KEY (`id_log`) REFERENCES `db_transaksi` (`id_log`);

--
-- Constraints for table `db_supplier_produk`
--
ALTER TABLE `db_supplier_produk`
  ADD CONSTRAINT `db_supplier_produk_ibfk_1` FOREIGN KEY (`id_supplier`) REFERENCES `db_supplier` (`id_supplier`),
  ADD CONSTRAINT `db_supplier_produk_ibfk_2` FOREIGN KEY (`id_produk`) REFERENCES `db_produk` (`id_produk`);

--
-- Constraints for table `db_transaksi`
--
ALTER TABLE `db_transaksi`
  ADD CONSTRAINT `db_transaksi_ibfk_1` FOREIGN KEY (`id_supplier`) REFERENCES `db_supplier` (`id_supplier`),
  ADD CONSTRAINT `db_transaksi_ibfk_2` FOREIGN KEY (`id_produk`) REFERENCES `db_produk` (`id_produk`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
