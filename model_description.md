### **Program contains only one model:**
ContentWebPage, which has fields like  
**name** -> CharField max length 100  
**language** -> CharField max length 5  
**content** -> JsonField (only in postgresSQL)  
for each field name content has another build:  
- for name =  **whoami**  
    - first_info  
    - studied_about  
    - programming_languages  
    - end_info  
    - date_of_adding  

- for name = **cv**
    - telephone_text: str
    - telephone: str
    - date_of_birth: str
    - town: str
    - work_experience_title: str
    - work_experience:  
        - period: str
        - title: str
        - where: str
    - education_title: str
    - education:
        - period: str
        - where: str
        - major: str
        - specialization: str
        - education_level: str
    - skills_title: str
    - skills:
    - programming:[list]
    - systems:[list]
    - network:[list]
    - others:[list]
    - training_courses_title: str
    - training_courses:
        - date: str
        - name: str
    - interests_title: str
    - interests:[list]
    - link_title: str
    - link:
        - github: str
        - microsoft: str
        - linkedin: str

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


Why do I choose this approoach?
1. Simply adding new pages, by adding new record.
2. Quickly and easily editing the specific page with specific language.
3. In this case we do not need any relationship. (this simply model).

Cons:
- We need to document all content with all his types, which are created on specific page. It helps us to know, which field we can also add.  
Ex. name = contact, content -> phone_number is for containg phone number