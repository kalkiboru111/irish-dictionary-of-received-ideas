# Irish Dictionary of Received Ideas

This is a dictionary of the latest and greatest Irish platitudes. It is modeled on Gustave Flaubert's "Dictionary of Received Ideas" (en Francaise, Le Dictionnaire des idées reçues), 
a short satirical work collected and published in 1911. It provides users with definitions of the latest cliches, a means to upvote and downvote them based on 
their accuracy and/or social salience, and a means to refine and update the terms and definitions as necessary. 

This serves the purposes of alerting users to the latest truisms being peddled by politicians, pundits, and talking heads; of providing social commentary; and also
just provides entertainment value. 

NOTE: I am in the process of adding additional functionality, such as user login and voting fucntionality. However, I have commented this functionality out for the time being, 
due to the fact that it is not considered as part of the assessment criteria. 
 
## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.
In accordance with the goal of providing social commentary, the UX of this project focuses on providing the user with salient content. The homepage therefore directs users directly to the dictionary, omitting 
any intermediary preabmble. Given that the purpose of the site is fairly self-explanatory, explanatory text is kept to a minimum. 

The purpose of this application is the content. The dictionary is therefore given pride of place on the homepage, and is given a great deal of "real estate". 

Likewise, the search icon is placed in the top-left hand corner of the navbar and the navbar is available on every page of the application, except for the preliminary 
login and registration pages. The consistent presence of the nav bar with search icon allows users to readily search for any term, regardless of where they are in the application. This minimizes friction for users seeking to search for and post content.
The search field occupies the full space of the navbar, which maximizes the presence of the search content, but also minimizes the use of real estate on the page. 

Consistent with the application's focus on content, the Hilitor component highlights content on the page that matches the user's search query. This enables users to quickly and conveniently identify relevant content returned for a given search query. Also, in terms of the user's ability to improve content (also a goal of any application 
focused on content), users can readily refine definitions (using the large colorful "Refine" button) or delete definitions (using the large colorful "Passe" button).

User Stories:
- As a new user, I want to quickly understand what this site is about, so that I can determine whether it is a worthwhile investment of my time. This goal is satisfied by having minimal preamble,
and having the user directed directly to the home page, which contains a brief blub and the dictionary itself. 
- As a passive user, I want to peruse the terms for entertainment value, or for social commentary, I can check the dictionary on the home page. In future, I plan to add a feed that is updated in realtime called "The Zeitgeist", which will show the most upvote and therefore salient additions to the dictionary.
- As an active contributor, I have a new term that I want to add to the dictionary. To this end, I can navigate to the "Add Term" or "Add Category" page, which are readily available in the navbar.

Wireframes for this project were developed and are availabe in the "wireframes directory" in the Github repository.

### Existing Features
- Registration Page - allows new users to register, by having them fill out a registration form.
- Login Page - allows users to log in to the application, by having them fill out the log in form. 
- Home Page - The home page dipslays the dictionary with entries listed in terms of the term, definition, origin and category. 
- Refine Button - The refine button allows users to edit terms. This button redirects to the "Edit Term" page (at edit_term.html) which then populates with the term selected for editing.
- Passe Button - The passe button allows users to delete terms. This button quickly deletes the term selected for deletion. 
- Add Term Page - allows users to add terms, by having them fill out the "Add Term" form (at add_term.html).
- Add Categories - allows users to add categories, by having them fill out the "Add Category" form (at addcategory.html).
- Search Bar - allows users to search for a term, by having them enter a search query in the search bar. The search bar autocompletes with predictions of search queries, thereby minimizing frictions for users. 

### Features Left to Implement
- Instead of a dropdown select menu for categories, I would like to implement "search tags" which will be non-mutually exclusive categories that definitions are tagged with in lieu of categories. This will make the search results more fulsome and interconnected.
- I plan to implement a newsfeed feature on the home page called "The Zeitgeist" which shows the currently most upvoted terms. This is in accord with the purpose of the site to provide social commentary with high salience.
- I plan to add in upvote and downvote functionality, which rewards users based upon their submissions (similar to the formate of Reddit.com).
- Along with the upvote and downvote functionality, I plan to introduce a native currency called "cache" which will serve the same role as Karma on Reddit.

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - The project uses **HTML5** to define properties and behaviors of the application's pages.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
    - The project uses **CSS** to stylize the content of the application's pages.
