
-- --------------------------------------------------------

--
-- Estrutura para tabela `sede`
--

DROP TABLE IF EXISTS `sede`;
CREATE TABLE IF NOT EXISTS `sede` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `tipo` enum('Matriz','Filial') DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nome` (`nome`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tabela truncada antes do insert `sede`
--

TRUNCATE TABLE `sede`;
--
-- Despejando dados para a tabela `sede`
--

INSERT DELAYED IGNORE INTO `sede` (`id`, `nome`, `tipo`) VALUES(1, 'SVI - COROADO', 'Matriz');
INSERT DELAYED IGNORE INTO `sede` (`id`, `nome`, `tipo`) VALUES(2, 'SVI - BOULEVARD', 'Filial');
