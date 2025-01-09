
-- --------------------------------------------------------

--
-- Estrutura para tabela `setor`
--

DROP TABLE IF EXISTS `setor`;
CREATE TABLE IF NOT EXISTS `setor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `sede_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sede_id` (`sede_id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tabela truncada antes do insert `setor`
--

TRUNCATE TABLE `setor`;
--
-- Despejando dados para a tabela `setor`
--

INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(1, 'Administração', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(2, 'Compras', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(3, 'Dept. Pessoal', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(4, 'Embalagem', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(5, 'Estoque S4', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(6, 'Estoque Automação', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(7, 'Estoque Anexo', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(8, 'Estoque CD', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(9, 'Fiscal', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(10, 'Financeiro', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(11, 'Logística', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(12, 'Marketing', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(13, 'Mezanino', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(14, 'RH', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(15, 'Recebimento', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(16, 'Salão', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(17, 'Vendas', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(18, 'SGI', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(19, 'Segurança', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(20, 'Trabalho', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(21, 'Televendas', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(22, 'TI', 1);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(24, 'Administração', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(25, 'Compras', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(26, 'Dept. Pessoal', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(27, 'Embalagem', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(28, 'Estoque S4', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(29, 'Estoque Automação', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(30, 'Estoque Anexo', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(31, 'Estoque CD', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(32, 'Fiscal', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(33, 'Financeiro', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(34, 'Logística', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(35, 'Marketing', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(36, 'Mezanino', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(37, 'RH', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(38, 'Recebimento', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(39, 'Salão', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(40, 'Vendas', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(41, 'SGI', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(42, 'Segurança', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(43, 'Trabalho', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(44, 'Televendas', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(45, 'TI', 2);
INSERT DELAYED IGNORE INTO `setor` (`id`, `nome`, `sede_id`) VALUES(46, 'Administração', 2);
