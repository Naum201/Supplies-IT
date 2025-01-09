
-- --------------------------------------------------------

--
-- Estrutura para tabela `movimento`
--

DROP TABLE IF EXISTS `movimento`;
CREATE TABLE IF NOT EXISTS `movimento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data` datetime DEFAULT NULL,
  `sede_id` int(11) DEFAULT NULL,
  `setor_id` int(11) DEFAULT NULL,
  `tipo_material_id` int(11) DEFAULT NULL,
  `tipo_objeto_id` int(11) DEFAULT NULL,
  `quantidade` int(11) DEFAULT NULL,
  `movimento` enum('Entrada','Saída') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sede_id` (`sede_id`),
  KEY `setor_id` (`setor_id`),
  KEY `tipo_material_id` (`tipo_material_id`),
  KEY `tipo_objeto_id` (`tipo_objeto_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tabela truncada antes do insert `movimento`
--

TRUNCATE TABLE `movimento`;