- [Python](https://www.python.org/)
    - The project uses **Python** to define fucntions and behaviors of the application's pages.
- [Flask](https://palletsprojects.com/p/flask/)
    - The project uses **Flask** as a lightweight web application frameworks.
- [Pymongo](https://api.mongodb.com/python/current/)
    - The project uses **PyMongo** as a Python library to communicate with the MongoDB database.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Materialize](https://materializing.com)
    - The project uses **Materialize** to assist with the formatting of the navbar, tables and forms..
- [Javascript](https://javascript.com)
    - The project uses **Javascript** to for the logic of the application.
- [FontAwesome](https://fontawesome.com)
    - The project uses **FontAwesome** for logos and icons.
- [Hilitor](https://github.com/GerHobbelt/hilitor)
    - The project uses **Hilitor** to highlight query terms in search results.


## Testing

Maual tests were conducted as follows: 

1. Registration form:
    1. Go to the "Registration" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with an invalid password and verify that a relevant error message appears
    5. Try to submit the form with all inputs valid and verify that a success message appears.
    6. Verify that the user and password have been input into the correct collection in the MongoDB Database
    
2. Login form:
    1. Go to the "Login" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with an invalid password and verify that a relevant error message appears
    5. Try to submit the form with all inputs valid and verify that a success message appears, and that the user is redirected to the home page of the application

3. Home Page:
    1. Go to the "Home" page
    2. Try to scroll through the terms, and verify that the grid scrolls correctly and that all the terms appear in the grid
    3. Try to delete a term by clicking on the "Passe" button and verify that the term is removed from the home page (and removed from the MongoDB database)
    4. Try to edit a term by clicking on the "Refine" button and verify that the user is redirected to the edit term page 

4. Add Term Page:
    1. Go to the "Add Term" page
    2. Try to add a new term by clicking on the "Add Term" link in the Nav Bar, and verify that the user is redirected to the Add Term page
    3. Try to add a new term by filling out the fields in the form and verify that the term is added to the database and that the term appears on the homepage when the submit button is clicked

5. Edit Term Page:
    1. Try to click on the "Refine" button next to a term and verify that the user is redirected to the edit term page, with the fields of the edit form populated by the correct data (category, origin, definition)
    2. Try to edit each of the fields of the term and verify that the changes are submitted to the database, and reflected on the home page, when the submit button is clicked
   
6. Search for a Term:
    1. Go to the "Search" icon in the navbar
    2. Try to search for a term by entering a search query in the navbar, and verify that the user is redirected a results page
    3. Verify that the search results page contains all results that match the search query

7. Hilitor:
    1. Go to the "Search" icon in the navbar
    2. Try to search for a term by entering a search query in the navbar, and verify that the user is redirected a results page
    3. Verify that the results in the search results page that match the search query are highlighted

8. Logout:
    1. Click the "Logout" link in the navbar
    2. Verify that the user is logged out

The project was tested to verify it works on the following screen sizes:

1. Screensizes:
    1. iPhone 5 - iPhoneX
    2. iPad mini - iPadpro
    3. MacBook Pro
    4. iMac, 27 inch.

The project was tested to verify it works on the following browsers:
1. Browsers:
    1. Safari
    2. Chrome
    3. iOS

## Deployment

The application was coded on Cloud9 on AWS. The code was committed to GITHUB at https://github.com/kalkiboru111/irish-dictionary-of-received-ideas

The application was then deployed to Heroku at https://dictionary-of-received-ideas.herokuapp.com/

The database is stored on MongoDB. The database is setup within Heroku.

## Credits
Login and Registeration functionalities were taken from "Pretty Printed" github (on the understanding that authentication is not one of the criteria of assessment for this milestone project, as mentioned in the project submission guidelines.)
Voting functionality was adapted from the code here: https://www.cssscript.com/instagram-style-voting-system-versus/

### Acknowledgements

- I received inspiration for this project from Gustave Flaubert's "Dictionary of Received Ideas" (en Francaise, Le Dictionnaire des idées reçues), 
a short satirical work collected and published in 1911 (https://en.wikipedia.org/wiki/Dictionary_of_Received_Ideas).