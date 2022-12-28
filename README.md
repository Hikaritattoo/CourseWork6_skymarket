# Course Work 6
## Skymarket
### ads site

* Backend: django restframework
* Database: postgresql
* Backend-server: gunicorn
* Frontend: react (provided)
* Frontend localhost:3000
* Backend localhost:8000

***To launch project locally use command: docker-compose up --build -d***

This course work is a backend part for the ad site. The frontend part is already done. The backend part of the project involves the implementation of the following functionality:

- Authorization and authentication of users.
- Distribution of roles between users (user and administrator).
- Password recovery via email (optional).
- CRUD for ads on the site (admin can delete or edit all ads, and users can only edit their own).
- Under each ad, users can leave reviews.
- In the header of the site, you can search for ads by name.
