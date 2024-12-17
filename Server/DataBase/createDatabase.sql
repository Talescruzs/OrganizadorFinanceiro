USE Financas;

CREATE TABLE `usuarios` (
  `id` int PRIMARY KEY,
  `senha` hash NOT NULL,
  `autenticador` hash NOT NULL,
  `nome` varchar2 NOT NULL,
  `email` varchar2
);

CREATE TABLE `contas` (
  `id` int PRIMARY KEY,
  `nome_banco` varchar2,
  `tipo` char NOT NULL,
  `valor` int
);

CREATE TABLE `usuario_conta` (
  `id` int PRIMARY KEY,
  `fk_usuario` int,
  `fk_conta` int,
  `data_vinculo` datetime,
  `valida` bool
);

CREATE TABLE `movimentacoes` (
  `id` int PRIMARY KEY,
  `conta_fim` int,
  `conta_ini` int,
  `valor` int,
  `data` datetime
);

CREATE TABLE `rotina` (
  `id` int PRIMARY KEY,
  `conta_fim` int,
  `conta_ini` int,
  `valor` int,
  `tipo` char,
  `data_prox` datetime
);

CREATE TABLE `investimentos` (
  `id` int PRIMARY KEY,
  `fk_conta` int,
  `data_ini` date,
  `cod` varchar2,
  `valor` int
);

ALTER TABLE `usuario_conta` ADD FOREIGN KEY (`fk_usuario`) REFERENCES `usuarios` (`id`);

ALTER TABLE `usuario_conta` ADD FOREIGN KEY (`fk_conta`) REFERENCES `contas` (`id`);

ALTER TABLE `movimentacoes` ADD FOREIGN KEY (`conta_fim`) REFERENCES `contas` (`id`);

ALTER TABLE `movimentacoes` ADD FOREIGN KEY (`conta_ini`) REFERENCES `contas` (`id`);

ALTER TABLE `rotina` ADD FOREIGN KEY (`conta_fim`) REFERENCES `contas` (`id`);

ALTER TABLE `rotina` ADD FOREIGN KEY (`conta_ini`) REFERENCES `contas` (`id`);

ALTER TABLE `investimentos` ADD FOREIGN KEY (`fk_conta`) REFERENCES `contas` (`id`);