CREATE TABLE clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_admin SMALLINT(1) DEFAULT 0
);

CREATE TABLE shipments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    weight INT NOT NULL,
    size INT NOT NULL,
    price FLOAT NOT NULL,
    status VARCHAR(255) NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id)
);

