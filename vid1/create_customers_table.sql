DROP TABLE IF EXISTS Customers CASCADE;
DROP TABLE IF EXISTS Products CASCADE;
DROP TABLE IF EXISTS Orders CASCADE;

-- Create tables
CREATE TABLE Customers (
  customer_id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  address VARCHAR(100)
);

CREATE TABLE Products (
  product_id INT PRIMARY KEY,
  name VARCHAR(100),
  price DECIMAL(10, 2),
  description VARCHAR(200)
);

CREATE TABLE Orders (
  order_id INT PRIMARY KEY,
  customer_id INT,
  product_id INT,
  quantity INT,
  order_date DATE,
  FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
  FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Populate Customers table
INSERT INTO Customers (customer_id, name, email, address)
VALUES
  (1, 'John Doe', 'john@example.com', '123 Main St'),
  (2, 'Jane Smith', 'jane@example.com', '456 Elm St'),
  (3, 'Mike Johnson', 'mike@example.com', '789 Oak St');

-- Populate Products table
INSERT INTO Products (product_id, name, price, description)
VALUES
  (1, 'T-Shirt', 19.99, 'Comfortable cotton t-shirt'),
  (2, 'Jeans', 49.99, 'Slim-fit denim jeans'),
  (3, 'Sneakers', 79.99, 'Running shoes with cushioned sole');

-- Populate Orders table
INSERT INTO Orders (order_id, customer_id, product_id, quantity, order_date)
VALUES
  (1, 1, 1, 2, '2023-05-01'),
  (2, 1, 3, 1, '2023-05-05'),
  (3, 2, 2, 2, '2023-05-10'),
  (4, 3, 1, 1, '2023-05-15');