# Study Plan - Final Project to CS50 Web - by Murilo de Oliveira Silva

## Distinctiveness and Complexity
- My project is based on some principles of memorization that I learned in a book by Daniel J. Levetin called "The organized mind", where he details and explains the importance of revisions, categorization and the use of multiple meanings in learning for memorization . In reflecting on these principles, I decided to make an application that categorizes the studies and allows you to use several elements to improve and complement my studies and reviews. Thus, this project becomes different from all the others I did in this course, and it also becomes complex due to the number of models that were used, the need to handle files and even access the microphone through the browser and create an mp3 file and store it with the blob using javascript. It took me a few months to carry out this project because I am still a beginner, I had some headaches but it worked and I learned many new things.


## Organization and archives
- /study_plan/static/courses:
    - In the application, the admin is allowed to create courses and disseminate them according to their area of coverage, for now I haven't created all the functions to enter and have access to the course, but in that folder are the pdfs, audios, videos and other materials from each course, separated in distance and face-to-face.

- /study_plan/static/docs:
    - I created a module to be able to manage and have access to all files stored and attached in the studies, for now they are separated into PDF and AUDIO and they are in that folder.

- /study_plan/static/hard_skills:
    - All courses that are created must detail which hard skills will be acquired over time, in this folder are the icons of each hard skill.

- /study_plan/static/icons:
    - Here in this folder icons are the icons in general like those used in some buttons and also the icons of the studied sciences.

- /study_plan/static/institutions:
    - In this folder are the archives of the institutions such as the logo and other materials.

- /study_plan/static/study_plan:
    - tinymce:
        - I used a lib from a javascript text editor called Tinymce in the free version, here are the files for that lib.
    - vídeos:
        - I used a video of an animation that I made myself in Cinema4D with objects and a specific location in my city, this animation summarizes some principles that I learned in the book I mentioned earlier as the filters of attention and associative memory. Anyway, this video is here
    - create_study.css:
        - In this CSS I include the specific element styles of the study creation page, such as the text editor, the study post editing navbars, the navbars to manage and view the files and others.
    - create_study.js:
        - In this JS file I put some animation functions, some form handling functions and files, etc.
    - favicon.ico:
        - favicon of the web app
    - index.css:
        - In this CSS I put the styles and some definitions of responsiveness of the entire site and the other elements that are not part of the study creation page.
    - record.js:
        - On the study creation page, as I said, you must add several elements to compose a good study, one of which is to record an audio summarizing your study, this audio will be used in the future for review using associative memory. This JS file contains the functions that enable the use of the standard microphone, records the audio with the browser permission and generates an mp3 file with the blob and sends it to the form with a file type input.
    - scripts.js:
        - In this JS file it contains all the functions that call animations, enable the login and register screen, check the registration data, create the elements of the courses, studies and reviews according to the json response of the routes and others.

- /study_plan/static/users:
    - Here are the profile pictures of the users

- /study_plan/templates/study_plan:
    - content.html:
        - This HTML page I imported the layout and added a navbar on the left side to manage the type of content that will appear in the center, each button on this navbar has an active function in the click that will request a route that will return a json response and create the content according to parameters passed in the function.
    - create_study.html:
        - I imported this HTML page and added a navbar on the left side that enables the import of PDFS for reading in a canvas, for this I used lib pdfjsLib. I also created a lower navbar to fill out the study description, the summary that is what will appear on the audio review and recording card. In the center I put the main text editor of the study.
    - index.html:
        - This HTML page is the page where it will be checked if the user is authenticated and will provide a login and registration form for him if he is not authenticated, as soon as he is authenticated he will be redirected to the content.html page.
    - layout.html:
        - This HTML page is the standard layout of the website where you have a navbar at the top with a user profile image that when you click opens a fixed navbar on the left side with a logout button only for now, it also has a home button, a study creation and a search button to search the main content of the content page according to science, specific subarea or subtopic, this categorization was done and separated into models Sciences, Subareas and Subtopics, the contents are received with a request and presented in alphabetical order after the creation of the elements according to the json answer. At the end of the navbar there is a button that, when clicking, opens a navbar on the right side with the revisions of the studies done by the currently logged in user, these review cards have the title, the category, o summary the audio summary, the dates that must be made the revisions and the management of the files, by placing the cursor over the summary it zooms to allow a better reading.

