# Recipe Sharing - Data-Centric-Milestone-3

## Introduction
This project is developed with the intention for users to share their recipes with others. The main functions of this Recipe Sharing revolves around the 4 functionalities- Create, Read, Update, Delete.

Database was stored and retrieved from the backend (MongoDB).

I chose to do recipe sharing as I enjoy cooking and wish to share my personal recipes with others. Likewise, I am also interested in other people's recipes and I can also try them out on my own.

## UX
| User Stories        | Description   |  
| :------------- |:-------------| 
| 1    | As someone who enjoys cooking, I want to share my recipes with like-minded people so that they can whip up dishes that they also like.|
| 2    | As a person who does not know much about cooking, I want to have access to various recipes so that I have the steps for recipes that may interest me.|
| 3    | As a general user, I wish that there are such recipe sharing platforms so that I can use them whenever I need. |


The website will be designed based on the identified goals and hence allow users to do the following:

-add new recipes to the website where they can include the cuisines, the recipe name, the ingredients, and the cooking steps.

-edit any recipe on the website.

-view details of the individual recipes.

-delete any recipe.

-search recipe by cuisines.


(i) Wireframes

[Wireframes DataCentric](https://drive.google.com/open?id=1UnhRookhnV4_G75Wt2_pGjqgzN7CFKan)

## Project Skeleton - Features

**Existing Features**

-The Recipe Sharing logo on the top left side of the navbar links to the mainpage.

-The Search by Cuisine button allows users to search for recipes by cuisines where it is designed to be case insensitive.

-The All Recipes button allows users to see all the recipes available in the website that has been added by other users.

-The Add Recipe button allows users to add recipe to the website.

-Users can click on the edit button if they want to update or change details of specific recipes.

-Users can click on the delete button if they want to remove a specific recipe from the website.

-Users can click on the view button to see the details of the specific recipe where the ingredients will be returned as an unordered list and the cooking steps will be returned as an ordered list. Users will have to add semicolon after each steps to denote a separation of each step.


**Feature(s) for Future Implementation**

Implement sign in feature for users such that only signed in users can share recipes and only delete their own recipes.

The ability to upload images for individual recipes.


## Testing (Manual)

(i) Mobile Responsiveness

The website has been tested on **Macbook Air/iPad Mini/iPad/iPhone XS/iPhone 6/ Sony Xperia** which covers various screen-size. The browsers used for testings are Google Chrome & Apple Safari.

During the testing process, I found out that:

-On devices such as iPhone X or smaller screen sizes, the brand logo 'Recipe Sharing' overspills to the next line. Hence I added media query such that from screen sizes of iPhone X and below, the font size will decrease.

-Search results will not be shown if I did not type in the exact cuisine name. Hence, the regular expression function has been used to make search function dynamic.

-Ordered list was unable to display properly in the view recipe page. Hence, I used split to solve the problem and the steps is now able to be displayed in an ordered list.


(ii) Test Cases

| Test Case(s)      | Test Description   | Outcome | 
| :------------- |:-------------| :-------------| 
| 1    | Users will see all recipes at the landing page. | Pass|
| 2    | If on mobile, users will see a navbar on top with a hamburger on the left and the brand logo 'Recipe Sharing' in the middle. | Pass|
| 3    | When users click on the hamburger, they will see 3 links 'Search by Cuisine', 'All Recipes', and 'Add Recipe', on top of one another| Pass|
| 4    | If on web browser on laptop/desktop, users will see a navbar on top with the brand logo on the left and the other 3 links 'Search by Cuisine', 'All Recipes', and 'Add Recipe' on the right side. | Pass|
| 5    | At the landing page, when users click on the edit button, they will be able to edit and update the recipe that they selected. | Pass|
| 6    | At the landing page, when users click on the delete button, they will be able delete the selected recipe. | Pass|
| 7    | At the landing page, when users click on the view button, they will be able to see the details of the recipe that they have selected where the ingredients appear as an unordered list and the cooking steps appear as an ordered list. | Pass|
| 8    | When users click on the 'Search by Cuisine' button on the navbar, they will be able to see a search bar and the list of recipes below. | Pass|
| 9    | When users search for the cuisine that they want, relevant results will appear below. | Pass|
| 10   | When users click on the 'All Recipes' button and the brand logo 'Recipe Sharing', it will direct them to the main/landing page. | Pass|
| 11   | When users click on the 'Add Recipe' button, they will see a form where they can choose a cuisine category by clicking on the dropdown button, add their recipe name, the ingredients and the cooking steps. After adding, the recipe will be shown in the All Recipes page. | Pass|


## Technologies Used

* [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)/[JQuery](https://jquery.com/download/)
* [Python3](https://www.python.org/)
* [Flask](https://pypi.org/project/Flask/)
* [NoSQL-MongoDB](https://www.mongodb.com/)
* [Materialize CSS- 0.100.2](http://archives.materializecss.com/0.100.2/)
* [Google Fonts](https://fonts.google.com/)
* [Heroku](https://www.heroku.com/)

## Deployment
### GitHub Deployment

My code was written using AWS Cloud9. AWS Cloud9 serves as the local repository which was then deployed to GitHub. Whenever a new commit is done to the master branch, the deployed site will be updated accordingly. 

This repository can also be deployed locally by cloning the repository. This can be done by going to the main page of the repository to clone/download directly into the editor of choice by pasting git clone into terminal.

### Heroku Deployment

- Project was also deployed and hosted to heroku. Website can be found [here](https://lzq-recipe-share.herokuapp.com/)
- Created Procfile and requirements.txt for dependencies.
- Created new heroku app and set environment variables.
- Linked Github and environment with Heroku.
- Project was pushed to Heroku once in awhile to ensure that update features are working.


## Credits

1) Website design/outlook was inspired by http://recipebook-project.herokuapp.com/

2) Background image was taken from [Pexels](https://www.pexels.com/)

3) [Stack Overflow](https://stackoverflow.com/)

4) [w3schools](www.w3schools.com)

**This is for educational use only.**


