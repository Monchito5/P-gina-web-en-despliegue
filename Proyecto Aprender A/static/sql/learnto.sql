-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-11-2022 a las 05:55:18
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `learnto`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `article`
--

CREATE TABLE `article` (
  `ida` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  `idc` int(11) NOT NULL,
  `title` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `content` text COLLATE utf8_spanish_ci NOT NULL,
  `views` int(11) NOT NULL,
  `pdate` date NOT NULL,
  `learningchannel` varchar(20) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comments`
--

CREATE TABLE `comments` (
  `idc` int(11) NOT NULL,
  `date` date NOT NULL,
  `contents` text COLLATE utf8_spanish_ci NOT NULL,
  `reaction` varchar(50) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `email` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `password` char(102) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `fullname` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `age` varchar(5) COLLATE utf8_spanish_ci NOT NULL,
  `schoolgrade` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `auth` char(1) COLLATE utf8_spanish_ci NOT NULL DEFAULT 'U',
  `imgprofile` varchar(5000) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='Tabla de usuario';

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `password`, `fullname`, `age`, `schoolgrade`, `auth`, `imgprofile`) VALUES
(1, 'Monchonetreitor', 'guille2807lol@gmail.com', 'pbkdf2:sha256:260000$BFFHjvkFCqVYnpUD$37275b500b1a32af81d6c47eda631d942c90ca31085d297febc9d70175e2df4d', 'GUILLERMO DANIEL ZARAGOZA CASTRO', '20', 'preparatoria', 'A', ''),
(2, 'Pancho', 'panchito5@gmail.com', 'pbkdf2:sha256:260000$qylavDl4SkA2cu3n$e9bc8aa4f8d8c583159dd75c18f7059416fdbb08b22f939ee02b22ee133f7c58', 'Francisco Valle', '54', 'primaria', 'U', ''),
(19, 'Eric Aitor García', 'eric007garcia@gmail.com', 'pbkdf2:sha256:260000$bWjYTV1FURrRFpH8$f343f9f1c3074f8423ba903b1e12be4c8f25e94310fbb85b518be6155da2b0d6', 'Eric Fernando García Y Ramos', '37', 'Licenciatura', 'U', ''),
(23, 'Oscarín', 'learntoapplication@gmail.com', 'pbkdf2:sha256:260000$b1ZpJvprQ2lZhMyw$d40c23ced06b9731371fa8f7fa799783ce365e5bf1f2fe930996b85e80fb5312', 'Óscar Maya', '27', 'Licenciatura', 'U', ''),
(26, 'RouSan', 'sandyros.16.09@gmail.com', 'pbkdf2:sha256:260000$uzmpjPnpnz8wIbyI$2839948e48ee38520465eefa88d0d55b5e3a2db5e9620afbd7166a20bf5e2ced', 'Sandra Yessica Del Rocío Zaragoza Castro', '21', 'Licenciatura', 'U', '');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `article`
--
ALTER TABLE `article`
  ADD PRIMARY KEY (`ida`);

--
-- Indices de la tabla `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`idc`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `article`
--
ALTER TABLE `article`
  MODIFY `ida` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `comments`
--
ALTER TABLE `comments`
  MODIFY `idc` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `article`
--
ALTER TABLE `article`
  ADD CONSTRAINT `article_ibfk_1` FOREIGN KEY (`ida`) REFERENCES `user` (`id`);

--
-- Filtros para la tabla `comments`
--
ALTER TABLE `comments`
  ADD CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`idc`) REFERENCES `article` (`ida`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
