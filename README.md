# 🚦 Rusdi Parking System (OOP-Based)
A simple yet robust Parking Management System built with Python, demonstrating core Object-Oriented Programming (OOP) principles. This system handles different types of vehicles, calculates dynamic rates, and manages parking lot capacity.

## 🚀 Features
Vehicle Specialization: Different logic for Motorcycles and Cars using Inheritance.

Dynamic Pricing: Automatic tariff calculation based on vehicle type and duration.

Capacity Management: Prevents new vehicles from entering when the lot is full.

Professional Receipt: Generates a clean, formatted parking ticket upon exit.

Status Dashboard: Real-time monitoring of currently parked vehicles.

## 🛠️ OOP Principles Applied
This project serves as a practical implementation of:

Encapsulation: Using private attributes (__) and @property decorators to protect data.

Inheritance: A Parent class (kendaraan) providing a blueprint for Child classes (motor, mobil).

Polymorphism: Method overriding where the tarif() method behaves differently based on the object type.

Abstraction: Providing a clear interface for parking operations without exposing internal list management.

## 📦 Class Structure
kendaraan: The base class containing shared attributes (Plate, Brand, Entry Time).

motor: Derived class for motorcycles with a rate of Rp 2,000/hour.

mobil: Derived class for cars with a rate of Rp 5,000/hour.

tempat_parkir: The controller class that manages the parking flow and storage.