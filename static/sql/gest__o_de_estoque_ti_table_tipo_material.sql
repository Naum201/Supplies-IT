
-- --------------------------------------------------------

--
-- Estrutura para tabela `tipo_material`
--

DROP TABLE IF EXISTS `tipo_material`;
CREATE TABLE IF NOT EXISTS `tipo_material` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `icone` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nome` (`nome`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tabela truncada antes do insert `tipo_material`
--

TRUNCATE TABLE `tipo_material`;
--
-- Despejando dados para a tabela `tipo_material`
--

INSERT DELAYED IGNORE INTO `tipo_material` (`id`, `nome`, `icone`) VALUES(2, 'Computadores', 'bi bi-pc-display-horizontal');
INSERT DELAYED IGNORE INTO `tipo_material` (`id`, `nome`, `icone`) VALUES(5, 'Impressoras', 'bi bi-printer-fill');
INSERT DELAYED IGNORE INTO `tipo_material` (`id`, `nome`, `icone`) VALUES(6, 'Monitores', 'bi bi-display');
INSERT DELAYED IGNORE INTO `tipo_material` (`id`, `nome`, `icone`) VALUES(7, 'Suprimentos - Impressora', 'bi bi-droplet-half');
