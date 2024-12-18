USE Financas;

CREATE TABLE `usuarios` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `senha` VARCHAR(255),
  `autenticador` VARCHAR(255),
  `nome` VARCHAR(255),
  `email` VARCHAR(255)
);

CREATE TABLE `contas` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `nome_banco` VARCHAR(255),
  `tipo` CHAR(1) NOT NULL,
  `valor` INT
);

CREATE TABLE `usuario_conta` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `fk_usuario` INT,
  `fk_conta` INT,
  `data_vinculo` DATETIME,
  `valida` BOOLEAN
);

CREATE TABLE `movimentacoes` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `conta_fim` INT,
  `conta_ini` INT,
  `valor` INT,
  `data` DATETIME
);

CREATE TABLE `rotina` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `conta_fim` INT,
  `conta_ini` INT,
  `valor` INT,
  `tipo` CHAR(1),
  `data_prox` DATETIME
);

CREATE TABLE `investimentos` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `fk_conta` INT,
  `data_ini` DATE,
  `cod` VARCHAR(255),
  `valor` INT
);

ALTER TABLE `usuario_conta` ADD FOREIGN KEY (`fk_usuario`) REFERENCES `usuarios` (`id`);
ALTER TABLE `usuario_conta` ADD FOREIGN KEY (`fk_conta`) REFERENCES `contas` (`id`);

ALTER TABLE `movimentacoes` ADD FOREIGN KEY (`conta_fim`) REFERENCES `contas` (`id`);
ALTER TABLE `movimentacoes` ADD FOREIGN KEY (`conta_ini`) REFERENCES `contas` (`id`);

ALTER TABLE `rotina` ADD FOREIGN KEY (`conta_fim`) REFERENCES `contas` (`id`);
ALTER TABLE `rotina` ADD FOREIGN KEY (`conta_ini`) REFERENCES `contas` (`id`);

ALTER TABLE `investimentos` ADD FOREIGN KEY (`fk_conta`) REFERENCES `contas` (`id`);
