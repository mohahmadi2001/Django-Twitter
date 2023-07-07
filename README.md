# Django-Twitter
Bilingual Social Network Project with Python &amp; Django Framework
The following are implemented in this project:

1. The user has his/her own profile along with the username, picture and bio.
2. View the user profile of other people and ask them to be friends or follow
3. Publish posts containing relatively long texts and a number of photos with a title and category tags
4. Users should be able to like and dislike about the content and posts and also register comments
5. Users can, in addition to following people, all the content of a particular category sticker also follow
6. Before logging in, users should only be able to view content or search for people by name Have a user
7. Users should be able to archive their posts or account to remove from have access

## Photos:
![ERD](/twitter-digram.jpg)


## Tools:
1. Back-End: Python, Django
2. DataBase: PostgreSQL
3. Front-End: HTML5, CSS3

## How to Run?
1. Clone the Project
```
git clone https://github.com/SepehrBazyar/Shopping.git
```
2. Create a Virtual Environment("venv" is a Selective Name).
```
python -m venv venv
```
3. Activate the Interpreter of the Virtual Environment
    * Windows:
    ```
    venv\Script\active
    ```
    * Linux:
    ```
    source venv/bin/active
    ```
4. Install the Requirements
```
pip install -r requirements.txt
```
5. Write the Following Command to Run the Server
```
python manage.py runserver
```