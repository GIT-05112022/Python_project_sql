
USE gs;

CREATE TABLE `customer_type` (
  `Type` varchar(45) NOT NULL,
  `Discount` int NOT NULL,
  PRIMARY KEY (`Type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `coupons` (
  `Coupon_ID` int NOT NULL,
  `Discount` int NOT NULL,
  PRIMARY KEY (`Coupon_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `grocery_items` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `Product_Name` varchar(100) NOT NULL,
  `Unit` varchar(50) NOT NULL,
  `Cost` int NOT NULL,
  `Days left for expiry` varchar(45) NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `other_items` (
  `product_id` int NOT NULL,
  `Product_name` varchar(45) NOT NULL,
  `Unit` varchar(45) NOT NULL,
  `Cost` int NOT NULL,
  `Days left for expiry` varchar(45) NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

