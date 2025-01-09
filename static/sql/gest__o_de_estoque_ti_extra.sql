
--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `movimento`
--
ALTER TABLE `movimento`
  ADD CONSTRAINT `movimento_ibfk_1` FOREIGN KEY (`sede_id`) REFERENCES `sede` (`id`),
  ADD CONSTRAINT `movimento_ibfk_2` FOREIGN KEY (`setor_id`) REFERENCES `setor` (`id`),
  ADD CONSTRAINT `movimento_ibfk_3` FOREIGN KEY (`tipo_material_id`) REFERENCES `tipo_material` (`id`),
  ADD CONSTRAINT `movimento_ibfk_4` FOREIGN KEY (`tipo_objeto_id`) REFERENCES `tipo_objeto` (`id`);

--
-- Restrições para tabelas `setor`
--
ALTER TABLE `setor`
  ADD CONSTRAINT `setor_ibfk_1` FOREIGN KEY (`sede_id`) REFERENCES `sede` (`id`);

--
-- Restrições para tabelas `tipo_objeto`
--
ALTER TABLE `tipo_objeto`
  ADD CONSTRAINT `tipo_objeto_ibfk_1` FOREIGN KEY (`tipo_material_id`) REFERENCES `tipo_material` (`id`);