- /study_plan/:
    - admin.py
        - On my Admin.py I put the fields and list_displays for my 17 models, I will explain a little more about each of the most upcoming days.
    
    - models.py
        - User:
            - Here at User I used AbstractUser and added only one field to place a profile picture.
        - Instructors:
            - Here at Instructors, users who are instructors of some course and the respective courses taught will be stored.
        - Students:
            - Here at Students, users who are students of a course and their respective courses will be stored
        - Docs:
            - Here in Docs the files that are sent by users in their Studies will be stored, separated by 2 types PDF and MP3, each file also has an area and / or topic categorization.
        - Sciences:
            - Here at Sciences will be the Sciences that can be studied and serve as categorization of the search and definition of each content, it contains 2 fields, one named and the other to save the icon image file.
        - SubArea:
            - Here in SubArea the subareas are stored in 2 fields according to each science with a MayToManyField ratio and their name.
        - SubTopic
            - Here in SubTopic, Subtopics are stored in 2 fields according to each SubArea with a MayToManyField ratio and its name.
        - Studys
            - Here at Studies are all the studies that are created by users,  these studies have a title, definition whether it is public or private, user who was created, credit of the study, subarea, subtopic, main content of the study, study summary, pdf that is related to Docs, audio summary of the study also related to Docs, day the study was created, and the 4 study review dates
        - Event
            - Here at the Event will be the events that exist according to Sciencias, Subareas and Subtopics, are future functions.
        - Courses
            - Here at Courses will be the courses that exist according to Sciencias, Subareas and Subtopics, are future functions
        - Rooms
            - Here at Rooms will be the course rooms that exist according to Sciencias, Subareas and Subtopics, are future functions.
        - Lessons
            - Here at Lessons are the lessons of each course, leassons have audio, video, slides, notes, source_code and others that make up the leassons of the course, are future functions.
        - Projects
            - Here at Projects will be the projects of society that citizens can participate in, they are future functions.
        - HardSkills
            - Here at HardSkills are the hardskills that are part of the description of each course, they are future functions.
        - SoftSkills
            - Here at Softskills are the Softskills that are part of the description of each course, they are future functions.
        - Certificates
            - Here at Certificates are the certificates for each course for users to print, they are future functions.
        - Institutions
            - Here at the Institutions are the institutions that offer the platform courses, they are universities, technical schools and others, etc. They are future functions.
    
    - urls.py and views.py
        - Here at Urls.py we have the following routes:
            - index:
                - Index is the main route that has the index.html page as its response
            - login:
                - Login_view is the authentication route that has a redirect to the Index as a response.
            - logout:
                - Login_view is the logout route that has a redirect to the Index as a response.
            - register:
                - Register is the registration route that receives the information from the form, which has a redirect to the Index as its response.
            - create_study/<int:type>/<str:topic_selected:
                - Create_study is the route that creates studies, this route has 2 parameters, int: type and str: topic_selected, has a request request for the create_study.html page in response if you have not received a request.POST. If the study was created successful, will return to the index page, if not it will continue on the page.
            - content:
                - Content is the route that takes the user to the content of the website's home, this route has as response to the content.html page.
            - get_content_items/<str:type>/<str:name>/<str:content_name>/<str:is_review>:
                - Get_content_items is a route that will require the content that will appear on the content.html page, these contents can be Studies or Courses for now. These contents are filtered according to the parameters of the route <str: type> / <str: name> / <str: content_name> / <str: is_review>, which are respectively the type of category in the area of the study or course ( Subarea or Subtopic), the name of the category, the content (Study or Course) and whether the content is a review.
            - get_subareas/<str:science>:
                - Get_subareas is a route that searches for objects in Subarea models according to their respective Science and returns a Json response. It has a filtering parameter that is sent when clicking on a Science <str: science>, in order to find the subareas of this science
            - get_subtopics/<str:subarea>:
                - Get_subtopics is a route that searches for objects in Subtopic models according to their respective Subarea and returns a Json response. It has a filtering parameter that is sent by clicking on a Subarea <str: subarea>, in order to find the subtopics of that subarea
            - uadoajsersalladaqeqe/<str:username_input>:
                - This route is used in the registration div on the index.html page, it checks according to the parameter <str: username_input> if the username the person typed is already in use and returns a json answer saying whether it exists or not.
            - asdajdawqeqweomemail/<str:email_input>:
                - This route is used in the registration div on the index.html page, it checks according to the parameter <str: email_input> if the email that the person typed is already in use and returns a json answer saying whether it exists or not.
        - 


## How to run my application
- The user entering the application will come across a login screen allowing the user to login if he already has the registration or he can register on that same page by clicking on "Register here" As soon as he registers and logs he will have access to the contenthtml page, on this page the user will be able to search for various types of content separated by Sciences, its subareas and subtopics, for now the only functionality of the contents is the StudyNo upper navbar the user can click on the magnifying glass and navigate through all the study categories and when hovering over the Subareas and Subtopics she can choose between clicking on the magnifying glass and seeing the contents on that theme on the same page or click on the other button with a pencil and a notebook to create a study in that chosen area, so the user will go to the create_studyhtml page on this page, the user will be able to do his study in that area, important pdf documents to base your study and recording the main content of your study in the textarea, then you must define the characteristics of the study post, add a written summary of your study using a maximum of 1500 words(This summary will be used later in the review card that will be created) add or remove the studied areas and record an audio summarizing your study in a maximum of 5 minutes, and then you can click on Create StudyLogo to create the study, the date of creation of the study and the dates for revisions to fix that content using the Ebbinghaus method will be stored in the Study models. These private studies can be seen by clicking on the calendar in the upper navbar, opening a div in the right corner with the review cards with the audios, summary of the content and the dates that should be made to the reviews to fix the studyIf the Study created is public it will appear on the contenthtml page by clicking on the Studies button or looking for the respective study theme in the Sciences menu and see the elements of the studies.
- The only models that the average user can change are User, Studies and Docs.
- As these are only the features, this project will be improved in the future, there is still a lot to be done and learned, thanks even for the great opportunity to see content like yours for free.