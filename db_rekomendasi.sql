-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 03, 2024 at 04:40 PM
-- Server version: 5.7.39
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_rekomendasi`
--

-- --------------------------------------------------------

--
-- Table structure for table `data_kombinasi`
--

CREATE TABLE `data_kombinasi` (
  `id_kombinasi` int(11) NOT NULL,
  `kombinasi_warna` text,
  `style_desain` text,
  `makna_warna` text,
  `sifat` text,
  `usia_pengguna` text,
  `warna_dasar` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `data_kombinasi`
--

INSERT INTO `data_kombinasi` (`id_kombinasi`, `kombinasi_warna`, `style_desain`, `makna_warna`, `sifat`, `usia_pengguna`, `warna_dasar`) VALUES
(1, 'Putih & Hitam', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Kekuatan, Suci', 'Panas, Dingin', 'D, L, R', 'Putih, Hitam'),
(2, 'Putih & Kuning', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Keceriaan, Suci', 'Panas, Dingin', 'D, L, A, R', 'Putih, Kuning'),
(3, 'Putih & Merah', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Suci, Keberanian', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih'),
(4, 'Putih & Ungu', 'American Classic, Alam, Modern, Tradisional, Industrial, Minimalis', 'Keagungan, Suci', 'Dingin', 'D, L, A, R', 'Merah, Putih, Biru'),
(5, 'Putih & Hijau', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Suci, Santai', 'Dingin', 'D, L, A, R', 'Putih, Kuning, Biru'),
(6, 'Putih & Biru', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Ketenangan, Suci', 'Dingin', 'D, L, A, R', 'Putih, Biru'),
(7, 'Putih & Oren', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Keceriaan, Suci', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning'),
(8, 'Putih & Coklat', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Kenyamanan, Suci', 'Hangat, Dingin', 'L, R', 'Merah, Putih, Kuning, Biru'),
(9, 'Putih & Abu-abu', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Kerendahan hati, Suci', 'Dingin', 'D, L, R', 'Putih, Hitam'),
(10, 'Putih & Merah muda', 'American Classic, Alam, Modern, Tradisional, Industrial, Minimalis', 'Kewanitaan, Suci', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih'),
(11, 'Putih & Merah tua', 'American Classic, Alam, Modern, Tradisional, Industrial, Minimalis', 'Suci, Keberanian', 'Panas, Dingin', 'L, R', 'Merah, Putih, Hitam'),
(12, 'Putih & Biru tua', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Ketenangan, Suci', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(13, 'Putih & Abu-abu tua', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Kerendahan hati, Suci', 'Panas, Dingin', 'D, L, R', 'Putih, Hitam'),
(14, 'Putih & Hijau tua', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Suci, Santai', 'Dingin', 'L, R', 'Putih, Hijau, Hitam'),
(15, 'Putih & Coklat tua', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Kejantanan, Suci', 'Hangat, Dingin', 'L, R', 'Merah, Putih, Kuning, Biru'),
(16, 'Putih & Coklat muda', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Kejantanan, Suci', 'Hangat, Dingin', 'L, R', 'Merah, Putih, Kuning, Biru'),
(17, 'Putih & Biru muda', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Kewanitaan, Suci', 'Dingin', 'D, L, A, R', 'Putih, Biru'),
(18, 'Putih & Abu-abu muda', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Kerendahan hati, Suci', 'Dingin', 'D, L, R', 'Putih, Hitam'),
(19, 'Putih & Hijau muda', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Kewanitaan, Suci', 'Hangat, Dingin', 'D, L, A, R', 'Putih, Kuning, Biru'),
(20, 'Putih & Magenta', 'American Classic, Alam, Modern, Tradisional, Industrial, Minimalis', 'Kewanitaan, Suci', 'Dingin', 'D, L, A, R', 'Merah, Putih, Biru'),
(21, 'Putih & Emas', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Keagungan, Suci', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(22, 'Putih & Biru navy', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Ketenangan, Suci', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(23, 'Putih & Merah maroon', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Keceriaan, Suci', 'Panas, Dingin', 'D, L, R', 'Merah, Putih, Kuning, Biru'),
(24, 'Putih & Peach', 'American Classic, Alam, Modern, Tradisional, Industrial, Minimalis', 'Kewanitaan, Suci', 'Hangat, Dingin', 'D, L, R', 'Merah, Putih, Kuning'),
(25, 'Putih & Silver', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Ketenangan, Suci', 'Dingin', 'D, L, R', 'Putih, Hitam'),
(26, 'Putih & Coral', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Kewanitaan, Suci', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning'),
(27, 'Putih & Biru air', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Ketenangan, Suci', 'Dingin', 'D, L, A, R', 'Putih, Biru'),
(28, 'Putih & Krem', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Kehangatan, Suci', 'Hangat, Dingin', 'D, L, R', 'Merah, Putih, Kuning, Biru'),
(29, 'Putih & Hijau lumut', 'American Classic, Alam, Tradisional, Industrial, Minimalis', 'Kejantanan, Suci', 'Dingin', 'L, R', 'Putih, Kuning, Biru'),
(30, 'Hitam & Kuning', 'Industrial, American Classic', 'Keceriaan, Kekuatan', 'Panas', 'D, A, R', 'Kuning, Hitam'),
(31, 'Hitam & Merah', 'Industrial, American Classic', 'Kekuatan, Keberanian', 'Panas', 'D, A, R', 'Merah, Hitam'),
(32, 'Hitam & Ungu', 'Modern, Industrial', 'Keagungan, Kekuatan', 'Panas, Dingin', 'D, A, R', 'Merah, Biru, Hitam'),
(33, 'Hitam & Hijau', 'Alam, Industrial', 'Kekuatan, Santai', 'Panas, Dingin', 'D, L, A, R', 'Kuning, Biru, Hitam'),
(34, 'Hitam & Biru', 'Alam, Industrial', 'Ketenangan, Kekuatan', 'Panas, Dingin', 'D, L, A, R', 'Biru, Hitam'),
(35, 'Hitam & Oren', 'Industrial, American Classic', 'Keceriaan, Kekuatan', 'Panas', 'D, L, A, R', 'Merah, Kuning, Hitam'),
(36, 'Hitam & Coklat', 'Alam, Industrial, Tradisional', 'Kenyamanan, Kekuatan', 'Panas, Hangat', 'D, L, R', 'Merah, Kuning, Biru, Hitam'),
(37, 'Hitam & Abu-abu', 'Industrial', 'Kerendahan hati, Kekuatan', 'Panas, Dingin', 'D, L, R', 'Putih, Hitam'),
(38, 'Hitam & Merah muda', 'Modern, Industrial', 'Kewanitaan, Kekuatan', 'Panas', 'D, A, R', 'Merah, Putih, Hitam'),
(39, 'Hitam & Merah tua', 'Modern, Industrial', 'Kekuatan, Keberanian', 'Panas', 'D, L, R', 'Merah, Hitam'),
(40, 'Hitam & Biru tua', 'Alam, Industrial', 'Ketenangan, Kekuatan', 'Panas, Dingin', 'D, L, A, R', 'Biru, Hitam'),
(41, 'Hitam & Abu-abu tua', 'Industrial', 'Kerendahan hati, Kekuatan', 'Panas', 'D, L, R', 'Putih, Hitam'),
(42, 'Hitam & Hijau tua', 'Alam, Industrial', 'Kekuatan, Santai', 'Panas, Dingin', 'D, L, R', 'Hijau, Hitam'),
(43, 'Hitam & Coklat tua', 'Alam, Industrial, Tradisional', 'Kejantanan, Kekuatan', 'Panas, Hangat', 'D, L, R', 'Merah, Kuning, Biru, Hitam'),
(44, 'Hitam & Coklat muda', 'Tradisional, Alam, Industrial, American Classic', 'Kejantanan, Kekuatan', 'Panas, Hangat', 'D, L, R', 'Merah, Kuning, Biru, Hitam'),
(45, 'Hitam & Biru muda', 'Alam, Industrial, American Classic', 'Kewanitaan, Kekuatan', 'Panas, Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(46, 'Hitam & Abu-abu muda', 'Industrial', 'Kerendahan hati, Kekuatan', 'Panas, Dingin', 'D, L, R', 'Putih, Hitam'),
(47, 'Hitam & Hijau muda', 'Alam, Industrial, American Classic', 'Kewanitaan, Kekuatan', 'Panas, Hangat', 'D, L, A, R', 'Kuning, Biru, Hitam'),
(48, 'Hitam & Magenta', 'Modern, Industrial, American Classic', 'Kewanitaan, Kekuatan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Biru, Hitam'),
(49, 'Hitam & Emas', 'Industrial, American Classic', 'Keagungan, Kekuatan', 'Panas', 'D, L, A, R', 'Merah, Kuning, Biru, Hitam'),
(50, 'Hitam & Biru navy', 'Alam, Industrial', 'Ketenangan, Kekuatan', 'Panas, Dingin', 'D, L, A, R', 'Biru, Hitam'),
(51, 'Hitam & Merah maroon', 'Alam, Industrial, Tradisional', 'Keceriaan, Kekuatan', 'Panas', 'D, L, R', 'Merah, Kuning, Biru, Hitam'),
(52, 'Hitam & Peach', 'Modern, Industrial, American Classic', 'Kewanitaan, Kekuatan', 'Panas, Hangat', 'D, L, R', 'Merah, Putih, Kuning,  &'),
(53, 'Hitam & Silver', 'Industrial', 'Ketenangan, Kekuatan', 'Panas, Dingin', 'D, L, R', 'Putih, Hitam'),
(54, 'Hitam & Coral', 'Industrial, American Classic', 'Kewanitaan, Kekuatan', 'Panas', 'D, L, A, R', 'Merah, Kuning, Hitam'),
(55, 'Hitam & Biru air', 'Alam, Industrial, American Classic', 'Ketenangan, Kekuatan', 'Panas, Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(56, 'Hitam & Krem', 'Industrial, American Classic', 'Kekuatan, Kehangatan', 'Panas, Hangat', 'D, L, R', 'Merah, Kuning, Biru, Hitam'),
(57, 'Hitam & Hijau lumut', 'Alam, Industrial', 'Kejantanan, Kekuatan', 'Panas, Dingin', 'D, L, R', 'Putih, Kuning, Biru, Hitam'),
(58, 'Kuning & Merah', 'American Classic', 'Keceriaan, Keberanian', 'Panas', 'D, A, R', 'Merah, Kuning'),
(59, 'Kuning & Ungu', 'Modern, American Classic', 'Keceriaan, Keagungan', 'Panas, Dingin', 'D, A, R', 'Merah, Kuning, Biru'),
(60, 'Kuning & Hijau', 'Alam, American Classic', 'Keceriaan, Santai', 'Panas, Dingin', 'D, L, A, R', 'Kuning, Biru'),
(61, 'Kuning & Biru', 'Alam, American Classic', 'Keceriaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Kuning, Biru'),
(62, 'Kuning & Oren', 'American Classic', 'Keceriaan', 'Panas', 'D, L, A, R', 'Merah, Kuning'),
(63, 'Kuning & Coklat', 'Tradisional, Alam, American Classic', 'Keceriaan, Kenyamanan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(64, 'Kuning & Abu-abu', 'Industrial, American Classic', 'Kerendahan hati, Keceriaan', 'Panas, Dingin', 'D, L, A, R', 'Putih, Kuning, Hitam'),
(65, 'Kuning & Merah muda', 'Modern, American Classic', 'Keceriaan, Kewanitaan', 'Panas', 'D, A, R', 'Merah, Putih, Kuning'),
(66, 'Kuning & Merah tua', 'Modern, American Classic', 'Keceriaan, Keberanian', 'Panas', 'D, L, A, R', 'Merah, Kuning, Hitam'),
(67, 'Kuning & Biru tua', 'Alam, American Classic', 'Keceriaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Kuning, Biru, Hitam'),
(68, 'Kuning & Abu-abu tua', 'Industrial, American Classic', 'Kerendahan hati, Keceriaan', 'Panas', 'D, L, A, R', 'Putih, Kuning, Hitam'),
(69, 'Kuning & Hijau tua', 'Alam, American Classic', 'Keceriaan, Santai', 'Panas, Dingin', 'D, L, A, R', 'Kuning, Hijau, Hitam'),
(70, 'Kuning & Coklat tua', 'Tradisional, Alam, American Classic', 'Keceriaan, Kejantanan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(71, 'Kuning & Coklat muda', 'Tradisional, Alam, American Classic', 'Keceriaan, Kejantanan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(72, 'Kuning & Biru muda', 'Alam, American Classic', 'Keceriaan, Kewanitaan', 'Panas, Dingin', 'D, L, A, R', 'Putih, Kuning, Biru'),
(73, 'Kuning & Abu-abu muda', 'Industrial, American Classic', 'Kerendahan hati, Keceriaan', 'Panas, Dingin', 'D, L, A, R', 'Putih, Kuning, Hitam'),
(74, 'Kuning & Hijau muda', 'Alam, American Classic', 'Keceriaan, Kewanitaan', 'Panas, Hangat', 'D, L, A, R', 'Kuning, Biru'),
(75, 'Kuning & Magenta', 'Modern, American Classic', 'Keceriaan, Kewanitaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(76, 'Kuning & Emas', 'American Classic', 'Keceriaan, Keagungan', 'Panas', 'D, L, A, R', 'Merah, Kuning, Biru'),
(77, 'Kuning & Biru navy', 'Alam, American Classic', 'Keceriaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Kuning, Biru, Hitam'),
(78, 'Kuning & Merah maroon', 'Tradisional, Alam, American Classic', 'Keceriaan', 'Panas', 'D, L, A, R', 'Merah, Kuning, Biru'),
(79, 'Kuning & Peach', 'Modern, American Classic', 'Keceriaan, Kewanitaan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Putih, Kuning'),
(80, 'Kuning & Silver', 'Industrial, American Classic', 'Keceriaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Putih, Kuning, Hitam'),
(81, 'Kuning & Coral', 'American Classic', 'Keceriaan, Kewanitaan', 'Panas', 'D, L, A, R', 'Merah, Kuning'),
(82, 'Kuning & Biru air', 'Alam, American Classic', 'Keceriaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Putih, Kuning, Biru'),
(83, 'Kuning & Krem', 'American Classic', 'Keceriaan, Kehangatan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(84, 'Kuning & Hijau lumut', 'Alam, American Classic', 'Keceriaan, Kejantanan', 'Panas, Dingin', 'D, L, A, R', 'Putih, Kuning, Biru'),
(85, 'Merah & Ungu', 'Modern, American Classic', 'Keagungan, Keberanian', 'Panas, Dingin', 'D, A, R', 'Merah, Biru'),
(86, 'Merah & Hijau', 'Alam, American Classic', 'Santai, Keberanian', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(87, 'Merah & Biru', 'Alam, American Classic', 'Ketenangan, Keberanian', 'Panas, Dingin', 'D, L, A, R', 'Merah, Biru'),
(88, 'Merah & Oren', 'American Classic', 'Keceriaan, Keberanian', 'Panas', 'D, L, A, R', 'Merah, Kuning'),
(89, 'Merah & Coklat', 'Tradisional, Alam, American Classic', 'Kenyamanan, Keberanian', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(90, 'Merah & Abu-abu', 'Industrial, American Classic', 'Kerendahan hati, Keberanian', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Hitam'),
(91, 'Merah & Merah muda', 'Modern, American Classic', 'Kewanitaan, Keberanian', 'Panas', 'D, A, R', 'Merah, Putih'),
(92, 'Merah & Merah tua', 'Modern, American Classic', 'Keberanian', 'Panas', 'D, L, A, R', 'Merah, Hitam'),
(93, 'Merah & Biru tua', 'Alam, American Classic', 'Ketenangan, Keberanian', 'Panas, Dingin', 'D, L, A, R', 'Merah, Biru, Hitam'),
(94, 'Merah & Abu-abu tua', 'Industrial, American Classic', 'Kerendahan hati, Keberanian', 'Panas', 'D, L, A, R', 'Merah, Putih, Hitam'),
(95, 'Merah & Hijau tua', 'Alam, American Classic', 'Santai, Keberanian', 'Panas, Dingin', 'D, L, A, R', 'Merah, Hijau, Hitam'),
(96, 'Merah & Coklat tua', 'Tradisional, Alam, American Classic', 'Kejantanan, Keberanian', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(97, 'Merah & Coklat muda', 'Tradisional, Alam, American Classic', 'Kejantanan, Keberanian', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(98, 'Merah & Biru muda', 'Alam, American Classic', 'Kewanitaan, Keberanian', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Biru'),
(99, 'Merah & Abu-abu muda', 'Industrial, American Classic', 'Kerendahan hati, Keberanian', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Hitam'),
(100, 'Merah & Hijau muda', 'Alam, American Classic', 'Kewanitaan, Keberanian', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(101, 'Merah & Magenta', 'Modern, American Classic', 'Kewanitaan, Keberanian', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Biru'),
(102, 'Merah & Emas', 'American Classic', 'Keagungan, Keberanian', 'Panas', 'D, L, A, R', 'Merah, Kuning, Biru'),
(103, 'Merah & Biru navy', 'Alam, American Classic', 'Ketenangan, Keberanian', 'Panas, Dingin', 'D, L, A, R', 'Merah, Biru, Hitam'),
(104, 'Merah & Merah maroon', 'Tradisional, Alam, American Classic', 'Keceriaan, Keberanian', 'Panas', 'D, L, A, R', 'Merah, Kuning, Biru'),
(105, 'Merah & Peach', 'Modern, American Classic', 'Kewanitaan, Keberanian', 'Panas, Hangat', 'D, L, A, R', 'Merah, Putih, Kuning'),
(106, 'Merah & Silver', 'Industrial, American Classic', 'Ketenangan, Keberanian', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Hitam'),
(107, 'Merah & Coral', 'American Classic', 'Kewanitaan, Keberanian', 'Panas', 'D, L, A, R', 'Merah, Kuning'),
(108, 'Merah & Biru air', 'Alam, American Classic', 'Ketenangan, Keberanian', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Biru'),
(109, 'Merah & Krem', 'American Classic', 'Kehangatan, Keberanian', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(110, 'Merah & Hijau lumut', 'Alam, American Classic', 'Kejantanan, Keberanian', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(111, 'Ungu & Hijau', 'Modern, Alam', 'Keagungan, Santai', 'Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(112, 'Ungu & Biru', 'Modern, Alam', 'Keagungan, Ketenangan', 'Dingin', 'D, L, A, R', 'Merah, Biru'),
(113, 'Ungu & Oren', 'Modern, American Classic', 'Keagungan, Keceriaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(114, 'Ungu & Coklat', 'Modern, Alam, Tradisional', 'Keagungan, Kenyamanan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(115, 'Ungu & Abu-abu', 'Modern, Industrial', 'Kerendahan hati, Keagungan', 'Dingin', 'D, L, A, R', 'Merah, Putih, Biru, Hitam'),
(116, 'Ungu & Merah muda', 'Modern', 'Keagungan, Kewanitaan', 'Panas, Dingin', 'D, A, R', 'Merah, Putih, Biru'),
(117, 'Ungu & Merah tua', 'Modern', 'Keagungan, Keberanian', 'Panas, Dingin', 'D, L, A, R', 'Merah, Biru, Hitam'),
(118, 'Ungu & Biru tua', 'Modern, Alam', 'Keagungan, Ketenangan', 'Dingin', 'D, L, A, R', 'Merah, Biru, Hitam'),
(119, 'Ungu & Abu-abu tua', 'Modern, Industrial', 'Kerendahan hati, Keagungan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Biru, Hitam'),
(120, 'Ungu & Hijau tua', 'Modern, Alam', 'Keagungan, Santai', 'Dingin', 'D, L, A, R', 'Merah, Hijau, Biru, Hitam'),
(121, 'Ungu & Coklat tua', 'Modern, Alam, Tradisional', 'Keagungan, Kejantanan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(122, 'Ungu & Coklat muda', 'Modern, Alam, Tradisional, American Classic', 'Keagungan, Kejantanan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(123, 'Ungu & Biru muda', 'Modern, Alam, American Classic', 'Keagungan, Kewanitaan', 'Dingin', 'D, L, A, R', 'Merah, Putih, Biru'),
(124, 'Ungu & Abu-abu muda', 'Modern, Industrial', 'Kerendahan hati, Keagungan', 'Dingin', 'D, L, A, R', 'Merah, Putih, Biru, Hitam'),
(125, 'Ungu & Hijau muda', 'Modern, Alam, American Classic', 'Keagungan, Kewanitaan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(126, 'Ungu & Magenta', 'Modern, American Classic', 'Keagungan, Kewanitaan', 'Dingin', 'D, L, A, R', 'Merah, Putih, Biru'),
(127, 'Ungu & Emas', 'Modern, American Classic', 'Keagungan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(128, 'Ungu & Biru navy', 'Modern, Alam', 'Keagungan, Ketenangan', 'Dingin', 'D, L, A, R', 'Merah, Biru, Hitam'),
(129, 'Ungu & Merah maroon', 'Modern, Alam, Tradisional', 'Keagungan, Keceriaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(130, 'Ungu & Peach', 'Modern, American Classic', 'Keagungan, Kewanitaan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(131, 'Ungu & Silver', 'Modern, Industrial', 'Keagungan, Ketenangan', 'Dingin', 'D, L, A, R', 'Merah, Putih, Biru, Hitam'),
(132, 'Ungu & Coral', 'Modern, American Classic', 'Keagungan, Kewanitaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(133, 'Ungu & Biru air', 'Modern, Alam, American Classic', 'Keagungan, Ketenangan', 'Dingin', 'D, L, A, R', 'Merah, Putih, Biru'),
(134, 'Ungu & Krem', 'Modern, American Classic', 'Keagungan, Kehangatan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(135, 'Ungu & Hijau lumut', 'Modern, Alam', 'Keagungan, Kejantanan', 'Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(136, 'Hijau & Biru', 'Alam', 'Ketenangan, Santai', 'Dingin', 'D, L, A, R', 'Kuning, Biru'),
(137, 'Hijau & Oren', 'Alam, American Classic', 'Keceriaan, Santai', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(138, 'Hijau & Coklat', 'Alam, Tradisional', 'Kenyamanan, Santai', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(139, 'Hijau & Abu-abu', 'Alam, Industrial', 'Kerendahan hati, Santai', 'Dingin', 'D, L, A, R', 'Putih, Kuning, Biru, Hitam'),
(140, 'Hijau & Merah muda', 'Alam, Modern', 'Kewanitaan, Santai', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(141, 'Hijau & Merah tua', 'Alam, Modern', 'Keberanian, Santai', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru, Hitam'),
(142, 'Hijau & Biru tua', 'Alam', 'Ketenangan, Santai', 'Dingin', 'D, L, A, R', 'Kuning, Biru, Hitam'),
(143, 'Hijau & Abu-abu tua', 'Alam, Industrial', 'Kerendahan hati, Santai', 'Panas, Dingin', 'D, L, A, R', 'Putih, Kuning, Biru, Hitam'),
(144, 'Hijau & Hijau tua', 'Alam', 'Santai', 'Dingin', 'D, L, A, R', 'Hitam, Kuning, Biru, Hijau'),
(145, 'Hijau & Coklat tua', 'Alam, Tradisional', 'Kejantanan, Santai', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(146, 'Hijau & Coklat muda', 'Alam, Tradisional, American Classic', 'Kejantanan, Santai', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(147, 'Hijau & Biru muda', 'Alam, American Classic', 'Kewanitaan, Santai', 'Dingin', 'D, L, A, R', 'Putih, Kuning, Biru'),
(148, 'Hijau & Abu-abu muda', 'Alam, Industrial', 'Kerendahan hati, Santai', 'Dingin', 'D, L, A, R', 'Putih, Kuning, Biru, Hitam'),
(149, 'Hijau & Hijau muda', 'Alam, American Classic', 'Kewanitaan, Santai', 'Hangat, Dingin', 'D, L, A, R', 'Kuning, Biru'),
(150, 'Hijau & Magenta', 'Alam, Modern, American Classic', 'Kewanitaan, Santai', 'Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(151, 'Hijau & Emas', 'Alam, American Classic', 'Keagungan, Santai', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(152, 'Hijau & Biru navy', 'Alam', 'Ketenangan, Santai', 'Dingin', 'D, L, A, R', 'Kuning, Biru, Hitam'),
(153, 'Hijau & Merah maroon', 'Alam, Tradisional', 'Keceriaan, Santai', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(154, 'Hijau & Peach', 'Alam, Modern, American Classic', 'Kewanitaan, Santai', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(155, 'Hijau & Silver', 'Alam, Industrial', 'Ketenangan, Santai', 'Dingin', 'D, L, A, R', 'Putih, Kuning, Biru, Hitam'),
(156, 'Hijau & Coral', 'Alam, American Classic', 'Kewanitaan, Santai', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(157, 'Hijau & Biru air', 'Alam, American Classic', 'Ketenangan, Santai', 'Dingin', 'D, L, A, R', 'Putih, Kuning, Biru'),
(158, 'Hijau & Krem', 'Alam, American Classic', 'Kehangatan, Santai', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(159, 'Hijau & Hijau lumut', 'Alam', 'Kejantanan, Santai', 'Dingin', 'D, L, A, R', 'Putih, Kuning, Biru'),
(160, 'Biru & Oren', 'Alam, American Classic', 'Keceriaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(161, 'Biru & Coklat', 'Alam, Tradisional', 'Kenyamanan, Ketenangan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(162, 'Biru & Abu-abu', 'Alam, Industrial', 'Kerendahan hati, Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(163, 'Biru & Merah muda', 'Alam, Modern', 'Kewanitaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Biru'),
(164, 'Biru & Merah tua', 'Alam, Modern', 'Ketenangan, Keberanian', 'Panas, Dingin', 'D, L, A, R', 'Merah, Biru, Hitam'),
(165, 'Biru & Biru tua', 'Alam', 'Ketenangan', 'Dingin', 'D, L, A, R', 'Biru, Hitam'),
(166, 'Biru & Abu-abu tua', 'Alam, Industrial', 'Kerendahan hati, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(167, 'Biru & Hijau tua', 'Alam', 'Ketenangan, Santai', 'Dingin', 'D, L, A, R', 'Hijau, Biru, Hitam'),
(168, 'Biru & Coklat tua', 'Alam, Tradisional', 'Kejantanan, Ketenangan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(169, 'Biru & Coklat muda', 'Alam, Tradisional, American Classic', 'Kejantanan, Ketenangan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(170, 'Biru & Biru muda', 'Alam, American Classic', 'Kewanitaan, Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Biru'),
(171, 'Biru & Abu-abu muda', 'Alam, Industrial', 'Kerendahan hati, Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(172, 'Biru & Hijau muda', 'Alam, American Classic', 'Kewanitaan, Ketenangan', 'Hangat, Dingin', 'D, L, A, R', 'Kuning, Biru'),
(173, 'Biru & Magenta', 'Alam, Modern, American Classic', 'Kewanitaan, Ketenangan', 'Dingin', 'D, L, A, R', 'Merah, Putih, Biru'),
(174, 'Biru & Emas', 'Alam, American Classic', 'Keagungan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(175, 'Biru & Biru navy', 'Alam', 'Ketenangan', 'Dingin', 'D, L, A, R', 'Biru, Hitam'),
(176, 'Biru & Merah maroon', 'Alam, Tradisional', 'Keceriaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(177, 'Biru & Peach', 'Alam, Modern, American Classic', 'Kewanitaan, Ketenangan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(178, 'Biru & Silver', 'Alam, Industrial', 'Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(179, 'Biru & Coral', 'Alam, American Classic', 'Kewanitaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(180, 'Biru & Biru air', 'Alam, American Classic', 'Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Biru'),
(181, 'Biru & Krem', 'Alam, American Classic', 'Ketenangan, Kehangatan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru'),
(182, 'Biru & Hijau lumut', 'Alam', 'Kejantanan, Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Kuning, Biru'),
(183, 'Oren & Coklat', 'Tradisional, Alam, American Classic', 'Keceriaan, Kenyamanan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(184, 'Oren & Abu-abu', 'Industrial, American Classic', 'Kerendahan hati, Keceriaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Hitam'),
(185, 'Oren & Merah muda', 'Modern, American Classic', 'Keceriaan, Kewanitaan', 'Panas', 'D, L, A, R', 'Merah, Putih, Kuning'),
(186, 'Oren & Merah tua', 'Modern, American Classic', 'Keceriaan, Keberanian', 'Panas', 'D, L, A, R', 'Merah, Kuning, Hitam'),
(187, 'Oren & Biru tua', 'Alam, American Classic', 'Keceriaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru, Hitam'),
(188, 'Oren & Abu-abu tua', 'Industrial, American Classic', 'Kerendahan hati, Keceriaan', 'Panas', 'D, L, A, R', 'Merah, Putih, Kuning, Hitam'),
(189, 'Oren & Hijau tua', 'Alam, American Classic', 'Keceriaan, Santai', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Hijau, Hitam'),
(190, 'Oren & Coklat tua', 'Tradisional, Alam, American Classic', 'Keceriaan, Kejantanan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(191, 'Oren & Coklat muda', 'Tradisional, Alam, American Classic', 'Keceriaan, Kejantanan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(192, 'Oren & Biru muda', 'Alam, American Classic', 'Keceriaan, Kewanitaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(193, 'Oren & Abu-abu muda', 'Industrial, American Classic', 'Kerendahan hati, Keceriaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Hitam'),
(194, 'Oren & Hijau muda', 'Alam, American Classic', 'Keceriaan, Kewanitaan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(195, 'Oren & Magenta', 'Modern, American Classic', 'Keceriaan, Kewanitaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(196, 'Oren & Emas', 'American Classic', 'Keceriaan, Keagungan', 'Panas', 'D, L, A, R', 'Merah, Kuning, Biru'),
(197, 'Oren & Biru navy', 'Alam, American Classic', 'Keceriaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru, Hitam'),
(198, 'Oren & Merah maroon', 'Tradisional, Alam, American Classic', 'Keceriaan', 'Panas', 'D, L, A, R', 'Merah, Kuning, Biru'),
(199, 'Oren & Peach', 'Modern, American Classic', 'Keceriaan, Kewanitaan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Putih, Kuning'),
(200, 'Oren & Silver', 'Industrial, American Classic', 'Keceriaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Hitam'),
(201, 'Oren & Coral', 'American Classic', 'Keceriaan, Kewanitaan', 'Panas', 'D, L, A, R', 'Merah, Kuning'),
(202, 'Oren & Biru air', 'Alam, American Classic', 'Keceriaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(203, 'Oren & Krem', 'American Classic', 'Keceriaan, Kehangatan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(204, 'Oren & Hijau lumut', 'Alam, American Classic', 'Keceriaan, Kejantanan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(205, 'Coklat & Abu-abu', 'Alam, Industrial, Tradisional', 'Kerendahan hati, Kenyamanan', 'Hangat, Dingin', 'D, L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(206, 'Coklat & Merah muda', 'Alam, Modern, Tradisional', 'Kenyamanan, Kewanitaan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(207, 'Coklat & Merah tua', 'Alam, Modern, Tradisional', 'Kenyamanan, Keberanian', 'Panas, Hangat', 'L, R', 'Merah, Kuning, Biru, Hitam'),
(208, 'Coklat & Biru tua', 'Alam, Tradisional', 'Kenyamanan, Ketenangan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru, Hitam'),
(209, 'Coklat & Abu-abu tua', 'Alam, Industrial, Tradisional', 'Kerendahan hati, Kenyamanan', 'Panas, Hangat', 'D, L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(210, 'Coklat & Hijau tua', 'Alam, Tradisional', 'Kenyamanan, Santai', 'Hangat, Dingin', 'L, R', 'Hijau, Merah, Hitam, Kuning, Biru'),
(211, 'Coklat & Coklat tua', 'Alam, Tradisional', 'Kenyamanan, Kejantanan', 'Hangat', 'L, R', 'Merah, Kuning, Biru'),
(212, 'Coklat & Coklat muda', 'American Classic, Alam, Tradisional', 'Kenyamanan, Kejantanan', 'Hangat', 'L, R', 'Merah, Kuning, Biru'),
(213, 'Coklat & Biru muda', 'American Classic, Alam, Tradisional', 'Kenyamanan, Kewanitaan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(214, 'Coklat & Abu-abu muda', 'Alam, Industrial, Tradisional', 'Kerendahan hati, Kenyamanan', 'Hangat, Dingin', 'D, L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(215, 'Coklat & Hijau muda', 'American Classic, Alam, Tradisional', 'Kenyamanan, Kewanitaan', 'Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(216, 'Coklat & Magenta', 'American Classic, Alam, Modern, Tradisional', 'Kenyamanan, Kewanitaan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(217, 'Coklat & Emas', 'American Classic, Alam, Tradisional', 'Kenyamanan, Keagungan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(218, 'Coklat & Biru navy', 'Alam, Tradisional', 'Kenyamanan, Ketenangan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru, Hitam'),
(219, 'Coklat & Merah maroon', 'Alam, Tradisional', 'Kenyamanan, Keceriaan', 'Panas, Hangat', 'D, L, R', 'Merah, Kuning, Biru'),
(220, 'Coklat & Peach', 'American Classic, Alam, Modern, Tradisional', 'Kenyamanan, Kewanitaan', 'Hangat', 'D, L, R', 'Merah, Putih, Kuning, Biru'),
(221, 'Coklat & Silver', 'Alam, Industrial, Tradisional', 'Kenyamanan, Ketenangan', 'Hangat, Dingin', 'D, L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(222, 'Coklat & Coral', 'American Classic, Alam, Tradisional', 'Kenyamanan, Kewanitaan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(223, 'Coklat & Biru air', 'American Classic, Alam, Tradisional', 'Kenyamanan, Ketenangan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(224, 'Coklat & Krem', 'American Classic, Alam, Tradisional', 'Kenyamanan, Kehangatan', 'Hangat', 'D, L, R', 'Merah, Kuning, Biru'),
(225, 'Coklat & Hijau lumut', 'Alam, Tradisional', 'Kenyamanan, Kejantanan', 'Hangat, Dingin', 'L, R', 'Merah, Putih, Kuning, Biru'),
(226, 'Abu-abu & Merah muda', 'Modern, Industrial', 'Kerendahan hati, Kewanitaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Hitam'),
(227, 'Abu-abu & Merah tua', 'Modern, Industrial', 'Kerendahan hati, Keberanian', 'Panas, Dingin', 'D, L, R', 'Merah, Putih, Hitam'),
(228, 'Abu-abu & Biru tua', 'Alam, Industrial', 'Kerendahan hati, Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(229, 'Abu-abu & Abu-abu tua', 'Industrial', 'Kerendahan hati', 'Panas, Dingin', 'D, L, R', 'Putih, Hitam'),
(230, 'Abu-abu & Hijau tua', 'Alam, Industrial', 'Kerendahan hati, Santai', 'Dingin', 'D, L, R', 'Putih, Hijau, Hitam'),
(231, 'Abu-abu & Coklat tua', 'Alam, Industrial, Tradisional', 'Kerendahan hati, Kejantanan', 'Hangat, Dingin', 'D, L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(232, 'Abu-abu & Coklat muda', 'Tradisional, Alam, Industrial, American Classic', 'Kerendahan hati, Kejantanan', 'Hangat, Dingin', 'D, L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(233, 'Abu-abu & Biru muda', 'Alam, Industrial, American Classic', 'Kerendahan hati, Kewanitaan', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(234, 'Abu-abu & Abu-abu muda', 'Industrial', 'Kerendahan hati', 'Dingin', 'D, L, R', 'Putih, Hitam'),
(235, 'Abu-abu & Hijau muda', 'Alam, Industrial, American Classic', 'Kerendahan hati, Kewanitaan', 'Hangat, Dingin', 'D, L, A, R', 'Putih, Kuning, Biru, Hitam'),
(236, 'Abu-abu & Magenta', 'Modern, Industrial, American Classic', 'Kerendahan hati, Kewanitaan', 'Dingin', 'D, L, A, R', 'Merah, Putih, Biru, Hitam'),
(237, 'Abu-abu & Emas', 'Industrial, American Classic', 'Kerendahan hati, Keagungan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(238, 'Abu-abu & Biru navy', 'Alam, Industrial', 'Kerendahan hati, Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(239, 'Abu-abu & Merah maroon', 'Alam, Industrial, Tradisional', 'Kerendahan hati, Keceriaan', 'Panas, Dingin', 'D, L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(240, 'Abu-abu & Peach', 'Modern, Industrial, American Classic', 'Kerendahan hati, Kewanitaan', 'Hangat, Dingin', 'D, L, R', 'Merah, Putih, Kuning, Hitam'),
(241, 'Abu-abu & Silver', 'Industrial', 'Kerendahan hati, Ketenangan', 'Dingin', 'D, L, R', 'Putih, Hitam'),
(242, 'Abu-abu & Coral', 'Industrial, American Classic', 'Kerendahan hati, Kewanitaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Hitam'),
(243, 'Abu-abu & Biru air', 'Alam, Industrial, American Classic', 'Kerendahan hati, Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(244, 'Abu-abu & Krem', 'Industrial, American Classic', 'Kerendahan hati, Kehangatan', 'Hangat, Dingin', 'D, L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(245, 'Abu-abu & Hijau lumut', 'Alam, Industrial', 'Kerendahan hati, Kejantanan', 'Dingin', 'D, L, R', 'Putih, Kuning, Biru, Hitam'),
(246, 'Merah muda & Merah tua', 'Modern', 'Kewanitaan, Keberanian', 'Panas', 'D, L, A, R', 'Merah, Putih, Hitam'),
(247, 'Merah muda & Biru tua', 'Modern, Alam', 'Kewanitaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Biru, Hitam'),
(248, 'Merah muda & Abu-abu tua', 'Modern, Industrial', 'Kerendahan hati, Kewanitaan', 'Panas', 'D, L, A, R', 'Merah, Putih, Hitam'),
(249, 'Merah muda & Hijau tua', 'Modern, Alam', 'Kewanitaan, Santai', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Hijau, Hitam'),
(250, 'Merah muda & Coklat tua', 'Modern, Alam, Tradisional', 'Kewanitaan, Kejantanan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(251, 'Merah muda & Coklat muda', 'Modern, Alam, Tradisional, American Classic', 'Kewanitaan, Kejantanan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(252, 'Merah muda & Biru muda', 'Modern, Alam, American Classic', 'Kewanitaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Biru'),
(253, 'Merah muda & Abu-abu muda', 'Modern, Industrial', 'Kerendahan hati, Kewanitaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Hitam'),
(254, 'Merah muda & Hijau muda', 'Modern, Alam, American Classic', 'Kewanitaan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(255, 'Merah muda & Magenta', 'Modern, American Classic', 'Kewanitaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Biru'),
(256, 'Merah muda & Emas', 'Modern, American Classic', 'Keagungan, Kewanitaan', 'Panas', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(257, 'Merah muda & Biru navy', 'Modern, Alam', 'Kewanitaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Biru, Hitam'),
(258, 'Merah muda & Merah maroon', 'Modern, Alam, Tradisional', 'Keceriaan, Kewanitaan', 'Panas', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(259, 'Merah muda & Peach', 'Modern, American Classic', 'Kewanitaan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Putih, Kuning'),
(260, 'Merah muda & Silver', 'Modern, Industrial', 'Kewanitaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Hitam'),
(261, 'Merah muda & Coral', 'Modern, American Classic', 'Kewanitaan', 'Panas', 'D, L, A, R', 'Merah, Putih, Kuning'),
(262, 'Merah muda & Biru air', 'Modern, Alam, American Classic', 'Kewanitaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Biru'),
(263, 'Merah muda & Krem', 'Modern, American Classic', 'Kewanitaan, Kehangatan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(264, 'Merah muda & Hijau lumut', 'Modern, Alam', 'Kewanitaan, Kejantanan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(265, 'Merah tua & Biru tua', 'Modern, Alam', 'Ketenangan, Keberanian', 'Panas, Dingin', 'D, L, A, R', 'Merah, Biru, Hitam'),
(266, 'Merah tua & Abu-abu tua', 'Modern, Industrial', 'Kerendahan hati, Keberanian', 'Panas', 'D, L, R', 'Merah, Putih, Hitam'),
(267, 'Merah tua & Hijau tua', 'Modern, Alam', 'Santai, Keberanian', 'Panas, Dingin', 'L, R', 'Merah, Hijau, Hitam'),
(268, 'Merah tua & Coklat tua', 'Modern, Alam, Tradisional', 'Kejantanan, Keberanian', 'Panas, Hangat', 'L, R', 'Merah, Kuning, Biru, Hitam'),
(269, 'Merah tua & Coklat muda', 'Modern, Alam, Tradisional, American Classic', 'Kejantanan, Keberanian', 'Panas, Hangat', 'L, R', 'Merah, Kuning, Biru, Hitam'),
(270, 'Merah tua & Biru muda', 'Modern, Alam, American Classic', 'Kewanitaan, Keberanian', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Biru, Hitam'),
(271, 'Merah tua & Abu-abu muda', 'Modern, Industrial', 'Kerendahan hati, Keberanian', 'Panas, Dingin', 'D, L, R', 'Merah, Putih, Hitam'),
(272, 'Merah tua & Hijau muda', 'Modern, Alam, American Classic', 'Kewanitaan, Keberanian', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru, Hitam'),
(273, 'Merah tua & Magenta', 'Modern, American Classic', 'Kewanitaan, Keberanian', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Biru, Hitam'),
(274, 'Merah tua & Emas', 'Modern, American Classic', 'Keagungan, Keberanian', 'Panas', 'D, L, A, R', 'Merah, Kuning, Biru, Hitam'),
(275, 'Merah tua & Biru navy', 'Modern, Alam', 'Ketenangan, Keberanian', 'Panas, Dingin', 'D, L, A, R', 'Merah, Biru, Hitam'),
(276, 'Merah tua & Merah maroon', 'Modern, Alam, Tradisional', 'Keceriaan, Keberanian', 'Panas', 'D, L, R', 'Merah, Kuning, Biru, Hitam'),
(277, 'Merah tua & Peach', 'Modern, American Classic', 'Kewanitaan, Keberanian', 'Panas, Hangat', 'D, L, R', 'Merah, Putih, Kuning, Hitam'),
(278, 'Merah tua & Silver', 'Modern, Industrial', 'Ketenangan, Keberanian', 'Panas, Dingin', 'D, L, R', 'Merah, Putih, Hitam'),
(279, 'Merah tua & Coral', 'Modern, American Classic', 'Kewanitaan, Keberanian', 'Panas', 'D, L, A, R', 'Merah, Kuning, Hitam'),
(280, 'Merah tua & Biru air', 'Modern, Alam, American Classic', 'Ketenangan, Keberanian', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Biru, Hitam'),
(281, 'Merah tua & Krem', 'Modern, American Classic', 'Kehangatan, Keberanian', 'Panas, Hangat', 'D, L, R', 'Merah, Kuning, Biru, Hitam'),
(282, 'Merah tua & Hijau lumut', 'Modern, Alam', 'Kejantanan, Keberanian', 'Panas, Dingin', 'L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(283, 'Biru tua & Abu-abu tua', 'Alam, Industrial', 'Kerendahan hati, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(284, 'Biru tua & Hijau tua', 'Alam', 'Ketenangan, Santai', 'Dingin', 'D, L, A, R', 'Hijau, Biru, Hitam'),
(285, 'Biru tua & Coklat tua', 'Alam, Tradisional', 'Kejantanan, Ketenangan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru, Hitam'),
(286, 'Biru tua & Coklat muda', 'Alam, Tradisional, American Classic', 'Kejantanan, Ketenangan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru, Hitam'),
(287, 'Biru tua & Biru muda', 'Alam, American Classic', 'Kewanitaan, Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(288, 'Biru tua & Abu-abu muda', 'Alam, Industrial', 'Kerendahan hati, Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(289, 'Biru tua & Hijau muda', 'Alam, American Classic', 'Kewanitaan, Ketenangan', 'Hangat, Dingin', 'D, L, A, R', 'Kuning, Biru, Hitam'),
(290, 'Biru tua & Magenta', 'Alam, Modern, American Classic', 'Kewanitaan, Ketenangan', 'Dingin', 'D, L, A, R', 'Merah, Putih, Biru, Hitam'),
(291, 'Biru tua & Emas', 'Alam, American Classic', 'Keagungan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru, Hitam'),
(292, 'Biru tua & Biru navy', 'Alam', 'Ketenangan', 'Dingin', 'D, L, A, R', 'Biru, Hitam'),
(293, 'Biru tua & Merah maroon', 'Alam, Tradisional', 'Keceriaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru, Hitam'),
(294, 'Biru tua & Peach', 'Alam, Modern, American Classic', 'Kewanitaan, Ketenangan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(295, 'Biru tua & Silver', 'Alam, Industrial', 'Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(296, 'Biru tua & Coral', 'Alam, American Classic', 'Kewanitaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru, Hitam'),
(297, 'Biru tua & Biru air', 'Alam, American Classic', 'Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(298, 'Biru tua & Krem', 'Alam, American Classic', 'Ketenangan, Kehangatan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru, Hitam'),
(299, 'Biru tua & Hijau lumut', 'Alam', 'Kejantanan, Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Kuning, Biru, Hitam'),
(300, 'Abu-abu tua & Hijau tua', 'Alam, Industrial', 'Kerendahan hati, Santai', 'Panas, Dingin', 'D, L, R', 'Putih, Hijau, Hitam'),
(301, 'Abu-abu tua & Coklat tua', 'Alam, Industrial, Tradisional', 'Kerendahan hati, Kejantanan', 'Panas, Hangat', 'D, L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(302, 'Abu-abu tua & Coklat muda', 'Tradisional, Alam, Industrial, American Classic', 'Kerendahan hati, Kejantanan', 'Panas, Hangat', 'D, L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(303, 'Abu-abu tua & Biru muda', 'Alam, Industrial, American Classic', 'Kerendahan hati, Kewanitaan', 'Panas, Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(304, 'Abu-abu tua & Abu-abu muda', 'Industrial', 'Kerendahan hati', 'Panas, Dingin', 'D, L, R', 'Putih, Hitam'),
(305, 'Abu-abu tua & Hijau muda', 'Alam, Industrial, American Classic', 'Kerendahan hati, Kewanitaan', 'Panas, Hangat', 'D, L, A, R', 'Putih, Kuning, Biru, Hitam'),
(306, 'Abu-abu tua & Magenta', 'Modern, Industrial, American Classic', 'Kerendahan hati, Kewanitaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Biru, Hitam'),
(307, 'Abu-abu tua & Emas', 'Industrial, American Classic', 'Kerendahan hati, Keagungan', 'Panas', 'D, L, A, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(308, 'Abu-abu tua & Biru navy', 'Alam, Industrial', 'Kerendahan hati, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(309, 'Abu-abu tua & Merah maroon', 'Alam, Industrial, Tradisional', 'Kerendahan hati, Keceriaan', 'Panas', 'D, L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(310, 'Abu-abu tua & Peach', 'Modern, Industrial, American Classic', 'Kerendahan hati, Kewanitaan', 'Panas, Hangat', 'D, L, R', 'Merah, Putih, Kuning, Hitam'),
(311, 'Abu-abu tua & Silver', 'Industrial', 'Kerendahan hati, Ketenangan', 'Panas, Dingin', 'D, L, R', 'Putih, Hitam'),
(312, 'Abu-abu tua & Coral', 'Industrial, American Classic', 'Kerendahan hati, Kewanitaan', 'Panas', 'D, L, A, R', 'Merah, Putih, Kuning, Hitam'),
(313, 'Abu-abu tua & Biru air', 'Alam, Industrial, American Classic', 'Kerendahan hati, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(314, 'Abu-abu tua & Krem', 'Industrial, American Classic', 'Kerendahan hati, Kehangatan', 'Panas, Hangat', 'D, L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(315, 'Abu-abu tua & Hijau lumut', 'Alam, Industrial', 'Kerendahan hati, Kejantanan', 'Panas, Dingin', 'D, L, R', 'Putih, Kuning, Biru, Hitam'),
(316, 'Hijau tua & Coklat tua', 'Alam, Tradisional', 'Kejantanan, Santai', 'Hangat, Dingin', 'L', 'Hijau, Merah, Hitam, Kuning, Biru'),
(317, 'Hijau tua & Coklat muda', 'Alam, Tradisional, American Classic', 'Kejantanan, Santai', 'Hangat, Dingin', 'L', 'Hijau, Merah, Hitam, Kuning, Biru'),
(318, 'Hijau tua & Biru muda', 'Alam, American Classic', 'Kewanitaan, Santai', 'Dingin', 'D, L, A, R', 'Biru, Putih, Hijau, Hitam'),
(319, 'Hijau tua & Abu-abu muda', 'Alam, Industrial', 'Kerendahan hati, Santai', 'Dingin', 'D, L, R', 'Putih, Hijau, Hitam'),
(320, 'Hijau tua & Hijau muda', 'Alam, American Classic', 'Kewanitaan, Santai', 'Hangat, Dingin', 'D, L, A, R', 'Biru, Kuning, Hijau, Hitam'),
(321, 'Hijau tua & Magenta', 'Alam, Modern, American Classic', 'Kewanitaan, Santai', 'Dingin', 'D, L, A, R', 'Hijau, Merah, Putih, Hitam, Biru'),
(322, 'Hijau tua & Emas', 'Alam, American Classic', 'Keagungan, Santai', 'Panas, Dingin', 'D, L, A, R', 'Hijau, Merah, Hitam, Kuning, Biru'),
(323, 'Hijau tua & Biru navy', 'Alam', 'Ketenangan, Santai', 'Dingin', 'D, L, A, R', 'Biru, Hijau, Hitam'),
(324, 'Hijau tua & Merah maroon', 'Alam, Tradisional', 'Keceriaan, Santai', 'Panas, Dingin', 'D, L, R', 'Hijau, Merah, Hitam, Kuning, Biru'),
(325, 'Hijau tua & Peach', 'Alam, Modern, American Classic', 'Kewanitaan, Santai', 'Hangat, Dingin', 'D, L, R', 'Hijau, Merah, Putih, Hitam, Kuning'),
(326, 'Hijau tua & Silver', 'Alam, Industrial', 'Ketenangan, Santai', 'Dingin', 'D, L, R', 'Putih, Hijau, Hitam'),
(327, 'Hijau tua & Coral', 'Alam, American Classic', 'Kewanitaan, Santai', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Hijau, Hitam'),
(328, 'Hijau tua & Biru air', 'Alam, American Classic', 'Ketenangan, Santai', 'Dingin', 'D, L, A, R', 'Biru, Putih, Hijau, Hitam'),
(329, 'Hijau tua & Krem', 'Alam, American Classic', 'Kehangatan, Santai', 'Hangat, Dingin', 'D, L, R', 'Hijau, Merah, Hitam, Kuning, Biru'),
(330, 'Hijau tua & Hijau lumut', 'Alam', 'Kejantanan, Santai', 'Dingin', 'L', 'Hijau, Putih, Hitam, Kuning, Biru'),
(331, 'Coklat tua & Coklat muda', 'American Classic, Alam, Tradisional', 'Kejantanan', 'Hangat', 'L', 'Merah, Kuning, Biru'),
(332, 'Coklat tua & Biru muda', 'American Classic, Alam, Tradisional', 'Kewanitaan, Kejantanan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(333, 'Coklat tua & Abu-abu muda', 'Alam, Industrial, Tradisional', 'Kerendahan hati, Kejantanan', 'Hangat, Dingin', 'D, L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(334, 'Coklat tua & Hijau muda', 'American Classic, Alam, Tradisional', 'Kewanitaan, Kejantanan', 'Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(335, 'Coklat tua & Magenta', 'American Classic, Alam, Modern, Tradisional', 'Kewanitaan, Kejantanan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(336, 'Coklat tua & Emas', 'American Classic, Alam, Tradisional', 'Keagungan, Kejantanan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(337, 'Coklat tua & Biru navy', 'Alam, Tradisional', 'Ketenangan, Kejantanan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru, Hitam'),
(338, 'Coklat tua & Merah maroon', 'Alam, Tradisional', 'Keceriaan, Kejantanan', 'Panas, Hangat', 'D, L, R', 'Merah, Kuning, Biru'),
(339, 'Coklat tua & Peach', 'American Classic, Alam, Modern, Tradisional', 'Kewanitaan, Kejantanan', 'Hangat', 'D, L, R', 'Merah, Putih, Kuning, Biru'),
(340, 'Coklat tua & Silver', 'Alam, Industrial, Tradisional', 'Ketenangan, Kejantanan', 'Hangat, Dingin', 'D, L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(341, 'Coklat tua & Coral', 'American Classic, Alam, Tradisional', 'Kewanitaan, Kejantanan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(342, 'Coklat tua & Biru air', 'American Classic, Alam, Tradisional', 'Ketenangan, Kejantanan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(343, 'Coklat tua & Krem', 'American Classic, Alam, Tradisional', 'Kejantanan, Kehangatan', 'Hangat', 'D, L, R', 'Merah, Kuning, Biru'),
(344, 'Coklat tua & Hijau lumut', 'Alam, Tradisional', 'Kejantanan', 'Hangat, Dingin', 'L', 'Merah, Putih, Kuning, Biru'),
(345, 'Coklat muda & Biru muda', 'Tradisional, Alam, American Classic', 'Kewanitaan, Kejantanan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(346, 'Coklat muda & Abu-abu muda', 'Tradisional, Alam, Industrial, American Classic', 'Kerendahan hati, Kejantanan', 'Hangat, Dingin', 'D, L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(347, 'Coklat muda & Hijau muda', 'Tradisional, Alam, American Classic', 'Kewanitaan, Kejantanan', 'Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(348, 'Coklat muda & Magenta', 'Modern, Tradisional, Alam, American Classic', 'Kewanitaan, Kejantanan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(349, 'Coklat muda & Emas', 'Tradisional, Alam, American Classic', 'Keagungan, Kejantanan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(350, 'Coklat muda & Biru navy', 'Tradisional, Alam, American Classic', 'Ketenangan, Kejantanan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru, Hitam'),
(351, 'Coklat muda & Merah maroon', 'Tradisional, Alam, American Classic', 'Keceriaan, Kejantanan', 'Panas, Hangat', 'D, L, R', 'Merah, Kuning, Biru'),
(352, 'Coklat muda & Peach', 'Modern, Tradisional, Alam, American Classic', 'Kewanitaan, Kejantanan', 'Hangat', 'D, L, R', 'Merah, Putih, Kuning, Biru'),
(353, 'Coklat muda & Silver', 'Tradisional, Alam, Industrial, American Classic', 'Ketenangan, Kejantanan', 'Hangat, Dingin', 'D, L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(354, 'Coklat muda & Coral', 'Tradisional, Alam, American Classic', 'Kewanitaan, Kejantanan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(355, 'Coklat muda & Biru air', 'Tradisional, Alam, American Classic', 'Ketenangan, Kejantanan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(356, 'Coklat muda & Krem', 'Tradisional, Alam, American Classic', 'Kejantanan, Kehangatan', 'Hangat', 'D, L, R', 'Merah, Kuning, Biru'),
(357, 'Coklat muda & Hijau lumut', 'Tradisional, Alam, American Classic', 'Kejantanan', 'Hangat, Dingin', 'L', 'Merah, Putih, Kuning, Biru'),
(358, 'Biru muda & Abu-abu muda', 'Alam, Industrial, American Classic', 'Kerendahan hati, Kewanitaan', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(359, 'Biru muda & Hijau muda', 'Alam, American Classic', 'Kewanitaan', 'Hangat, Dingin', 'D, L, A, R', 'Putih, Kuning, Biru'),
(360, 'Biru muda & Magenta', 'Alam, Modern, American Classic', 'Kewanitaan', 'Dingin', 'D, L, A, R', 'Merah, Putih, Biru'),
(361, 'Biru muda & Emas', 'Alam, American Classic', 'Keagungan, Kewanitaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(362, 'Biru muda & Biru navy', 'Alam, American Classic', 'Kewanitaan, Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(363, 'Biru muda & Merah maroon', 'Alam, Tradisional, American Classic', 'Keceriaan, Kewanitaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(364, 'Biru muda & Peach', 'Alam, Modern, American Classic', 'Kewanitaan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(365, 'Biru muda & Silver', 'Alam, Industrial, American Classic', 'Kewanitaan, Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(366, 'Biru muda & Coral', 'Alam, American Classic', 'Kewanitaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(367, 'Biru muda & Biru air', 'Alam, American Classic', 'Kewanitaan, Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Biru'),
(368, 'Biru muda & Krem', 'Alam, American Classic', 'Kewanitaan, Kehangatan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(369, 'Biru muda & Hijau lumut', 'Alam, American Classic', 'Kewanitaan, Kejantanan', 'Dingin', 'D, L, A, R', 'Putih, Kuning, Biru'),
(370, 'Abu-abu muda & Hijau muda', 'Alam, Industrial, American Classic', 'Kerendahan hati, Kewanitaan', 'Hangat, Dingin', 'D, L, A, R', 'Putih, Kuning, Biru, Hitam'),
(371, 'Abu-abu muda & Magenta', 'Modern, Industrial, American Classic', 'Kerendahan hati, Kewanitaan', 'Dingin', 'D, L, A, R', 'Merah, Putih, Biru, Hitam');
INSERT INTO `data_kombinasi` (`id_kombinasi`, `kombinasi_warna`, `style_desain`, `makna_warna`, `sifat`, `usia_pengguna`, `warna_dasar`) VALUES
(372, 'Abu-abu muda & Emas', 'Industrial, American Classic', 'Kerendahan hati, Keagungan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(373, 'Abu-abu muda & Biru navy', 'Alam, Industrial', 'Kerendahan hati, Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(374, 'Abu-abu muda & Merah maroon', 'Alam, Industrial, Tradisional', 'Kerendahan hati, Keceriaan', 'Panas, Dingin', 'D, L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(375, 'Abu-abu muda & Peach', 'Modern, Industrial, American Classic', 'Kerendahan hati, Kewanitaan', 'Hangat, Dingin', 'D, L, R', 'Merah, Putih, Kuning, Hitam'),
(376, 'Abu-abu muda & Silver', 'Industrial', 'Kerendahan hati, Ketenangan', 'Dingin', 'D, L, R', 'Putih, Hitam'),
(377, 'Abu-abu muda & Coral', 'Industrial, American Classic', 'Kerendahan hati, Kewanitaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Hitam'),
(378, 'Abu-abu muda & Biru air', 'Alam, Industrial, American Classic', 'Kerendahan hati, Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(379, 'Abu-abu muda & Krem', 'Industrial, American Classic', 'Kerendahan hati, Kehangatan', 'Hangat, Dingin', 'D, L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(380, 'Abu-abu muda & Hijau lumut', 'Alam, Industrial', 'Kerendahan hati, Kejantanan', 'Dingin', 'D, L, R', 'Putih, Kuning, Biru, Hitam'),
(381, 'Hijau muda & Magenta', 'Alam, Modern, American Classic', 'Kewanitaan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(382, 'Hijau muda & Emas', 'Alam, American Classic', 'Keagungan, Kewanitaan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(383, 'Hijau muda & Biru navy', 'Alam, American Classic', 'Kewanitaan, Ketenangan', 'Hangat, Dingin', 'D, L, A, R', 'Kuning, Biru, Hitam'),
(384, 'Hijau muda & Merah maroon', 'Alam, Tradisional, American Classic', 'Keceriaan, Kewanitaan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(385, 'Hijau muda & Peach', 'Alam, Modern, American Classic', 'Kewanitaan', 'Hangat', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(386, 'Hijau muda & Silver', 'Alam, Industrial, American Classic', 'Kewanitaan, Ketenangan', 'Hangat, Dingin', 'D, L, A, R', 'Putih, Kuning, Biru, Hitam'),
(387, 'Hijau muda & Coral', 'Alam, American Classic', 'Kewanitaan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(388, 'Hijau muda & Biru air', 'Alam, American Classic', 'Kewanitaan, Ketenangan', 'Hangat, Dingin', 'D, L, A, R', 'Putih, Kuning, Biru'),
(389, 'Hijau muda & Krem', 'Alam, American Classic', 'Kewanitaan, Kehangatan', 'Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(390, 'Hijau muda & Hijau lumut', 'Alam, American Classic', 'Kewanitaan, Kejantanan', 'Hangat, Dingin', 'D, L, A, R', 'Putih, Kuning, Biru'),
(391, 'Magenta & Emas', 'Modern, American Classic', 'Keagungan, Kewanitaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(392, 'Magenta & Biru navy', 'Modern, Alam, American Classic', 'Kewanitaan, Ketenangan', 'Dingin', 'D, L, A, R', 'Merah, Putih, Biru, Hitam'),
(393, 'Magenta & Merah maroon', 'Modern, Alam, Tradisional, American Classic', 'Keceriaan, Kewanitaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(394, 'Magenta & Peach', 'Modern, American Classic', 'Kewanitaan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(395, 'Magenta & Silver', 'Modern, Industrial, American Classic', 'Kewanitaan, Ketenangan', 'Dingin', 'D, L, A, R', 'Merah, Putih, Biru, Hitam'),
(396, 'Magenta & Coral', 'Modern, American Classic', 'Kewanitaan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(397, 'Magenta & Biru air', 'Modern, Alam, American Classic', 'Kewanitaan, Ketenangan', 'Dingin', 'D, L, A, R', 'Merah, Putih, Biru'),
(398, 'Magenta & Krem', 'Modern, American Classic', 'Kewanitaan, Kehangatan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(399, 'Magenta & Hijau lumut', 'Modern, Alam, American Classic', 'Kewanitaan, Kejantanan', 'Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(400, 'Emas & Biru navy', 'Alam, American Classic', 'Keagungan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru, Hitam'),
(401, 'Emas & Merah maroon', 'Tradisional, Alam, American Classic', 'Keagungan, Keceriaan', 'Panas', 'D, L, A, R', 'Merah, Kuning, Biru'),
(402, 'Emas & Peach', 'Modern, American Classic', 'Keagungan, Kewanitaan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(403, 'Emas & Silver', 'Industrial, American Classic', 'Keagungan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(404, 'Emas & Coral', 'American Classic', 'Keagungan, Kewanitaan', 'Panas', 'D, L, A, R', 'Merah, Kuning, Biru'),
(405, 'Emas & Biru air', 'Alam, American Classic', 'Keagungan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(406, 'Emas & Krem', 'American Classic', 'Keagungan, Kehangatan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(407, 'Emas & Hijau lumut', 'Alam, American Classic', 'Keagungan, Kejantanan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(408, 'Biru navy & Merah maroon', 'Alam, Tradisional', 'Keceriaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru, Hitam'),
(409, 'Biru navy & Peach', 'Alam, Modern, American Classic', 'Kewanitaan, Ketenangan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(410, 'Biru navy & Silver', 'Alam, Industrial', 'Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(411, 'Biru navy & Coral', 'Alam, American Classic', 'Kewanitaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru, Hitam'),
(412, 'Biru navy & Biru air', 'Alam, American Classic', 'Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(413, 'Biru navy & Krem', 'Alam, American Classic', 'Ketenangan, Kehangatan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Kuning, Biru, Hitam'),
(414, 'Biru navy & Hijau lumut', 'Alam', 'Kejantanan, Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Kuning, Biru, Hitam'),
(415, 'Merah maroon & Peach', 'American Classic, Alam, Modern, Tradisional', 'Keceriaan, Kewanitaan', 'Panas, Hangat', 'D, L, R', 'Merah, Putih, Kuning, Biru'),
(416, 'Merah maroon & Silver', 'Alam, Industrial, Tradisional', 'Keceriaan, Ketenangan', 'Panas, Dingin', 'D, L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(417, 'Merah maroon & Coral', 'American Classic, Alam, Tradisional', 'Keceriaan, Kewanitaan', 'Panas', 'D, L, A, R', 'Merah, Kuning, Biru'),
(418, 'Merah maroon & Biru air', 'American Classic, Alam, Tradisional', 'Keceriaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(419, 'Merah maroon & Krem', 'American Classic, Alam, Tradisional', 'Keceriaan, Kehangatan', 'Panas, Hangat', 'D, L, R', 'Merah, Kuning, Biru'),
(420, 'Merah maroon & Hijau lumut', 'Alam, Tradisional', 'Keceriaan, Kejantanan', 'Panas, Dingin', 'D, L, R', 'Merah, Putih, Kuning, Biru'),
(421, 'Peach & Silver', 'Modern, Industrial, American Classic', 'Kewanitaan, Ketenangan', 'Hangat, Dingin', 'D, L, R', 'Merah, Putih, Kuning, Hitam'),
(422, 'Peach & Coral', 'Modern, American Classic', 'Kewanitaan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Putih, Kuning'),
(423, 'Peach & Biru air', 'Modern, Alam, American Classic', 'Kewanitaan, Ketenangan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(424, 'Peach & Krem', 'Modern, American Classic', 'Kewanitaan, Kehangatan', 'Hangat', 'D, L, R', 'Merah, Putih, Kuning, Biru'),
(425, 'Peach & Hijau lumut', 'Modern, Alam, American Classic', 'Kewanitaan, Kejantanan', 'Hangat, Dingin', 'D, L, R', 'Merah, Putih, Kuning, Biru'),
(426, 'Silver & Coral', 'Industrial, American Classic', 'Kewanitaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Hitam'),
(427, 'Silver & Biru air', 'Alam, Industrial, American Classic', 'Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Biru, Hitam'),
(428, 'Silver & Krem', 'Industrial, American Classic', 'Ketenangan, Kehangatan', 'Hangat, Dingin', 'D, L, R', 'Merah, Putih, Hitam, Kuning, Biru'),
(429, 'Silver & Hijau lumut', 'Alam, Industrial', 'Kejantanan, Ketenangan', 'Dingin', 'D, L, R', 'Putih, Kuning, Biru, Hitam'),
(430, 'Coral & Biru air', 'Alam, American Classic', 'Kewanitaan, Ketenangan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(431, 'Coral & Krem', 'American Classic', 'Kewanitaan, Kehangatan', 'Panas, Hangat', 'D, L, A, R', 'Merah, Kuning, Biru'),
(432, 'Coral & Hijau lumut', 'Alam, American Classic', 'Kewanitaan, Kejantanan', 'Panas, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(433, 'Biru air & Krem', 'Alam, American Classic', 'Ketenangan, Kehangatan', 'Hangat, Dingin', 'D, L, A, R', 'Merah, Putih, Kuning, Biru'),
(434, 'Biru air & Hijau lumut', 'Alam, American Classic', 'Kejantanan, Ketenangan', 'Dingin', 'D, L, A, R', 'Putih, Kuning, Biru'),
(435, 'Krem & Hijau lumut', 'Alam, American Classic', 'Kejantanan, Kehangatan', 'Hangat, Dingin', 'D, L, R', 'Merah, Putih, Kuning, Biru');

-- --------------------------------------------------------

--
-- Table structure for table `data_warna`
--

CREATE TABLE `data_warna` (
  `id_warna` int(11) NOT NULL,
  `warna` text,
  `style_desain` text,
  `makna_warna` text,
  `sifat` text,
  `usia_pengguna` text,
  `warna_dasar` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `data_warna`
--

INSERT INTO `data_warna` (`id_warna`, `warna`, `style_desain`, `makna_warna`, `sifat`, `usia_pengguna`, `warna_dasar`) VALUES
(1, 'Putih', 'American Classic, Tradisional, Industrial, Minimalis, Alam', 'Suci', 'Dingin', 'R, L', 'Putih'),
(2, 'Hitam', 'Industrial', 'Kekuatan', 'Panas', 'R, D', 'Hitam'),
(3, 'Kuning', 'American Classic', 'Keceriaan', 'Panas', 'A, R, D', 'Kuning'),
(4, 'Merah', 'American Classic', 'Keberanian', 'Panas', 'A, R, D', 'Merah'),
(5, 'Ungu', 'Modern', 'Keagungan', 'Dingin', 'A, R, D', 'Merah, Biru'),
(6, 'Hijau', 'Alam', 'Santai', 'Dingin', 'A, R, D, L', 'Kuning, Biru'),
(7, 'Biru', 'Alam', 'Ketenangan', 'Dingin', 'A, R, D, L', 'Biru'),
(8, 'Oren', 'American Classic', 'Keceriaan', 'Panas', 'A, R, D, L', 'Merah, Kuning'),
(9, 'Coklat', 'Tradisional, Alam', 'Kenyamanan', 'Hangat', 'R, L', 'Merah, Biru, Kuning'),
(10, 'Abu-Abu', 'Industrial', 'Kerendahan hati', 'Dingin', 'R, D, L', 'Hitam, Putih'),
(11, 'Merah muda', 'Modern', 'Kewanitaan', 'Panas', 'A, R, D', 'Merah, Putih'),
(12, 'Merah tua', 'Modern', 'Keberanian', 'Panas', 'R, L', 'Merah, Hitam'),
(13, 'Biru tua', 'Alam', 'Ketenangan', 'Dingin', 'A, R, D, L', 'Biru, Hitam'),
(14, 'Abu-Abu tua', 'Industrial', 'Kerendahan hati', 'Panas', 'D, R, L', 'Putih, Hitam'),
(15, 'Hijau tua', 'Alam', 'Santai', 'Dingin', 'L', 'Hijau, Hitam'),
(16, 'Coklat tua', 'Tradisional, Alam', 'Kejantanan', 'Hangat', 'L', 'Merah, Biru, Kuning'),
(17, 'Coklat muda', 'American Classic, Tradisional, Alam', 'Kejantanan', 'Hangat', 'L', 'Merah, Biru, Kuning'),
(18, 'Biru muda', 'American Classic, Alam', 'Kewanitaan', 'Dingin', 'A, R, D, L', 'Biru, Putih'),
(19, 'Abu-Abu muda', 'Industrial', 'Kerendahan hati', 'Dingin', 'R, D, L', 'Hitam, Putih'),
(20, 'Hijau muda', 'American Classic, Alam', 'Kewanitaan', 'Hangat', 'A, R, D, L', 'Biru, Kuning'),
(21, 'Magenta', 'American Classic, Modern', 'Kewanitaan', 'Dingin', 'A, R, D, L', 'Biru, Merah, Putih'),
(22, 'Emas', 'American Classic', 'Keagungan', 'Panas', 'A, R, D, L', 'Merah, Biru, Kuning'),
(23, 'Biru navy', 'Alam', 'Ketenangan', 'Dingin', 'A, R, D, L', 'Biru, Hitam'),
(24, 'Merah maroon', 'Tradisional, Alam', 'Keceriaan', 'Panas', 'R, D, L', 'Merah, Biru, Kuning'),
(25, 'Peach', 'American Classic, Modern', 'Kewanitaan', 'Hangat', 'R, D, L', 'Merah, Kuning, Putih'),
(26, 'Silver', 'Industrial', 'Ketenangan', 'Dingin', 'R, D, L', 'Hitam, Putih'),
(27, 'Coral', 'American Classic', 'Kewanitaan', 'Panas', 'A, R, D, L', 'Merah, Kuning'),
(28, 'Biru air', 'American Classic, Alam', 'Ketenangan', 'Dingin', 'A, R, D, L', 'Biru, Putih'),
(29, 'Krem', 'American Classic', 'Kehangatan', 'Hangat', 'R, D, L', 'Merah, Biru, Kuning'),
(30, 'Hijau lumut', 'Alam', 'Kejantanan', 'Dingin', 'L', 'Biru, Kuning, Putih');

-- --------------------------------------------------------

--
-- Table structure for table `riwayat_rekomendasi`
--

CREATE TABLE `riwayat_rekomendasi` (
  `id_riwayat` int(11) NOT NULL,
  `nama_kombinasi` text,
  `id_warna_1` text,
  `id_warna_2` text,
  `style_desain` text,
  `makna_warna` text,
  `sifat` text,
  `usia_pengguna` text,
  `warna_dasar` text,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `riwayat_rekomendasi`
--

INSERT INTO `riwayat_rekomendasi` (`id_riwayat`, `nama_kombinasi`, `id_warna_1`, `id_warna_2`, `style_desain`, `makna_warna`, `sifat`, `usia_pengguna`, `warna_dasar`, `created_at`) VALUES
(2, 'Putih & Ungu', 'A1', 'A2', 'Modern', 'Keceriaan', 'Hangat', 'Remaja (12-25 tahun)', 'Hitam', '2024-05-26 15:50:04');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data_kombinasi`
--
ALTER TABLE `data_kombinasi`
  ADD PRIMARY KEY (`id_kombinasi`);

--
-- Indexes for table `data_warna`
--
ALTER TABLE `data_warna`
  ADD PRIMARY KEY (`id_warna`);

--
-- Indexes for table `riwayat_rekomendasi`
--
ALTER TABLE `riwayat_rekomendasi`
  ADD PRIMARY KEY (`id_riwayat`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `data_kombinasi`
--
ALTER TABLE `data_kombinasi`
  MODIFY `id_kombinasi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=436;

--
-- AUTO_INCREMENT for table `data_warna`
--
ALTER TABLE `data_warna`
  MODIFY `id_warna` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `riwayat_rekomendasi`
--
ALTER TABLE `riwayat_rekomendasi`
  MODIFY `id_riwayat` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
