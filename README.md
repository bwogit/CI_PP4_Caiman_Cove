# caribbeann Cove

![Am I Responsive](docs/)

**Developer: BWOGIT**

💻 [Visit live website](https://herokuapp.com/)  
(Ctrl + click to open in new tab)



## Table of Contents
  - [About](#about)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
    - [Wireframes](#wireframes)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
    - [Tests on various devices](#tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

### About

Caribbean Cove is a restaurant. This project is a smart interface which will allow the user to brose the menu online and make a reservation. The user can then view his reservations, edit and delete them.
<hr>

### User Goals

- Make a reservation
- Manage Bookings
- Explore menus, a blog and contact info

### Site Owner Goals

- Enable online Table reservations
- Enhance business appeal with a polished website
- Deliver a User-Friendly Modern experience
- Ensure Full Responsiveness and Accessibility
<hr>

## User Experience

### Target Audience
- Users that wish to book a table to experience culinary prestige and Glamour
- Tourists for memorable dining experience
- Attract local and visiting guests

### User Requirements and Expectations

- Seamless responsiveness across diverse devices and screen sizes
- Compliance with accessibility standards to ensure inclusivity
- Implementation of an inviting and user-centric design
- Integration of social media functionalities for enhanced engagement
- Clear presentation of relevant contact information
- Prioritization of accessibility features to ensure inclusiveness

##### Back to [top](#table-of-contents)<hr>


## User Stories

### Users
1.	As a User, I can Navigate the Site Easily and Intuitively:
2.	As a User, I can Efficiently Use the Navbar, Footer, and Social Media Icons
3.	As a User, I can access a dedicated "Contact Us" Page for Effective Communication
4.	As a User, I can quickly Access Opening Hours and Essential Contact Information iemail, phone, and social media.
5.	As a User, I can Seamlessly Choose Preferred Dates and Times for Reservation
6.	As a User, I can asily modify my booking by selecting an alternative
7.  As a User, I can Conveniently Delete My Reservation
8.  As a User, I can Easily View My Booked Reservations
9.  As a User, I can Receive Timely Alerts for Booking Actions 
10. As a User, I can Register to Enable Reservation Creation
11. As a User, I can Authenticate Myself to Access Reservation Functionality
12. As a User, I can Clearly Observe My Current Login Status
13. As a User, I can Experience Admin-controlled Booking Confirmation Modes
14. As a User, I can Engage with Informative Blog Content
15. As a User, I can Explore the Comprehensive Food and Drink Menu
16. As a User, I can Ensure Future-Date Bookings
17. As a User, I can Prevent Duplicate Bookings



### Admin / Privileged User
18.	As an Admin or Privileged User, I can Log In to Access the Site's Backend
19.	As an Admin or Privileged User, I can Manually Add Bookings for Phone or Email Reservations 
20. As an Admin or Privileged User, I can Accept or Reject Bookings to Prevent Double Bookings
23. As an Admin or Privileged User, I can Search Through Bookings and Menus
24. As an Admin or Privileged User, I can Filter Bookings by Date for Specific Day Insight
21. As an Admin, I can Log In to Manage Food and Cocktail Menu Items
22.	As an Admin, I can CRUD Food and Drink Items in the Database

### Site Owner  
23. As a Site Owner, I Can Offer a Fully Responsive Site for Optimal User Experience
24. As a Site Owner, I Can Implement Data Validation to Ensure Accurate Submission.

### Kanban
- GitHub Kanban was used to track all open user stories
- Backlog, In Progress, Done headings were used in the kanban

<details><summary>Epics</summary>
</details>

<details><summary>User Stories</summary>
</details>

<details><summary>kanban</summary>
</details>

##### Back to [top](#table-of-contents)<hr>

## Design

### Colours

The choice of a dark background for the website draws inspiration from the allure of a luxurious jewelry box's dark material. This carefully selected color scheme serves to elevate the visual presentation of the website's content, especially the high-quality images of exquisite dishes and captivating ambiances. By embracing the dark backdrop, the website aims to create a sense of opulence and sophistication, mirroring the lavishness associated with the Caribbean Cove's culinary offerings

### Fonts

 The fonts selected were from Google Fonts, Montserrat wits sans-serif as a backup font.

### Structure

#### Website pages
The website design prioritizes user freindliness, featuring a top navigation bar for seamless navigation and a hamburger menu button for smaller screens. This ensures an intuitive user experience across devices.

Prominently featured in the footer are essential social media links, enabling users to engage with the business across various platforms. This strategic inclusion enhances the business's online presence, garnering followers, likes, and shares. The site features the following pages:

 - A dynamic homepage with intuitive cards for table booking and menu exploration.
 - A comprehensive food menu, thoughtfully sorted into starters, mains, and desserts, showcasing the rich array of culinary offerings.
 - An expansive drinks menu categorized by type, presenting a diverse selection of available beverages.
 - An engaging blog section, thoughtfully paginated, where authorized users share insights and experiences.
 - Detailed blog expansion offers users an opportunity to delve into selected content, with logged-in users contributing moderated comments.
 - The user-friendly booking page empowers registered users to effortlessly secure a table by specifying guest count, date, time, and desired table location.
 - The "My Bookings" section conveniently displays users' active reservations, automatically expiring past bookings.
 - The edit booking feature allows users to adapt reservation details, including date, time, table, and guest count.
 - The cancel booking option permits hassle-free reservation cancellation, removing bookings from the database.
 - The "Contact Us" page facilitates user communication via DM for registered users, or via the provided email, phone number, or physical  address.
 - The seamless "Login" and "Logout" functionality enables users to access booking features and reservation management.
 - The registration process empowers users to create accounts, facilitating access to the booking system.
 - A polished "404 Error" page elegantly addresses any encountered errors.

 #### Database

- Built with Python Django framework and Postgres for deployement to heroku

<details><summary>Show diagram</summary>
<img src="docs/erd_output.png">
</details>

##### User Model
The User is a built-in Django feature and is used for authentication and has the following fields:
- user_id
- password
- last_login
- is_superuser
- username
- first_name
- last_name
- email
- is_staff
- is_active
- date_joined

<details><summary>Show model</summary>
<img src="docs/model_User.jpg">
</details>

##### FoodMenuItem Model
The FoodMenuItem Model contains the following fields:
- food_item_id
- food_item_name
- food_description
- food_price
- food_available

<details><summary>Show model</summary>
<img src="docs/model_FoodMenuItem.jpg">
</details>

##### DrinkMenuItem Model
The DrinkIMenutem Model contains the following fields:
- drink_item_id
- drink_item_name
- drink_description
- drink_price
- drink_available

<details><summary>Show model</summary>
<img src="docs/model_DrinkMenuItem.jpg">
</details>


##### Table Model
The Table Model contains the following fields:
- table_id (PrimaryKey)
- capacity
- reserved
- table_number

<details><summary>Show model</summary>
<img src="docs/model_Table.jpg">
</details>

##### Reservation Model
The Reservation Model contains the following fields:
- reservation_id (PrimaryKey)
- reserved_date
- requested_date
- reserved_time_slot
- table (ForeignKey)
- user (ForeignKey)
- guest_count
- name
- email
- phone
- status
- seats

<details><summary>Show model</summary>
<img src="docs/model_reservation.jpg.jpg">
</details>

##### Post Model
The Post Model contains the following:
- post_id (PrimaryKey)
- author (ForeignKey)
- content
- created_on
- excerpt
- featured_image
- slug
- status
- title
- updated_on

<details><summary>Show model</summary>
<img src="docs/model_post.jpg">
</details>

##### Comment Model
The Comment Model contains the following:
- id (primary Key)
- post (ForeignKey)
- approved
- body
- created_on
- email
- name

<details><summary>Show model</summary>
<img src="docs/model_Comment.jpg">
</details>

##### Contact Model
The Contact Model contains the following fields:
- message_id (PrimaryKey)
- user (ForeignKey)
- email 
- message
- name
- phone

<details><summary>Show model</summary>
<img src="docs/model_Contact.jpg">
</details>

### Wireframes
The wireframes were created using Balsamiq

#### home page
Home page responsive wireframes

<details><summary></summary>
<img src="docs/wireframes/wireframes_home.jpg">
</details>

#### meal/drink menu page
Menus responsive wireframes
<details><summary></summary>
<img src="docs/wireframes/wireframes_menu.jpg">
</details>

#### book a table page
Book a table through this responsive and high quality app
<details><summary></summary>
<img src="docs/wireframes/wireframes_book.jpg">
</details>

#### View past and future bookings page (data gathering)
View bookings
<details><summary></summary>
<img src="docs/wireframes/wireframes_bookings.jpg">
</details>

#### Read the blogs page
Read the blogs from a variaty of interesting topics page
<details><summary></summary>
<img src="docs/wireframes/wireframes_blog.jpg">
</details>

#### Enquire page
Enquire / Contact us and we will get backt to you
<details><summary></summary>
<img src="docs/wireframes/wireframes_contact_us.jpg">
</details>

#### Logout page
You can now log ou in a safe manner. 
<details><summary></summary>
<img src="docs/wireframes/wireframes_logout.jpg">
</details>

#### Login required (booking)
You have to log in before you book a table
<details><summary></summary>
<img src="docs/wireframes/wireframes_book_login_required.jpg">
</details>

#### Blog (login required)
Blog log in required
<details><summary></summary>
<img src="docs/wireframes/wireframes_Blog_loggedIn.jpg">
</details>

#### Blog Read more 
You have found the topic that you want to delve into.
<details><summary></summary>
<img src="docs/wireframes/wireframes_Blog_read_more.jpg">
</details>

#### Enquire 
Enquire (loging Required)
<details><summary></summary>
<img src="docs/wireframes/wireframes_Enquire_login_required.jpg">
</details>

#### Log IN
Responsive LogIn
<details><summary></summary>
<img src="docs/wireframes/wireframes_login.jpg">
</details>

#### Sign up
Responsive sign up page
<details><summary></summary>
<img src="docs/wireframes/wireframes_SignUp.jpg">
</details>


## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Django


### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/)
- [Balsamiq](https://balsamiq.com/)
- [Bootstrap v5.2](https://getbootstrap.com/)
- [Cloudinary](https://cloudinary.com/)
- [Favicon.io](https://favicon.io)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
- [Font Awesome](https://fontawesome.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Google Fonts](https://fonts.google.com/)
- [Heroku Platform](https://id.heroku.com/login)
- [jQuery](https://jquery.com)
- [Postgres](https://www.postgresql.org/)
- [Summernote](https://summernote.org/)
- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  - [JShint](https://jshint.com/)
  - [Pycodestyle(PEP8)](https://pypi.org/project/pycodestyle/)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
  - [Wave Validator](https://wave.webaim.org/)

  ##### Back to [top](#table-of-contents)

  ## Features

### Logo & Navigation
- Logo
- Responsive down to hamburger menu
- Indicates login/logout in status
- displayed on all pages (inc. 404)

<details><summary>See feature images</summary>

![Footer](docs/feature/feature_navbar.jpg)
</details>

### Footer
- Includes social media links and all details of a modern business (email, telephone address, and opening hours)
- consistently visible on every page

<details><summary>See feature images</summary>

![Footer](docs/feature/feature_footer.jpg)
</details>

### Home page
- Home page includes nav bar, main body and a footer

<details><summary>See feature images</summary>

![Home page](docs/feature/features_home.jpg)
</details>


### Food Menu
- The food menu showcases a comprehensive selection of available dishes.
- The menu is categorized into starters, main courses, and desserts.
- Authorized staff members can edit the menu via the backend admin panel.
- uthorized staff members can perform actions such as creating, updating, and removing food items using the admin panel.
  
<details><summary>See feature images</summary>

![Food Menu](docs/feature/feature_meals_menu.jpg)
</details>


### Drinks Menu
- The drink menu showcases a comprehensive selection of available drinks.
- The menu is categorized into non alcoholic, cocktails, beers and ruhums
- Authorized staff members can edit the menu via the backend admin panel.
- uthorized staff members can perform actions such as creating, updating, and removing drink items using the admin panel.
<details><summary>See feature images</summary>

![Drinks Menu](docs/feature/feature_drinks_menu.jpg)
</details>

### Login
- User is required to login to reserve a table, view bookings, 
edit and delete bookings and comment a blog.

<details><summary>See feature images</summary>

![Login](docs/feature/feature_login.jpg)
</details>


### Logout
- Allows the user to securely log out

<details><summary>See feature images</summary>

![Logout](docs/feature/feature_logout.jpg)
</details>

### Sign up / Register
- Allow users to create an acoount
- Use Django built-in authentication. Seameless.


<details><summary>See feature images</summary>

![Register](docs/feature/feature_signup.jpg)
</details>


### Blog
- The blog displays each post made by authorised user
- The main blog list features exerpts and Pictures
- Paginations is used to display 2 posts per page
  
<details><summary>See feature images</summary>

![Blog](docs/feature/feature_blog.jpg)
</details>


### Blog Read More
- Click on read more to expand the selection you have chosen
- Registerd user can comment on the blog
- Staff can approve comments via the admin panel on the backend
  
  
<details><summary>See feature images</summary>

![Blog Expanded](docs/feature/feature_blog_read_more.jpg)
</details>


### Comments
- Comments made are set to pending approval status
- Only registered users can comment on a blog post
- Staff are the moderators
  
<details><summary>See feature images</summary>

![Comments](docs/feature/feature_blog_comments.jpg)
</details>

### Pagination
- used on the blog page
- Ensures the page is kept tidy as only 2 items are displayed per page
  
<details><summary>See feature images</summary>

![Pagination](docs/feature/feature_pagination.jpg)
</details>


### Contact Us
- Registered users can DM staff via the message box
- Contact info such as,name, email, and address is displayed
  
<details><summary>See feature images</summary>

![Contact Us](docs/feature/feature_enquire.jpg)
</details>

##### Back to [top](#table-of-contents)<hr>


## Validation

The W3C Markup Validation Service
<details><summary>Home</summary>
<img src="docs/validation/validation_html_index.jpg">
</details>

<details><summary>SingUp</summary>
<img src="docs/validation/validation_html_signup.jpg">
</details>

<details><summary>Login</summary>
<img src="docs/validation/validation_html_login.jpg">
</details>

<details><summary>Logout</summary>
<img src="docs/validation/validation_html_logout.jpg">
</details>

<details><summary>Bookings</summary>
<img src="docs/validation/validation_html_booking_list.jpg">
</details>

<details><summary>Booking confirmation</summary>
<img src="docs/validation/validation_html_booking_confirmation.jpg">
</details>

<details><summary>Edit Booking</summary>
<img src="docs/validation/validation_html_edit_booking.jpg">
</details>

<details><summary>delete Booking</summary>
<img src="docs/validation/validation_html_delete_booking.jpg">
</details>

<details><summary>Meal Menu</summary>
<img src="docs/validation/validation_html_food_menu.jpg">
</details>

<details><summary>Beverage Menu</summary>
<img src="docs/validation/validation_html_drink_menu.jpg">
</details>

<details><summary>Blog</summary>
<img src="docs/validation/validation_html_blog_list.jpg">
</details>

<details><summary>Blog Read more</summary>
<img src="docs/validation/validation_html_blog_details_1.jpg">
</details>

<details><summary>Enquire</summary>
<img src="docs/validation/validation_html_contact_us.jpg">
</details>

<details><summary>Confirmed</summary>
<img src="docs/validation/validation_html_booking_confirmation.jpg">
</details>

<details><summary>404</summary>
<img src="docs/validation/validation_html_404.jpg">
</details><hr>


### CSS Validation
The W3C Jigsaw CSS Validation Service

<details><summary>Style.css</summary>
<img src="docs/validation/validation-css.jpg">
</details><hr>



### PEP8 Validation
PEP8 Validation Service from CodeInstitute was used.
- [pep8ci](https://pep8ci.herokuapp.com/)

<hr><summary>food_and_drinks</summary><hr>

<details><summary>admin.py</summary>
<img src="">
</details>


<details><summary>views.py</summary>
<img src="docs/validation/pep8-food_and_drinks_views.jpg">
</details>

<details><summary>urls.py</summary>
<img src="docs/validation/pep8-food_and_drinks_urls.jpg">
</details>

<details><summary>models.py</summary>
<img src="docs/validation/pep8-food_and_drinks_models.jpg">
</details>

<details><summary>admin.py</summary>
<img src="docs/validation/pep8_food_and_drinks_admin.jpg">
</details>

<hr><summary>blog</summary><hr>

<details><summary>views.py</summary>
<img src="docs/validation/pep8_blog_views.jpg">
</details>

<details><summary>urls.py</summary>
<img src="docs/validation/blog_urls.jpg">
</details>

<details><summary>forms.py</summary>
<img src="docs/validation/pep8_blog_forms.jpg">
</details>

<details><summary>models.py</summary>
<img src="docs/validation/pep8_blog_models.jpg">
</details>

<details><summary>admin.py</summary>
<img src="docs/validation/pep8_blog_admin.jpg">
</details>

<hr><summary>contact_us</summary><hr>

<details><summary>views.py</summary>
<img src="docs/validation/pep8_contact_us_views.jpg">
</details>

<details><summary>models.py</summary>
<img src="docs/validation/pep8_contact_us_models.jpg">
</details>

<details><summary>urls.py</summary>
<img src="docs/validation/pep8_contact_us_urls.jpg">
</details>

<details><summary>forms.py</summary>
<img src="docs/validation/pep8_contact_us_forms.jpg">
</details>

<details><summary>admin.py</summary>
<img src="docs/validation/pep8_contact_us_admin.jpg">
</details>

<hr><summary>home</summary><hr>

<details><summary>views.py</summary>
<img src="docs/validation/pep8_home_views.jpg">
</details>

<details><summary>urls.py</summary>
<img src="docs/validation/pep8_home_urls.py.jpg">
</details>

