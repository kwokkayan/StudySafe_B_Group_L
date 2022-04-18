## Envrionment Variables
.env should contain these variables for local development and testing
```.env
DJANGO_SECRET=**FIND ON HEROKU**
DJANGO_DEBUG=true
LOCAL_DEV=true
```
---
## StudySafe Core Endpoints
- API Root: https://studysafe-b-group-l.herokuapp.com/studysafe-core/api
- API Docs: https://studysafe-b-group-l.herokuapp.com/studysafe-core/api/docs
- Admin Page: https://studysafe-b-group-l.herokuapp.com/admin
---
## Registration of user accounts
1. In the admin page, select the user group "Users".
<img width="696" alt="Screenshot 2022-04-18 at 14 42 11" src="https://user-images.githubusercontent.com/67239147/163767098-e332209b-bb6d-4f2f-a3be-f53eb98fc06b.png">
2. Select "ADD USER".
<img width="989" alt="Screenshot 2022-04-18 at 14 43 55" src="https://user-images.githubusercontent.com/67239147/163767393-2201b4f4-bf36-4ef2-9566-0efb4df86d0d.png">
3. Enter username and password for the account as promted. <br>  
4a. If the account would be registered as admin, have the permission "Staff status" checked in the "Permission" section, and select the option "admin". <br> 
4b. If the account would be registered as taskforce member, select the option "member".  <br>
4c. If the account would be registered as taskforce device, select the option "device".  <br>
<img width="989" alt="Screenshot 2022-04-18 at 14 47 16" src="https://user-images.githubusercontent.com/67239147/163767515-1c387584-f4bd-4d7b-85e0-3956f026d575.png">
5. Hit the button "SAVE".
