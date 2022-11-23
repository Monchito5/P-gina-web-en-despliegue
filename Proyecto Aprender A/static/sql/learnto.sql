-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-11-2022 a las 04:34:17
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
  `id` int(11) NOT NULL,
  `title` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `content` text COLLATE utf8_spanish_ci NOT NULL,
  `views` int(11) NOT NULL,
  `pdate` date NOT NULL,
  `clchannel` varchar(20) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comments`
--

CREATE TABLE `comments` (
  `id` int(11) NOT NULL,
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
  `dateregister` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='Tabla de usuario';

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `password`, `fullname`, `age`, `schoolgrade`, `auth`, `dateregister`) VALUES
(1, 'Monchonetreitor', 'guille2807lol@gmail.com', 'pbkdf2:sha256:260000$BFFHjvkFCqVYnpUD$37275b500b1a32af81d6c47eda631d942c90ca31085d297febc9d70175e2df4d', 'GUILLERMO DANIEL ZARAGOZA CASTRO', '20', 'preparatoria', 'A', '2022-11-02'),
(2, 'Pancho', 'panchito5@gmail.com', 'pbkdf2:sha256:260000$qylavDl4SkA2cu3n$e9bc8aa4f8d8c583159dd75c18f7059416fdbb08b22f939ee02b22ee133f7c58', 'Francisco Valle', '54', 'primaria', 'U', '2022-10-30'),
(4, 'Sandy', 'sandy12@gmail.com', 'pbkdf2:sha256:260000$vs65zJgsptT4gFRl$6d53f0fb58800445a0e412c743d2cbbc652d4be9d7337f96bd8bf76bbd02b187', 'Sandra', '22', 'licenciatura', 'U', '2022-10-30'),
(5, 'Juanito34', 'learntoapplication@gmail.com', 'pbkdf2:sha256:260000$XjeJ3PKbQc2lcMk9$2f4cc7148da6645047aec1d90c3852dc0e9ca89b1e833706bb9c27c21e08966a', 'Juan Pérez', '26', 'secundaria', 'U', '2022-10-30'),
(19, 'Eric Aitor García', 'eric007garcia@gmail.com', 'pbkdf2:sha256:260000$bWjYTV1FURrRFpH8$f343f9f1c3074f8423ba903b1e12be4c8f25e94310fbb85b518be6155da2b0d6', 'Eric Fernando García Y Ramos', '37', 'Licenciatura', 'U', '2022-11-20');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `article`
--
ALTER TABLE `article`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`id`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `comments`
--
ALTER TABLE `comments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `article`
--
ALTER TABLE `article`
  ADD CONSTRAINT `article_ibfk_1` FOREIGN KEY (`id`) REFERENCES `user` (`id`);

--
-- Filtros para la tabla `comments`
--
ALTER TABLE `comments`
  ADD CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
