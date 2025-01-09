
-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_objeto`
--

DROP TABLE IF EXISTS `tipo_objeto`;
CREATE TABLE IF NOT EXISTS `tipo_objeto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `tipo_material_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nome` (`nome`),
  KEY `tipo_material_id` (`tipo_material_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tabela truncada antes do insert `tipo_objeto`
--

TRUNCATE TABLE `tipo_objeto`;