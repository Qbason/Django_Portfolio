# Portfolio made using Django
## HTML, CSS, JS, Python
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

Special row for links in navbar is called navbarlinks  
If the navbarlinks is not founded 404 is throw


Why do I choose this approoach?
1. Simply adding new pages, by adding new record.
2. Quickly and easily editing the specific page with specific language.
3. In this case we do not need any relationship. (this simply model).

Cons:
- We need to document all content with all his types, which are created on specific page.  
It helps us to know, which field we can also add.  
Ex. name = contact, content -> phone_number is for containg phone number


## Django
We have two templates in templates called index.html and 404.html  
If page would not be found then template 404.html will be generated.  
In index.html file we have references to specific content in the model.  
Like {{cv.content.date_of_birth}} -> from model named then field content takes json date_of_birth.   
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

# How to run?
### We need to have installed:
- Docker
- Docker compose

The necesarry packages will be downloaded in container.

### Configuration:
- Add superadmin for Django by sudo docker exec -it <id_container> bash
- then run python manage.py run createsuperuser
- add user username and password
- go to 127.0.0.1:8000/api and add page data by api or 127.0.0.1:8000/admin
- change index.html to replace specific images, css etc.
- go to portfolio_manager/porfolio_manger/settings.py and change your secret


### Run
- sudo docker compose up --build  <-- for first run, ctrl+c to cancel
- sudo docker compose up -d <-- to run docker container in background
- sudo docker compose down <-- to shutdown docker container

## Another option to see results? 
Welcome to [jakubk.pl](jakubk.pl) to see how does it work


