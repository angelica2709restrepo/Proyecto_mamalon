-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-01-2025 a las 17:23:06
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sena2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `arl`
--

CREATE TABLE `arl` (
  `id` int(11) NOT NULL,
  `nombreARL` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `arl`
--

INSERT INTO `arl` (`id`, `nombreARL`) VALUES
(1, 'ARL Positiva'),
(2, 'Seguros Bolívar S.A'),
(3, 'Seguros de Vida Aurora S.A'),
(4, 'Liberty Seguros de Vida'),
(5, 'Mapfre Colombia Vida Seguros S.A.'),
(6, 'Riesgos Laborales Colmena'),
(7, 'Seguros de Vida Alfa S.A'),
(8, 'Seguros de Vida Colpatria S.A'),
(9, 'Seguros de Vida la Equidad Organismo C.'),
(10, 'Sura – Cia. Suramericana de Seguros de Vida');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `banco`
--

CREATE TABLE `banco` (
  `id` int(11) NOT NULL,
  `nombreBanco` varchar(255) NOT NULL,
  `tipoCuenta` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `banco`
--

INSERT INTO `banco` (`id`, `nombreBanco`, `tipoCuenta`) VALUES
(1, 'BANCO COMERCIAL AV VILLAS S.A.', 1),
(2, 'BANCO DAVIVIENDA S.A.', 1),
(3, 'BANCOLOMBIA S.A.', 1),
(4, 'BANCO CAJA SOCIAL S.A.', 1),
(5, 'BANCO DE BOGOTA S. A.', 1),
(6, 'SCOTIABANK COLPATRIA SA', 1),
(7, 'BANCO BILBAO VIZCAYA ARGENTARIA COLOMBIA S.A. BBVA', 1),
(8, 'BANCO GNB SUDAMERIS S A', 1),
(9, 'BANCO POPULAR S. A.', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cargo`
--

CREATE TABLE `cargo` (
  `id` int(11) NOT NULL,
  `nombreCargo` varchar(255) NOT NULL,
  `idJefe` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cargo`
--

INSERT INTO `cargo` (`id`, `nombreCargo`, `idJefe`) VALUES
(1, 'Administrativo Contratista', 1),
(2, 'Instructor Contratista', 1),
(3, 'Instructor Contratista - Virtual', 1),
(4, 'Instructor Contratista - Articulación', 1),
(5, 'Instructor Contratista - Desplazados', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ciudad`
--

CREATE TABLE `ciudad` (
  `id` int(11) NOT NULL,
  `nombreCiudad` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ciudad`
--

INSERT INTO `ciudad` (`id`, `nombreCiudad`) VALUES
(18, 'Bogotá D.C');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id` int(11) NOT NULL,
  `primerNombre` varchar(255) NOT NULL,
  `segundoNombre` varchar(255) NOT NULL,
  `primerApellido` varchar(255) NOT NULL,
  `segundoApellido` varchar(255) NOT NULL,
  `tipoDocumento` int(11) NOT NULL,
  `departamentoExpedicion` int(11) NOT NULL,
  `ciudadExpedicion` int(11) NOT NULL,
  `fechaExpedicion` date NOT NULL,
  `genero` int(11) NOT NULL,
  `fechaNacimento` date NOT NULL,
  `Rh` int(11) NOT NULL,
  `dirrecion` varchar(250) NOT NULL,
  `correo` varchar(250) NOT NULL,
  `correoAdicional` varchar(255) NOT NULL,
  `celular` int(15) NOT NULL,
  `telefono` int(11) NOT NULL,
  `ARL` int(11) NOT NULL,
  `EPS` int(11) NOT NULL,
  `PAA` int(11) NOT NULL,
  `idBanco` int(11) NOT NULL,
  `numeroCuenta` int(11) NOT NULL,
  `CDP` int(11) NOT NULL,
  `fechaRegistro` date NOT NULL,
  `ultimoAcceso` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Estado` int(11) NOT NULL,
  `usuarioCreador` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id`, `primerNombre`, `segundoNombre`, `primerApellido`, `segundoApellido`, `tipoDocumento`, `departamentoExpedicion`, `ciudadExpedicion`, `fechaExpedicion`, `genero`, `fechaNacimento`, `Rh`, `dirrecion`, `correo`, `correoAdicional`, `celular`, `telefono`, `ARL`, `EPS`, `PAA`, `idBanco`, `numeroCuenta`, `CDP`, `fechaRegistro`, `ultimoAcceso`, `Estado`, `usuarioCreador`) VALUES
(5646, 'asdad', 'asdasd', 'asdad', 'dad', 1, 2, 18, '2024-10-08', 1, '2024-10-08', 2, 'dfsdfasd', 'miguel@gmail.com', 'borbon@gmail.com', 131231, 123213, 1, 1, 1231223, 2, 1313, 12313, '2024-10-08', '2024-10-08 05:00:00', 1, 46),
(72151, 'dadad', 'asddasssdf', 'sdsdf', 'sdfsf', 1, 2, 18, '2024-10-08', 1, '2024-10-08', 2, 'dfsdfasd', 'miguel@gmail.com', 'borbon@gmail.com', 131231, 123213, 1, 1, 1231223, 2, 1313, 12313, '2024-10-08', '2024-10-08 05:00:00', 1, 46);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contrato`
--

CREATE TABLE `contrato` (
  `id` int(11) NOT NULL,
  `idVersion` varchar(255) NOT NULL,
  `idClientes` int(11) NOT NULL,
  `idTipoContrato` int(11) NOT NULL,
  `idCargo` int(11) NOT NULL,
  `idDependecia` int(11) NOT NULL,
  `idObjeto` int(11) NOT NULL,
  `ObEspCon` int(11) NOT NULL,
  `descripcionContrato` varchar(255) NOT NULL,
  `Vigencia` date NOT NULL,
  `terminacion` date NOT NULL,
  `autorizacionContratos` int(20) NOT NULL,
  `valorContrato` int(20) NOT NULL,
  `consecutivo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `contrato`
--

INSERT INTO `contrato` (`id`, `idVersion`, `idClientes`, `idTipoContrato`, `idCargo`, `idDependecia`, `idObjeto`, `ObEspCon`, `descripcionContrato`, `Vigencia`, `terminacion`, `autorizacionContratos`, `valorContrato`, `consecutivo`) VALUES
(63, '63-1', 5646, 2, 1, 5, 78, 7, 'qqqqqq', '2024-10-09', '2026-10-15', 123456, 987, 5678),
(65, '63-2', 5646, 2, 1, 5, 78, 7, 'qqqqqq', '2024-10-09', '2026-10-15', 123456, 987, 5678),
(66, '63-2', 5646, 2, 1, 5, 78, 7, 'qqqqqq', '2024-10-09', '2026-10-15', 123456, 987, 5678),
(67, '63-3', 5646, 2, 1, 5, 78, 7, 'qqqqqq', '2024-10-09', '2026-10-15', 123456, 987, 5678);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamentos`
--

CREATE TABLE `departamentos` (
  `id` int(11) NOT NULL,
  `nombreDepartamento` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `departamentos`
--

INSERT INTO `departamentos` (`id`, `nombreDepartamento`) VALUES
(2, 'Amazonas'),
(3, 'Antioquia'),
(4, 'Arauca'),
(5, 'Atlántico'),
(6, 'Bolívar '),
(7, 'Boyacá'),
(8, 'Caldas'),
(9, 'Caquetá'),
(10, 'Casanare'),
(11, 'Cauca'),
(12, 'Cesar'),
(13, 'Chocó'),
(14, 'Córdoba'),
(15, 'Cundinamarca'),
(16, 'Guainía'),
(17, 'Guaviare'),
(18, 'Huila '),
(19, 'La Guajira'),
(20, 'Magdalena'),
(21, 'Meta'),
(22, 'Nariño'),
(23, 'Norte de Santander'),
(24, 'Putumayo'),
(25, 'Quindío'),
(26, 'Risaralda'),
(27, 'San Andrés y Providencia'),
(28, 'Santander'),
(29, 'Sucre'),
(30, 'Tolima'),
(31, 'Valle del Cauca'),
(32, 'Vaupés'),
(33, 'Vichada');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dependencia`
--

CREATE TABLE `dependencia` (
  `id` int(11) NOT NULL,
  `nombreDependencia` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `dependencia`
--

INSERT INTO `dependencia` (`id`, `nombreDependencia`) VALUES
(1, 'Presupuesto'),
(2, 'Subdireccion'),
(3, 'SENNOVA'),
(4, 'CCL'),
(5, 'Coordinación Academica Presencial'),
(6, 'Coordinación Formación Profesional'),
(7, 'Contratación'),
(8, 'Planeación'),
(9, 'Coordinación Administración Educativa'),
(10, 'Coordinación Académica Presencial'),
(11, 'Contabilidad'),
(12, 'Coordinación Academica Virtual'),
(13, 'SIGA'),
(14, 'Bienestar'),
(15, 'Talento Humano'),
(16, 'Almacen'),
(17, 'Producción de Centros'),
(18, 'Biblioteca'),
(19, 'ECCL'),
(20, 'Contratacion'),
(21, 'Subdirección'),
(22, 'Archivo'),
(23, 'FCCL'),
(24, 'Produccion de centro'),
(25, 'Soporte'),
(26, 'Almacen\r\n');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `eps`
--

CREATE TABLE `eps` (
  `id` int(11) NOT NULL,
  `nombreEPS` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `eps`
--

INSERT INTO `eps` (`id`, `nombreEPS`) VALUES
(1, 'COOSALUD EPS-S '),
(2, 'NUEVA EPS'),
(3, 'MUTUAL SER  '),
(5, 'SALUD TOTAL EPS S.A.'),
(6, 'EPS SANITAS '),
(7, 'EPS SURA '),
(8, 'FAMISANAR'),
(9, 'SERVICIO OCCIDENTAL DE SALUD EPS SOS'),
(10, 'SALUD MIA'),
(11, 'COMFENALCO VALLE'),
(12, 'COMPENSAR EPS '),
(13, 'EPM - EMPRESAS PUBLICAS DE MEDELLIN'),
(14, 'FONDO DE PASIVO SOCIAL DE FERROCARRILES \nNACIONALES DE COLOMBIA '),
(15, 'CAJACOPI ATLANTICO '),
(16, 'CAPRESOCA '),
(17, 'COMFACHOCO'),
(18, 'COMFAORIENTE '),
(19, 'EPS FAMILIAR DE COLOMBIA'),
(20, 'ASMET  SALUD  '),
(21, 'EMSSANAR E.S.S. '),
(22, 'CAPITAL SALUD EPS-S'),
(23, 'SAVIA SALUD EPS '),
(24, 'DUSAKAWI EPSI '),
(25, 'ASOCIACION INDIGENA DEL CAUCA EPSI '),
(26, 'ANAS WAYUU EPSI '),
(27, 'MALLAMAS EPSI '),
(28, 'PIJAOS SALUD EPSI '),
(29, 'SALUD BÓLIVAR EPS SAS ');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado`
--

CREATE TABLE `estado` (
  `id` int(11) NOT NULL,
  `tipoEstado` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estado`
--

INSERT INTO `estado` (`id`, `tipoEstado`) VALUES
(1, 'Activo'),
(2, 'Inactivo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genero`
--

CREATE TABLE `genero` (
  `id` int(11) NOT NULL,
  `nombreGenero` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `genero`
--

INSERT INTO `genero` (`id`, `nombreGenero`) VALUES
(1, 'MASCULINO'),
(2, 'FEMENINO ');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jefe`
--

CREATE TABLE `jefe` (
  `id` int(11) NOT NULL,
  `nombreJefe` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `jefe`
--

INSERT INTO `jefe` (`id`, `nombreJefe`) VALUES
(1, 'Miguel'),
(2, 'a'),
(3, 'a'),
(4, 'a'),
(5, 'a'),
(6, 'a'),
(7, 'a'),
(8, 'a'),
(9, 'a'),
(10, 'a'),
(11, 'a'),
(12, 'q'),
(2828, 'joana');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `objeto`
--

CREATE TABLE `objeto` (
  `id` int(11) NOT NULL,
  `nombreObjeto` varchar(900) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `objeto`
--

INSERT INTO `objeto` (`id`, `nombreObjeto`) VALUES
(0, 'Prestar servicios personales de carácter temporal para impartir formación profesional integral titulada y/o complementaria y/o realizar seguimiento a etapa productiva, de acuerdo a la programación establecida por el Centro para la Industria de la Comunicación Gráfica en las diferentes jornadas académicas en los diferentes niveles de acuerdo a las competencias requeridas en cada uno de los programas de formación presenciales y/o virtuales que sean asignados'),
(1, 'Prestar servicios personales de carácter temporal para impartir formación profesional integral titulada y/o complementaria y/o realizar seguimiento a etapa productiva, de acuerdo a la programación establecida por el Centro para la Industria de la Comunicación Gráfica en las diferentes jornadas académicas en los diferentes niveles de acuerdo a las competencias requeridas en cada uno de los programas de formación presenciales y/o virtuales que sean asignados.'),
(28, 'Prestar servicios personales de carácter temporal para impartir formación profesional integral titulada y/o complementaria y/o realizar seguimiento a etapa productiva, de acuerdo a la programación establecida por el Centro para la Industria de la Comunicación Gráfica en las diferentes jornadas académicas en los diferentes niveles de acuerdo a las competencias requeridas en cada uno de los programas de formación presenciales y/o virtuales que sean asignados.'),
(29, 'Prestar servicios personales de carácter temporal para impartir formación profesional integral titulada y/o complementaria y/o realizar seguimiento a etapa productiva, de acuerdo a la programación establecida por el Centro para la Industria de la Comunicación Gráfica en las diferentes jornadas académicas en los diferentes niveles de acuerdo a las competencias requeridas en cada uno de los programas de formación presenciales y/o virtuales que sean asignados'),
(30, 'Prestar servicios personales de carácter temporal para impartir formación profesional integral titulada y/o complementaria y/o realizar seguimiento a etapa productiva, de acuerdo a la programación establecida por el Centro para la Industria de la Comunicación Gráfica en las diferentes jornadas académicas en los diferentes niveles. de acuerdo a las competencias requeridas en cada uno de los programas de formación presenciales y/o virtuales que sean asignados.'),
(31, 'Prestar los servicios personales para adelantar y desarrollar acciones orientadas a la promoción de la salud mental y prevención de problemas psicosociales, así como el fortalecimiento del liderazgo y desarrollo humano integral de los Aprendices que favorezcan su permanencia en el proceso formativo en el marco del Plan Nacional de Bienestar de los Aprendices de acuerdo con la normatividad vigente'),
(32, 'Prestar de servicios de apoyo de carácter temporal para la gestión y administración de los recursos y servicios de información de la unidad de audiovisuales del Centro para la Industria de la Comunicación'),
(33, 'Prestar los servicios profesionales para apoyar los procesos administrativos y operativos propios de la contratación y planeación estratégica del Centro para la Industria de la Comunicación Gráfica del SENA Distrito Capital.'),
(34, 'Prestar servicios de apoyo de carácter temporal en la gestión administrativa en las actividades relacionadas con el manejo del talento humano del Centro para la Industria de la Comunicación Gráfica'),
(35, 'Prestar servicios de carácter temporal como apoyo en la administración del almacén, como en el respectivo seguimiento y control de los diferentes bienes del Centro para la Industria Gráfica.'),
(36, 'Prestar de servicios de apoyo de carácter temporal para la gestión de los recursos y servicios de información de la unidad de audiovisuales del Centro para la Industria de la Comunicación Gráfica del SENA.'),
(37, 'Prestación de servicios temporales como apoyo a la gestión administrativa de los procesos de producción de centros del Centro para la Industria de la Comunicación Gráfica.'),
(38, 'Prestar servicios personales de carácter temporal para impartir formación profesional integral titulada y/o realizar seguimiento a etapa productiva en el programa articulación con la educación media, de acuerdo a la programación establecida por el Centro para la Industria de la Comunicación Gráfica en las diferentes jornadas académicas en los diferentes niveles de acuerdo a las competencias requeridas en cada uno de los programas de formación que sean asignados. '),
(39, 'Prestar servicios personales para brindar atención a usuarios del ambiente virtual y plataformas conexas en aspectos técnicos, administrativos y funcionales, necesarios en los procesos de formación, proporcionando respuesta oportuna a las necesidades de los usuarios y realizando acciones para fomentar el uso y dominio por parte de los roles asociados a la formación.'),
(40, 'Prestar los servicios personales para apoyar el desarrollo de actividades orientadas al fortalecimiento de habilidades socioemocionales de los aprendices del centro de formación en el marco del plan nacional integral de bienestar de los aprendices.'),
(41, 'Prestar los servicios personales para la planificación, coordinación y ejecución de actividades físicas, deportivas, recreativas, eventos relacionados con el deporte, el aprovechamiento del tiempo libre, así como la promoción de hábitos saludables de los aprendices en el Centro de Formación, en el marco del Plan Nacional Integral de Bienestar de los Aprendices y normatividad vigente.'),
(42, 'Prestar los servicios personales para adelantar y desarrollar acciones orientadas a la promoción de la salud mental y prevención de problemas psicosociales, así como el fortalecimiento del liderazgo y desarrollo humano integral de los Aprendices que favorezcan su permanencia en el proceso formativo en el marco del Plan Nacional de Bienestar de los Aprendices de acuerdo con la normatividad vigente.'),
(43, 'Prestar servicios personales de carácter temporal para impartir formación profesional integral titulada y/o realizar seguimiento a etapa productiva en el programa articulación con la educación media, de acuerdo a la programación establecida por el Centro para la Industria de la Comunicación Gráfica en las diferentes jornadas académicas en los diferentes niveles de acuerdo a las competencias requeridas en cada uno de los programas de formación que sean asignados.'),
(44, 'Prestar servicios personales de carácter temporal para impartir formación profesional integral titulada y/o realizar seguimiento a etapa productiva en el programa articulación con la educación media, de acuerdo a la programación establecida por el Centro para la Industria de la Comunicación Gráfica en las diferentes jornadas académicas en los diferentes niveles de acuerdo a las competencias requeridas en cada uno de los programas de formación que sean asignados.	'),
(45, 'Prestar servicios profesionales en el Centro para la Industria de la Comunicación Gráfica para asegurar la planificación, el desarrollo, la implementación, el mantenimiento y la mejora del sistema de gestión aplicable a la tipología de Servicios Tecnológicos de SENNOVA.'),
(46, 'Prestar servicios personales de carácter temporal para impartir formación profesional integral titulada y/o realizar seguimiento a etapa productiva en el programa articulación con la educación media, de acuerdo a la programación establecida por el Centro para la Industria de la Comunicación Gráfica en las diferentes jornadas académicas en los diferentes niveles de acuerdo a las competencias requeridas en cada uno de los programas de formación que sean asignados.'),
(47, 'Prestación de servicios de carácter temporal de un tecnólogo para apoyar el desarrollo y organización de las colecciones y los servicios de información de la biblioteca en correspondencia con el Manual de funcionamiento del Sistema de Bibliotecas'),
(48, 'Prestar los servicios personales para acompañar la asignación y seguimiento de los apoyos socioeconómicos y/o estímulos, en el marco del plan nacional integral de bienestar al aprendizaje y normatividad vigente.'),
(49, 'Prestar los servicios personales, para apoyar los diferentes procesos administrativos de la gestión de la formación profesional integral contemplados para ejecutar el plan de bienestar al aprendiz del centro de formación.'),
(50, 'Prestar servicios de apoyo a la gestión para atender y garantizar el proceso de selección, ingreso y certificación académica en el aplicativo dispuesto para la gestión educativa en el centro para la industria de la comunicación gráfica.'),
(51, 'Prestar los servicios personales para impulsar y desarrollar actividades de prevención de las enfermedades y promoción de la salud integral, dirigidas a los aprendices del Centro de formación, en el marco del Plan Nacional Integral de Bienestar de los Aprendices'),
(52, 'Prestar temporalmente los servicios profesionales en la Evaluación y Certificación de Competencias Laborales del SENA, y construcción y revisión de instrumentos de evaluación, en las funciones productivas o áreas clave Industria de la Comunicación Grafica, Mercadeo y Gestión Administrativa en las que podrá evaluar competencias, construir y revisar instrumentos, según necesidades, para el cumplimiento de las metas establecidas en este proceso.'),
(53, 'Prestación de servicios profesionales de carácter temporal como apoyo jurídico en las actuaciones relacionadas con el proceso formativo y contractual respecto a la adquisición de bienes y servicios asignados al Centro para la Industria de la Comunicación Gráfica articulado con el grupo de Apoyo Administrativo Intercentros del Complejo de Paloquemao'),
(54, 'Prestar servicios profesionales para responder por la ejecución de las actividades técnicas y operativas, relacionadas con la implementación, aseguramiento técnico y mantenimiento del portafolio de servicios del proyecto SGPS-11972-2024 del Centro para la Industria de la comunicación Gráfica y el fomento de la I. +D+i.'),
(55, 'Prestar temporalmente los servicios profesionales en la Evaluación y Certificación de Competencias Laborales del SENA, y construcción y revisión de instrumentos de evaluación, en las funciónes productivas o áreas clave Industria de la Comunicación Grafica, Audiovisuales y Gestión Administrativa en las que podrá evaluar competencias, construir y revisar instrumentos, según necesidades, para el cumplimiento de las metas establecidas en este proceso.'),
(56, 'Prestación de servicios de carácter temporal de un técnico para apoyar el procesamiento físico de las colecciones y los servicios de información de la biblioteca en correspondencia con el Manual de funcionamiento del Sistema de Bibliotecas'),
(57, 'Prestación de servicios técnicos para apoyar las actividades administrativas en la actividad contractual del Centro de Formación (Centro para la Industria de la Comunicación Gráfica)'),
(58, 'PRESTAR LOS SERVICIOS PERSONALES PARA APOYAR LOS PROCESOS QUE SE DEBEN GESTIONAR EN EL TRÁMITE DE ATENCIÓN AL CIUDADANO CONFORME A LAS COMUNICACIONES RECIBIDAS DE LOS MEDIOS EXTERNOS E INTERNOS PARA LAS DIFERENTES DEPENDENCIAS DEL CENTRO DE LA INDUSTRIA DE LA COMUNICACIÓN GRÁFICA.'),
(59, 'Prestar servicios personales para apoyar las actividades derivadas del proceso de la gestión documental en cumplimiento de los lineamientos y normatividad vigente para el centro para la industria de la comunicación gráfica.'),
(60, 'Prestar los servicios personales, para apoyar los diferentes procesos administrativos relacionados con Pruebas TYT y atención a Egresados del SENA, así como la atención al usuario en general.'),
(61, 'Prestar servicios personales de apoyo de carácter temporal para las actividades propias de la coordinación académica asignada, garantizando el adecuado tramite de los procesos académicos y de la gestión educativa en cumplimiento a los lineamientos vigentes establecidos para el Centro Para La Industria De La Comunicación Gráfica.'),
(62, 'Prestar los servicios personales para apoyar en la gestión de los proyectos, planes e iniciativas del Proceso de Gestión de Instancias de Concertación y Competencias Laborales en los Centros de Formación.'),
(63, 'Prestar temporalmente los servicios profesionales en la Evaluación y Certificación de Competencias Laborales del SENA, y construcción y revisión de instrumentos de evaluación, en las funciones productivas o áreas clave Gestión Administrativa y Mercadeo en las que podrá evaluar competencias, construir y revisar instrumentos, según necesidades, para el cumplimiento de las metas establecidas en este proceso.'),
(64, 'Prestar los servicios personales para implementar acciones que promuevan el reconocimiento de la Cultura como creadora de identidad, generadora de inclusión y catalizadora de diversidad, en el marco del Plan Nacional Integral de Bienestar de los Aprendices.'),
(65, 'Prestar servicios de apoyo de carácter temporal en el proceso de producción de centros en el área de producción gráfica del Centro para la Industria de la Comunicación Gráfica del SENA.'),
(66, 'Prestación de servicios profesionales de abogado para realizar las acciones jurídicas de la gestión contractual y convencional del Centro de Formación (Centro para la Industria de la Comunicación Gráfica).'),
(67, 'Prestar los servicios profesionales para acompañar el mantenimiento, seguimiento y mejoramiento del Modelo de operación del SIGA compuesto por Modelo integrado de planeación y gestión- MIPG,\r\nModelo estándar control interno MECI, Sistema de Gestión de Calidad, Ambiental y de Eficiencia Energética, bajo las Normas Técnicas ISO 9001, ISO 14001, ISO 27001 e ISO 50001, así como la implementación de la Estrategia de Sostenibilidad de la Entidad, como Dinamizador CF del Sistema Integrado de Gestión y Autocontrol (SIGA) implementando, gestionando, y monitoreando, mediante el\r\nenfoque por procesos a nivel Del Centro para la Industria de la Comunicación Gráfica, así como de sus sedes, en articulación con todos los sistemas que conforman el SIGA.'),
(68, 'Prestar los servicios profesionales de carácter temporal para apoyar la gestión de la biblioteca del Centro de Formación según los lineamientos del Manual de funcionamiento del Sistema de Bibliotecas.'),
(69, 'Prestar servicios de apoyo de carácter temporal en el proceso de producción de centros en el área de producción gráfica del Centro para la Industria de la Comunicación Gráfica del SENA.'),
(70, 'Prestación de servicios de carácter temporal como apoyo en el seguimiento, gestión y administración de la infraestructura tecnológica del Centro para la Industria de la Comunicación Gráfica.'),
(71, 'Prestar los servicios personales de carácter temporal como conductor de los vehículos asignados al Centro para la Industria de la Comunicación Gráfica.'),
(72, 'Prestación de servicios profesionales de carácter temporal como apoyo a la gestión seguimiento y control de los procesos de producción de centros del Centro para la Industria de la Comunicación Gráfica.'),
(73, 'Prestar los servicios profesionales para el acompañamiento a la ejecución del Plan Nacional Integral de Bienestar al Aprendiz-PNIBA, desde los programas asociados a economía Popular y CampeSENA.'),
(74, 'Prestar los servicios profesionales, para respaldar y facilitar los procesos de\r\nplanificación, diseño, implementación, gestión, integración, operación,\r\nseguimiento y mejora continua de los servicios tecnológicos TIC.'),
(75, 'Prestar los servicios personales de apoyo a la gestión, para el\r\ndesempeño asistencial de actividades técnicas, implementación y\r\nconfiguración de soluciones tecnológicas para los usuarios de la\r\ninfraestructura tecnológica de la entidad.'),
(76, 'Prestación de servicios profesionales de carácter temporal para\r\napoyar en la estructuración y seguimiento de los procesos de\r\ncontratación de mantenimiento, adecuaciones e infraestructura y\r\ndemás actividades requeridas por el Centro para la Industria de la\r\nComunicación Gráfica.'),
(77, 'Prestación de servicios de apoyo de carácter temporal a la gestión de actividades de creación de contenidos que sirvan de soporte para integrar a los desarrollos de cada sala del museo virtual del proyecto SGPS 12154 denominado: Museo Virtual Interactivo para el fomento del arte, la formación y la investigación utilizando tecnologías inmersivas.'),
(78, 'Prestar los servicios personales de apoyo a la gestión, para el desempeño asistencial de actividades técnicas, implementación y configuración de soluciones tecnológicas para los usuarios de la infraestructura tecnológica de la entidad. '),
(79, 'Prestar servicios personales de carácter temporal para impartir formación profesional integral titulada y/o complementaria y/o realizar seguimiento a etapa productiva, de acuerdo a la programación establecida por el Centro para la Industria de la Comunicación Gráfica en las diferentes jornadas académicas en los diferentes niveles de acuerdo a las competencias requeridas en cada uno de los programas de formación presenciales y/o virtuales que sean asignados. '),
(80, 'Prestar servicios profesionales de carácter temporal como apoyo en la gestión de los procesos administrativos y estructurales de las áreas contables y financieras del grupo de apoyo administrativo intercentros del complejo de Paloquemao.'),
(81, 'Prestación de servicios de apoyo de carácter temporal a la gestión de actividades de creación de contenido digital que sirvan de soporte para integrar a los desarrollos front del proyecto SGPS 12837 denominado: Sistema de información documental de proyectos formativos en contenidos digitales del centro para la Industria de la Comunicación Gráfica del SENA.'),
(82, 'Prestar los servicios personales de apoyo a la gestión, para el desempeño asistencial de actividades técnicas, implementación y configuración de soluciones tecnológicas para los usuarios de la infraestructura tecnológica de la entidad.'),
(83, 'sdadadsad'),
(84, 'qeqeqeq');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `obligacionesespecificas`
--

CREATE TABLE `obligacionesespecificas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(1600) NOT NULL,
  `idObjeto` int(11) NOT NULL,
  `año` year(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `obligacionesespecificas`
--

INSERT INTO `obligacionesespecificas` (`id`, `nombre`, `idObjeto`, `año`) VALUES
(1, ' Apoyar al seguimiento de la planeación con base en los indicadores, objetivos y metas propuestas. 2. Apoyar en el análisis y control del presupuesto con el fin de garantizar una óptima ejecución. 3.Apoyar en el Manejo del aplicativo SIIF Nación. 4. Brindar apoyo en la expedición de CDPs, Registros presupuestales y demás movimientos que se requieran. 5. Apoyar en la elaboración de informes financieros que se requieran. 6. Organizar y entregar los documentos y archivos a cargo durante la ejecución del contrato, según guías y TRD de gestión documental establecidas por dirección general. 7. Ejecutar de manera idónea el objeto del contrato conforme a los lineamientos del Sistema Integrado de Centro y Autocontrol (SIGA) del SENA, el cual se encuentra documentado en la plataforma compromiso. 8. Atender oportunamente los requerimientos que haga el supervisor del contrato. 9. Aplicar los procesos y procedimientos establecidos por la entidad, para la gestión documental relacionada con el objeto contractual.', 0, '0000'),
(2, 'Apoyar en el seguimiento y mantener actualizada la información del estado físico de los Ambientes de Aprendizaje, las máquinas y equipos existentes en cada uno de ellos. 2. Apoyar en el seguimiento y administración de las áreas que conforman el Grupo de Apoyo Administrativo Intercentros del Complejo Paloquemao. 3. Apoyar en la realización de la planeación de los procesos de mantenimiento de instalaciones y de maquinaria y equipos. 4. Presentar los informes y requerimientos de mantenimientos periódicamente y en el momento que sean solicitados. 5. Proveer las acciones y recursos necesarios para el cuidado y mantenimiento de la infraestructura de los ambientes de formación y establecer acciones de mejora. 6. Informar oportunamente a quien corresponda sobre daños y/o deterioros de la infraestructura, maquinaria y equipo de los ambientes de formación. 7. Apoyar a la Subdirección en la programación del personal de aseo y servicios generales, velando por la correcta ejecución de sus labores. 8. Apoyar técnicamente los procesos de contratación de centro, según se requiera. 9. Entregar por escrito los informes que se le soliciten de las actividades realizadas conforme con el objeto contractual y asistir a las reuniones y/o comités programados cuando sea requerido o asignado. 10. Ejecutar de manera idónea el objeto del contrato conforme a los lineamientos del Sistema Integrado de Gestión y Autocontrol (SIGA) del SENA, el cual se encuentra documentado en la plataforma compromiso. 11. Mantener la debida reserva sobre los asuntos manejados y conocidos dentro de la ejecución del contrato', 0, '0000'),
(3, ' Aportar a la construcción de rutas y herramientas desde el Centro de Formación y en articulación con sus actores, para el fortalecimiento y consolidación del sistema de I+D+i. 2. Apoyar técnica, administrativa y operativamente la implementación de las estrategias del ecosistema SENNOVA conforme a los lineamientos establecidos por la Dirección de Formación Profesional. 3. Articular con las áreas encargadas y apoyar el desarrollo de las actividades relacionadas con la contratación en sus diferentes etapas, apoyo técnico con la ejecución de contratos gestionados para el desarrollo de los procesos de I+D+i del sistema SENNOVA. 4. Desarrollar las actividades de seguimiento administrativo y financiero de los procesos y actividades del Sistema de I+D+i SENNOVA, de acuerdo con los lineamientos del Centro de Formación y las orientaciones de la Dirección de Formación Profesional. 5. Elaborar de manera oportuna los informes que se requieran sobre los procesos del Sistema de I+D+i SENNOVA, los avances tanto en la ejecución técnico-presupuestal de los proyectos en I+D+i, como en los indicadores y metas definidos para las actividades del Sistema, garantizando que dicha información sea veraz, este completa y se disponga oportunamente en las herramientas dispuestas para ello. 6. Participar en las actividades que se definan en el marco de la convocatoria anual SENNOVA para la formulación y evaluación de proyectos de I+D+i a financiar con recursos de la Ley 344 de 1996, y vigilar el registro de los proyectos que se desarrollen a partir de las capacidades instaladas del Centro de Formación. ', 0, '0000'),
(4, ' Contribuir en el registro y cargue de la información y documentación del proceso Gestión de Evaluación y Certificación de Competencias Laborales, en el Sistema de Información DSNFT. 2. Participar en la transferencia de conocimientos a desarrollarse, relacionada con el proceso Gestión de Evaluación y Certificación de Competencias Laborales. 3. Apoyar la promoción y divulgación de la oferta de evaluación y certificación de competencias laborales, y el análisis de información resultante en las CERTIFICATONES, que incluyan al centro de formación. 4. Apoyar a los evaluadores para propiciar objetividad y transparencia en la recolección de las evidencias. 5. Apoyar, cuando se requiera, al dinamizador de ECCL del centro de formación y a los evaluadores en el registro y cargue de información, evidencias y emisión de juicios en el Sistema de Información DSNFT. 6. Apoyar el envío de información que se solicite desde la Dirección General o de otras instancias dentro o fuera del SENA, teniendo en cuenta los lineamientos establecidos por la Entidad. 7. Apoyar en la organización, clasificación y archivo de la documentación del proceso Gestión de Evaluación y Certificación de Competencias Laborales, de acuerdo con la Tabla de Retención Documental que aplica a los centros de formación profesional. 8. Apoyar la elaboración de actas correspondientes a las reuniones realizadas sobre Evaluación y Certificación de Competencias Laborales y realizar el seguimiento a los compromisos registrados. 9. Apoyar el trámite, elaboración y seguimiento de comunicaciones internas, externas y PQRS del centro ', 0, '0000'),
(5, ' Asegurar la implementación, el mantenimiento y la mejora del sistema de gestión, así como la eficacia de las actividades técnicas del laboratorio, los requisitos legales, reglamentarios y los establecidos en las orientaciones emitidas por SENNOVA y la entidad. 2. Identificar oportunamente la presencia de riesgos, oportunidades y la ocurrencia desviaciones en el sistema de gestión, o de los procedimientos de ensayo/calibración para su reporte, y desarrollar acciones destinadas a prevenir, minimizar o corregir dichos desvíos, de acuerdo con procedimientos documentados. 3. Asegurar el correcto funcionamiento de las operaciones técnicas y desarrollar, verificar o validar los métodos de ensayo/calibración apropiados que satisfagan las necesidades del cliente, incluida la evaluación de su incertidumbre. 4. Realizar las actividades de ensayo/calibración/muestreo y emitir los resultados correspondientes, teniendo en cuenta los procedimiento verificados o validados y los requisitos del cliente, asegurando la validez de los resultados y los tiempos de entrega planeados. 5. Trabajar de manera articulada con el equipo del laboratorio en la implementación, mantenimiento y mejora del Sistema de Gestión e informar oportunamente las novedades que puedan afectar el desarrollo de las actividades programadas. 6. Utilizar adecuadamente los recursos necesarios para asegurar la calidad y el normal funcionamiento de las actividades del laboratorio, de acuerdo con los procedimientos documentados. 7. Apoyar al cumplimiento de los servicios de ensayo/calibración solicitados al laboratorio y gestion', 0, '0000'),
(6, 'Realizar transferencia técnica y pedagógica a los Establecimientos Educativos articulados para que adopten la formación por competencias, proyectos, la normatividad y lineamientos vigente del SENA. 2. Orientar a los Establecimientos Educativos en la planeación y articulación curricular de acuerdo con el procedimiento establecido. 3. Apoyar a las Secretarías de Educación y Establecimientos Educativos, en la configuración y organización de los ambientes de aprendizaje requeridos por el SENA para desarrollar las acciones de formación en programas técnicos. 4. Realizar apoyo con el instructor en la visita técnica a los ambientes de formación y remitir informes a los Establecimientos Educativos. 5. Elaborar el plan operativo anual institucional del programa entre el Centro de Formación con el Establecimiento Educativo articulado, y concertar con el mismo la entrega de información referida para el programa: Informes, formatos y demás solicitados por las Secretarías de Educación y Regionales del SENA según acuerdos establecidos. 6. Apoyar el seguimiento y evaluación al cumplimiento del plan operativo institucional juntamente con el Establecimiento Educativo articulado para garantizar el cumplimiento de las obligaciones estipuladas en el convenio. 7. Efectuar el informe de gestión en cumplimiento de las obligaciones contractuales del programa. 8. Ejercer acompañamiento al proceso de ejecución de la formación que imparten los instructores de manera presencial como a través de los medios digitales de apoyo a la formación dispuestas por el SENA y usadas por los instructores con base e', 0, '0000'),
(7, '1.Apoyar la recepción, verificación, almacenamiento y entrega de los bienes devolutivos, bienes en administración y bienes de consumo entregados por los proveedores. 2.Alistar los bienes muebles, bienes de consumo y equipos que se deben entregar y recibir 3. Agregar la marcación y plaqueteo de bienes de los funcionarios y contratistas del centro de formación. 4. Apoyar en la realización de traspasos entre cuentadantes del centro de formación y el reintegro de los bienes por parte de estos desde la solicitud de traspaso de bienes hasta la legalización de estos. 5. Apoyar la realización de la toma física y realización de los documentos necesarios 6. Apoyar al Centro de formación en la clasificación de bienes servibles e inservibles reintegrados al almacén con el fin de iniciar el proceso de baja 7.Ejecutar de manera idónea el objeto del contrato conforme a los lineamientos del Sistema Integrado de Gestión y Autocontrol (SIGA) del SENA, el cual se encuentra documentado en la plataforma compromiso. 8.Mantener la debida reserva sobre los asuntos manejados y conocidos dentro de la ejecución del contrato. 9.Realizar las demás actividades relacionadas con el objeto del contrato que le sean asignadas por el supervisor y/o el subdirector del centro que correspondan a la naturaleza del contrato.1.Apoyar la recepción, verificación, almacenamiento y entrega de los bienes devolutivos, bienes en administración y bienes de consumo entregados por los proveedores. 2.Alistar los bienes muebles, bienes de consumo y equipos que se deben entregar y recibir 3. Agregar la marcación', 0, '0000'),
(8, '1. Apoyar el seguimiento de metas e indicadores de la Coordinación Misional. 2. Apoyar al\r\nCentro en la elaboración y proyección de informes y documentación administrativa. 3. Apoyar a la Coordinación\r\nMisional en el proceso de Inducción de los aprendices. 4. Apoyo en las actividades de Campesena y Economia\r\nPopular 5. Asistir a la Coordinación Misional en la elaboración de informes y reportes solicitados por el Grupo de\r\nFormación Profesional de la Regional Distrito Capital y el centro de formación según sea requerido respecto de\r\nlos convenios, cadena de formación, procesos de articulación, poblaciones vulnerables y empleo entre otros. 6.\r\nAsistir al supervisor en las actividades de planeación, divulgación, proyección, seguimiento, estructuración y\r\nacompañamiento de los diferentes trámites y gestiones administrativas que se le soliciten 7. Gestionar\r\ninformación en los diferentes aplicativos destinados por la entidad para la administración de datos e información.\r\n8. Apoyar técnicamente los procesos de contratación de centro, según se requiera. 9. Entregar por escrito los\r\ninformes que se le soliciten de las actividades realizadas conforme con el objeto contractual y asistir a las\r\nreuniones y/o comités programados cuando sea requerido o asignado. 10. Ejecutar de manera idónea el objeto\r\ndel contrato conforme a los lineamientos del Sistema Integrado de Gestión y Autocontrol (SIGA) del SENA, el\r\ncual se encuentra documentado en la plataforma compromiso. 11. Mantener la debida reserva sobre los asuntos\r\nmanejados y conocidos dentro de la ejecución del contrato. 12. Realiza', 0, '0000'),
(9, '1. Apoyar la\r\nproyección de la documentación a que haya lugar en las etapas precontractuales, contractuales y post\r\ncontractuales de los procesos de vinculación contractual que adelante el Centro de Formación. 2. Apoyar\r\nal Centro en la elaboración y proyección de informes, actas y demas documentación administrativa que se\r\nrequiera. 3. Apoyar la construcción y seguimiento de los procesos de contratación del centro, según\r\nrequiera la subdirección 4. Apoyar a la oficina de contratación en el manejo de los aplicativos como SECOP\r\nII, Sistema de Información y Gestión del Empleo Público SIGEP II, sus actualizaciones y demás aplicativos\r\ncreados\r\npara la administración de datos e información contractual. 5. Realizar la verificación y seguimiento de la\r\ndocumentación a que haya lugar de las etapas precontractuales, contractuales y post contractuales cuando\r\nla subdirección lo solicite. 6. Gestionar la afiliación de los contratistas ante la aseguradora de riesgos\r\nlaborales ARL que ellos escojan en procesos de contratación o adición y\r\nprórroga. 7 Elaborar los informes que soliciten las dependencias internas del SENA y/o entes de control.\r\n8.Gestionar la afiliación de los contratistas ante la Administradora de Riesgos Profesionales seleccionados\r\npor ellos y remitir la planilla “Y” de pago de aportes de contratistas nivel 4 y 5 en ARL ante la regional 9.\r\nProyectar las certificaciones contractuales solicitadas por el contratista.10. Aplicar los procesos y\r\nprocedimientos establecidos por la entidad, para la gestión documental relacionada con el objeto\r\ncontractual. 11. Realizar l', 0, '0000'),
(10, '1. Apoyar al Centro en la elaboración y\r\nproyección de informes y documentación administrativa. 2. Asistir al supervisor en las actividades de\r\nplaneación, divulgación, proyección, seguimiento, estructuración y acompañamiento de los diferentes\r\ntrámites y gestiones administrativas que se le soliciten. 3.Gestionar información en los diferentes aplicativos\r\ndestinados por la entidad para la administración de datos e información. 4.Atención a los clientes internos\r\ny externos de acuerdo con las políticas del Centro de Formación.5. Registrar actividades de contrato de\r\naprendizaje y las diversas opciones de etapa productiva de los aprendices del centro para la industria de la\r\ncomunicación 6. Entregar por escrito los informes que se le soliciten de las actividades realizadas conforme\r\ncon el objeto contractual y asistir a las reuniones y/o comités programados cuando sea requerido o\r\nasignado. 7. Ejecutar de manera idónea el objeto del contrato conforme a los lineamientos del Sistema\r\nIntegrado de Gestión y Autocontrol (SIGA) del SENA, el cual se encuentra documentado en la plataforma\r\ncompromiso.8. Mantener la debida reserva sobre los asuntos manejados y conocidos dentro de la ejecución\r\ndel contrato. 9. Realizar las demás actividades relacionadas con el objeto del contrato que le sean\r\nasignadas por el supervisor y/o el subdirector del centro que correspondan a la naturaleza del contrato.10.\r\nAplicar los procesos y procedimientos establecidos por la entidad, para la gestión documental relacionada\r\ncon el objeto contractual', 0, '0000'),
(11, '1. Elaborar estudios y análisis de los resultados del centro de formación que sirvan de\r\ninsumo para garantizar la pertinencia y calidad de los servicios institucionales. 2. Generar los reportes e\r\ninformes de cumplimento de las políticas, estrategias, procesos, resultados, planes, programas y proyectos\r\nrequeridos a nivel interno y externo apoyados en herramientas de análisis de datos. 3. Apoyar la\r\nformulación, seguimiento y consolidación del Plan de Acción con la participación de las coordinaciones del\r\ncentro. 4. Apoyar metodológica y técnicamente a las coordinaciones del centro en el análisis de los\r\ninformes de costos, en el marco de la política de gestión presupuestal y eficiencia del gasto público. 5.\r\nRealizar el seguimiento a la ejecución del presupuesto del centro de formación. 6. Apoyar a la\r\nsubdirección de centro en la implementación y seguimiento a las políticas definidas en el Modelo Integrado\r\nde Planeación y Gestión MIPG que corresponden a las temáticas de fortalecimiento organizacional y\r\nsimplificación de procesos, seguridad digital, control interno, y apoyar las estrategias de relación estado\r\nciudadano y demás estrategias en el marco del Modelo Integrado de Planeación y Gestión MIPG. 7.\r\nApoyar y asistir a todas las dependencias del centro en la formulación y/o diseño de las políticas, planes,\r\nprogramas, proyectos, estrategias, con el fin de promover una gestión orientada a resultados. 8.\r\nAcompañar a la subdirección del Centro de formación en el seguimiento y consolidación de los informes de\r\ngestión y desempeño, definidos en el Modelo Integrado de P', 0, '0000'),
(12, '1. Apoyar el seguimiento de las solicitudes\r\ndel centro de formación ingresadas por medios físicos y electrónicos de clientes internos y externos y\r\nbrindar respuesta a las que le sean asignadas 2. Registrar en los aplicativos que señale la entidad los\r\ndocumentos tanto recibidos como producidos que conlleva la gestión del centro de formación. 3. Apoyar\r\nla revisión de documentos allegados a la subdirección por cada una de las áreas del centro, de acuerdo\r\ncon lo establecido en el Sistema Integrado de Gestión y Autocontrol (SIGA). 4. Presentar los informes de\r\ncarácter estadístico respecto de los temas manejados en respuesta y novedades de las solicitudes\r\nteniendo en cuenta la normatividad vigente. 5. Apoyar la revisión de actos administrativos académicos y\r\nlos que sean solicitados por la subdirección del centro de formación. 6. Brindar apoyo en la gestión\r\noportunamente los eventos asignados y llevar la agenda de los compromisos fijados por la subdirección\r\nde centro frente a las demás direcciones 7. Apoyar en la organización, gestión y coordinación servicios\r\nsolicitados al parque automotor del centro de formación. 8. Apoyar en la estructuración y orientación en\r\nlas comunicaciones, documentos, oficios y cartas de clientes internos y externos que ingresan al centro\r\nde formación para su oportuna respuesta y gestión en los aplicativos dispuesto por la entidad. 9. Brindar\r\napoyo en la organización del archivo físico y electrónico de los trámites administrativos desarrollados en\r\nel área y la unidad de correspondencia. 10. Entregar por escrito los informes que se le solici', 0, '0000'),
(13, '1.Asistir y Administrar el rol encargado de certificación del Centro. 2.Asistir la generación\r\nde listado de fichas con estados terminados y disponibles para certificar. 3.Apoyar en la consolidación de\r\nlas novedades de certificación de los aprendices que no se les genera los documentos académicos.\r\n4.Determinar del listado de fichas si la formación es complementaria para consultar aprendices por certificar\r\ny marcar en el aplicativo de la entidad los documentos académicos que pueden ser generados y cuáles no.\r\n5. Determinar del listado de fichas si la formación es titulada para validar los requisitos de certificación en\r\nel aplicativo. 6.Confirmar el cumplimiento de los requisitos establecidos en la citación para la certificación.\r\nprogramados cuando sea requerido o asignado. 7.Solicitar la carga de registros en el aplicativo firmador.\r\n8.Apoyar al subdirector de Centro en el cargue de los documentos académicos en el aplicativo firmador,\r\ngenerar la firma de los documentos académicos y transferir los documentos al aplicativo de la entidad para\r\nla consulta. 9.Apoyar los procesos de gestión de pruebas y matrícula de las convocatorias por demanda\r\nsocial, empresarial y social.10. Apoyar la gestión, seguimiento y respuesta a los requerimientos del cliente\r\ninterno y externo del Centro de Formación 11. Asistir a las reuniones y/o comités programados cuando sea\r\nrequerido o asignado 12. Apoyar la depuración, análisis y gestión de PQRS remitidas a la Coordinación de\r\nAdministración Educativa. 13.Apoyar y garantizar que las novedades presentadas en la verificación de los\r\ndatos b', 0, '0000'),
(14, '1. Apoyar el seguimiento y control al buen funcionamiento de los\r\ndiferentes ambientes de formación en hardware y software y establecer las prioridades en el mantenimiento\r\nde sistemas informáticos. 2. Prestar apoyo técnico y logístico a pruebas de selección de aprendices de\r\nformación titulada presencial en las diferentes fases del proceso en cada uno de los trimestres de la vigencia\r\n3. Apoyar en la logística requerida para el proceso de inducción de aprendices de formación titulada\r\npresencial en las 4 ofertas de la vigencia. 4. Mantener un registro actualizado de las novedades\r\npresentadas en cada uno de los ambientes de formación y reportar de acuerdo a los formatos establecidos\r\nen la plataforma compromiso. 5. Apoyar las diferentes actividades administrativas relacionadas con\r\natención al cliente, registros de información en los aplicativos correspondientes de la Coordinación\r\nAcadémica de acuerdo con lo establecido en el proceso de Gestión de Formación Profesional Integral. 6.\r\nApoyar en la gestión y generación del proceso de carnetización de aprendices de formación titulada\r\npresencial en las 4 ofertas de la vigencia así como instructores y administrativos de acuerdo al\r\nrequerimiento del Centro. 7. Apoyar en la gestión de necesidades de mantenimiento y materiales de\r\nformación para el correcto desarrollo de la formación profesional integral. 8. Apoyar en el acompañamiento\r\ntécnico y asesoramiento a los niveles de soporte básico al personal que atiende a los usuarios finales sobre\r\nlas funcionalidades y el uso adecuado de los servicios e infraestructura TIC. 9. Apoy', 0, '0000'),
(15, '1.Apoyar al\r\nCentro en la elaboración y proyección de informes, documentación y trámites administrativos. 2. Proyectar\r\nlos estudios previos de cada una de las modalidades de selección que utilice el SENA en sus procesos\r\ncontractuales 3. Apoyaren el seguimiento y control previo y posterior a los procesos de pago de los\r\nproveedores; en temas relacionados con, informes de ejecución y facturación de los contratos efectuados\r\ndurante la vigencia presupuestal. 4. Apoyar a la oficina de subdirección en el manejo de los aplicativos\r\ncomo Tienda Virtual del estado colombiano, Sistema de Información y Gestión del Empleo Público SIGEP,\r\nSistema de Información de Contratistas y demás aplicativos creados para la administración de datos e\r\ninformación contractual. 5. Apoyo como estructurador en el registro y seguimiento en el aplicativo SECOP\r\nfrente a los procesos contractuales que realice el centro de formación. 6. Proyectar el análisis jurídico de\r\nlas diferentes situaciones contractuales o administrativas que le solicite la supervisión o subdirección del\r\ncentro de formación. 7. Realizar estudios de mercados, presupuestos y análisis del sector para los procesos\r\ncontractuales de la entidad. 8.Participar en la planeación, programación, organización, ejecución y control\r\nde las actividades contractuales propias requeridas para el apoyo adecuado a las diferentes dependencias.\r\n9. Asistir en la proyección de la documentación a que haya lugar en las etapas precontractuales,\r\ncontractuales y post contractuales de los procesos de vinculación contractual de instructores y\r\nadministrativos', 0, '0000'),
(16, '1. Brindar apoyo en el desarrollo de los procesos misionales de las diferentes\r\náreas del Centro de Formación. 2. Apoyar en la respuesta oportuna a las PQRS interpuestas por la comunidad\r\neducativa, de conformidad con la normativa interna del Sena y demás normas concomitantes que regulan los\r\nprocedimientos administrativos. 3. Generar en Sofía Plus los reportes requeridos por cualquier instancia de la\r\ninstitución. 4. Brindar apoyo en el proceso de revisión de las actas académicas y actos administrativos\r\ncorrespondientes a los Comités de Evaluación y Seguimiento. 5. Gestionar ante las Coordinaciones Académicas\r\nla solicitud de información faltante y de ajustes que se requieran en las actas de Comité y actos administrativos\r\nsegún se requiera. 6.Realizar el registro de la información correspondiente a los aprendices llevados a Comité\r\nde Evaluación y Seguimiento, en las Bases de Datos correspondientes a los procesos académicos de los\r\naprendices del centro de formación. 7. Brindar atención al cliente interno y externo según se requiera. 8. Hacer\r\nseguimiento y llevar la trazabilidad del proceso de los actos administrativos, mediante el registro de la\r\ninformación en las Bases de Datos (DRIVE, SOFIA PLUS). 9. Entregar por escrito los informes que se le soliciten\r\nde las actividades realizadas conforme con el objeto contractual y asistir a las reuniones y/o comités\r\nprogramados cuando sea requerido o asignado. 10. Ejecutar de manera idónea el objeto del contrato conforme\r\na los lineamientos del Sistema Integrado de Gestión y Autocontrol (SIGA) del SENA, el cual se encuentra\r\n', 0, '0000'),
(17, '1. Recibir, analizar y verificar la documentación soporte para el registro\r\ncontable en el sistema de información SIIF nación de contratistas, proveedores, apoyos de sostenimiento,\r\nmonitorias, servicios públicos, impuestos, proveedor Sena-Sena y demás que se requiera. 2. Asistir en la\r\ngeneración de informes contables requeridos por las dependencias del Sena y/o entes de control. 3.\r\nColaborar en la presentación y remitir la conciliación de la cuenta 138413001 – Devolución de IVA Entidades\r\nde Educación Superior- la cual deberá cargarse en el FTP a más tardar los primeros quince días calendario\r\ndel mes siguiente al cierre de cada bimestre de acuerdo a las directrices de la Entidad. 4. Remitir por correo\r\nelectrónico institucional a contabilidad de la Dirección Regional, los primeros quince días calendario del\r\nmes siguiente al cierre del bimestre, el formato de las obligaciones del IVA que quedan pendiente de pago\r\nal cierre de cada bimestre (cuentas por pagar de IVA) de acuerdo a las directrices de la Entidad. 5.\r\nColaborar en la verificación mensual de saldos negativos por terceros o cuantías menores en la cuenta\r\n138413001 – Devolución de IVA Entidades de Educación Superior. 6. Apoyar con oportunidad el registro\r\nde todas las deducciones de impuestos por concepto de retención en la fuente a título de renta, IVA e ICA,\r\nestampillas, contribución de obra pública y estampilla pro-universidad Nacional de Colombia. 7. Efectuar\r\nseguimiento y depuración a los saldos contables reflejados mensualmente por concepto de viáticos, y\r\ncuentas por pagar bienes y servicios. 8. Adelan', 0, '0000'),
(18, '1. Apoyar en el proceso de\r\nasentamiento de matrícula de los aspirantes seleccionados que cumplan con los requisitos establecidos en el\r\ndiseño curricular. 2. Realizar los formularios de las diferentes fichas de las ofertas abiertas y cerradas de las\r\nmodalidades virtual y presencial para realizar las respectivas matriculas de la formación titulada. 3. Tener\r\nactualizado el one drive del correo de matriculas9217@sena.edu.co, con toda la documentación de los\r\naprendices matriculados de las diferentes convocatorias. 4. Apoyar con la elaboración de los formatos requeridos\r\ncuando se aplican pruebas Fase II en las diferentes convocatorias de la vigencia. 5. Apoyar en la logística para\r\nla realización de las Pruebas web controlada y/o taller 6. Apoyar el seguimiento y control permanente a las\r\nactividades del procedimiento de certificación, brigadas de depuración de la información académica y gestión\r\nadministrativa. 7.Asistir al Grupo de Administración educativa en divulgar e informar a la comunidad todo lo\r\nrelacionado con el ingreso a la formación, el manejo del aplicativo de gestión educativa y todo lo referente a los\r\nprogramas ofertados. 8. Apoyar al Centro en la elaboración y proyección de informes y documentación\r\nadministrativa. 9. Apoyar la depuración, análisis y gestión de PQRS. 9. Apoyar la revisión de datos personales\r\nde los aprendices registrados en el aplicativo SOFIA PLUS, antes del proceso de ingreso y/o certificación, de los\r\naprendices en los niveles de formación Titulada y Complementaria. 10. Apoyar la verificación y actualización de\r\ndocumentos de los apren', 0, '0000'),
(19, '1. Gestionar las diferentes actividades administrativas relacionadas con atención al cliente\r\ninterno y externo y registro de información en los aplicativos correspondientes a la Coordinación Académica\r\nde acuerdo con lo establecido en el proceso de Gestión de Formación Profesional Integral. 2. Apoyar en el\r\nproceso administrativo y documental de supervisión de contratos de servicios personales y bienes y\r\nservicios asignados a la coordinación académica. 3. Tramitar la información necesaria para dar respuesta\r\na las PQRS relacionadas con la formación profesional integral y que sean competencia de la Coordinación\r\nAcadémica teniendo en cuenta la promesa de valor institucional. 4. Apoyar la depuración de las fichas de\r\nformación a cargo de la Coordinación, según requerimientos presentados. 5. Gestionar el proceso de\r\nnovedades de aprendices hasta el reporte a la Coordinación de Formación Profesional del Centro. 6. Apoyar\r\na la Coordinación académica en lo relacionado con el sistema de gestión documental y los demás procesos\r\nque hacen parte de la gestión de la formación profesional integral. 7. Revisar y actualizar los indicadores\r\nde gestión asignados a la Coordinación Académica con las respectivas evidencias. 8. Verificar el registro\r\nde juicios evaluativos de la formación profesional integral en el aplicativo Sofia Plus según lineamientos\r\ninstitucionales y avance del proceso formativo. 9.Ejecutar de manera idónea el objeto del contrato conforme\r\na los lineamientos del Sistema Integrado de Gestión y Autocontrol (SIGA) del SENA, el cual se encuentra\r\ndocumentado en la plata', 0, '0000'),
(20, '1.Diseñar el Plan de trabajo general de los proyectos de servicios tecnológicos financiados en el centro de\r\nformación con metas, actividades, productos, resultados, impactos esperados y cronograma que aseguren la\r\nejecución del proyecto avalado para la vigencia y el apoyo al cumplimiento de los lineamientos de la entidad,\r\nlineamientos de SENNOVA, Lineamientos de la Estrategia de Servicios Tecnológicos, lineamientos\r\ndel Sistema unificado de Gestión Documental SENNOVA, Plan de Acción, Plan estratégico Institucional u\r\notro que aplique a la tipología del servicio. 2. Liderar la divulgación y oferta de servicios del portafolio de\r\nServicios Tecnológicos, la atención de usuarios (internos y externos) y el fomento de la I+D+i. 3. Identificar\r\noportunamente los riesgos, las oportunidades y la ocurrencia de desviaciones en el sistema de gestión, o de los\r\nprocedimientos técnicos para su gestión y reporte, y desarrollar las acciones destinadas a prevenir, minimizar o\r\ncorregir dichos desvíos, de acuerdo con los procedimientos documentados del laboratorio. 4. Asegurar la\r\nactualización del portafolio de servicios tecnológicos en las bases de datos definidas por la dirección general. 5.\r\nCumplir la normativa, reglamentaciones, lineamientos, políticas que direccionan el que hacer del laboratorio y\r\nlas metas establecidas en los indicadores definidos por la Dirección. 6. Liderar la articulación del portafolio\r\nde Servicios Tecnológicos con las demás líneas SENNOVA y los programas de formación del centro al que\r\npertenece. 7. Informar a la Subdirección del Centro acerca del desempeño ', 0, '0000'),
(21, '1. Gestionar y registrar la programación de\r\nambientes siguiendo la guía de procedimientos y documentos de orientación de la Dirección de Formación\r\nProfesional y demás lineamientos que indique la entidad de acuerdo a la programación realizada por las\r\ncoordinaciones académicas del Centro de Formación. 2. Apoyar y procesar en el aplicativo de gestión académica\r\ninstitucional, en los siguientes aspectos: a) Asociación fichas por programación y reprogramación de\r\ncompetencias técnicas y transversales b) Asociación de los resultados de aprendizaje de las fichas asignadas a\r\nlos instructores d) Creación de la ruta de formación de las fichas asignadas a los instructores. 3. Gestionar el\r\nregistro de información de acuerdo a la programación de la formación profesional de cada una de las fichas\r\nactivas en la presente vigencia y el cargue de horas de los instructores de planta y contrato. 4. Preparar informes\r\nperiódicos de las horas registradas en la plataforma sofia, así como dar respuesta a los requerimientos de la\r\ndirección regional o dirección general frente al registro de la programación de instructores de planta y de contrato.\r\n5. Apoyar a la Coordinación Académica presencial en la realización de Comités de Evaluación y Seguimiento\r\nhasta la elaboración de los actos administrativos. 6. Ejecutar de manera idónea el objeto del contrato conforme\r\na los lineamientos del Sistema Integrado de Gestión y Autocontrol (SIGA) del SENA, el cual se encuentra\r\ndocumentado en la plataforma compromiso. 7. Mantener la debida reserva sobre los asuntos manejados\r\ny conocidos dentro de la eje', 0, '0000'),
(22, '1.Apoyar la planeación y publicación de las ofertas educativas por demanda social y especiales (empresariales,\r\nsociales, ampliación de cobertura y articulación con la media) 2. Apoyar la planeación de ingreso y gestión de\r\npruebas de las ofertas educativas que el Centro de formación participe 3. Apoyar a la realización de las pruebas\r\nFase I y II de acuerdo al cronograma establecido. 4. Apoyar la convocatoria a matricula de aspirantes\r\nseleccionados de acuerdo a requisitos de ingreso 5. Apoyar la recepción y verificación de documentación del\r\naspirante convocado al programa de formación. 6) Realizar el asentamiento de matrícula por los medios físicos\r\ny electrónicos dispuestos. 7) Realizar la actualización de la información básica de aprendices y restablecimiento\r\nde las contraseñas en el aplicativo Sena Sofía Plus. 8. Gestionar planes y estrategias de mejoramiento que\r\natiendan de manera integral los resultados de los cruces de información con la Registraduría Nacional del Estado\r\nCivil y los reportes periódicos que remite la Dirección de Formación Profesional. 9) Realizar seguimientos\r\nperiódicos de la ejecución del Centro para que se refleje en los reportes oficiales de planeación. 10) Realizar la\r\nformalización de los procesos de Administración Educativa en el aplicativo Sofía plus que se deriven de los\r\nconvenios de ampliación de cobertura y otros de carácter especial suscritos por la Dirección Regional. 11.Apoyar\r\nla gestión, seguimiento y respuesta a los requerimientos del cliente interno y externo del Centro de Formación.\r\n12. Asistir a las reuniones y/o comités pr', 0, '0000'),
(23, '1.Gestionar las diferentes actividades administrativas relacionadas con\r\natención al cliente interno y externo y registro de información en los aplicativos correspondientes a la\r\nCoordinación Académica de acuerdo con lo establecido en el proceso de Gestión de Formación Profesional\r\nIntegral. 2. Tramitar la información necesaria para dar respuesta a las PQRS y/o CRM relacionadas con la\r\nformación profesional integral y que sean de la competencia de la Coordinación Académica teniendo en cuenta\r\nla promesa de valor institucional. 3. Apoyar las acciones definidas por la coordinación académica para realizar\r\nla depuración periódica y oportuna de las fichas activas, que garantice el estado actualizado de los aprendices\r\npertenecientes a las mismas, según procesos, procedimientos, acuerdos, debido proceso y/o circulares\r\ninstitucionales. 4. Apoyar la implementación de estrategias y acciones definidas por la coordinación académica\r\npara la ejecución, control y retención escolar en aprendices de formación titulada virtual en etapa lectiva,\r\ngenerando alertas tempranas a la coordinación académica en caso de presentarse riesgo de deserción, o que\r\nla participación en los procesos formativos sea baja o nula. 5. Apoyar a la Coordinación Académica en la\r\norganización y realización de Comités de Evaluación y Seguimiento, hasta la elaboración de los actos\r\nacadémicos y/o administrativos que surjan del proceso, y el control de la correcta aplicación en el sistema de\r\ninformación por parte del rol competente. 6. Realizar el proceso de novedades de aprendices hasta la generación\r\nde los actos', 0, '0000'),
(24, '1. Brindar apoyo en la identificación, planeación y ejecución de\r\ntransferencias de conocimiento en los temas técnicos relacionados con el modelo de operación SIGA\r\ndirigidas a los funcionarios y contratistas del Centro de formación. Y participar activamente en las\r\ntransferencias de conocimiento impartidas por el Despacho Regional y la Dirección General con relación al\r\nmodelo de operación del SIGA. 2. Acompañar la planeación para la ejecución de las actividades del SIGA\r\nestablecidas en el plan anual de mantenimiento PAM en su Centro de formación y sedes adscritas. 3. Asistir\r\nen la realización de los ejercicios de evaluación del desempeño por dependencias y de rendición de cuentas\r\na la ciudadanía y la consolidación de informes de gestión requeridos por la entidad y entes de control\r\nrelacionados con el modelo de operación del SIGA. 4. Dar acompañamiento en la ejecución de las\r\nactividades establecidas en el Plan anual de mantenimiento para la implementación, seguimiento y mejora\r\ndel modelo de operación SIGA. 5. Apoyar la programación, realización y documentación de las visitas de\r\nverificación, auditorías internas a las instalaciones de las sedes a cargo o que sean designadas desde la\r\nDirección General. 6.Efectuar el seguimiento a la ejecución de las actividades establecidas en el Plan\r\nanual de mantenimiento para la implementación, seguimiento y mejora del modelo de operación SIGA. 7.\r\nApoyar en el seguimiento, medición, análisis y evaluación del modelo de operación del SIGA y asistir a la\r\nalta dirección en la formulación de estrategias de la mejora continua a travé', 0, '0000'),
(25, '1. Orientar y acompañar en forma permanente e integral los aprendices en el área, las\r\ncompetencias, resultados de aprendizaje y actividades en etapa lectiva y/o productiva de los proyectos de\r\nformación y/o proyectos productivos programados dentro de los tiempos que para cada acción de formación se\r\ndetermine por el Centro, correspondientes a la línea y red tecnológica de acuerdo a su perfil. 2. Reportar en el\r\naplicativo Sofía Plus en un plazo máximo de tres (3) días todas las actividades de acuerdo con los procesos que\r\nson de su responsabilidad, garantizando la calidad de la información y su coherencia en el proceso formativo,\r\ntales como: a. registro de juicios evaluativos. b. asociación de aprendices a la ruta de formación. c. Comunicar\r\nal Coordinador Académico oportunamente anomalías, inconsistencias, novedades de aprendices y hallazgos en\r\nel registro de la información, así como demás informes dentro de los plazos estipulados por el centro para tal\r\nefecto conforme a los lineamientos del Sistema Integrado de Gestión (SIG) del SENA el cual se encuentra\r\ndocumentado en la plataforma CompromISO. 3. Participar en la programación y ejecución del proceso de\r\ninducción de aprendices de formación titulada. 4. Responder por la integridad y buen uso de materiales, equipos\r\ny demás elementos de la institución puestos bajo su cuidado para desarrollar su objeto contractual. 5. Mantener\r\nel debido respeto por la dignidad, intimidad e integridad de los miembros de la comunidad educativa, así como\r\nguardar lealtad a la Institución, actuando de buena fe y conservando la debida rese', 0, '0000'),
(26, '1. Orientar y acompañar en forma permanente e integral los aprendices en el área, las\r\ncompetencias, resultados de aprendizaje y actividades en etapa lectiva y/o productiva de los proyectos de\r\nformación y/o proyectos productivos programados dentro de los tiempos que para cada acción de formación se\r\ndetermine por el Centro, correspondientes a la línea y red tecnológica de acuerdo a su perfil. 2. Reportar en el\r\naplicativo Sofía Plus en un plazo máximo de tres (3) días todas las actividades de acuerdo con los procesos que\r\nson de su responsabilidad, garantizando la calidad de la información y su coherencia en el proceso formativo,\r\ntales como: a. registro de juicios evaluativos. b. asociación de aprendices a la ruta de formación. c. Comunicar\r\nal Coordinador Académico oportunamente anomalías, inconsistencias, novedades de aprendices y hallazgos en\r\nel registro de la información, así como demás informes dentro de los plazos estipulados por el centro para tal\r\nefecto conforme a los lineamientos del Sistema Integrado de Gestión (SIG) del SENA el cual se encuentra\r\ndocumentado en la plataforma CompromISO. 3. Participar en la programación y ejecución del proceso de\r\ninducción de aprendices de formación titulada. 4. Responder por la integridad y buen uso de materiales, equipos\r\ny demás elementos de la institución puestos bajo su cuidado para desarrollar su objeto contractual. 5. Mantener\r\nel debido respeto por la dignidad, intimidad e integridad de los miembros de la comunidad educativa, así como\r\nguardar lealtad a la Institución, actuando de buena fe y conservando la debida rese', 0, '0000'),
(27, '1. Orientar y acompañar en forma permanente e integral los\r\naprendices en el área, las competencias, resultados de aprendizaje y actividades en etapa lectiva y/o productiva\r\nde los proyectos de formación y/o proyectos productivos programados dentro de los tiempos que para cada\r\nacción de formación se determine por el Centro, correspondientes a la línea y red tecnológica de acuerdo a su\r\nperfil. 2. Reportar en el aplicativo Sofía Plus en un plazo máximo de tres (3) días todas las actividades de\r\nacuerdo con los procesos que son de su responsabilidad, garantizando la calidad de la información y su\r\ncoherencia en el proceso formativo, tales como: a. registro de juicios evaluativos. b. asociación de aprendices a\r\nla ruta de formación. c. Comunicar al Coordinador Académico oportunamente anomalías, inconsistencias,\r\nnovedades de aprendices y hallazgos en el registro de la información, así como demás informes dentro de los\r\nplazos estipulados por el centro para tal efecto conforme a los lineamientos del Sistema Integrado de Gestión\r\n(SIG) del SENA el cual se encuentra documentado en la plataforma CompromISO. 3. Participar en la\r\nprogramación y ejecución del proceso de inducción de aprendices de formación titulada. 4. Responder por la\r\nintegridad y buen uso de materiales, equipos y demás elementos de la institución puestos bajo su cuidado para\r\ndesarrollar su objeto contractual. 5. Mantener el debido respeto por la dignidad, intimidad e integridad de los\r\nmiembros de la comunidad educativa, así como guardar lealtad a la Institución, actuando de buena fe y\r\nconservando la debida res', 0, '0000'),
(28, ' 1. Orientar y acompañar en forma permanente e integral los aprendices en el área, las\r\ncompetencias, resultados de aprendizaje y actividades en etapa lectiva y/o productiva de los proyectos de\r\nformación y/o proyectos productivos programados dentro de los tiempos que para cada acción de formación se\r\ndetermine por el Centro, correspondientes a la línea y red tecnológica de acuerdo a su perfil. 2. Reportar en el\r\naplicativo Sofía Plus en un plazo máximo de tres (3) días todas las actividades de acuerdo con los procesos que\r\nson de su responsabilidad, garantizando la calidad de la información y su coherencia en el proceso formativo,\r\ntales como: a. registro de juicios evaluativos. b. asociación de aprendices a la ruta de formación. c. Comunicar\r\nal Coordinador Académico oportunamente anomalías, inconsistencias, novedades de aprendices y hallazgos en\r\nel registro de la información, así como demás informes dentro de los plazos estipulados por el centro para tal\r\nefecto conforme a los lineamientos del Sistema Integrado de Gestión (SIG) del SENA el cual se encuentra\r\ndocumentado en la plataforma CompromISO. 3. Participar en la programación y ejecución del proceso de\r\ninducción de aprendices de formación titulada. 4. Responder por la integridad y buen uso de materiales, equipos\r\ny demás elementos de la institución puestos bajo su cuidado para desarrollar su objeto contractual. 5. Mantener\r\nel debido respeto por la dignidad, intimidad e integridad de los miembros de la comunidad educativa, así como\r\nguardar lealtad a la Institución, actuando de buena fe y conservando la debida res', 0, '0000'),
(29, '1. Orientar y acompañar en forma permanente e integral los aprendices en el área, las\r\ncompetencias, resultados de aprendizaje y actividades en etapa lectiva y/o productiva de los proyectos de\r\nformación y/o proyectos productivos programados dentro de los tiempos que para cada acción de formación se\r\ndetermine por el Centro, correspondientes a la línea y red tecnológica de acuerdo a su perfil. 2. Reportar en el\r\naplicativo Sofía Plus en un plazo máximo de tres (3) días todas las actividades de acuerdo con los procesos que\r\nson de su responsabilidad, garantizando la calidad de la información y su coherencia en el proceso formativo,\r\ntales como: a. registro de juicios evaluativos. b. asociación de aprendices a la ruta de formación. c. Comunicar\r\nal Coordinador Académico oportunamente anomalías, inconsistencias, novedades de aprendices y hallazgos en\r\nel registro de la información, así como demás informes dentro de los plazos estipulados por el centro para tal\r\nefecto conforme a los lineamientos del Sistema Integrado de Gestión (SIG) del SENA el cual se encuentra\r\ndocumentado en la plataforma CompromISO. 3. Participar en la programación y ejecución del proceso de\r\ninducción de aprendices de formación titulada. 4. Responder por la integridad y buen uso de materiales, equipos\r\ny demás elementos de la institución puestos bajo su cuidado para desarrollar su objeto contractual. 5. Mantener\r\nel debido respeto por la dignidad, intimidad e integridad de los miembros de la comunidad educativa, así como\r\nguardar lealtad a la Institución, actuando de buena fe y conservando la debida rese', 0, '0000'),
(30, ' 1. Orientar y acompañar en forma permanente e integral los aprendices en el área, las\r\ncompetencias, resultados de aprendizaje y actividades en etapa lectiva y/o productiva de los proyectos de\r\nformación y/o proyectos productivos programados dentro de los tiempos que para cada acción de formación se\r\ndetermine por el Centro, correspondientes a la línea y red tecnológica de acuerdo a su perfil. 2. Reportar en el\r\naplicativo Sofía Plus en un plazo máximo de tres (3) días todas las actividades de acuerdo con los procesos que\r\nson de su responsabilidad, garantizando la calidad de la información y su coherencia en el proceso formativo,\r\ntales como: a. registro de juicios evaluativos. b. asociación de aprendices a la ruta de formación. c. Comunicar\r\nal Coordinador Académico oportunamente anomalías, inconsistencias, novedades de aprendices y hallazgos en\r\nel registro de la información, así como demás informes dentro de los plazos estipulados por el centro para tal\r\nefecto conforme a los lineamientos del Sistema Integrado de Gestión (SIG) del SENA el cual se encuentra\r\ndocumentado en la plataforma CompromISO. 3. Participar en la programación y ejecución del proceso de\r\ninducción de aprendices de formación titulada. 4. Responder por la integridad y buen uso de materiales, equipos\r\ny demás elementos de la institución puestos bajo su cuidado para desarrollar su objeto contractual. 5. Mantener\r\nel debido respeto por la dignidad, intimidad e integridad de los miembros de la comunidad educativa, así como\r\nguardar lealtad a la Institución, actuando de buena fe y conservando la debida res', 0, '0000');
INSERT INTO `obligacionesespecificas` (`id`, `nombre`, `idObjeto`, `año`) VALUES
(31, '1. Presentar para aprobación por parte del supervisor del contrato, un plan de\r\ntrabajo que incluya cronograma y entregables. 2. Identificar, generar y evaluar, estrategias orientadas a la retención\r\nde los aprendices dentro del alcance del objeto contractual, articulando con el equipo que adelanta acciones del plan\r\nde bienestar y grupos internos del Centro de formación, el desarrollo de mecanismos que mejoren la retención de\r\naprendices. 3. Desarrollar las actividades del objeto contractual en las diferentes modalidades de formación que\r\naplique para el Centro de Formación acompañando la programación académica, según lineamientos institucionales.\r\n4. Formular e implementar estrategias para el desarrollo de habilidades blandas en los aprendices del centro de\r\nformación de las diferentes modalidades: presencial, virtual y a distancia, que permitan mejorar sus capacidades de\r\nafrontamiento a las situaciones de la vida cotidiana. 5. Asistir al supervisor en las actividades de planeación,\r\ndivulgación, proyección, seguimiento, estructuración y acompañamiento de los diferentes trámites y gestiones\r\nadministrativas que se le soliciten. 6. Realizar acciones orientadas a la Implementación de la política de atención a\r\npersonas con discapacidad, la política de atención con enfoque pluralista y diferencial. 7. Generar estrategias de\r\ndivulgación permanentes de las actividades a desarrollar, dentro de su objeto contractual. Orientando y hacer\r\nseguimiento a las estrategias para el desarrollo de la cultura institucional, ciudadana, digital y ambiental, que incentiven\r\nel cumplimiento ', 0, '0000'),
(32, '1.Apoyar y supervisar el proceso de préstamo de equipos\r\naudiovisuales a aprendices e instructores u otros usuarios autorizados y mantener un registro preciso de los\r\npréstamos y devoluciones de los mismos. 2. Establecer políticas y procedimientos para el préstamo de equipos\r\ny garantizar su cumplimiento. 3.Proporcionar capacitación a los usuarios finales sobre el uso adecuado de los\r\nequipos y ofrecer asistencia técnica y apoyo durante los eventos o sesiones de formación que requieran equipos\r\naudiovisuales. 4.Realizar seguimiento al inventario de equipos audiovisuales, mantenerlo actualizado y coordinar\r\nrevisiones periódicas para asegurar la exactitud de los registros. 5.Implementar medidas de seguridad para\r\nprevenir pérdidas, robos o daños a los equipos 6.Prestar apoyo logístico en los eventos que realice el Centro\r\nde Formación dentro o fuera de sus instalaciones. 7. Hacer y coordinar el recorrido por los ambientes con el fin\r\nde revisar el estado de los mismos y los equipos instalados al inicio de los procesos de formación de acuerdo a\r\nlas franjas establecidas por la coordinación académica del Centro de Formación. 8. Apoyar técnicamente los\r\nprocesos de contratación del Centro, según se requiera. 9.Ejecutar de manera idónea el objeto del contrato\r\nconforme a los lineamientos del Sistema Integrado de Gestión y Autocontrol (SIGA) del SENA, el cual se\r\nencuentra documentado en la plataforma compromiso. 10.Mantener la debida reserva sobre los asuntos\r\nmanejados y conocidos dentro de la ejecución del contrato. 11. Realizar las demás actividades relacionadas\r\ncon el objet', 0, '0000'),
(33, '1.Proyectar los estudios previos y documentación a que haya lugar de cada una de las modalidades de selección\r\ny sus etapas precontractuales, contractuales y post contractuales que utilice el SENA en sus procesos\r\ncontractuales 2. Apoyar en el seguimiento y control previo y posterior a los procesos de pago de los proveedores;\r\nen temas relacionados con, informes de ejecución y facturación de los contratos efectuados durante la vigencia\r\n2023. 3. Apoyar la publicación de los procesos contractuales en las plataformas establecidas por Colombia\r\nCompra para la celebración de contratos del Centro de Formación. 4. Realizar estudios de mercados,\r\npresupuestos y análisis del sector para los procesos contractuales de la entidad. 5. Elaborar reportes e informes\r\nde carácter técnico y estadístico del proceso de gestión contractual, con el propósito de evidenciar la gestión\r\nrealizada en el proceso 6. Realizar acciones de gestión y seguimiento al cumplimiento de la ejecución de los\r\nprocesos de adquisición de los bienes, servicios personales directos e indirectos a contratar por parte de la\r\nentidad. 7. Apoyar las actualizaciones o modificaciones del Plan Anual de Adquisiciones 8. Mantener la debida\r\nreserva sobre los asuntos manejados y conocidos dentro de la ejecución del contrato. 9. Ejecutar de manera\r\nidónea el objeto del contrato conforme a los lineamientos del Sistema Integrado de Gestión y Autocontrol (SIGA)\r\ndel SENA, el cual se encuentra documentado en la plataforma compromiso. 10. Apoyar en las actividades de\r\nplaneación propias del Centro de formación con el fin de dar cump', 0, '0000'),
(34, '1. Apoyar el trámite de actividades administrativas de talento humano del centro. 2. Apoyar\r\nen la realización oportuna y adecuada aplicación de los procesos de seguimiento, evaluación del desempeño\r\nlaboral y calificación de los funcionarios del Centro de Formación y reporte oportuno de información. 3.Apoyar\r\nen la coordinación y tramite, ejecutar de las situaciones administrativas de los servidores públicos del Centro de\r\nFormación, su ingreso, permanencia y retiro, así como proyectar los actos administrativos correspondientes. 4.\r\nClasificar, organizar, actualizar, custodiar y controlar los archivos físicos y magnéticos de los servidores públicos\r\nactivos y retirados del Centro de Formación, cumpliendo con lo establecido en las tablas de retención\r\ndocumental, la ficha técnica y los procedimientos dispuestos en el aplicativo compromiso. 5. Acompañar las\r\njornadas de Inducción o entrenamiento en el puesto de trabajo y reinducción. 6. Realizar el seguimiento a las\r\nacciones de capacitación para el personal de planta de la entidad y verificar el cumplimiento de las acciones de\r\ncapacitación. 7. Promover las actividades relacionadas con el programa de Bienestar social e incentivos y Cultura\r\nInstitucional. 8. Apoyar el proceso de compra de la dotación y ropa de trabajo para los funcionarios del Centro\r\nde Formación. 9. Apoyo en la elaboración de informes de gestión y demás que son propios del área de Talento\r\nhumano solicitados por las diferentes dependencias 10. Apoyar la realización de actividades dinámicas,\r\nintegración, inducción y reinducción del personal del centro. 11', 0, '0000'),
(35, '1. Apoyar la administración de los procesos del almacén e inventario del centro\r\n2. Brindar asistencia en el alistamiento y entrega de elementos de consumo y devolutivos del centro de\r\nformación. 3. Gestionar la información de las notas de ingreso y de salida de los elementos de consumo y\r\ndevolutivos del centro de formación en los aplicativos dispuestos por la entidad. 4. Apoyar en los traspasos entre\r\ncuentadantes del centro de formación y el reintegro de los bienes por parte de los mismos desde la solicitud de\r\ntraspaso de bienes hasta la legalización de los mismos. 5. Brindar apoyo en el respectivo reintegro de bienes\r\nservibles e inservibles de inventarios de los cuentadantes solicitantes del centro. 6. Apoyar en la toma física y/o\r\nvirtual de bienes devolutivos que los servidores públicos del centro de formación tengan a su cargo. 7. Apoyar\r\nal centro de formación en el proceso de bajas conforme a los lineamientos establecidos por la Entidad. 8. Apoyar\r\nen la recepción, verificación y almacenamiento de los bienes de consumo y devolutivos del centro de formación\r\nentregados por los proveedores. 9. Gestionar los informes periódicos ante las dependencias que lo requieran, o\r\na solicitud del supervisor del contrato. 10. Mantener la información organizada, actualizada y completa de los\r\nelementos en bodega de devolutivos, consumo y reintegrados, utilizando los aplicativos sistemas de información\r\nestablecidos por la Entidad. 11. Ejecutar de manera idónea el objeto del contrato, conforme a los lineamientos\r\ndel Sistema Integrado de Gestión y Autocontrol (SIGA) del SENA el c', 0, '0000'),
(36, '1. Apoyar y supervisar el proceso de préstamo de equipos\r\naudiovisuales a aprendices e instructores u otros usuarios autorizados y mantener un registro preciso de los\r\npréstamos y devoluciones de los mismos. 2. Establecer políticas y procedimientos para el préstamo de equipos\r\ny garantizar su cumplimiento. 3. Proporcionar capacitación a los usuarios finales sobre el uso adecuado de\r\nlos equipos y ofrecer asistencia técnica y apoyo durante los eventos o sesiones de formación que requieran\r\nequipos audiovisuales. 4. Realizar seguimiento al inventario de equipos audiovisuales, mantenerlo\r\nactualizado y coordinar revisiones periódicas para asegurar la exactitud de los registros. 5. Implementar\r\nmedidas de seguridad para prevenir pérdidas, robos o daños a los equipos 6.Prestar apoyo logístico en los\r\neventos que realice el Centro de Formación dentro o fuera de sus instalaciones. 7.Hacer y coordinar el recorrido\r\npor los ambientes con el fin de revisar el estado de los mismos y los equipos instalados al inicio de los procesos\r\nde formación de acuerdo a las franjas establecidas por la coordinación académica del Centro de Formación.\r\n8.Apoyar técnicamente los procesos de contratación del Centro, según se requiera. 9.Ejecutar de manera idónea\r\nel objeto del contrato conforme a los lineamientos del Sistema Integrado de Gestión y Autocontrol (SIGA) del\r\nSENA, el cual se encuentra documentado en la plataforma compromiso. 10Mantener la debida reserva sobre los\r\nasuntos manejados y conocidos dentro de la ejecución del contrato. 11. Realizar las demás actividades\r\nrelacionadas con el obje', 0, '0000'),
(37, '1. Apoyar la gestión y elaboración de cotizaciones\r\ny solicitudes de productos gráficos de forma precisa y oportuna a clientes internos o externos realizadas por\r\nlas diferentes instancias, centros de formación o regionales del SENA a nivel nacional. 2.Generar y gestionar\r\nel envío de facturas de forma precisa y oportuna a clientes internos o externos por los servicios y productos\r\ngráficos proporcionados. 3.Realizar un seguimiento de los pagos realizados por los clientes internos y\r\nexternos, coordinar con la dirección general el correcto registro de los mismos y apoyar en la solución de las\r\ndiferentes situaciones que se presenten frente a dicha actividad. 4.Revisar y actualizar los indicadores de\r\ngestión asignados a la producción de centros con las respectivas evidencias y elaborar los informes\r\nsolicitados de acuerdo a los requerimientos de las diferentes instancias de la dirección regional o dirección\r\ngeneral del SENA. 5.Elaborar actas resultantes del comité de precios de manera trimestral y/o de acuerdo a\r\nlos requerimientos del centro de formación. 6.Ejecutar de manera idónea el objeto del contrato conforme a\r\nlos lineamientos del Sistema Integrado de Gestión y Autocontrol (SIGA) del SENA, el cual se encuentra\r\ndocumentado en la plataforma compromiso. 7.Mantener la debida reserva sobre los asuntos manejados y\r\nconocidos dentro de la ejecución de contrato. 8.Adelantar la entrega física y documental del almacén del\r\nCentro para la Industria de la Comunicación Gráfica a la persona indicada por la subdirección en los meses\r\nenero, febrero y marzo de 2024 para lo cual d', 0, '0000'),
(38, '1.Analizar, diagnosticar, registrar trazabilidad y resolver, los casos presentados de la\r\nplataforma LMS y demás sistemas conexos que se reciban desde los diferentes canales disponibles para el\r\nsoporte técnico, administrativo y funcional, que se gestiona desde el Grupo de la Oferta, la Ejecución y la\r\nCertificación de la Formación o grupo encargado desde la Dirección de Formación Profesional acorde a los\r\nprotocolos y lineamientos establecidos. 2. Escalar a las instancias respectivas, los casos que requieren atención\r\nespecializada, así como, realizar el seguimiento, cierre y documentación de los casos acorde a los protocolos y\r\nlineamientos establecidos. 3. Brindar transferencias de conocimiento según necesidades identificadas en\r\nreferencia a la plataforma virtual de formación (LMS), el sistema de soporte técnico de LMS SENA y, demás\r\nsistemas conexos, de acuerdo con las directrices y programación establecidas desde el Grupo de la Oferta, la\r\nEjecución y la Certificación de la Formación o grupo encargado desde la Dirección de Formación Profesional.\r\n4. Realizar gestión de usuarios, cursos, enrolamientos, semillas, comunidad virtual y demás acciones técnicas,\r\nadministrativas y funcionales requeridas en el LMS y los sistemas utilizados para el acompañamiento y soporte\r\nde la ejecución de formación virtual requeridos desde el Grupo de la Oferta, la Ejecución y la Certificación de la\r\nFormación o grupo encargado desde la Dirección de Formación Profesional. 5. Realizar la creación, revisión y\r\nactualización de manuales, guías, protocolos, y demás recursos de apoyo al uso del', 0, '0000'),
(39, '1. Formular e implementar estrategias para el desarrollo de habilidades blandas en los\r\naprendices del centro de formación, que mejoren sus capacidades de afrontamiento a las situaciones de la vida\r\ncotidiana. 2.Participar en la formulación del plan de bienestar al aprendiz del Centro de formación según\r\nnormatividad vigente. 3.Apoyar estrategias para la orientación de los aprendices en temas relacionados con la\r\nsalud física y mental que puedan afectar la permanencia del aprendiz en su proceso formativo. 4.Apoyar\r\nacciones orientadas al fortalecimiento del liderazgo de los aprendices en especial de los representantes de\r\naprendices y voceros. 5.Articular con los demás profesionales que ejecutan el plan de bienestar del centro\r\nestrategias o campañas orientadas a fomentar en los aprendices, actitudes positivas frente a su ser, su proyecto\r\nde vida, su formación y la convivencia ciudadana. 6.Articular con el equipo que adelanta acciones del plan de\r\nbienestar, así como con los grupos internos del Centro de formación, para apoyar el desarrollo de mecanismos\r\npara la retención de aprendices, la implementación de la política de atención a personas con discapacidad, la\r\npolítica de atención con enfoque pluralista y diferencial, la inducción de aprendices, la divulgación y evaluación\r\ndel plan de bienestar al aprendiz. 7. Realizar informes, reportes u otros documentos asociados a las actividades\r\nrelacionadas con su objeto contractual y obligaciones. 8. Aplicar los procesos y procedimientos establecidos por\r\nla entidad, para la gestión documental relacionada con el objeto contrac', 0, '0000'),
(40, '1. Formular e implementar actividades lúdicas y deportivas que involucren la participación de\r\nlos aprendices en jornadas intercentros e intercentros donde se promuevan los valores. 2. Desarrollar estrategias\r\nque fomenten el desarrollo de la actividad física y el aprovechamiento del tiempo libre, desde lo grupal e\r\nindividual, buscando sensibilizar a los aprendices sobre los beneficios de desarrollar actividad física en el\r\nsostenimiento de una vida saludable. 3. Apoyar la gestión de espacios y recursos requeridos para el desarrollo\r\nde las actividades físicas y deportivas que se formulen. 4. Articular con los demás profesionales responsables\r\nde la ejecución del plan de bienestar estrategias o campañas que vinculen la actividad física y los hábitos de\r\nvida saludables, orientadas a fomentar en los aprendices, actitudes positivas frente a su ser, su proyecto de vida,\r\nsu formación y la convivencia ciudadana. 5. Participar en la formulación del plan de bienestar al aprendiz del\r\nCentro de formación según normatividad vigente. 6. Articular con el equipo que adelanta acciones del plan de\r\nbienestar, así como con los grupos internos del Centro de formación, para apoyar el desarrollo de mecanismos\r\npara la retención de aprendices, la implementación de la política de atención a personas con discapacidad, la\r\npolítica de atención con enfoque pluralista y diferencial, la inducción de aprendices, la divulgación y evaluación\r\ndel plan de bienestar al aprendiz. 7. Realizar informes, reportes u otros documentos asociados a las actividades\r\nrelacionadas con su objeto contractual y obli', 0, '0000'),
(41, '1. Presentar para aprobación por parte del supervisor del contrato, un plan de trabajo que incluya cronograma y entregables.\r\n2. Identificar, generar y evaluar, estrategias orientadas a la retención de los aprendices dentro del alcance del\r\nobjeto contractual, articulando con el equipo que adelanta acciones del plan de bienestar y grupos internos del\r\nCentro de formación, el desarrollo de mecanismos que mejoren la retención de aprendices. 3. Desarrollar las\r\nactividades del objeto contractual en las diferentes modalidades de formación que aplique para el Centro de\r\nFormación y acompañar la programación académica, según lineamientos institucionales. 4. Participar en la\r\nejecución de actividades que permitan el desarrollo de actitudes y habilidades sociales como responsabilidad,\r\ncumplimiento, tolerancia, comunicación asertiva, liderazgo, resolución de conflictos, solidaridad entre otras, de\r\nacuerdo con las debilidades identificadas en los grupos de aprendices, 5. Articular estrategias o campañas\r\norientadas a fomentar en los aprendices, actitudes positivas frente a su ser, su proyecto de vida, su formación y\r\nla convivencia ciudadana, 6. Apoyar la planeación, y ejecutar actividades para el fortalecimiento de las relaciones\r\nfamiliares de los aprendices a través de la utilización del dialogo y herramientas de construcción, como medio\r\npara el desarrollo personal de los aprendices, 7. Desarrollar acciones para el autocuidado y el cuidado del otro,\r\ndesde la práctica de acciones. Articular estrategias o campañas orientadas a fomentar en los aprendices\r\nactitudes positivas fren', 0, '0000'),
(42, '1.Diseñar el Plan de trabajo de cada área de servicios tecnológicos del centro de formación para garantizar la\r\nimplementación, mantenimiento y mejora del sistema de gestión de los servicios tecnológicos, con metas,\r\nactividades, productos, resultados, responsables y cronograma. 2. Asegurar la implementación, mantenimiento\r\ny mejora del sistema de gestión y de las actividades de los servicios tecnológicos (servicios de laboratorio o\r\nservicios técnicos o servicios especiales), de acuerdo con los requisitos legales, reglamentarios, normativos, los\r\nestablecidos en SENA, Lineamientos Operativos SENNOVA y en el sistema unificado de gestión documental de\r\nSENNOVA 3. Garantizar que la gestión documental sea acorde con los procedimientos internos y del SENA,\r\nasegurando el control de los documentos, el uso de la última versión vigente de los mismos y la conservación\r\nde los registros. 4. Identificar, documentar y reportar oportunamente la presencia de riesgos, oportunidades y la\r\nocurrencia de desviaciones en el sistema de gestión, o de los procedimientos de los servicios tecnológicos\r\n(servicios de Laboratorio o servicios técnicos o servicios especiales) e iniciar y gestionar acciones destinadas a\r\nprevenir, minimizar o corregir dichos desvíos, de acuerdo con procedimientos documentados. 5. Acompañar la\r\nactualización de la información/evidencia de la ejecución de los proyectos de servicios tecnológicos en la\r\nplataforma definida por la entidad 6. Gestionar las revisiones por la dirección del sistema de gestión de la calidad\r\nde los de los servicios tecnológicos (servicios de La', 0, '0000'),
(43, 'Proponer y apoyar el desarrollo del plan de\r\ntrabajo que guíe la gestión de la biblioteca en las líneas: colecciones, servicios, extensión cultural y preservación\r\nde la memoria. b. Brindar a la comunidad educativa servicios de información innovadores para contribuir a la\r\ncalidad de la formación profesional integral del Centro. c. Apoyar la programación para la realización de talleres\r\nde acceso y uso de la información disponible en el Sistema de Bibliotecas. d. Apoyar la identificación y difusión\r\nde colecciones de acuerdo a las áreas o redes de conocimiento que atiende el centro de formación. e. Organizar\r\nlas colecciones de acuerdo con el sistema de clasificación utilizado por el Sistema de Bibliotecas. f. Realizar el\r\ningreso y procesamiento técnico de las colecciones físicas adquiridas para la biblioteca del Centro. g. Apoyar la\r\nprogramación, ejecución y evaluación de las actividades de extensión cultural - LEO en correspondencia con los\r\nlineamientos del Sistema de Bibliotecas. h. Apoyar la identificación de las publicaciones de autoría SENA que\r\ncontribuyan a la preservación de memoria institucional para su visibilización y disponibilidad desde el Repositorio\r\nInstitucional y el Portal de Revistas. i. Apoyar la elaboración y difusión de informes de gestión de la biblioteca.', 0, '0000'),
(44, '1. Presentar para\r\naprobación por parte del supervisor del contrato, un plan de trabajo que incluya cronograma y entregables. 2.\r\nIdentificar, generar y evaluar, estrategias orientadas a la retención de los aprendices dentro del alcance del\r\nobjeto contractual, articulando con el equipo que adelanta acciones del plan de bienestar y grupos internos del\r\nCentro de formación, el desarrollo de mecanismos que mejoren la retención de aprendices. 3. Desarrollar las\r\nactividades del objeto contractual en las diferentes modalidades de formación que aplique para el Centro de\r\nFormación y acompañar la programación académica, según lineamientos institucionales. 4. Gestionar\r\nmensualmente, o cuando se requiera, reportes sobre el estado de los aprendices beneficiarios de estímulos y\r\napoyos socioeconómicos en el sistema de gestión académico administrativo, e informar al responsable del\r\nmonitoreo del plan de acción de bienestar al aprendiz sobre los porcentajes de permanencia de estos\r\naprendices.5. Evaluar el grado de satisfacción de los aprendices beneficiarios de apoyos de sostenimiento y\r\nestímulos del centro de formación y entregar informe al responsable de monitoreo del centro de formación.5.\r\nImplementar acciones de bienestar al aprendiz dirigidas a los beneficiarios de apoyos. 6. socioeconómicos en\r\ncoordinación con los demás integrantes del equipo responsables de la ejecución del plan de bienestar, para\r\npromover el adecuado uso de los apoyos, así como su propósito en la permanencia y certificación del aprendiz.\r\n7. Participar conforme a su objeto contractual en la formulación d', 0, '0000'),
(45, '1.Presentar para aprobación por parte del\r\nsupervisor del contrato, un plan de trabajo que incluya cronograma y entregables. 2. Identificar, generar y\r\nevaluar, estrategias orientadas a la retención de los aprendices dentro del alcance del objeto contractual,\r\narticulando con el equipo que adelanta acciones del plan de bienestar y grupos internos del Centro de formación,\r\nel desarrollo de mecanismos que mejoren la retención de aprendices. 3. Desarrollar las actividades del objeto\r\ncontractual en las diferentes modalidades de formación que aplique para el Centro de Formación acompañando\r\nla programación académica, según lineamientos institucionales. 4. Realizar trámites administrativos en la\r\ndependencia de Bienestar del aprendiz. 5. Proyectar y archivar documentos que se originen en el marco de las\r\nactividades del programa de bienestar al aprendiz. 6. Brindar atención y orientación a los aprendices y\r\ncomunidad educativa que lo requieran, en cuanto al desarrollo de los programas de bienestar al aprendiz 7.\r\nApoyar en el proceso de gestión documental, que genera el equipo de Bienestar al Aprendiz del Centro de\r\nFormación, así como realizar seguimiento en la entrega de correspondencia del área de Bienestar del Aprendiz.\r\n8. Proyectar respuestas a solicitudes relacionadas directamente con Bienestar del aprendiz. 9. Elaboraciones\r\ninformes, presentaciones, actas y documentos relacionados con el programa bienestar del aprendiz. Asi como\r\nel apoyo en la elaboración de los informes trimestrales. 10. Coadyuvar en la logística de ejecución del desarrollo\r\ndel Plan de Bienestar del ', 0, '0000'),
(46, '1.Apoyar a los interesados o\r\naspirantes al SENA en la elección de programas de Formación técnicos, tecnológicos y a través de la\r\npresentación de pruebas de orientación (piloto) y cursos complementarios que fortalezcan el desarrollo de\r\nhabilidades cognitivas para potenciar los recursos personales de los aspirantes, hacia el camino más efectivo\r\nde realización profesional. 2. Apoyar a la inscripción de aspirantes a los programas de formación ofertados por\r\nel Centro 3. Gestionar la ejecución de las pruebas de orientación vocacional (piloto) que se tienen disponibles.\r\n4. Asistir al Grupo de Administración educativa en divulgar e informar a la comunidad todo lo relacionado con el\r\ningreso a la formación, el manejo del aplicativo de gestión educativa y todo lo referente a los programas\r\nofertados. 5. Apoyar a la Coordinación de Administración Educativa en la elaboración y proyección de informes\r\ny documentación administrativa. 6. Asistir al supervisor en las actividades de planeación, divulgación,\r\nproyección, seguimiento, estructuración y acompañamiento de los diferentes trámites y gestiones administrativas\r\nque se le soliciten. 7. Apoyar la gestión, seguimiento y respuesta a los requerimientos del cliente interno y externo\r\ndel Centro de Formación. 8. Apoyar la depuración, análisis y gestión de PQRS. 9. Apoyar la recepción y\r\nverificación de la documentación del aspirante convocado al proceso de formación. 10. Gestionar el\r\nasentamiento de matrícula. 11. Apoyar a la inscripción de aspirantes a los programas de formación ofertados\r\npor el Centro 12. Participar en la divulga', 0, '0000'),
(47, ' 1. Participar en la formulación del plan de bienestar al aprendiz del Centro de\r\nformación según normatividad vigente. 2. Identificar factores de riesgo de enfermedad con mayor incidencia en\r\nlos aprendices y adelantar acciones articuladas para la prevención de los riesgos identificados. 3. Adelantar\r\nacciones que fomenten y promuevan hábitos de vida saludable. 4.Identificar rutas de atención que permitan\r\nremitir para la atención en salud, a los aprendices que lo requieran. 5. Articular el desarrollo de estrategias o\r\ncampañas para la promoción de la salud y la prevención de la enfermedad con los demás integrantes del equipo\r\nresponsables de la ejecución del plan de bienestar. 6. Articular con el equipo que adelanta acciones del plan de\r\nbienestar, así como con los grupos internos del Centro de formación, para apoyar el desarrollo de mecanismos\r\npara la retención de aprendices, la implementación de la política de atención a personas con discapacidad, la\r\npolítica de atención con enfoque pluralista y diferencial, la inducción de aprendices, la divulgación y evaluación\r\ndel plan de bienestar al aprendiz. 7. Desarrollar talleres virtuales y/o presenciales al mes orientados hacia la\r\nconstrucción de estilos de vida y entornos saludables de acuerdo con el portafolio de talleres de bienestar al\r\nAprendiz. 8. Realizar registro de las actividades realizadas en el aplicativo SofiaPlus y en las demás plataformas\r\ndispuestas por el supervisor del contrato en los tiempos establecidos por el mismo. 9. Realizar informes, reportes\r\nu otros documentos asociados a las actividades relacion', 0, '0000'),
(48, '1. Contribuir al desarrollo de las actividades de\r\nla evaluación de competencias laborales para los proyectos establecidos en la programación anual del\r\ncentro de formación, de acuerdo con los lineamientos y la metodología del proceso Gestión de Evaluación y\r\nCertificación de Competencias Laborales del SENA. 2. Participar en la transferencia de conocimientos y/o\r\nreuniones del proceso a desarrollarse para los evaluadores de competencias laborales de ECCL. 3. Construir\r\nlos ítems e indicadores de un proyecto de instrumentos de evaluación de competencia laboral por\r\ncada 4 meses de contrato, de acuerdo con los lineamientos y la metodología establecida por el SENA en el\r\nproceso Gestión de Evaluación y certificación de competencias laborales. Para los evaluadores que cuenten\r\ncon menos de 4 meses de contrato, deben construir ítems y/o indicadores de desempeño y\r\nproducto, proporcional a los meses de contratación, en concertación con el dinamizador de instrumentos\r\npara ECCL asignado. (Ver nota 1). 4. Contribuir al cumplimiento de la meta de los indicadores del proceso\r\nGECCL del Centro de Formación, realizando como mínimo 50 evaluaciones de competencias laborales\r\npromedio mes en ejecución del contrato. (Ver nota 2). 5. Participar en mesas técnicas de estrategias para\r\nel aseguramiento de la calidad de los ítems e indicadores de evaluación cuando sea convocado por el grupo\r\nde Evaluación y Certificación de Competencias Laborales de la DSNFT. 6. Contribuir en la elaboración\r\nde informes, reportes y demás documentos relativosal desarrollo de la evaluación de competencias laboral', 0, '0000'),
(49, '1. Prestar apoyo en la proyección de estudios\r\nprevios, análisis del sector y matriz de riesgos de las diferentes modalidades de contratación del Centro para la\r\nIndustria de la Comunicación Gráfica de acuerdo con los criterios técnicos y normatividad vigente. 2. Apoyar en\r\nel cargue de procesos contractuales en las diferentes plataformas tales como SECOP II y Tienda Virtual del\r\nEstado Colombiano los procesos a su cargo atendiendo los instructivos y circulares de Colombia Compra\r\nEficiente. 3. Revisar jurídicamente la documentación acorde al objeto contractual, allegada a la subdirección del\r\nCentro para la Industria de la Comunicación Gráfica. 4. Apoyar la proyección de respuestas y seguimiento\r\noportuno de los requerimientos formulados por los usuarios internos, externos y entes de control a la\r\nsubdirección del Centro para la Industria de la Comunicación Gráfica, (tutelas, resoluciones, derechos de\r\npetición) en razón a su objeto contractual. 5. Prestar apoyo en las diferentes reuniones, eventos y otras\r\nactividades en las que se requiera acorde a su objeto contractual 6. Realizar la verificación y evaluación de los\r\nrequisitos jurídicos de las propuestas para los procesos de contratación que le sean asignados. 7. Proyectar\r\nactos administrativos propios de los procesos contractuales 8. Apoyar en la elaboración del plan de trabajo para\r\nlos procesos de adquisición de bienes y/o servicios de acuerdo con los criterios y procedimientos internos\r\nestablecidos en materia contractual. 9. Apoyar a las diferentes áreas en la consecución y/o elaboración de fichas\r\ntécnicas para ', 0, '0000'),
(50, '1. Diseñar el Plan de trabajo general de los proyectos de servicios tecnológicos financiados en el centro de formación con metas, actividades, productos, resultados, impactos esperados y cronograma que aseguren la ejecución del proyecto avalado para la vigencia y el apoyo al cumplimiento de los lineamientos de la entidad, lineamientos de SENNOVA, Lineamientos de la Estrategia de Servicios Tecnológicos, lineamientos del Sistema unificado de Gestión Documental SENNOVA, Plan de Acción, Plan estratégico Institucional u otro que aplique a la tipología del servicio. *Obligaciones a incluir, sólo en los casos en que no se cuente con un Responsable de Servicios Tecnológicos vinculado al centro de formación. 2. Elaborar la documentación técnica y administrativa correspondiente, según los procedimientos establecidos, asegurando el uso de la última versión vigente y la conservación de los registros, y revisar y ajustar en su caso. 3. Identificar los riesgos, oportunidades y ocurrencia de desviaciones en el sistema de gestión, o de los procedimientos técnicos para su gestión y reporte, y desarrollar acciones para prevenir, minimizar o corregir dichos desvíos, según los procedimientos documentados de los servicios tecnológicos. 4. Hacer seguimiento al tratamiento de salidas no conformes que se presenten en los diversos puntos del sistema de gestión y de las operaciones técnicas a las cuales se encuentre autorizado. 5. Asegurar la correcta ejecución de las operaciones técnicas y el desarrollo, verificación o validación de los servicios tecnológicos que satisfagan las necesidades del clie', 0, '0000'),
(51, '1. Contribuir al desarrollo de las actividades de\r\nla evaluación de competencias laborales para los proyectos establecidos en la programación anual del\r\ncentro de formación, de acuerdo con los lineamientos y la metodología del proceso Gestión de Evaluación y\r\nCertificación de Competencias Laborales del SENA. 2. Participar en la transferencia de conocimientos y/o\r\nreuniones del proceso a desarrollarse para los evaluadores de competencias laborales de ECCL. 3. Construir\r\nlos ítems e indicadores de un proyecto de instrumentos de evaluación de competencia laboral por\r\ncada 4 meses de contrato, de acuerdo con los lineamientos y la metodología establecida por el SENA en el\r\nproceso Gestión de Evaluación y certificación de competencias laborales. Para los evaluadores que cuenten\r\ncon menos de 4 meses de contrato, deben construir ítems y/o indicadores de desempeño y\r\nproducto, proporcional a los meses de contratación, en concertación con el dinamizador de instrumentos\r\npara ECCL asignado. (Ver nota 1). 4. Contribuir al cumplimiento de la meta de los indicadores del proceso\r\nGECCL del Centro de Formación, realizando como mínimo 50 evaluaciones de competencias laborales\r\npromedio mes en ejecución del contrato. (Ver nota 2). 5. Participar en mesas técnicas de estrategias para\r\nel aseguramiento de la calidad de los ítems e indicadores de evaluación cuando sea convocado por el grupo\r\nde Evaluación y Certificación de Competencias Laborales de la DSNFT. 6. Contribuir en la elaboración\r\nde informes, reportes y demás documentos relativosal desarrollo de la evaluación de competencias laboral', 0, '0000'),
(52, ' 1. Apoyar el desarrollo del plan de trabajo para\r\nla gestión de la biblioteca en las líneas: colecciones, servicios, extensión cultural y preservación de la\r\nmemoria. 2. Brindar a la comunidad educativa servicios de información innovadores necesarios para\r\ncontribuir a la calidad de la formación profesional integral del Centro 3. Apoyar la realización de talleres de\r\nacceso y uso de la información disponible en el Sistema de Bibliotecas. 4. Organizar las colecciones de\r\nacuerdo con el sistema de clasificación utilizado por el Sistema de Bibliotecas. 5. Apoyar el ingreso y\r\nprocesamiento técnico de las colecciones físicas para la disposición en estantería de la biblioteca del\r\nCentro. 6. Apoyar la ejecución de actividades de extensión cultural - LEO en correspondencia con los\r\nlineamientos del Sistema de Bibliotecas. 7. Apoyar la identificación de las publicaciones de autoría SENA\r\nque contribuyan a la preservación de memoria institucional para su visibilización y disponibilidad desde el\r\nRepositorio Institucional y el Portal de Revistas. 8. Apoyar la elaboración y difusión de informes de gestión\r\nde la biblioteca.\r\n', 0, '0000'),
(53, '1. Apoyar los trámites de\r\ncomunicaciones, archivo y de gestión documental asociados al proceso de gestión contractual del Centro. 2. Realizar\r\nlos reportes e informes asociados a la contratación del centro de formación: SIRECI, DIARI, Ley de\r\nemprendimiento, y demás de ley, o requeridos a la Coordinación Administrativa del Centro. 3Apoyar el registro de\r\nlos contratos del Centro de Formación en el RUES de Confecámaras. 4. Proporcionar información para la elaboración\r\nde los indicadores de gestión y respuesta a los requerimientos de otras coordinaciones, áreas, dirección general, entes\r\ninternos y externos de control. 5. Elaborar las actas de reunión requeridas, así como, la custodia de estas. 6. Recordar\r\nen el Centro de Formación el uso de los formatos, listas de verificación, procedimientos, instructivos y documentos\r\nSIGA del proceso de Gestión Contractual. 7. Brindar atención telefónica y presencial a los grupos de valor en materia\r\ncontractual tanto internos como externos. 8. Tramitar y gestionar la completitud de los expedientes contractuales y el\r\ncierre de estos en el SECOP I, SECOP II y TVEC. 9. Las demás actividades relacionadas con el objeto contractual\r\nque sean asignados por el supervisor del contrato. 10. Apoyar técnicamente las actividades contractuales y\r\nconvencionales en cada etapa del proceso asignado. 11. Apoyar en la entrega física y documental del almacén del\r\nCentro para la Industria de la Comunicación Gráfica a la persona indicada por la subdirección en los meses febrero y\r\nmarzo de 2024', 0, '0000'),
(54, '1. Apoyar las diferentes dependencias del\r\ncentro de formación en la atención personal, telefónica y virtual a la comunidad educativa en general. 2.\r\nRecibir, registrar, direccionar y hacer su respectivo seguimiento a la comunidad educativa y en general\r\ndirigida al Centro. 3.Establecer contactos y desarrollar las actividades de comunicación o divulgación interna\r\no externa, bajo las orientaciones y normas de la institución y orientación del subdirector del Centro, dentro\r\ndel tiempo establecido 4.Orientar a los ciudadanos que solicitan información sobre los diferentes trámites y\r\nservicios que ofrece el SENA y/o registro de información en la web institucional y/o en los sistemas y\r\naplicativos dispuestos por la entidad para soportar la oferta del portafolio institucional. 5. Divulgar el portafolio\r\nde servicios del centro de formación por los diferentes canales de atención a disposición del centro de\r\nformación. 6. Apoyar las diferentes estrategias de seguimiento en la gestión y respuesta oportuna de las\r\nPQRS. 7. Apoyar la gestión y consolidación de respuesta en los sistemas de información SGVA, SOFIA\r\nPLUS, CRM, entre otros) 8. Apoyo en la conservación de la documentación relacionada con el área, de\r\nacuerdo con las normas y las tablas de retención documental según normatividad vigente. 9. Participar en\r\nlas diferentes campañas y estrategias de comunicación para la consolidación de las ofertas educativas por\r\ndemanda social y especiales, bienestar de aprendices, Sennova, competencias laborales entre otras.\r\n', 0, '0000'),
(55, '1. Apoyar el trámite administrativo y de\r\nseguimiento al plan de acción archivístico generado a nivel de centro de formación acorde a las directrices\r\nimpartidas por las áreas respondientes del proceso. 2. Apoyar en la clasificación de los documentos físicos y\r\ndigitales en las diferentes áreas del Centro de Formación. 3. Organizar de manera cronológica la documentación\r\nencontrada de acuerdo con la TRD en cada uno de los procesos de la entidad. 4. Apoyar la clasificación y\r\norganización de los archivos físicos y digitales a los encargados de los procesos que se llevan a cabo en el\r\nCentro de formación. 5. Elaborar los Inventarios documentales teniendo en cuenta las series y subseries de\r\nacuerdo la TRD. 6. Entregar por escrito los informes que se le soliciten de las actividades realizadas conforme\r\ncon el objeto contractual y asistir a las reuniones y/o comités programados cuando sea requerido o asignado. 7.\r\nMantener la debida reserva sobre los asuntos manejados y conocidos dentro de la ejecución del contrato. 8.\r\nRealizar las demás actividades relacionadas con el objeto del contrato que le sean asignadas por el supervisor\r\ny/o el subdirector del centro que correspondan a la naturaleza del contrato.', 0, '0000'),
(56, '1. Manejo del correo\r\ninstitucional de TyT y Egresados. 2.Dar respuesta oportuna a las solicitudes de los aprendices en el proceso de\r\nTyT y Egresados. 3. Manejo de la información enviada desde regional para ser divulgada aprendices Egresados\r\ny del proceso pruebas TyT del centro de formación. 4. Actualización de base de datos de egresados y proceso\r\npruebas TyT. 5.Conocer Portafolio de servicios de los programas del Centro dirigido a esta comunidad. 6. Manejo\r\nde herramientas ofimáticas. 7. Elaboración mensual de informes para ser remitidos a la Regional 8. Realizar las\r\ndemás actividades relacionadas con el objeto del contrato que le sean asignadas por el supervisor y/o el\r\nsubdirector del centro que correspondan a la naturaleza del contrato. 9. Atención a los clientes internos y\r\nexternos de acuerdo con requerimiento de los aprendices y egresados. 10. Aplicar los procesos y procedimientos\r\nestablecidos por la entidad, para la gestión documental relacionada con el objeto contractual.', 0, '0000'),
(57, '1.Gestionar las diferentes actividades administrativas relacionadas con atención al cliente interno y externo y registro de información en los aplicativos correspondientes a la Coordinación Académica de acuerdo con lo establecido en el proceso de Gestión de Formación Profesional Integral. 2.Tramitar la información necesaria para dar respuesta a las PQRS y/o CRM relacionadas con la formación profesional integral y que sean de la competencia de la Coordinación Académica teniendo en cuenta la promesa de valor institucional. 3. Apoyar las acciones definidas por la coordinación académica para realizar la depuración periódica y oportuna de las fichas activas, que garantice el estado actualizado de los aprendices pertenecientes a las mismas, según procesos, procedimientos, acuerdos, debido proceso y/o circulares institucionales. 4.Apoyar la implementación de estrategias y acciones definidas por la coordinación académica para la ejecución, control y retención escolar en aprendices de formación titulada virtual en etapa productiva y en formación complementaria virtual, generando alertas tempranas a la coordinación académica en caso de presentarse riesgo de deserción, o que la participación en los procesos formativos sea baja o nula. 5. Apoyar a la Coordinación Académica en la organización y realización de Comités de Evaluación y Seguimiento, hasta la elaboración de los actos académicos y/o administrativos que surjan del proceso, y el control de la correcta aplicación en el sistema de información por parte del rol competente. 6. Realizar el proceso de novedades de aprendices hasta la', 0, '0000'),
(58, ' 1. Organizar, preparar, gestionar y documentar\r\nlas reuniones, encuentros y eventos de la(s) Mesa(s) Sectorial(es) asignadas o del proceso de Gestión de\r\nInstancias de Concertación y Competencias Laborales (Virtuales, presenciales e hibridas) de acuerdo con\r\norientaciones y lineamientos institucionales. 2. Apoyar en el diseño y ejecución de actividades que permitan el\r\ncumplimiento del Plan de Acción 2024 de las Mesa(s) Sectorial(es) asignadas, brindar respuesta a los\r\nrequerimientos y solicitudes de los grupos de valor del proceso Gestión de Instancias de Concertación y\r\nCompetencias Laborales y fomentar el relacionamiento y articulación institucional en los Centros de Formación.\r\n3. Gestionar la vinculación, renovación y participación de organizaciones en las Mesas Sectoriales de acuerdo\r\ncon los lineamientos institucionales. 4. Realizar la consecución, convocatoria, confirmación y seguimiento de\r\nExpertos Técnicos para la normalización de Competencias Laborales, contribuyendo al desarrollo, ejecución y\r\ncumplimiento del Proyecto Anual de Estandarización/Normalización 2024 y a las estrategias del banco de\r\nexpertos y trabajo en red. 5. Apoyar en la gestión administrativa y logística de la Estandarización/Normalización\r\nde Competencias Laborales. 6. Proponer estrategias o acciones que aporten a la visibilización del proceso, así\r\ncomo diseñar y elaborar material gráfico, audiovisual, boletines, infografías, entre otros, para la divulgación y\r\ndifusión de información de las Mesa(s) Sectorial(es) asignadas, la Normalización de Competencias a través de\r\nredes sociales y medi', 0, '0000'),
(59, '1. Contribuir al desarrollo de las actividades de\r\nla evaluación de competencias laborales para los proyectos establecidos en la programación anual del centro\r\nde formación, de acuerdo con los lineamientos y la metodología del proceso Gestión de Evaluación y\r\nCertificación de Competencias Laborales del SENA. 2. Participar en la transferencia de conocimientos y/o\r\nreuniones del proceso a desarrollarse para los evaluadores de competencias laborales de ECCL. 3 Construir los\r\nítems e indicadores de un proyecto de instrumentos de evaluación de competencia laboral por cada 4 meses\r\nde contrato, de acuerdo con los lineamientos y la metodología establecida por el SENA en el proceso Gestión\r\nde Evaluación y certificación de competencias laborales. Para los evaluadores que cuenten con menos de 4.\r\nmeses de contrato, deben construir ítems y/o indicadores de desempeño y producto, proporcional\r\na los meses de contratación, en concertación con el dinamizador de instrumentos para ECCL asignado.\r\n(Ver nota 1). 4. Contribuir al cumplimiento de la meta de los indicadores del proceso GECCL del Centro de\r\nFormación, realizando como mínimo 50 evaluaciones de competencias laborales promedio mes en ejecución\r\ndel contrato. (Ver nota 2). 5. Participar en mesas técnicas de estrategias para el aseguramiento de la calidad de\r\nlos ítems e indicadores de evaluación cuando sea convocado por el grupo de Evaluación y Certificación de\r\nCompetencias Laborales de la DSNFT. 6. Contribuir en la elaboración de informes, reportes y demás\r\ndocumentos relativos al desarrollo de la evaluación de competencias labora', 0, '0000'),
(60, '1.Presentar para aprobación por parte del supervisor del contrato, un plan de trabajo que incluya cronograma y entregables. 2. Identificar, generar y evaluar, estrategias orientadas a la retención de los aprendices dentro del alcance del objeto contractual, articulando con el equipo que adelanta acciones del plan de bienestar y grupos internos del Centro de formación, el desarrollo de mecanismos que mejoren la retención de aprendices. 3. Desarrollar las actividades del objeto contractual en las diferentes modalidades de formación que aplique para el Centro de Formación acompañando la programación académica, según lineamientos institucionales. 4. implementar acciones que promuevan en los aprendices el desarrollo de una sensibilidad personal y social a través de las diversas manifestaciones del arte (Danza, teatro, dibujo, pintura, fotografía, entre otras). 5. fomentar la conformación de grupos en expresiones de arte para los aprendices que permita el desarrollo de la sensibilidad personal y social. Realizando talleres virtuales y/o presenciales por lo menos una vez al mes, que fomenten la apreciación artística y el acceso a distintas expresiones verbales, corporales y escritas de acuerdo con el portafolio de talleres de bienestar al aprendiz 6. Realizar encuentros intracentros e intercentros para incentivar y reconocer el talento artístico de los aprendices. 7. Apoyar la gestión de espacios y recursos requeridos para el desarrollo de las actividades artísticas y culturales que se formulen. 8. Articular con el equipo del plan de bienestar del centro estrategias o campañas que', 0, '0000'),
(61, '1. Apoyar los procesos de producción del Centro de Formación, en las áreas de producción gráfica de acuerdo\r\na los requerimientos del cliente.\r\n2. Imprimir productos gráficos de acuerdo a las órdenes de producción, verificando condiciones de calidad.\r\n3. Velar por el cumplimiento de los plazos y horas de entregas establecidas para la impresión, envió y entrega\r\nde los impresos bajo su cargo.\r\n4. Garantizar la calidad de impresión de los productos, incluyendo la consistencia del color, el registro\r\nadecuado y la resolución de impresión, y/o finalización de productos impresos.\r\n5. Apoyar en el monitoreo a los aprendices en etapa productivo que apoyan el proceso de producción de\r\ncentros.\r\n6. Mantener registros precisos de la producción, incluyendo la cantidad de productos impresos, problemas\r\nencontrados y acciones tomadas.\r\n7. Entregar por escrito los informes que se le soliciten de las actividades realizadas conforme con el objeto\r\ncontractual y asistir a las reuniones y/o comités programados cuando sea requerido o asignado.\r\n8. Ejecutar de manera idónea el objeto del contrato conforme a los lineamientos del Sistema Integrado de\r\nGestión y Autocontrol (SIGA) del SENA, el cual se encuentra documentado en la plataforma compromiso.\r\n9. Mantener la debida reserva sobre los asuntos manejados y conocidos dentro de la ejecución de contrato.\r\n10. Realizar las demás actividades relacionadas con el objeto del contrato que le sean asignadas por el\r\nsupervisor y/o el Subdirector del centro que correspondan a la naturaleza del contrato.', 0, '0000');
INSERT INTO `obligacionesespecificas` (`id`, `nombre`, `idObjeto`, `año`) VALUES
(62, '1.Apoyar los procesos de producción del Centro\r\nde Formación, en las áreas de impresión de acuerdo a los requerimientos del cliente. 2. Imprimir productos\r\ngráficos de acuerdo a las órdenes de producción, verificando condiciones de calidad. 3. Velar por el cumplimiento\r\nde los plazos y horas de entregas establecidas para la impresión, envió y entrega de los impresos bajo su cargo.\r\n4. Garantizar la calidad de impresión de los productos, incluyendo la consistencia del color, el registro adecuado\r\ny la resolución de impresión, y/o finalización de productos impresos. 5.Apoyar en el monitoreo a los aprendices\r\nen etapa productivo que apoyan el proceso de producción de centros 6.Mantener registros precisos de la\r\nproducción, incluyendo la cantidad de productos impresos, problemas encontrados y acciones tomadas.\r\n7.Entregar por escrito los informes que se le soliciten de las actividades realizadas conforme con el objeto\r\ncontractual y asistir a las reuniones y/o comités programados cuando sea requerido o asignado. 8.Ejecutar de\r\nmanera idónea el objeto del contrato conforme a los lineamientos del Sistema Integrado de Gestión y Autocontrol\r\n(SIGA) del SENA, el cual se encuentra documentado en la plataforma compromiso. 9. Mantener la debida\r\nreserva sobre los asuntos manejados y conocidos dentro de la ejecución de contrato. 10. Realizar las demás\r\nactividades relacionadas con el objeto del contrato que le sean asignadas por el supervisor y/o el subdirector del\r\ncentro que correspondan a la naturaleza del contrato', 0, '0000'),
(63, '1. Brindar apoyo en la planeación y estructuración de los procesos contractuales y convencionales en sus\r\ndiferentes modalidades de selección para cada una de las etapas contractuales y convencionales (pre,\r\ncontractual y convencional – contractual y convencional – Pos, contractual y convencional) en las diferentes\r\nplataformas de contratación pública.\r\n2. Apoyar en la revisión de evaluaciones jurídicas de las ofertas enviadas por los diferentes proponentes,\r\nrespecto a la revisión de los requisitos jurídicos habilitantes, cumplimiento al manual de contratación del SENA y la\r\nnormatividadvigente.\r\n3. Asistir jurídicamente para la elaboración y revisión de conceptos, informes, respuestas a derechos de\r\npeticióny los diferentes tramites allegados en materia de Gestión Contractual y convencional.\r\n4. Brindar apoyo en la asistencia jurídica de las audiencias producto de los procesos de contratación y\r\nconvencionales asignados y proyectar las actas correspondientes por cada audiencia.\r\n5. Apoyar en la elaboración de los documentos que sean necesarios para garantizar el soporte jurídico en\r\ntodos los procesos de contratación y convencionales que le sean asignados.\r\n6. Asistir jurídica y técnicamente en el trámite de aprobación de garantías de cumplimiento contractual y\r\nconvencional que se desprendan de los contratos celebrados por el SENA.\r\n7. Asistir los trámites de modificaciones, prorrogas, adiciones, suspensiones y demás modificaciones\r\ncontractuales solicitadas por la supervisión de los contratos u ordenador del gasto del Centro de Formación.\r\n8. Brindar el apoyo jurídico e', 0, '0000'),
(64, '1. Gestionar las diferentes actividades administrativas relacionadas con atención al cliente\r\ninterno y externo y registro de información en los aplicativos correspondientes a la\r\nCoordinación Académica de acuerdo con lo establecido en el proceso de Gestión de\r\nFormación Profesional Integral.\r\n2. Tramitar la información necesaria para dar respuesta a las PQRS y/o CRM relacionadas con\r\nla formación profesional integral y que sean de la competencia de la Coordinación\r\nAcadémica teniendo en cuenta la promesa de valor institucional.\r\n3. Apoyar las acciones definidas por la coordinación académica para realizar la depuración\r\nperiódica y oportuna de las fichas activas, que garantice el estado actualizado de los\r\naprendices pertenecientes a las mismas, según procesos, procedimientos, acuerdos, debido\r\nproceso y/o circulares institucionales.\r\n4. Apoyar la implementación de estrategias y acciones definidas por la coordinación\r\n5\r\nGTH-F-075 V08\r\nacadémica para la ejecución, control y retención escolar en aprendices de formación\r\ntitulada virtual en etapa productiva y en formación complementaria virtual, generando\r\nalertas tempranas a la coordinación académica en caso de presentarse riesgo de deserción,\r\no que la participación en los procesos formativos sea baja o nula.\r\n5. Apoyar a la Coordinación Académica en la organización y realización de Comités de\r\nEvaluación y Seguimiento, hasta la elaboración de los actos académicos y/o administrativos\r\nque surjan del proceso, y el control de la correcta aplicación en el sistema de información\r\npor parte del rol competente.\r\n6. Realizar el pr', 0, '0000'),
(65, '1. Brindar apoyo en la identificación, planeación y\r\nejecución de transferencias de conocimiento en los temas técnicos relacionados con el modelo de operación SIGA\r\ndirigidas a los funcionarios y contratistas del Centro de formación. Y participar activamente en las transferencias\r\nde conocimiento impartidas por el Despacho Regional y la Dirección General con relación al modelo de operación\r\ndel SIGA.\r\n2. Acompañar la planeación para la ejecución de las actividades del SIGA establecidas en el plan anual de\r\nmantenimiento PAM en su Centro de formación y sedes adscritas.\r\n3. Asistir en la realización de los ejercicios de evaluación del desempeño por dependencias y de rendición de\r\ncuentas a la ciudadanía y la consolidación de informes de gestión requeridos por la entidad y entes de control\r\nrelacionados con el modelo de operación del SIGA.\r\n4. Dar acompañamiento en la ejecución de las actividades establecidas en el Plan anual de mantenimiento para\r\nla implementación, seguimiento y mejora del modelo de operación SIGA.\r\n5. Apoyar la programación, realización y documentación de las visitas de verificación, auditorías internas a las\r\ninstalaciones de las sedes a cargo o que sean designadas desde la Dirección General.\r\n 6.Efectuar el seguimiento a la ejecución de las\r\nactividades establecidas en el Plan anual de mantenimiento para la implementación, seguimiento y mejora del\r\nmodelo de operación SIGA.\r\n7. Apoyar en el seguimiento, medición, análisis y evaluación del modelo de operación del SIGA y asistir a la alta\r\ndirección en la formulación de estrategias de la mejora continua a t', 0, '0000'),
(66, ' 1. Proponer, desarrollar y hacer\r\nseguimiento al plan de trabajo que guíe la gestión de la biblioteca en las líneas: colecciones, servicios, extensión\r\ncultural y preservación de la memoria 2. Brindar a la comunidad educativa servicios de información innovadores\r\npara contribuir a la calidad de la formación profesional integral del Centro. 3. Planear y realizar talleres de\r\nformación de usuarios que faciliten y fomenten el acceso y uso de la información disponible en el Sistema de\r\nBibliotecas. 4. Identificar y difundir colecciones de acuerdo a las áreas o redes de conocimiento que atiende el\r\ncentro de formación. 5. Verificar que las colecciones se encuentren organizadas de acuerdo con el sistema de\r\nclasificación utilizado por el Sistema de Bibliotecas 6. Realizar la gestión de las colecciones físicas de apoyo a\r\nla formación profesional integral, lo cual incluye la adquisición, catalogación, evaluación y descarte de material.\r\n7. Programar, desarrollar y evaluar las actividades de extensión cultural - LEO en correspondencia con los\r\nlineamientos del Sistema de Bibliotecas. 8. Implementar los servicios de apoyo a la investigación de acuerdo\r\ncon las orientaciones del Sistema de Bibliotecas. 9. Identificar las publicaciones de autoría SENA que\r\ncontribuyan a la preservación de memoria institucional para su visibilización y disponibilidad desde el Repositorio\r\nInstitucional y el Portal de Revistas. 10. Elaborar y difundir informes de gestión de la biblioteca.\r\n', 0, '0000'),
(67, '1. Brindar apoyo en la identificación, planeación y ejecución de transferencias de\r\nconocimiento en los temas técnicos relacionados con el modelo de operación SIGA dirigidas\r\na los funcionarios y contratistas del Centro de formación. Y participar activamente en las\r\ntransferencias de conocimiento impartidas por el Despacho Regional y la Dirección General\r\ncon relación al modelo de operación del SIGA.\r\n2. Acompañar la planeación para la ejecución de las actividades del SIGA establecidas en el\r\nplan anual de mantenimiento PAM en su Centro de formación y sedes adscritas.\r\n3. Asistir en la realización de los ejercicios de evaluación del desempeño por dependencias\r\n5\r\nGTH-F-075 V08\r\ny de rendición de cuentas a la ciudadanía y la consolidación de informes de gestión\r\nrequeridos por la entidad y entes de control relacionados con el modelo de operación del\r\nSIGA.\r\n4. Dar acompañamiento en la ejecución de las actividades establecidas en el Plan anual de\r\nmantenimiento para la implementación, seguimiento y mejora del modelo de operación\r\nSIGA.\r\n5. Apoyar la programación, realización y documentación de las visitas de verificación,\r\nauditorías internas a las instalaciones de las sedes a cargo o que sean designadas desde la\r\nDirección General.\r\n6.Efectuar el seguimiento a la ejecución de las actividades establecidas en el Plan anual de\r\nmantenimiento para la implementación, seguimiento y mejora del modelo de operación\r\nSIGA.\r\n7. Apoyar en el seguimiento, medición, análisis y evaluación del modelo de operación del\r\nSIGA y asistir a la alta dirección en la formulación de estrategias de la', 0, '0000'),
(68, '1. Presentar para aprobación por parte del supervisor del contrato, un plan de trabajo que\r\nincluya cronograma y entregables.\r\n2. Identificar, generar y evaluar, estrategias orientadas a la retención de los aprendices\r\ndentro del alcance del objeto contractual, articulando con el equipo que adelanta acciones\r\ndel plan de bienestar y grupos internos del Centro de formación, el desarrollo de\r\nmecanismos que mejoren la retención de aprendices.\r\n3. Desarrollar las actividades del objeto contractual en las diferentes modalidades de\r\nformación que aplique para el Centro de Formación acompañando la programación\r\nacadémica, según lineamientos institucionales.\r\n4. implementar acciones que promuevan en los aprendices el desarrollo de una sensibilidad\r\npersonal y social a través de las diversas manifestaciones del arte (Danza, teatro, dibujo,\r\npintura, fotografía, entre otras).\r\n5\r\nGTH-F-075 V08\r\n5. fomentar la conformación de grupos en expresiones de arte para los aprendices que\r\npermita el desarrollo de la sensibilidad personal y social. Realizando talleres virtuales y/o\r\npresenciales por lo menos una vez al mes, que fomenten la apreciación artística y el\r\nacceso a distintas expresiones verbales, corporales y escritas de acuerdo con el portafolio\r\nde talleres de bienestar al aprendiz\r\n6. Realizar encuentros intracentros e intercentros para incentivar y reconocer el talento\r\nartístico de los aprendices.\r\n7. Apoyar la gestión de espacios y recursos requeridos para el desarrollo de las actividades\r\nartísticas y culturales que se formulen.\r\n8. Articular con el equipo del plan de bienest', 0, '0000'),
(69, '1. Apoyar los procesos de producción del Centro de Formación, en las áreas de impresión\r\nde acuerdo a los requerimientos del cliente.\r\n2. Imprimir productos gráficos de acuerdo a las órdenes de producción, verificando\r\ncondiciones de calidad.\r\n3. Velar por el cumplimiento de los plazos y horas de entregas establecidas para la\r\nimpresión, envió y entrega de los impresos bajo su cargo.\r\n4. Garantizar la calidad de impresión de los productos, incluyendo la consistencia del\r\ncolor, el registro adecuado y la resolución de impresión, y/o finalización de productos\r\nimpresos.\r\n5. Apoyar en el monitoreo a los aprendices en etapa productivo que apoyan el proceso\r\nde producción de centros\r\n6. Mantener registros precisos de la producción, incluyendo la cantidad de productos\r\nimpresos, problemas encontrados y acciones tomadas.\r\n7. Entregar por escrito los informes que se le soliciten de las actividades realizadas\r\nconforme con el objeto contractual y asistir a las reuniones y/o comités programados\r\ncuando sea requerido o asignado.\r\n8. Ejecutar de manera idónea el objeto del contrato conforme a los lineamientos del\r\nSistema Integrado de Gestión y Autocontrol (SIGA) del SENA, el cual se encuentra\r\ndocumentado en la plataforma compromiso.\r\n5\r\nGTH-F-075 V08\r\n9. Mantener la debida reserva sobre los asuntos manejados y conocidos dentro de la\r\nejecución de contrato.\r\n10. Realizar las demás actividades relacionadas con el objeto del contrato que le sean\r\nasignadas por el supervisor y/o el Subdirector del centro que correspondan a la\r\nnaturaleza del contrato', 0, '0000'),
(70, '1. Apoyar y asesorar técnicamente a los niveles de soporte básico que atienden a los\r\nusuarios finales sobre las funcionalidades y el uso adecuado de los servicios e infraestructura TIC.\r\n2. Verificar el correcto mantenimiento de hardware y software de los equipos realizado por\r\nlos niveles de soporte técnico del centro de formación\r\n3. Establecer las prioridades en el mantenimiento de sistemas informáticos para los\r\ndiferentes ambientes de formación y áreas administrativas\r\n4. Implementar y hacer seguimiento a las medidas que garanticen la gestión global de la\r\nseguridad de la información.\r\n5.Gestionar y/o implementar soluciones y/o repositorios, como bases de datos, integración de\r\nherramientas digitales integrales, o sistemas de información, como apoyo a la gestión de las\r\ndiferentes dependencias del centro para la industria de la comunicación gráfica, que permitan un\r\nmanejo centralizado de la información de forma segura, consistente y fiable.\r\n6. Verificar la correcta operación de las redes de datos y de energía regulada bajo los\r\nparámetros y funcionalidades establecidas para la entidad.\r\n7. Apoyar técnicamente los procesos de formulación de necesidades del centro, según se\r\nrequiera en el área TIC´S.\r\n8. Emitir conceptos técnicos que se requieren a los procesos de bajas de equipos de sistema\r\nadelantadas por el centro de formación.\r\n9. Llevar un control sobre obsolescencia de equipos de sistemas del Centro de Formación y\r\nentregar los informes que sobre el particular le solicite la supervisión del contrato y/o subdirección\r\ndel centro de formación.\r\n10. Prestar apoyo', 0, '0000'),
(71, 'A. Cumplir con el objeto del contrato.\r\n5\r\nGTH-F-075 V08\r\nB. Movilizar el aula móvil según la programación establecida.\r\nC. Velar por la seguridad del vehículo y los equipos, maquinaria y materiales contenidos en el aula\r\nmóvil.\r\nD. Apoyar en el diligenciamiento de los diferentes formatos que se requieran (chequeo antes de\r\nmarcha- vehículos), haciendo inspección y registrando el estado del vehículo.\r\nE. Hacer revisión tecnicomecanica del vehículo según las orientaciones establecidas del parque\r\nautomotor.\r\nF. Proyectar oportunamente el mantenimiento preventivo y correctivo de los vehículos dispuestos\r\npara la ejecución de su contrato.\r\nG. Realizar informe de novedades por cada viaje o cuando se considere necesario en función del\r\ncumplimiento del objeto del contrato.\r\nH. Realizar los requerimientos de materiales acorde con las actividades a desarrollar según el plan\r\nde mantenimiento existente para el vehículo.\r\nI. Llevar registro en la hoja de vida del equipo y/o vehículo sobre las actividades de mantenimiento\r\nrealizadas con base en las necesidades presentadas o el mantenimiento programado para el quipo\r\ny/o vehículo.\r\nJ. Avisar sobre riesgos potenciales o reales por deficiencias detectadas en el desarrollo de las\r\nactividades de mantenimiento.\r\nK. Velar por la aplicación de todas las normas de seguridad en función de proteger la vida y salud\r\nde los ocupantes del vehículo y condiciones de uso de los materiales.\r\nL. Aplicar todas las normas de seguridad en el área en la cual se desarrollan las actividades de\r\nmantenimiento, en función de evitar accidentes o deterioro de ', 0, '0000'),
(72, '1. Presentar para aprobación por parte del supervisor del contrato, un plan de trabajo que\r\nincluya cronograma y entregables.\r\n2. Identificar, generar y evaluar, estrategias orientadas a la retención de los aprendices\r\ndentro del alcance del objeto contractual, articulando con el equipo que adelanta acciones\r\ndel plan de bienestar y grupos internos del Centro de formación, el desarrollo de\r\nmecanismos que mejoren la retención de aprendices.\r\n3. Desarrollar las actividades del objeto contractual en las diferentes modalidades de\r\nformación que aplique para el Centro de Formación acompañando la programación\r\nacadémica, según lineamientos institucionales.\r\n4. Formular e implementar estrategias para el desarrollo de habilidades blandas en los\r\naprendices del centro de formación de las diferentes modalidades: presencial, virtual y a\r\ndistancia, que permitan mejorar sus capacidades de afrontamiento a las situaciones de la\r\nvida cotidiana.\r\n5. Asistir al supervisor en las actividades de planeación, divulgación, proyección,\r\nseguimiento, estructuración y acompañamiento de los diferentes trámites y gestiones\r\nadministrativas que se le soliciten.\r\n6. Realizar acciones orientadas a la Implementación de la política de atención a personas\r\ncon discapacidad, la política de atención con enfoque pluralista y diferencial.\r\n7. Generar estrategias de divulgación permanentes de las actividades a desarrollar, dentro\r\nde su objeto contractual. Orientando y hacer seguimiento a las estrategias para el\r\ndesarrollo de la cultura institucional, ciudadana, digital y ambiental, que incentiven el\r\ncumpli', 0, '0000'),
(73, '1.Apoyar la recepción, verificación, almacenamiento y entrega de los bienes devolutivos, bienes en\r\nadministración y bienes de consumo entregados por los proveedores.\r\n2.Alistar los bienes muebles, bienes de consumo y equipos que se deben entregar y recibir\r\n3. Agregar la marcación y paqueteo de bienes de los funcionarios y contratistas del centro de\r\nformación.\r\n4. Apoyar en la realización de traspasos entre cuentadantes del centro de formación y el reintegro\r\nde los bienes por parte de estos desde la solicitud de traspaso de bienes hasta la legalización de\r\nestos.\r\n5. Apoyar la realización de la toma física y realización de los documentos Necesarios\r\n6. Apoyar al Centro de formación en la clasificación de bienes servibles e inservibles reintegrados\r\nal almacén con el fin de iniciar el proceso de baja\r\n7. Gestionar los informes periódicos ante las dependencias que lo requieran, o a solicitud del\r\nsupervisor del contrato.\r\n8. Mantener la información organizada, actualizada y completa de los elementos en bodega de\r\ndevolutivos, consumo y reintegrados, utilizando los aplicativos sistemas de información\r\nestablecidos por la Entidad.\r\n6\r\nGTH-F-075 V08\r\n9. Ejecutar de manera idónea el objeto del contrato, conforme a los lineamientos del Sistema\r\nIntegrado de Gestión y Autocontrol (SIGA) del SENA el cual se encuentra documentado en la\r\nplataforma compromiso.\r\n10. Realizar las demás actividades relacionadas con el objeto del contrato que le sean asignadas\r\npor el supervisor y/o el subdirector del centro que correspondan a la naturaleza del contrato', 0, '0000'),
(74, '1 Apoyar en el proceso de definición de materiales y suministros necesarios para la\r\nproducción gráfica, asegurándose de cumplir con los procedimientos y políticas establecidos.\r\n2 Asesorar a clientes internos y externos frente a la solicitud de productos gráficos.\r\n3 Gestionar procesos de diseño y preprensa de acuerdo a los requerimientos de producción\r\nestablecidos por las diferentes instancias, centros y regionales del SENA a nivel nacional.\r\n4 Realizar propuestas innovadoras frente al portafolio de productos gráficos ofrecidos por el\r\ncentro de formación en el proceso de producción de centros.\r\n5 Apoyar en el seguimiento de las actividades desarrolladas por los operarios y aprendices en\r\netapa productiva asignados a producción de centros.\r\n6 Realizar, asignar y supervisar tareas administrativas y operativas relacionadas con la\r\nproducción gráfica.\r\n7 Apoyar en la gestión de necesidades de materiales de formación y mantenimiento de\r\nmaquinaria y equipos para el correcto desarrollo de los procesos de producción de centros.\r\n8 Adelantar procesos productivos de manera coordinada y concertada con los instructores y\r\napéndices asignados en el proceso de producción de centros.\r\n9 Preparar informes periódicos sobre el estado del inventario, el rendimiento del proceso y\r\ncualquier otro análisis relevante así como proporcionar datos y análisis para facilitar la toma de\r\ndecisiones.\r\n10 Ejecutar de manera idónea el objeto del contrato conforme a los lineamientos del Sistema\r\nIntegrado de Gestión y Autocontrol (SIGA) del SENA, el cual se encuentra documentado en la\r\nplataforma comp', 0, '0000'),
(75, '1. Brindar apoyo en la planeación y estructuración de los procesos contractuales y\r\nconvencionales en sus diferentes modalidades de selección para cada una de las etapas\r\ncontractuales y convencionales (pre, contractual y convencional – contractual y convencional – Pos,\r\ncontractual y convencional) en las diferentes plataformas de contratación pública.\r\n2. Apoyar en la revisión de evaluaciones jurídicas de las ofertas enviadas por los diferentes\r\nproponentes, respecto a la revisión de los requisitos jurídicos habilitantes, cumplimiento al manual\r\nde contratación del SENA y la normatividad vigente.\r\n3. Asistir jurídicamente para la elaboración y revisión de conceptos, informes, respuestas a\r\nderechos de petición y los diferentes tramites allegados en materia de Gestión Contractual y\r\nconvencional.\r\n4. Brindar apoyo en la asistencia jurídica de las audiencias producto de los procesos de\r\ncontratación y convencionales asignados y proyectar las actas correspondientes por cada audiencia.\r\n5. Apoyar en la elaboración de los documentos que sean necesarios para garantizar el soporte\r\njurídico en todos los procesos de contratación y convencionales que le sean asignados.\r\n6. Asistir jurídica y técnicamente en el trámite de aprobación de garantías de cumplimiento\r\ncontractual y convencional que se desprendan de los contratos celebrados por el SENA.\r\n7. Asistir los trámites de modificaciones, prorrogas, adiciones, suspensiones y demás\r\nmodificaciones contractuales solicitadas por la supervisión de los contratos u ordenador del gasto\r\ndel Centro de Formación.\r\n6\r\nGTH-F-075 V08\r\n8. Brind', 0, '0000'),
(76, '1. Orientar y acompañar en forma permanente e integral los\r\naprendices en el área, las competencias, resultados de aprendizaje y actividades en etapa lectiva y/o productiva de los\r\nproyectos de formación y/o proyectos productivos programados dentro de los tiempos que para cada acción de\r\nformación se determine por el Centro, correspondientes a la línea y red tecnológica de acuerdo a su perfil. 17 2.\r\nReportar en el aplicativo Sofía Plus en un plazo máximo de tres (3) días todas las actividades de acuerdo con los\r\nprocesos que son de su responsabilidad, garantizando la calidad de la información y su coherencia en el proceso\r\nformativo, tales como: a. registro de juicios evaluativos. b. asociación de aprendices a la ruta de formación. c.\r\nComunicar al Coordinador Académico oportunamente anomalías, inconsistencias, novedades de aprendices y\r\nhallazgos en el registro de la información, así como demás informes dentro de los plazos estipulados por el centro para\r\ntal efecto conforme a los lineamientos del Sistema Integrado de Gestión (SIG) del SENA el cual se encuentra\r\ndocumentado en la plataforma CompromISO. 3. Participar en la programación y ejecución del proceso de inducción\r\nde aprendices de formación titulada. 4. Responder por la integridad y buen uso de materiales, equipos y demás\r\nelementos de la institución puestos bajo su cuidado para desarrollar su objeto contractual. 5. Mantener el debido\r\nrespeto por la dignidad, intimidad e integridad de los miembros de la comunidad educativa, así como guardar lealtad\r\na la Institución, actuando de buena fe y conservando la debida r', 0, '0000'),
(77, '1. Proyectar los estudios previos y documentación a que haya lugar de cada una de las modalidades de selección y sus etapas precontractuales, contractuales y post contractuales que utilice el SENA en sus procesos contractuales 2. Apoyar en el seguimiento y control previo y posterior a los procesos de pago de los proveedores; en temas relacionados con, informes de ejecución y facturación de los contratos efectuados durante la vigencia 2024. 3. Apoyar la publicación de los procesos contractuales en las plataformas establecidas por Colombia Compra para la celebración de contratos del Centro de Formación. 4. Realizar estudios de mercados, presupuestos y análisis del sector para los procesos contractuales de la entidad. 5. Elaborar reportes e informes de carácter técnico y estadístico del proceso de gestión contractual, con el propósito de evidenciar la gestión realizada en el proceso 6. Realizar acciones de gestión y seguimiento al cumplimiento de la ejecución de los procesos de adquisición de los bienes, servicios personales directos e indirectos a contratar por parte de la entidad. 7. Apoyar las actualizaciones o modificaciones del Plan Anual de Adquisiciones 8. Mantener la debida reserva sobre los asuntos manejados y conocidos dentro de la ejecución del contrato. 9. Apoyar en las actividades de planeación propias del Centro de formación con el fin de dar cumplimiento de las metas establecidas10. Realizarlas demás actividades relacionadas con el objeto del contrato que le sean asignadas por el supervisor y/o el Subdirector del centro que correspondan a la naturaleza del contr', 0, '0000'),
(78, '1. Implementar acciones necesarias para la ejecución del PNIBA con aprendices de los programas\r\nasociados a economía popular y CampeSENA, garantizando una estrategia de atención diferencial,\r\nintegral e incluyente que permita el fortalecimiento de la asociatividad, organización, participación\r\ny reconocimiento social.\r\n2. Realizar actividades que ayuden a la identificación de las necesidades del sector productivo frente\r\na las competencias o habilidades para la vida de los aprendices de los programas asociados a\r\neconomía POPULAR y CampeSENA, en teniendo en cuenta la política de atención pluralista y\r\ndiferencial, de acuerdo con sus particularidades sociales, económicas y territoriales.\r\n3. Realizar acompañamiento a los aprendices de los programas asociados a ECONOMIA POPULAR y\r\nCampeSENA mediante talleres, foros, conversatorios y toda actividad lúdico-pedagógica enfocada a\r\n5\r\nGTH-F-075 V08\r\nfortalecer la asociatividad, participación, comunicación asertiva, trabajo en equipo, liderazgo,\r\nderechos humanos, cultura ambiental y organización comunitaria.\r\n4. Articular con las demás áreas del SENA a nivel de centro, regional y nacional, así como otras\r\nentidades públicas y privadas que permitan el intercambio de saberes, creación de nuevas empresas\r\ny desarrollo de habilidades emprendedoras en colectivo. Así como la cooperación para impulsar\r\nconjuntamente iniciativas de desarrollo rural y económico.\r\n5. Generar y articular acciones necesarias para la implementación y ejecución de los programas\r\nasociados a economía popular y CampeSENA y la presentación de los informes que se r', 0, '0000'),
(79, '1. Apoyar en la formulación, análisis de viabilidad y dimensionamiento de recursos para los\r\nproyectos de TIC de los Centros de Formación de conformidad con la planeación estratégica PETI,\r\noperativa vigente.\r\n2. Apoyar en las actividades de control y seguimiento a los diversos aliados encargados de los\r\ncomponentes de servicios TIC, articuladamente con los procesos y disposiciones administrativas de\r\nla Entidad, especialmente los emitidos por la Oficina de Sistemas de la Dirección General.\r\n3. Apoyar la gestión de activos de TI (ITAM) y demás activos digitales de la regional o centro\r\nde formación.\r\n4. Brindar acompañamiento técnico y asesoramiento a los niveles de servicio y gestión de la\r\nexperiencia digital a los usuarios de la regional o centro de formación.\r\n5. Gestionar informes, monitorear y evaluar el desempeño de los componentes de servicios\r\nTICS.\r\n6. Garantizar la alineación de los procesos tecnológicos con las estrategias de los lineamientos\r\nde gobierno de ti, políticas de seguridad de la información y la óptima protección de los activos\r\ndigitales.\r\n7. Facilitar procesos de gestión del cambio, asegurando que los usuarios finales se apropian\r\nadecuadamente de las nuevas tecnologías y procesos, minimizando la resistencia al cambio y\r\nmaximizando la adopción.\r\n5\r\nGTH-F-075 V08\r\n8. Verificar las actividades mantenimiento preventivo y correctivo de Hardware y Software de\r\nlos equipos ofimáticos e infraestructura tecnológica de la regional o centro de formación.\r\n9. Ejecutar un plan integral de acción que asegure la plena implementación y el riguroso\r\nseguimiento d', 0, '0000'),
(80, '1. Realizar la instalación y configuración de sistemas informáticos, aplicaciones de negocio y\r\nsistemas operativos.\r\n2. Ofrecer asistencia directa a los usuarios en las sedes regionales y centros de formación,\r\nresolviendo problemas de hardware, software y redes de telecomunicaciones.\r\n3. Registrar, priorizar y gestionar incidencias reportadas por los usuarios, así como atender\r\nsolicitudes de servicio relacionadas con componentes de servicio ofimáticos y demás infraestructura\r\ntecnológica.\r\n4. Actualizar la documentación técnica de sistemas, equipos y redes en las sedes regionales y centros\r\nde formación, incluyendo registros de configuración, procedimientos de mantenimiento y\r\nresolución de problemas.\r\n5. Ejecutar actividades programadas de mantenimiento para asegurar el funcionamiento óptimo de\r\nlos equipos y sistemas tecnológicos, además de intervenir rápidamente en caso de fallos o averías.\r\n6. Ofrecer orientación básica a los usuarios sobre el uso adecuado de los equipos y sistemas\r\ntecnológicos, así como proporcionar recomendaciones para mejorar la eficiencia y seguridad en el\r\nuso de la tecnología.\r\n7. Colaborar en la implementación y despliegue de nuevos servicios, redes o actualizaciones\r\ntecnológicas, minimizando el impacto en las operaciones.\r\n8. Interactuar con los proveedores externos de servicios y equipos tecnológicos para resolver\r\nproblemas o gestionar solicitudes que requieran soporte especializado.\r\n5\r\nGTH-F-075 V08\r\n9. Atender oportunamente los requerimientos que haga el supervisor del contrato y presentar los\r\ninformes. Priorizar las necesidades y req', 0, '0000'),
(81, '1. Apoyar técnicamente en la estructuración y evaluación de todos los procesos de\r\nmantenimiento, adecuación, construcción e infraestructura del Centro para la industria de la\r\ncomunicación Gráfica.\r\n2. Apoyar técnicamente a los supervisores de contrato de todos los procesos de mantenimiento,\r\nadecuación, construcción e infraestructura del Centro para la industria de la comunicación Gráfica.\r\n3. Realizar informes mensuales y/o en la periodicidad requerida del estado de la infraestructura\r\nfísica del centro.\r\n4. Apoyar en la definición de acciones predictivas, preventivas y correctivas de los posibles\r\neventos de daño en la infraestructura física del centro de formación.\r\n5\r\nGTH-F-075 V08\r\n5. Definir necesidades de mantenimiento, adecuación, construcción e infraestructura para ser\r\nincluidas en la proyección de la vigencias actual y posterior a la ejecución del contrato.\r\n6. Mantener la debida reserva sobre los asuntos manejados y conocidos dentro de la ejecución\r\ndel contrato.\r\n7. Realizar las demás actividades relacionadas con el objeto del contrato que le sean asignadas\r\npor el supervisor y/o el subdirector del centro que correspondan a la naturaleza del contrato.', 0, '0000'),
(82, '1. Proponer, desarrollar y hacer\r\nseguimiento al plan de trabajo que guíe la gestión de la biblioteca en las líneas: colecciones, servicios, extensión\r\ncultural y preservación de la memoria 2. Brindar a la comunidad educativa servicios de información innovadores\r\npara contribuir a la calidad de la formación profesional integral del Centro. 3. Planear y realizar talleres de\r\nformación de usuarios que faciliten y fomenten el acceso y uso de la información disponible en el Sistema de\r\nBibliotecas. 4. Identificar y difundir colecciones de acuerdo a las áreas o redes de conocimiento que atiende el\r\ncentro de formación. 5. Verificar que las colecciones se encuentren organizadas de acuerdo con el sistema de\r\nclasificación utilizado por el Sistema de Bibliotecas 6. Realizar la gestión de las colecciones físicas de apoyo a\r\nla formación profesional integral, lo cual incluye la adquisición, catalogación, evaluación y descarte de material.\r\n7. Programar, desarrollar y evaluar las actividades de extensión cultural - LEO en correspondencia con los\r\nlineamientos del Sistema de Bibliotecas. 8. Implementar los servicios de apoyo a la investigación de acuerdo\r\ncon las orientaciones del Sistema de Bibliotecas. 9. Identificar las publicaciones de autoría SENA que\r\ncontribuyan a la preservación de memoria institucional para su visibilización y disponibilidad desde el Repositorio\r\nInstitucional y el Portal de Revistas. 10. Elaborar y difundir informes de gestión de la biblioteca', 0, '0000'),
(83, '1. Realizar la instalación y configuración de sistemas informáticos, aplicaciones de negocio y\r\nsistemas operativos.\r\n2. Ofrecer asistencia directa a los usuarios en las sedes regionales y centros de formación,\r\nresolviendo problemas de hardware, software y redes de telecomunicaciones.\r\n3. Registrar, priorizar y gestionar incidencias reportadas por los usuarios, así como atender\r\nsolicitudes de servicio relacionadas con componentes de servicio ofimáticos y demás infraestructura\r\ntecnológica.\r\n4. Actualizar la documentación técnica de sistemas, equipos y redes en las sedes regionales y centros\r\nde formación, incluyendo registros de configuración, procedimientos de mantenimiento y\r\nresolución de problemas.\r\n5. Ejecutar actividades programadas de mantenimiento para asegurar el funcionamiento óptimo de\r\nlos equipos y sistemas tecnológicos, además de intervenir rápidamente en caso de fallos o averías.\r\n6. Ofrecer orientación básica a los usuarios sobre el uso adecuado de los equipos y sistemas\r\ntecnológicos, así como proporcionar recomendaciones para mejorar la eficiencia y seguridad en el\r\nuso de la tecnología.\r\n7. Colaborar en la implementación y despliegue de nuevos servicios, redes o actualizaciones\r\ntecnológicas, minimizando el impacto en las operaciones.\r\n8. Interactuar con los proveedores externos de servicios y equipos tecnológicos para resolver\r\nproblemas o gestionar solicitudes que requieran soporte especializado.\r\n9. Atender oportunamente los requerimientos que haga el supervisor del contrato y presentar los\r\ninformes. Priorizar las necesidades y requerimientos de los', 0, '0000'),
(84, 'a. Participar en la formación y capacitación continua para mejorar las habilidades técnicas y profesionales\r\nnecesarias para el proyecto.\r\nb. Colaborar en la redacción de informes y artículos científicos basados en la investigación realizada para\r\nsu publicación o presentación.\r\nc. Contribuir a la creación de manuales, guías de usuario y demás documentación técnica que constituya el\r\nproceso de creación del Museo Virtual.\r\nd. Participar en las diferentes reuniones y actividades programadas por la entidad y/o el centro de formación\r\na las que le sea notificada su participación, acerca de procesos, capacitaciones o avances del Museo Virtual.\r\ne. Organizar los elementos digitales (imágenes, videos, textos curatoriales, elementos 2D y 3D) que se\r\nreciban producto de la convocatoria para la participación de los centros de formación SENA.\r\nf. Apoyar la construcción de elementos digitales 2D y 3D que hagan parte de la interfaz, arquitectura y\r\nelementos que hacen parte del Museo Virtual.\r\ng. Mantener actualizada la documentación que corresponda a las diferentes fases del proyecto de Museo\r\nVirtual, a la investigación realizada y los hallazgos relevantes\r\nh. Participar y proponer actividades propias del semillero de investigación adscrito a SENNOVA.', 0, '0000'),
(85, '1. Realizar la instalación y configuración de sistemas informáticos, aplicaciones de negocio y sistemas\r\noperativos.\r\n2. Ofrecer asistencia directa a los usuarios en las sedes regionales y centros de formación, resolviendo\r\nproblemas de hardware, software y redes de telecomunicaciones.\r\n3. Registrar, priorizar y gestionar incidencias reportadas por los usuarios, así como atender solicitudes de servicio\r\nrelacionadas con componentes de servicio ofimáticos y demás infraestructura tecnológica.\r\n4. Actualizar la documentación técnica de sistemas, equipos y redes en las sedes regionales y centros de\r\nformación, incluyendo registros de configuración, procedimientos de mantenimiento y resolución de problemas.\r\n5. Ejecutar actividades programadas de mantenimiento para asegurar el funcionamiento óptimo de los equipos\r\ny sistemas tecnológicos, además de intervenir rápidamente en caso de fallos o averías.\r\n6. Ofrecer orientación básica a los usuarios sobre el uso adecuado de los equipos y sistemas tecnológicos, así\r\ncomo proporcionar recomendaciones para mejorar la eficiencia y seguridad en el uso de la tecnología.\r\n7. Colaborar en la implementación y despliegue de nuevos servicios, redes o actualizaciones tecnológicas,\r\nminimizando el impacto en las operaciones.\r\n8. Interactuar con los proveedores externos de servicios y equipos tecnológicos para resolver problemas o\r\ngestionar solicitudes que requieran soporte especializado.\r\n9. Atender oportunamente los requerimientos que haga el supervisor del contrato y presentar los informes.\r\nPriorizar las necesidades y requerimientos de los us', 0, '0000'),
(86, ' 1. Orientar y acompañar en forma permanente e integral los\r\naprendices en el área, las competencias, resultados de aprendizaje y actividades en etapa lectiva y/o productiva de los\r\nproyectos de formación y/o proyectos productivos programados dentro de los tiempos que para cada acción de\r\nformación se determine por el Centro, correspondientes a la línea y red tecnológica de acuerdo a su perfil. 17 2.\r\nReportar en el aplicativo Sofía Plus en un plazo máximo de tres (3) días todas las actividades de acuerdo con los\r\nprocesos que son de su responsabilidad, garantizando la calidad de la información y su coherencia en el proceso\r\nformativo, tales como: a. registro de juicios evaluativos. b. asociación de aprendices a la ruta de formación. c.\r\nComunicar al Coordinador Académico oportunamente anomalías, inconsistencias, novedades de aprendices y\r\nhallazgos en el registro de la información, así como demás informes dentro de los plazos estipulados por el centro para\r\ntal efecto conforme a los lineamientos del Sistema Integrado de Gestión (SIG) del SENA el cual se encuentra\r\ndocumentado en la plataforma CompromISO. 3. Participar en la programación y ejecución del proceso de inducción\r\nde aprendices de formación titulada. 4. Responder por la integridad y buen uso de materiales, equipos y demás\r\nelementos de la institución puestos bajo su cuidado para desarrollar su objeto contractual. 5. Mantener el debido\r\nrespeto por la dignidad, intimidad e integridad de los miembros de la comunidad educativa, así como guardar lealtad\r\na la Institución, actuando de buena fe y conservando la debida ', 0, '0000'),
(87, '1. Recibir, analizar y verificar la documentación soporte para el registro contable en el sistema de información\r\nSIIF nación de contratistas, proveedores, apoyos de sostenimiento, monitorias, servicios públicos, impuestos,\r\nproveedor Sena-Sena y demás que se requiera.\r\n2. Asistir en la generación de informes contables requeridos por las dependencias del Sena y/o entes de control.\r\n3. Colaborar en la presentación y remitir la conciliación de la cuenta 138413001 – Devolución de IVA Entidades\r\nde Educación Superior- la cual deberá cargarse en el FTP a más tardar los primeros quince días calendario del\r\nmes siguiente al cierre de cada bimestre de acuerdo a las directrices de la Entidad.\r\n4. Remitir por correo electrónico institucional a contabilidad de la Dirección Regional, los primeros quince días\r\ncalendario del mes siguiente al cierre del bimestre, el formato de las obligaciones del IVA que quedan pendiente\r\nde pago al cierre de cada bimestre (cuentas por pagar de IVA) de acuerdo a las directrices de la Entidad.\r\n5. Colaborar en la verificación mensual de saldos negativos por terceros o cuantías menores en la cuenta\r\n138413001 – Devolución de IVA Entidades de Educación Superior.\r\n6. Apoyar con oportunidad el registro de todas las deducciones de impuestos por concepto de retención en la\r\nfuente a título de renta, IVA e ICA, estampillas, contribución de obra pública y estampilla pro-universidad Nacional\r\nde Colombia.\r\n7. Efectuar seguimiento y depuración a los saldos contables reflejados mensualmente por concepto de viáticos,\r\ny cuentas por pagar bienes y servicios.\r\n8. Adel', 0, '0000'),
(88, '1. Orientar y acompañar en forma permanente e integral los\r\naprendices en el área, las competencias, resultados de aprendizaje y actividades en etapa lectiva y/o productiva de los\r\nproyectos de formación y/o proyectos productivos programados dentro de los tiempos que para cada acción de\r\nformación se determine por el Centro, correspondientes a la línea y red tecnológica de acuerdo a su perfil. 2. Reportar\r\nen el aplicativo Sofía Plus en un plazo máximo de tres (3) días todas las actividades de acuerdo con los procesos que\r\nson de su responsabilidad, garantizando la calidad de la información y su coherencia en el proceso formativo, tales\r\ncomo: a. registro de juicios evaluativos. b. asociación de aprendices a la ruta de formación. c. Comunicar al\r\nCoordinador Académico oportunamente anomalías, inconsistencias, novedades de aprendices y hallazgos en el\r\nregistro de la información, así como demás informes dentro de los plazos estipulados por el centro para tal efecto\r\nconforme a los lineamientos del Sistema Integrado de Gestión (SIG) del SENA el cual se encuentra documentado en la\r\nplataforma CompromISO. 3. Participar en la programación y ejecución del proceso de inducción de aprendices de\r\nformación titulada. 4. Responder por la integridad y buen uso de materiales, equipos y demás elementos de la\r\ninstitución puestos bajo su cuidado para desarrollar su objeto contractual. 5. Mantener el debido respeto por la\r\ndignidad, intimidad e integridad de los miembros de la comunidad educativa, así como guardar lealtad a la Institución,\r\nactuando de buena fe y conservando la debida rese', 0, '0000'),
(89, '1. Orientar y acompañar en forma permanente e integral los\r\naprendices en el área, las competencias, resultados de aprendizaje y actividades en etapa lectiva y/o productiva de los\r\nproyectos de formación y/o proyectos productivos programados dentro de los tiempos que para cada acción de\r\nformación se determine por el Centro, correspondientes a la línea y red tecnológica de acuerdo a su perfil. 2. Reportar\r\nen el aplicativo Sofía Plus en un plazo máximo de tres (3) días todas las actividades de acuerdo con los procesos que\r\nson de su responsabilidad, garantizando la calidad de la información y su coherencia en el proceso formativo, tales\r\ncomo: a. registro de juicios evaluativos. b. asociación de aprendices a la ruta de formación. c. Comunicar al\r\nCoordinador Académico oportunamente anomalías, inconsistencias, novedades de aprendices y hallazgos en el\r\nregistro de la información, así como demás informes dentro de los plazos estipulados por el centro para tal efecto\r\nconforme a los lineamientos del Sistema Integrado de Gestión (SIG) del SENA el cual se encuentra documentado en la\r\nplataforma CompromISO. 3. Participar en la programación y ejecución del proceso de inducción de aprendices de\r\nformación titulada. 4. Responder por la integridad y buen uso de materiales, equipos y demás elementos de la\r\ninstitución puestos bajo su cuidado para desarrollar su objeto contractual. 5. Mantener el debido respeto por la\r\ndignidad, intimidad e integridad de los miembros de la comunidad educativa, así como guardar lealtad a la Institución,\r\nactuando de buena fe y conservando la debida rese', 0, '0000'),
(90, '1- Apoyar el desarrollo del sistema (estructura Back end y Front end) que permita la comunicación,\r\nvisualización y filtro de la información contenida en la base de datos diseñada para la gestión del sistema.\r\n2- Apoyar la creación de la estructura metodológica para la presentación y publicación de los proyectos\r\nformativos del área en contenidos digitales con el fin de establecer un estándar de presentación y publicación a\r\nnivel regional.\r\n3- Apoyar la recopilación y clasificación de los proyectos formativos realizados en los últimos 5 años\r\nresultado del proceso formativo culminado en la etapa lectiva de aprendices e instructores de los programas de\r\nformación en el área de contenidos digitales en la regional.\r\n4- Comunicar a los autores del proyecto de todo cambio en el proceso de evolución del sistema tanto en\r\nback-end como en front-end.\r\n5- Incorporar mejoras en el código con buenas prácticas, documentando debidamente su cambio y mejora,\r\nestableciendo versionamiento del sistema.\r\n6- Colaborar en la implementación de medidas de seguridad informática para proteger la integridad y\r\nconfidencialidad de los datos almacenados en el sistema, siguiendo las normativas y estándares establecidos\r\npor la institución.\r\n7- Participar en sesiones de revisión de código y reuniones de equipo para discutir progresos, identificar\r\nposibles problemas y proponer soluciones que mejoren la eficiencia y funcionalidad del sistema.\r\n8- Contribuir en la realización de pruebas de calidad del software, tanto manuales como automatizadas, para\r\ngarantizar el correcto funcionamiento del sistema y ', 0, '0000'),
(91, '1.Apoyar los procesos de producción del Centro\r\nde Formación, en las áreas de impresión de acuerdo a los requerimientos del cliente. 2. Imprimir productos\r\ngráficos de acuerdo a las órdenes de producción, verificando condiciones de calidad. 3. Velar por el cumplimiento\r\nde los plazos y horas de entregas establecidas para la impresión, envió y entrega de los impresos bajo su cargo.\r\n4. Garantizar la calidad de impresión de los productos, incluyendo la consistencia del color, el registro adecuado\r\ny la resolución de impresión, y/o finalización de productos impresos. 5.Apoyar en el monitoreo a los aprendices\r\nen etapa productivo que apoyan el proceso de producción de centros 6.Mantener registros precisos de la\r\nproducción, incluyendo la cantidad de productos impresos, problemas encontrados y acciones tomadas.\r\n7.Entregar por escrito los informes que se le soliciten de las actividades realizadas conforme con el objeto\r\ncontractual y asistir a las reuniones y/o comités programados cuando sea requerido o asignado. 8.Ejecutar de\r\nmanera idónea el objeto del contrato conforme a los lineamientos del Sistema Integrado de Gestión y Autocontrol\r\n(SIGA) del SENA, el cual se encuentra documentado en la plataforma compromiso. 9. Mantener la debida\r\nreserva sobre los asuntos manejados y conocidos dentro de la ejecución de contrato. 10. Realizar las demás\r\nactividades relacionadas con el objeto del contrato que le sean asignadas por el supervisor y/o el Subdirector\r\ndel centro que correspondan a la naturaleza del contrato', 0, '0000');
INSERT INTO `obligacionesespecificas` (`id`, `nombre`, `idObjeto`, `año`) VALUES
(92, '1. Realizar la instalación y configuración de sistemas informáticos, aplicaciones de negocio y sistemas\r\noperativos.\r\n2. Ofrecer asistencia directa a los usuarios en las sedes regionales y centros de formación, resolviendo\r\nproblemas de hardware, software y redes de telecomunicaciones.\r\n3. Registrar, priorizar y gestionar incidencias reportadas por los usuarios, así como atender solicitudes de servicio\r\nrelacionadas con componentes de servicio ofimáticos y demás infraestructura tecnológica.\r\n4. Actualizar la documentación técnica de sistemas, equipos y redes en las sedes regionales y centros de\r\nformación, incluyendo registros de configuración, procedimientos de mantenimiento y resolución de problemas.\r\n5. Ejecutar actividades programadas de mantenimiento para asegurar el funcionamiento óptimo de los equipos\r\ny sistemas tecnológicos, además de intervenir rápidamente en caso de fallos o averías.\r\n6. Ofrecer orientación básica a los usuarios sobre el uso adecuado de los equipos y sistemas tecnológicos, así\r\ncomo proporcionar recomendaciones para mejorar la eficiencia y seguridad en el uso de la tecnología.\r\n7. Colaborar en la implementación y despliegue de nuevos servicios, redes o actualizaciones tecnológicas,\r\nminimizando el impacto en las operaciones.\r\n8. Interactuar con los proveedores externos de servicios y equipos tecnológicos para resolver problemas o\r\ngestionar solicitudes que requieran soporte especializado.\r\n9. Atender oportunamente los requerimientos que haga el supervisor del contrato y presentar los informes.\r\nPriorizar las necesidades y requerimientos de los us', 1, '0000');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rh`
--

CREATE TABLE `rh` (
  `id` int(11) NOT NULL,
  `tipoRh` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rh`
--

INSERT INTO `rh` (`id`, `tipoRh`) VALUES
(1, 'AB+'),
(2, 'AB- '),
(3, 'A+'),
(4, 'A-'),
(5, 'B+'),
(6, 'B-'),
(7, 'O+'),
(8, 'O-');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rolesusuarios`
--

CREATE TABLE `rolesusuarios` (
  `id` int(11) NOT NULL,
  `nombreRol` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rolesusuarios`
--

INSERT INTO `rolesusuarios` (`id`, `nombreRol`) VALUES
(1, 'SuperUsuario'),
(2, 'Administrador'),
(3, 'Contratista');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipodecontrato`
--

CREATE TABLE `tipodecontrato` (
  `id` int(11) NOT NULL,
  `nombreTipoContrato` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipodecontrato`
--

INSERT INTO `tipodecontrato` (`id`, `nombreTipoContrato`) VALUES
(1, 'Termino indefinido '),
(2, 'Contrato de aprendizaje'),
(4, 'Contrato por obra o labor'),
(5, 'Contrato de trabajo a término fijo'),
(6, 'Contrato temporal, ocasional o accidental');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipodecuenta`
--

CREATE TABLE `tipodecuenta` (
  `id` int(11) NOT NULL,
  `nombreTipoCuenta` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipodecuenta`
--

INSERT INTO `tipodecuenta` (`id`, `nombreTipoCuenta`) VALUES
(1, 'Debito'),
(2, 'Credito');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipodedocumento`
--

CREATE TABLE `tipodedocumento` (
  `id` int(11) NOT NULL,
  `numeroCedula` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipodedocumento`
--

INSERT INTO `tipodedocumento` (`id`, `numeroCedula`) VALUES
(1, 'CEDULA DE CIUDADANIA'),
(2, 'Cédula de extranjería'),
(3, 'Carné de identidad'),
(4, 'Tarjeta de identidad');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `numeroCedulaCliente` int(11) NOT NULL,
  `idRol` int(11) NOT NULL,
  `correoCli` varchar(255) NOT NULL,
  `contraseñaCli` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `numeroCedulaCliente`, `idRol`, `correoCli`, `contraseñaCli`) VALUES
(46, 1032937438, 1, 'm@', '$2b$12$PP/LLr0mTuRqy.Bl/ywJ1ezBaQV8k.PYOp5oYL6q/hyBqhhnSUlmW'),
(47, 12, 1, 'b@', '$2b$12$Hxcpd1Q801pHR8IPjqnr.eKJe8hJ85aMlw.a6H2WCIfZcw17PEp5W'),
(48, 6789, 2, 'q@', '$2b$12$XzHXcjVJ7gkbzABX7ltX/ugCgH7JsodIYy6VuBxGxkZ2W65ylxTSG');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `arl`
--
ALTER TABLE `arl`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `banco`
--
ALTER TABLE `banco`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tipoCuenta` (`tipoCuenta`);

--
-- Indices de la tabla `cargo`
--
ALTER TABLE `cargo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idJefe` (`idJefe`);

--
-- Indices de la tabla `ciudad`
--
ALTER TABLE `ciudad`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Estado` (`Estado`),
  ADD KEY `tipoDocumento` (`tipoDocumento`),
  ADD KEY `idBanco` (`idBanco`),
  ADD KEY `Rh` (`Rh`),
  ADD KEY `genero` (`genero`),
  ADD KEY `ciudadExpedicion` (`ciudadExpedicion`),
  ADD KEY `departamentoExpedicion` (`departamentoExpedicion`),
  ADD KEY `ARL` (`ARL`),
  ADD KEY `EPS` (`EPS`),
  ADD KEY `usuarioCreador` (`usuarioCreador`);

--
-- Indices de la tabla `contrato`
--
ALTER TABLE `contrato`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idTipoContrato` (`idTipoContrato`),
  ADD KEY `idCargo` (`idCargo`),
  ADD KEY `idClientes` (`idClientes`),
  ADD KEY `idDependecia` (`idDependecia`),
  ADD KEY `idObjeto` (`idObjeto`),
  ADD KEY `ObEspCon` (`ObEspCon`);

--
-- Indices de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `dependencia`
--
ALTER TABLE `dependencia`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `eps`
--
ALTER TABLE `eps`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `estado`
--
ALTER TABLE `estado`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `genero`
--
ALTER TABLE `genero`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `jefe`
--
ALTER TABLE `jefe`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `objeto`
--
ALTER TABLE `objeto`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `obligacionesespecificas`
--
ALTER TABLE `obligacionesespecificas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idObjeto` (`idObjeto`);

--
-- Indices de la tabla `rh`
--
ALTER TABLE `rh`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `rolesusuarios`
--
ALTER TABLE `rolesusuarios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tipodecontrato`
--
ALTER TABLE `tipodecontrato`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tipodecuenta`
--
ALTER TABLE `tipodecuenta`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tipodedocumento`
--
ALTER TABLE `tipodedocumento`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `numeroCedulaCliente` (`numeroCedulaCliente`),
  ADD KEY `idRol` (`idRol`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `arl`
--
ALTER TABLE `arl`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1032937439;

--
-- AUTO_INCREMENT de la tabla `banco`
--
ALTER TABLE `banco`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5566;

--
-- AUTO_INCREMENT de la tabla `cargo`
--
ALTER TABLE `cargo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=313214;

--
-- AUTO_INCREMENT de la tabla `ciudad`
--
ALTER TABLE `ciudad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `contrato`
--
ALTER TABLE `contrato`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=68;

--
-- AUTO_INCREMENT de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT de la tabla `dependencia`
--
ALTER TABLE `dependencia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT de la tabla `eps`
--
ALTER TABLE `eps`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT de la tabla `estado`
--
ALTER TABLE `estado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `genero`
--
ALTER TABLE `genero`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `jefe`
--
ALTER TABLE `jefe`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55465;

--
-- AUTO_INCREMENT de la tabla `objeto`
--
ALTER TABLE `objeto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=90;

--
-- AUTO_INCREMENT de la tabla `obligacionesespecificas`
--
ALTER TABLE `obligacionesespecificas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=107;

--
-- AUTO_INCREMENT de la tabla `rh`
--
ALTER TABLE `rh`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `rolesusuarios`
--
ALTER TABLE `rolesusuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `tipodecontrato`
--
ALTER TABLE `tipodecontrato`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=146;

--
-- AUTO_INCREMENT de la tabla `tipodecuenta`
--
ALTER TABLE `tipodecuenta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `tipodedocumento`
--
ALTER TABLE `tipodedocumento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `banco`
--
ALTER TABLE `banco`
  ADD CONSTRAINT `banco_ibfk_1` FOREIGN KEY (`tipoCuenta`) REFERENCES `tipodecuenta` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `cargo`
--
ALTER TABLE `cargo`
  ADD CONSTRAINT `cargo_ibfk_1` FOREIGN KEY (`idJefe`) REFERENCES `jefe` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD CONSTRAINT `clientes_ibfk_1` FOREIGN KEY (`tipoDocumento`) REFERENCES `tipodedocumento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `clientes_ibfk_10` FOREIGN KEY (`usuarioCreador`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `clientes_ibfk_2` FOREIGN KEY (`departamentoExpedicion`) REFERENCES `departamentos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `clientes_ibfk_3` FOREIGN KEY (`ciudadExpedicion`) REFERENCES `ciudad` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `clientes_ibfk_4` FOREIGN KEY (`genero`) REFERENCES `genero` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `clientes_ibfk_5` FOREIGN KEY (`Rh`) REFERENCES `rh` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `clientes_ibfk_6` FOREIGN KEY (`ARL`) REFERENCES `arl` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `clientes_ibfk_7` FOREIGN KEY (`EPS`) REFERENCES `eps` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `clientes_ibfk_8` FOREIGN KEY (`idBanco`) REFERENCES `banco` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `clientes_ibfk_9` FOREIGN KEY (`Estado`) REFERENCES `estado` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `contrato`
--
ALTER TABLE `contrato`
  ADD CONSTRAINT `contrato_ibfk_1` FOREIGN KEY (`idTipoContrato`) REFERENCES `tipodecontrato` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `contrato_ibfk_2` FOREIGN KEY (`idCargo`) REFERENCES `cargo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `contrato_ibfk_3` FOREIGN KEY (`idDependecia`) REFERENCES `dependencia` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `contrato_ibfk_4` FOREIGN KEY (`idClientes`) REFERENCES `clientes` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `contrato_ibfk_5` FOREIGN KEY (`idObjeto`) REFERENCES `objeto` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `contrato_ibfk_6` FOREIGN KEY (`ObEspCon`) REFERENCES `obligacionesespecificas` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `obligacionesespecificas`
--
ALTER TABLE `obligacionesespecificas`
  ADD CONSTRAINT `obligacionesespecificas_ibfk_1` FOREIGN KEY (`idObjeto`) REFERENCES `objeto` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`idRol`) REFERENCES `rolesusuarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
