USE Financas;

CREATE TABLE IF NOT EXISTS Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    senha VARCHAR(45) NOT NULL
);

CREATE TABLE IF NOT EXISTS Contas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    banco VARCHAR(100) NOT NULL,
    tipo VARCHAR(1),
    saldo float NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Rotinas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(1) NOT NULL,
    tipo_repeticao VARCHAR(1) NOT NULL,
    valor FLOAT NOT NULL,
    data_base TIMESTAMP NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    foi_add_manual INT NOT NULL,
    descricao VARCHAR(300),
    id_conta INT,
    FOREIGN KEY (id_conta) REFERENCES Contas(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Historico (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tipo VARCHAR(1) NOT NULL,
    valor FLOAT,
    descricao VARCHAR(300),
    id_conta INT,
    FOREIGN KEY (id_conta) REFERENCES Contas(id) ON DELETE CASCADE
);