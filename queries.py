CREATE_BANK_TABLE = """
CREATE TABLE IF NOT EXISTS bank_accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    balance DECIMAL(12, 2) DEFAULT 0.00,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
"""

INSERT_BANK_ACCOUNT = "INSERT INTO bank_accounts (user_id, balance) VALUES (%s, %s);"
GET_ACCOUNT_BY_USER = "SELECT * FROM bank_accounts WHERE user_id = %s;"
UPDATE_BALANCE = "UPDATE bank_accounts SET balance = %s WHERE user_id = %s;"

