-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 27, 2025 at 09:39 PM
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
-- Database: `car_dekho`
--

-- --------------------------------------------------------

--
-- Table structure for table `new_cars`
--

CREATE TABLE `new_cars` (
  `id` int(20) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Brand` varchar(20) NOT NULL,
  `Price` int(20) NOT NULL,
  `Model_year` year(4) NOT NULL,
  `Seating_capacity` int(20) NOT NULL,
  `Engine_Power` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `new_cars`
--

INSERT INTO `new_cars` (`id`, `Name`, `Brand`, `Price`, `Model_year`, `Seating_capacity`, `Engine_Power`) VALUES
(1, 'Civic', 'Honda', 25000, '2022', 5, 158),
(2, 'Corolla', 'Toyota', 23000, '2023', 5, 169),
(3, 'Model S', 'Tesla', 80000, '2023', 5, 1020),
(4, 'Mustang', 'Ford', 55000, '2022', 4, 450),
(5, 'Camry', 'Toyota', 27000, '2023', 5, 203),
(6, 'Accord', 'Honda', 28000, '2023', 5, 192),
(7, 'Elantra', 'Hyundai', 22000, '2022', 5, 147),
(8, '3 Series', 'BMW', 45000, '2023', 5, 255),
(9, 'A4', 'Audi', 46000, '2022', 5, 201),
(11, 'Altima', 'Nissan', 25000, '2023', 5, 188),
(12, 'Charger', 'Dodge', 32000, '2022', 5, 292),
(13, 'Tucson', 'Hyundai', 26000, '2023', 5, 187),
(14, 'Explorer', 'Ford', 34000, '2022', 7, 300),
(15, 'RAV4', 'Toyota', 28000, '2023', 5, 203),
(16, 'CX-5', 'Mazda', 29000, '2023', 5, 187),
(17, 'CR-V', 'Honda', 31000, '2023', 5, 190),
(18, 'Wrangler', 'Jeep', 33000, '2023', 5, 285),
(19, 'Cherokee', 'Jeep', 35000, '2022', 5, 271),
(20, 'X5', 'BMW', 65000, '2023', 5, 335),
(21, 'Q5', 'Audi', 55000, '2023', 5, 261),
(22, 'GLC', 'Mercedes-Benz', 58000, '2022', 5, 255),
(23, 'F-150', 'Ford', 45000, '2023', 5, 400),
(24, 'Silverado', 'Chevrolet', 46000, '2023', 5, 355),
(25, 'Ram 1500', 'Dodge', 47000, '2022', 5, 305),
(26, 'Sierra', 'GMC', 48000, '2023', 5, 355),
(27, 'Palisade', 'Hyundai', 41000, '2022', 7, 291),
(28, 'Telluride', 'Kia', 42000, '2023', 7, 291),
(29, 'Highlander', 'Toyota', 44000, '2022', 7, 295),
(30, 'Pilot', 'Honda', 45000, '2023', 7, 280),
(31, 'Grand Cherokee', 'Jeep', 48000, '2023', 5, 293),
(32, 'Suburban', 'Chevrolet', 58000, '2022', 7, 355),
(33, 'Tahoe', 'Chevrolet', 60000, '2023', 7, 355),
(34, 'Escalade', 'Cadillac', 90000, '2023', 7, 420),
(35, 'Range Rover', 'Land Rover', 95000, '2022', 5, 395),
(36, 'Defender', 'Land Rover', 70000, '2023', 5, 296),
(37, 'Macan', 'Porsche', 65000, '2022', 5, 261),
(38, 'Cayenne', 'Porsche', 75000, '2023', 5, 335),
(39, 'Aventador', 'Lamborghini', 500000, '2022', 2, 769),
(40, 'Huracan', 'Lamborghini', 300000, '2023', 2, 631),
(42, 'Portofino', 'Ferrari', 250000, '2023', 2, 591),
(43, 'DB11', 'Aston Martin', 240000, '2023', 2, 528),
(44, 'Vantage', 'Aston Martin', 210000, '2022', 2, 503),
(45, '911 Turbo', 'Porsche', 180000, '2023', 2, 572),
(46, 'Panamera', 'Porsche', 120000, '2023', 5, 325),
(47, 'RS7', 'Audi', 120000, '2022', 5, 591),
(48, 'M5', 'BMW', 130000, '2023', 5, 600),
(49, 'S-Class', 'Mercedes-Benz', 110000, '2023', 5, 496),
(50, 'G-Wagon', 'Mercedes-Benz', 150000, '2023', 5, 416),
(51, 'Verna', 'Hyundai', 850000, '2022', 5, 300),
(52, 'Scorpio', 'Mahindra', 250000, '2025', 7, 250);

-- --------------------------------------------------------

--
-- Table structure for table `old_cars`
--

CREATE TABLE `old_cars` (
  `id` int(20) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Brand_name` varchar(20) NOT NULL,
  `Model_year` year(4) NOT NULL,
  `km_used` int(11) NOT NULL,
  `price` int(20) NOT NULL,
  `No_of_owners` int(20) NOT NULL,
  `Seating capacity` int(20) NOT NULL,
  `Engine_power` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `old_cars`
--

INSERT INTO `old_cars` (`id`, `Name`, `Brand_name`, `Model_year`, `km_used`, `price`, `No_of_owners`, `Seating capacity`, `Engine_power`) VALUES
(1, 'Civic', 'Honda', '2015', 75000, 12000, 2, 5, 143),
(2, 'Corolla', 'Toyota', '2014', 82000, 11000, 2, 5, 132),
(3, 'Accord', 'Honda', '2016', 68000, 14000, 1, 5, 185),
(4, 'Camry', 'Toyota', '2015', 72000, 13000, 2, 5, 178),
(5, 'Elantra', 'Hyundai', '2013', 90000, 10000, 3, 5, 148),
(6, 'Sentra', 'Nissan', '2012', 95000, 9000, 3, 5, 130),
(7, 'Jetta', 'Volkswagen', '2015', 70000, 11500, 2, 5, 150),
(8, 'Passat', 'Volkswagen', '2016', 65000, 12500, 2, 5, 170),
(9, '3 Series', 'BMW', '2014', 78000, 17000, 1, 5, 240),
(10, 'C-Class', 'Mercedes-Benz', '2015', 72000, 19000, 1, 5, 241),
(12, 'Altima', 'Nissan', '2013', 88000, 10500, 3, 5, 182),
(13, 'Charger', 'Dodge', '2015', 77000, 18000, 2, 5, 292),
(14, 'Mustang', 'Ford', '2014', 60000, 17500, 1, 4, 305),
(15, 'Explorer', 'Ford', '2015', 72000, 20000, 1, 7, 290),
(16, 'RAV4', 'Toyota', '2014', 82000, 15500, 2, 5, 176),
(17, 'CR-V', 'Honda', '2015', 69000, 16000, 2, 5, 185),
(18, 'X5', 'BMW', '2016', 75000, 25000, 1, 5, 300),
(19, 'Q5', 'Audi', '2015', 79000, 23000, 2, 5, 220),
(20, 'Grand Cherokee', 'Jeep', '2014', 85000, 19000, 2, 5, 290),
(21, 'F-150', 'Ford', '2016', 70000, 22000, 1, 5, 325),
(22, 'Silverado', 'Chevrolet', '2015', 75000, 21000, 2, 5, 285),
(23, 'Ram 1500', 'Dodge', '2014', 90000, 20000, 3, 5, 305),
(24, 'CX-5', 'Mazda', '2016', 67000, 17500, 2, 5, 187),
(25, 'Tucson', 'Hyundai', '2015', 85000, 16500, 3, 5, 164),
(26, 'swift', 'suzuki', '2020', 65000, 150000, 1, 5, 165),
(27, 'wagonr', 'suzuki', '2022', 35000, 400000, 1, 5, 125),
(28, 'alto', 'suzuki', '2015', 120000, 100000, 2, 5, 150),
(29, 'XUV 700', 'Mahindra', '2022', 40000, 1400000, 1, 7, 250);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(20) NOT NULL,
  `username` varchar(16) NOT NULL,
  `password` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'Owner', '123456'),
(3, 'Arpit', 'Arpit123'),
(4, 'Arpit67', 'Arpit67'),
(5, 'Raj', 'Raj123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `new_cars`
--
ALTER TABLE `new_cars`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Name` (`Name`);

--
-- Indexes for table `old_cars`
--
ALTER TABLE `old_cars`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `new_cars`
--
ALTER TABLE `new_cars`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `old_cars`
--
ALTER TABLE `old_cars`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
