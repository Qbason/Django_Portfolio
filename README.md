# Portfolio made using Django
## HTML, CSS, JS, Django, Django REST Framework, Python, PostgreSQL, Docker, Bash, Apache2, Let's Encrypt
## Webpage portofolio
Welcome to [jakubk.pl](http://jakubk.pl) to see how does it work
## PostrgreSQL
### **Program contains only one model:**
ContentWebPage, which has fields like  
**name** -> CharField max length 100  
**language** -> CharField max length 5  
**content** -> JsonField (only in postgresSQL)  


for each field name content has another build (JSON!):  
- for name =  **whoami**  
    - first_info  
    - studied_about  
    - programming_languages  
    - end_info  
    - date_of_adding  

- for name = **cv**
    - telephone_text  
    - telephone  
    - date_of_birth  
    - town  
    - work_experience_title  
    - work_experience:  
        - period
        - title
        - where
    - education_title
    - education:
        - period
        - where
        - major
        - specialization
        - education_level
    - skills_title
    - skills:
    - programming:[list]
    - systems:[list]
    - network:[list]
    - others:[list]
    - training_courses_title
    - training_courses:
        - date
        - name
    - interests_title
    - interests:[list]
    - link_title
    - link:
        - github
        - microsoft
        - linkedin

- for name = **contact**
    - phone_number_info:str
    - phone_number:str
    - email_info:str
    - email:str

special row for links in navbar
- for name = **navbarlinks**
    - whoami: str
    - cv: str
    - contanct: str


Each page on website has her own name like whoami, cv, contact.  
In this way per one page is one record in the table.  
Language field contains shortened name of language.  
In my case I have PL for polish language on page
and EN to english language on page.

Special row for links in navbar is called navbarlinks(name in db).
If the navbarlinks is not founded 404 is thrown.


**Why do I choose this approoach?**
1. Simply adding new pages, by adding new record.
2. Quickly and easily editing the specific page with specific language.
3. In this case we do not need any relationship. (this simply model).

**Cons:**
- We need to document all content with all his types, which are created on specific page.  
It helps us to know, which field we can also add.  
Ex. name = contact, content -> phone_number is for containg phone number


## Django
We have two templates in templates called index.html and 404.html  
If page would not be found then template 404.html will be generated.  
In index.html file we have references to specific content in the model.  
Like {{cv.content.date_of_birth}} -> from model where name = cv takes content.date_of_birth json.   
This allows me to generate specific content in specific place.

## Django rest api
To easily upload data to database I created endpoint,  
where I can get,post,put,delete to do also another actions.  
I applied BasicAuth to rest api to make sure, that 
only me can have access to this page.  
There is an option to upload content or modify by Django administrion.

In future rest api can be used to send request from frontend application,  
where someone could upload, edit, delete specific content in portfolio.

## HTML JS
Using JS I made that we do not follow to each page separately.
But whole page is downloaded once.  
The JS controlls, which content will be loaded.
## CSS 
Bootstrap is used to make it responsive.  
Webapge works on phones, tablets, PC's.

## Apache
To make it full working page I decided to run our django project using apache.  
In dockerfile I declared, which packages should be installed to make sure, that  
everything is wokring correctly.

## HTTPS
Our project serves ssl. To get free ssl I used let's encrypt project.

## Docker
Our environment is prepared in docker.  
This solution makes easier running our project and do editing it.

# How to run?
### We need to have installed:
- Docker
- Docker compose

The necesarry packages will be downloaded in container.
## First to run
To get the ssl from let's encrypt. (You need to have your own domain)  
Go to generator_lets_encrypt then go to .env and change to yours:  

        email=youremail@gmail.com
        server_full_name=www.domain.com
        server_name=domain.com

In generator_lets_encrypt/ directory run:  

        sudo docker compose up le-apache -d  
        sudo docker compose up certbot  
Make sure that  port 80 is opened.  
Then:

    sudo docker compose down
### Configuration main docker:
- Change .env in main directory  
    Setup your database name, user, password, email etc.

        POSTGRES_DB=postgres
        POSTGRES_USER=user
        POSTGRES_PASSWORD=1234
        PGADMIN_DEFAULT_EMAIL=yoursaddressemail
        PGADMIN_DEFAULT_PASSWORD=1234
        PGADMIN_LISTEN_PORT=8001

- Go to portfolio_manager/porfolio_manger/ and create secret.py and generate SECRET_KEY value

        SECRET_KEY = 'yoursecret'

- Run your project for first time:
    It can take a while.

        sudo docker compose up --build


- When your docker is running open new terminal and add superadmin for Django by:
    If you would like to know, what is your id container then:

        sudo docker ps
    To run bash in our container:

        sudo docker exec -it <id_container> bash
    To add superuser:
    
        python manage.py run createsuperuser
    Write down your username and password then exit.

- go to 127.0.0.1:8000/api/contentwebpage (or 127.0.0.1:8000/admin) and log in  
    then setup navbarlinks for example like:

        name - > navbarlinks
        language - > en
        content -> 
        {
            "cv": "CV",
            "whoami": "Whoami?",
            "contact": "Contact"
        }
    You can decide, which language can be set, but you have remember to change urls.  
    Default is "pl" and "en".

    Then you have to add content for each page by sending for example:

        name - > whoami # it is the name from navbarlinks
        language -> en # default can be en/pl
        content - >
        {
            "title": "Whoami?",
            "end_info": "last paragraph",
            "first_info": "first paragraph",
            "localization": "localization",
            "studied_about": [
                "1 element",
                "2 element"
                # Subjects, which I studied in secondary school
                
            ],
            "who_made_page": "Webpage was made by ",#by who
            "date_of_adding": "21:37 22.05.2012",
            "programming_languages": [
                "Bash",
                "Batch",
                "..."
                # learnt programming languages
            ],
            "additional_information": "Additional informations"
        }
    Then do it for another pages based on PosgreSQL model, which I described.

- Change index.html to changing place content, replace specific images, css etc.

- And that's it :) 


### Commands
- sudo docker compose up --build  <-- for first run, ctrl+c to cancel
- sudo docker compose up -d <-- to run docker container in background
- sudo docker compose down <-- to shutdown docker container


### Ideas 
Make Flutter app to configure portfolio

