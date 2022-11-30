-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-11-2022 a las 04:02:07
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
-- Estructura de tabla para la tabla `articles`
--

CREATE TABLE `articles` (
  `ida` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  `idc` int(11) NOT NULL,
  `title` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `content` text COLLATE utf8_spanish_ci NOT NULL,
  `pdate` date NOT NULL,
  `learningchannel` varchar(20) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `articles`
--

INSERT INTO `articles` (`ida`, `id`, `idc`, `title`, `content`, `pdate`, `learningchannel`) VALUES
(1, 1, 1, 'Programación en Python', 'Fusce posuere mollis urna. Fusce in leo vitae nisl tincidunt dapibus vitae at magna. Suspendisse in metus pulvinar, iaculis enim eget, feugiat tortor. Etiam ac risus pretium, sollicitudin orci quis, gravida libero. Vestibulum eu arcu vestibulum, congue mi luctus, hendrerit ipsum. Mauris quis congue dolor. Fusce et luctus ex. In sed arcu molestie, vestibulum orci quis, condimentum ligula. Morbi tincidunt nisi sem, vitae sodales felis dapibus quis. Vestibulum vel pretium nisl. In fermentum molestie magna ac tempus. Vivamus mollis ligula lorem, ut pharetra magna pellentesque eu. In vestibulum nulla lobortis imperdiet pellentesque.\r\n\r\nSed erat mauris, facilisis a vehicula nec, eleifend vel mauris. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec vehicula metus in magna venenatis dictum. Integer dapibus euismod quam, a ullamcorper turpis efficitur sed. Suspendisse convallis quam sit amet tempor varius. Aliquam aliquet nec elit et pretium. Fusce sollicitudin accumsan egestas. Donec gravida justo facilisis malesuada rhoncus. Mauris eu enim at nibh rutrum mollis. Morbi varius urna a est tempor euismod. Phasellus ornare imperdiet commodo. Nam hendrerit tempus ex, sit amet aliquam augue laoreet sed. Phasellus felis felis, rhoncus nec ligula ac, ultrices sagittis orci. Quisque at luctus urna.\r\n\r\nDonec ac elit eros. Donec est metus, facilisis molestie lacus nec, gravida tristique odio. Morbi eget lectus feugiat, semper nisl nec, egestas dui. Ut vel ultricies velit. Nam blandit pretium elit, eget pellentesque leo rhoncus ac. Curabitur tincidunt non nisi sed consequat. Morbi quis commodo metus, vel convallis ipsum. Nunc et tempor diam. Vestibulum quis gravida dolor. Maecenas ac egestas velit. Quisque tincidunt ullamcorper dictum. In venenatis molestie laoreet.', '2023-03-15', 'Auditivo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comments`
--

CREATE TABLE `comments` (
  `idc` int(11) NOT NULL,
  `date` date NOT NULL,
  `contents` text COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `comments`
--

INSERT INTO `comments` (`idc`, `date`, `contents`) VALUES
(1, '2022-11-02', 'comentario');

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
(26, 'RouSan', 'sandyros.16.09@gmail.com', 'pbkdf2:sha256:260000$uzmpjPnpnz8wIbyI$2839948e48ee38520465eefa88d0d55b5e3a2db5e9620afbd7166a20bf5e2ced', 'Sandra Yessica Del Rocío Zaragoza Castro', '21', 'Licenciatura', 'U', ''),
(30, 'Oscarín', 'learntoapplication@gmail.com', 'pbkdf2:sha256:260000$XRwrijcJMmaIBzmu$0ab98942af421ede92da3b0afa19114ea14453309eb7a0fd5f8d72970348fa51', 'Óscar Maya', '25', 'Ingenieria', 'U', '2022005317learn.png');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `articles`
--
ALTER TABLE `articles`
  ADD PRIMARY KEY (`ida`),
  ADD KEY `id` (`id`),
  ADD KEY `idc` (`idc`);

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
-- AUTO_INCREMENT de la tabla `articles`
--
ALTER TABLE `articles`
  MODIFY `ida` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `comments`
--
ALTER TABLE `comments`
  MODIFY `idc` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `articles`
--
ALTER TABLE `articles`
  ADD CONSTRAINT `articles_ibfk_1` FOREIGN KEY (`id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `comments`
--
ALTER TABLE `comments`
  ADD CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`idc`) REFERENCES `articles` (`idc`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
