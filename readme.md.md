Software Design Principles(Bank Code) README

Overview

This README outlines the software design principles and patterns used in the development of the Bank System application. The application is designed to provide a simple banking system with features such as account creation, money submission, withdrawal, deletion, transfer, and account display.

             Principles

Keep It Simple, Stupid (KISS): The application is designed to be simple and easy to understand. For example, the create_account method is a simple and straightforward implementation of account creation.

Don't Repeat Yourself (DRY): The application avoids duplicated code and logic. For example, the submit_money and withdraw_money methods reuse the same logic for updating the account balance.

Single Responsibility Principle (SRP): Each class and method has a single responsibility and reason to change. For example, the BankSystem class is responsible for managing accounts, while the create_account method is responsible for creating a new account.

Open-Closed Principle (OCP): The application is designed to be open for extension but closed for modification. New features can be added without modifying existing code. For example, new account types can be added without modifying the existing account management logic.
             
             Patterns

Factory Pattern: The create_account method can be seen as a factory method that creates a new account object.

Command Pattern: The submit_money, withdraw_money, delete_account, and transfer_money methods can be seen as command objects that perform specific actions on the banking system.

             Design Decisions

Use of a single class: The BankSystem class is used to manage all aspects of the banking system. This decision was made to keep the code simple and easy to understand, following the KISS principle.

Use of a dictionary to store accounts: A dictionary is used to store accounts, with the account number as the key. This decision was made to provide fast lookup and retrieval of accounts, and to avoid duplicated code, following the DRY principle.

Use of input/output operations: The application uses input/output operations to interact with the user. This decision was made to provide a simple and intuitive user interface.

              Trade-offs

Performance: The application uses a dictionary to store accounts, which can lead to performance issues for large numbers of accounts. A more efficient data structure, such as a database, may be needed for a production-ready application.

Security: The application does not implement any security measures, such as authentication or encryption. These measures would be necessary for a production-ready application.

Scalability: The application is designed to run on a single machine and does not provide any mechanisms for scaling. A production-ready application would need to be designed with scalability in mind.

          Future Improvements

Add authentication and authorization: Implement authentication and authorization mechanisms to ensure that only authorized users can access and modify accounts.

Use a database: Replace the dictionary with a database to improve performance and scalability.

Add error handling: Implement error handling mechanisms to handle unexpected errors and exceptions.
Improve user interface: Improve the user interface to make it more intuitive and user-friendly.

By following the KISS and DRY principles, the application is designed to be simple, easy to understand, and maintainable. The use of design patterns and principles ensures that the application is flexible, scalable, and easy to extend.

Author: Muhammad Moiz Farooq/20240779
Whitecliffe College, AKL