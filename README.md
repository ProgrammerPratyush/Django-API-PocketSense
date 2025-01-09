# PocketSense - College Financial Management System

***By – Pratyush Puri Goswami***

***Email: ppurigoswami2002@gmail.com***



## Introduction


The PocketSense API provides a robust financial management platform tailored for students, enabling them to effectively track, manage, and share financial responsibilities. Designed with scalability, security, and user experience in mind, PocketSense ensures students can easily manage expenses, resolve disputes, and collaborate on shared financial goals.



## Core Features

**Expense Tracking:** Record and categorize expenses for better financial awareness. Supports recurring expenses with reminders and notifications to keep users updated on their financial activities.


**Smart Expense Splitting:** AI algorithms suggest optimal ways to split expenses, ensuring fairness by analyzing individual spending patterns, historical data, and group dynamics. Users can customize splitting rules or rely on AI-suggested options for equitable sharing.


**Savings Management:** Set and track savings goals with gamified elements for engagement.


**Dispute Resolution:** Resolve expense disputes through a voting mechanism.


**Collaborative Financial Management:** Share responsibilities within groups for effective expense tracking.


## Technologies Used


**Django:** Backend framework for handling API requests, data modeling, and business logic.


**Django REST Framework:** For building RESTful APIs.


**PostgreSQL:** Relational database for high availability and scalability.


**JWT Authentication:** Secure communication between client and server.


**AI Algorithms:** Leverages libraries like pandas and numpy for smart expense splitting based on historical data.



## Database Design and Models

### Expenses Model

**Fields:**


***amount (float):*** The total cost of the expense.


***category (foreign key):*** Links to the Categories model (e.g., food, travel).


***split_type (char):*** Defines how the expense is split (e.g., equally, custom percentages).


***date (datetime):*** The date and time when the expense was recorded.


### Students Model


**Fields:**


***college (char):*** Name of the college.


***semester (integer):*** Current semester of the student.


***default_payment_methods (JSON):*** List of default payment methods (e.g., UPI, credit card).


### Groups Model

**Fields:**

***group_name (char):*** Name of the group.


***group_type (char):*** Type of group (e.g., social, project, trip).


***members (many-to-many relation):*** List of students in the group.


### Settlements Model


**Fields:**


***payment_status (char):*** Status of the settlement (e.g., "pending", "paid").


***settlement_method (char):*** Method of settlement (e.g., UPI, cash).


***due_date (datetime):*** Settlement due date.


### Categories Model


**Fields:**


***food (boolean):*** Indicates food-related expenses.


***travel (boolean):*** Indicates travel-related expenses.


***academics (boolean):*** Indicates academic-related expenses.


***entertainment (boolean):*** Indicates entertainment-related expenses.


## Authentication System


**JWT Token-based Authentication**

***How It Works:***

1. User sends login credentials (username/email and password).


2. System validates credentials and generates a JWT token.


3. Token is sent to the client and used for all subsequent API requests.


***Benefits:***

1. Secure communication.


2.Short-lived tokens for added security.


3. Social Authentication


### Supported Providers: Google, Facebook.

**How It Works:**


1. User is redirected to the chosen provider for authentication.


2. Provider sends an authorization code to the server.


3. Server exchanges the code for an access token to fetch user information.


**College Email Verification**

Purpose: Ensures platform access is restricted to college students.


**How It Works:**

1. System sends a unique verification token to the user’s college email.


2. User confirms email to gain full access.


### UPI Payment Linking

Features:


1. Simplifies settlement of expenses.


2. Allows direct UPI payments within the app.


**How It Works:**


1. User links their UPI ID during setup.


2. Payments are processed directly through the app.


### Context-Aware Permissions


**Dynamic Access:**


1. Permissions are granted/revoked based on user actions (e.g., creating group trips).


2. Ensures security and relevance.


### API Testing

Key features and responses have been tested using Postman. The current API is under development, and feedback is welcome for improvements and fixes.



### Future Enhancements

1. Advanced analytics for spending habits.


2. Enhanced AI algorithms for dynamic group expense predictions.


3. Cross-platform mobile applications for seamless user experience.


4. Real-time notifications for settlement status and disputes.


### Contribution

Your support and commits are always appreciated.
