<!-- PROJECT LOGO -->
<div align="center">

# 🚗 Car Dekho - Vehicle Marketplace
✨ *A Console-Based Marketplace for Buying & Selling Cars* ✨

An interactive, console-based application built with **Python and MySQL** that provides a complete digital solution for buying, selling, and managing new and used vehicle inventory.

</div>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="MySQL" src="https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge">
</p>

---

## ✨ Overview
Welcome to the **Car Dekho Project**!

This project was created to be a one-stop digital solution for vehicle transactions. It offers a user-friendly **command-line interface** for customers to browse and purchase cars, and a separate, powerful admin panel for the owner to manage the entire inventory.

Built entirely in **Python** following Object-Oriented principles, this system demonstrates a strong backend structure connected to a robust MySQL database.

---

## 📋 Table of Contents
- [🌟 Features](#-features)
- [🛠️ Technology Stack](#️-technology-stack)
- [🚀 Getting Started](#-getting-started)
  - [✅ Prerequisites](#-prerequisites)
  - [⚡ Installation & Setup](#-installation--setup)
- [📂 Project Structure](#-project-structure)
- [🔮 Future Scope](#-future-scope)
- [📄 License](#-license)

---

## 🌟 Features
- ✅ **Dual User Roles:** Separate, feature-rich interfaces for both the Admin (Owner) and regular Users.
- ✅ **Admin Inventory Management:** A special menu for the owner to easily add, remove, and update vehicle listings.
- ✅ **Buy New or Used Cars:** Users can browse separate inventories for new and second-hand vehicles.
- ✅ **Advanced Search:** Find the perfect car by filtering based on budget or brand.
- ✅ **Sell Your Car:** A straightforward process for users to list their used cars for sale.
- ✅ **Secure User Authentication:** Safe and secure signup and login functionality for all users.

---

## 🛠️ Technology Stack
- **Python:**
  - **Object-Oriented Programming (OOP):** The entire application is built using classes (`Cars`, `Users`, etc.) to ensure the code is modular, reusable, and scalable.
  - **MySQL Connector:** The `mysql-connector-python` library is used to establish a seamless connection between the Python application and the MySQL database.
- **MySQL (Database):**
  - Serves as the relational database to persistently store and manage all data related to users, new cars, and used cars.
- **Jupyter Notebook:**
  - The `Final.ipynb` file acts as the main driver of the application, providing an interactive environment to run the code.

---

## 🚀 Getting Started
This is a backend-only project that runs in the console or a Jupyter environment.

### ✅ Prerequisites
- Python 3.x installed on your system.
- MySQL Server installed and running.
- The `mysql-connector-python` library.

### ⚡ Installation & Setup
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/patelarpit21/car-management-system.git
    ```

2.  **Navigate to the project folder:**
    ```bash
    cd car-management-system
    ```

3.  **Install required Python libraries:**
    ```bash
    pip install mysql-connector-python
    ```

4.  **Database Setup:**
    - Open your MySQL client (like phpMyAdmin, MySQL Workbench, or the command line).
    - Create a new database named `car_dekho`.
    - **Import the `car_dekho.sql` file** into your new database. This will automatically set up all the necessary tables (`users`, `new_cars`, `old_cars`) and populate them with sample data.

5.  **Configure Database Connection:**
    - Open the `database.py` file.
    - Update the `host`, `user`, and `password` fields to match your MySQL server credentials.

6.  **Run the Application:**
    - Open the `Final.ipynb` file in a Jupyter Notebook environment.
    - Run the cells to start the "Car Dekho" application.

---

## 📂 Project Structure

```bash
car-management-system/
│
├── database.py # Handles the connection to the MySQL database
├── users.py # Manages user authentication (signup, login)
├── cars.py # Contains all logic for buying, selling, and managing cars
├── Final.ipynb # The main entry point to run the application
└── car_dekho.sql # SQL dump file for easy database setup
```

## 🔮 Future Scope
📌 **Web Interface:** Develop a web-based front-end using a framework like Flask or Django for a graphical user experience.  
📌 **Image Uploads:** Allow users to upload images of their used cars.  
📌 **Enhanced Search:** Add more filtering options like model year, mileage, and location.  
📌 **API Development:** Expose the backend logic via a REST API to support a mobile application.  

---

## 📄 License
This project is licensed under the **MIT License**. You are free to use, modify, and distribute this project.

<br>

<div align="center">
  
💡 *Your digital showroom awaits.*  
*Happy Driving!* 🚗💨  

</div>
