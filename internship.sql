create database internship

use internship
go


-- Users table
CREATE TABLE Users (
    UserID INT PRIMARY KEY IDENTITY(1,1),
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT
);

-- Products table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY IDENTITY(1,1),
    ProductName VARCHAR(100),
    Price DECIMAL(10, 2)
);

-- Orders table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY IDENTITY(1,1),
    UserID INT FOREIGN KEY REFERENCES Users(UserID),
    ProductID INT FOREIGN KEY REFERENCES Products(ProductID),
    Quantity INT,
    OrderDate DATE,
    OrderName VARCHAR(100),
    Price DECIMAL(10,2) -- This is the price at the time of the order
);

-- Insert into Users (10 users)
INSERT INTO Users (FirstName, LastName, Age)
VALUES 
('Ali', 'Karimov', 25),
('Vali', 'Saidov', 30),
('Sara', 'Norova', 28),
('John', 'Smith', 35),
('Lola', 'Akbarova', 24),
('David', 'Beck', 40),
('Malika', 'Yuldasheva', 29),
('Nodir', 'Zokirov', 33),
('Sami', 'Tursunov', 22),
('Alex', 'Johnson', 31);

-- Insert into Products (10 products)
INSERT INTO Products (ProductName, Price)
VALUES
('Laptop', 1000.00),
('Mouse', 25.00),
('Keyboard', 45.00),
('Monitor', 200.00),
('USB Cable', 10.00),
('Smartphone', 700.00),
('Tablet', 450.00),
('Charger', 20.00),
('Headphones', 85.00),
('Webcam', 60.00);

-- Insert into Orders (50 orders)
-- Loop-simulated insert (not supported directly in SQL Server, so multiple INSERTS used)
INSERT INTO Orders (UserID, ProductID, Quantity, OrderDate, OrderName, Price)
VALUES
(1, 1, 1, '2025-01-01', 'Electronics', 1000.00),
(2, 2, 2, '2025-02-10', 'Accessories', 25.00),
(3, 3, 1, '2025-03-15', 'Peripherals', 45.00),
(4, 4, 1, '2025-03-20', 'Screens', 200.00),
(5, 5, 3, '2025-02-01', 'Cables', 10.00),
(6, 6, 1, '2025-01-25', 'Phones', 700.00),
(7, 7, 2, '2025-02-18', 'Tablets', 450.00),
(8, 8, 1, '2025-03-01', 'Chargers', 20.00),
(9, 9, 2, '2025-03-10', 'Audio', 85.00),
(10, 10, 1, '2025-01-30', 'Cameras', 60.00)


--11.  Barcha foydalanuvchilarni saralab olish uchun SQL so‘rov yozing.

	SELECT * FROM Users;

--12.  Ma'lum bir yoshdan(30) katta foydalanuvchilarni chiqaradigan SQL so‘rov yozing.

	SELECT * FROM Users WHERE Age > 30;

--13.  Bir xil ismga ega foydalanuvchilar sonini hisoblash uchun qanday so‘rov yozish kerak?
	
	SELECT FirstName, COUNT(*) AS NameCount  FROM Users
	GROUP BY FirstName
	HAVING COUNT(*) > 1;

--14.  Eng ko‘p ishlatiladigan 5 ta mahsulotni chiqarish uchun SQL yozing.

	SELECT * FROM Orders

	SELECT TOP 5 ProductID, COUNT(*) AS MostUsedProduct FROM Orders
	GROUP BY ProductID
	ORDER BY MostUsedProduct DESC;

--15.  Har bir mijozning buyurtma sonini hisoblash uchun qanday so‘rov yoziladi?
	
	SELECT * FROM Orders

	SELECT UserID, COUNT(*) AS OrderCount FROM Orders 
	GROUP BY UserID;

--```41.  Oxirgi 3 oy ichida eng ko‘p sotilgan 5 mahsulotni chiqarish uchun SQL yozing.
	
	SELECT * FROM Orders

	SELECT TOP 5 ProductID, COUNT(*) AS SalesCount FROM Orders
	WHERE OrderDate >= DATEADD(MONTH, -3, GETDATE())
	GROUP BY ProductID
	ORDER BY SalesCount DESC;

--42.  Mijozlar orasida bir xil nomdagi buyurtmalar sonini hisoblash uchun SQL yozing.
	
	SELECT * FROM Orders

	SELECT UserID, OrderName, COUNT(*) AS SameOrderCount FROM Orders
	GROUP BY UserID, OrderName
	HAVING COUNT(*) > 1;

--43.  Har bir mahsulotning oxirgi sotilgan narxini topish uchun SQL yozing.
	
	SELECT * FROM Orders

	SELECT O.ProductID, O.Price FROM Orders O 
	INNER JOIN ( SELECT ProductID, MAX(OrderDate) AS LatestDate FROM Orders GROUP BY ProductID )
		latest ON o.ProductID = latest.ProductID AND o.OrderDate = latest.LatestDate;

--44.  O‘tgan yilda eng kam sotilgan mahsulotlarni topish uchun SQL yozing.

	SELECT * FROM Orders

	SELECT TOP 5 ProductID, COUNT(*) AS SalesCount FROM Orders
	WHERE YEAR(OrderDate) = YEAR(GETDATE()) - 1
	GROUP BY ProductID
	ORDER BY SalesCount DESC;

--45.  Barcha buyurtmalarning umumiy narxini hisoblash uchun SQL yozing.
	
	SELECT *  FROM Orders

	SELECT SUM(Price * Quantity) AS TotalSum FROM Orders

--4. Extra: Case Study Savollar
--46.  Sizda millionlab yozuvlari bo‘lgan jadval bor. Qanday qilib so‘rovlarni tezlashtirasiz?

	-- indexlar yaratib olamz bu jarayonni  ancha tezlashitirshga yordam beradi
	-- yana bitta usuli bolaklarga bolib olamz tabledagi dataga asoslanib

--47.  Agar mijozlar jadvalidagi ID ustunida indeks bo‘lmasa, bu qanday ta’sir qiladi?

	-- bu jarayonni anchaga sekinlashtirib qoyishi mumkin misol uchun agar biz joinlarni ishlatmoqchi bolganimizda chunki id bn join qilish ancha osonroq jarayon boladi

--48.  Sizga yangi tizim loyihalash topshirildi. SQL yoki NoSQL dan qaysi birini tanlaysiz va nega?

	-- birinchi bolib projectga qaraymz agar project scalable, high performance da ishlashi kk bolgan project bolsa, yoki katta hajmdagi datalar saqlanishi kk boladiga bolsa SQL eng yaxshi tanlov 
	-- agar projectdan kuchli performance talab qilinmasa yoki unda katta hajmli data ishlatilinmasa NOSQL is the best option

--49.  O‘chirilgan yozuvlarni saqlash uchun qanday strategiyalarni qo‘llash mumkin?

	-- isdeleted qoshish orqali

--50.  Loyihada SQL Injection dan himoyalanish uchun qanday choralar ko‘rish kerak?

	-- yaxshi variantladan bittasi WAF(web application firewall) ishlatish
