# Kay’s Homemade Pizza (Shop Management System)  


* An electronic order system
* Users can visit the website, peruse the menu, and order the pizza they would like online
* A database for good record keeping, and for seeing who ordered what and when
* A finance database where profits, losses, expenditures can be recorded, saved, and accessed at a later date


## Technologies Used
* Database – SQLite 
* Backend framework – Flask 
* Rendering framework – jinja
* Frontend – HTML, CSS, JavaScript 

## Breakdown
# Transaction page
 This page is where transaction is going to be made. Where the vendor can specify the name, quantity and item to be bought. 
On this same page, the number of items left should be displayed on the screen or be accessible. 


# Admin page
Page where the owner of the business can get information about the transactions what items in in the inventory and a summary of information such as total revenue, profit, quantity sold, quantities left 
The admin page gives the owner the chance to restock items that are now on stock

The owner has the change to add a new item into the existing items

# Login page
This is going to authenticate the owner of the business 


# Extra feature
In the preorder request, if the owner is done restocking, he/she can decide to send emails to them with the click of a button 

# Timeline for project completion 
| Backend | Frontend |
| ------ | ------ |
| Database | searching for best HTML template (admin) |
| Routing | editing the template to make them fit context. Frontend group can be divided into 3. One takes the transaction, the other takes the admin page and the last takes the login page.  Since the login page is going to be easy, team merges into 2 after its done  |
| Working on the login system from the backend side | Final touches on the editing of the template and submission to supervisors for review. |
| Working on the admin and transaction page | Working on the admin and transaction page |
| Testing the project and final touches| Testing the project and final touches|
| Deployment | Deployment |
| ***Showcase and presentation to the businesses*** | ***Showcase and presentation to the businesses*** |
 
# To run this project locally
```sh
$ virtualenv .venv
```

```sh
$ source .venv/bin/activate
```
This  command only works on mac and linux. To activate your virtual environment for windows, please use the command below. To know why this is necessary, please visit this link [virtual environment][virtualenv]

```sh
$ .venv/Scripts/activate
```

```sh
$ pip install -r requirements.txt
```

```sh
$ python app.py
```

Your shop management system is ready to go :wink: :collision: :fire: :fire: :fire:

## Conclusion
> This project has been made simple. After we’re done with these features, we can add extra features to it. 
> If you think I have left out some core features, please let me know by 
> GitHub repository link [Github repository][repository]
> email: christopher.anamalia@ashesi.edu.gh or jean.dovonon@ashesi.edu.gh 

# Dedicated Group Members(To be updated)
* Stacy Sarfo
* Kristen Agyeman-Prempeh 
* Stephen Owusu
* David Angyuum
* Joshua Quartey

[repository]: <https://github.com/AshesiDevelopersStudentsClub/SMS.git>
[virtualenv]: <https://docs.python-guide.org/dev/virtualenvs/>

