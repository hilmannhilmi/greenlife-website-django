# Green Life - Sustainable E-commerce Platform
🌿 An e-commerce website designed with a focus on sustainability. The platform boasts a vibrant green theme reflecting the company's commitment to a better and greener future. Below in the description also included the screenshots of the website.

## Technologies Used:
- Backend: Django - A high-level Python Web framework that encourages rapid design and clean, pragmatic design.
- Frontend: HTML & CSS with Bootstrap for responsive and modern design.

## Database Models Overview:

### UserAccounts:
This model represents user accounts in our e-commerce platform.
- username: A unique identifier for the user.
- name: The full name of the user.
- datecreated: The date the account was created.
- email: The email associated with the user.
- buyerseller: Indicates whether the user is a buyer or a seller.

### UserProfiles:
This model offers additional information related to a user account.
- name: Foreign key relationship to the UserAccounts model.
- location: The location details of the user.

### Products:
This model holds information about the products listed on the platform.
- name: Name of the product.
- dateadded: The date when the product was added to the platform.
- quantity: The quantity available for the product.

### Orders:
This model manages the orders made on the platform.
- orderid: A unique identifier for the order.
- datecreated: The date the order was created.
- shippinglocation: The location to which the order will be shipped.

## Installation and Setup
1. Install django in a virtual env
2. Move all the files and folder in this repo in the folder with the virtual env
3. Activate the virtual env and run "Python manage.py runserver" in the terminal

## Screenshots:
- Screenshot of homepage
![image](https://github.com/hilmannhilmi/greenlife-website-django/assets/133535538/26f970c9-5278-471f-95a4-0105a524a2df)

- Screenshot of About Page
![image](https://github.com/hilmannhilmi/greenlife-website-django/assets/133535538/358dd3e5-8611-4292-9d03-a440548314dc)

- Screenhot of Log In Page
![image](https://github.com/hilmannhilmi/greenlife-website-django/assets/133535538/93daf62a-9226-42e3-aba3-2cce2377b50b)

- Screenshot of Database Page
![image](https://github.com/hilmannhilmi/greenlife-website-django/assets/133535538/9a802d97-a6c1-4bf4-87b4-7e5acfaccf9f)




