# **espressOrders** 

[View espressOrders website ](https://ab79-espressorders-dev.herokuapp.com/)

This espressOrders website has been produced by Andrew Boyd as a Milestone Project 4 for the Code Institute’s Full Stack Web Development course.

They seem to be everywhere you look these days - coffee carts!
From little trucks to converted horse boxes they are popping up everywhere - from beauty spot carparks, to the beach and even at kids football matches. The "post-covid" work office seems also to have created a coffee cart culture and it is this that I hope the espressOrders application will tap into.

The purpose of espressOrders is to allow ordering from your favourite coffee cart ahead of time - to beat that inevitable queue! 

The website aims to allow users to select a coffee cart and browse drinks are available from that cart; allow users to make their selection and customise their order and then pay for it within espressOrders site. The user will get confirmation of their order with a qr code, which will speed up collection and order processing and they have the ability to save their details for future visits.

---

## **Contents**
1. **[UX](#ux)**
    - [Business Goals](#Business-Goals)
    - [Target Audience](#Target-Audience)
    - [User Goals](#User-Goals)
    - [User Stories](#User-Stories)
    - [User Considerations](#User-considerations)
    - [Wireframe diagrams](#Wireframe-diagrams)
        - [Home Page](#Home-page)
        - [Places to go Page](#Places-to-go-page)


    - [Design Considerations](#Design-considerations)
        - [Colours](#Colours)
        - [Fonts](#Fonts)
        - [Icons](#Icons)

2. **[Features](#Features)**
    - [Initial Release Features](#Initial-release-features)
        - [Global Features](#Global-features)
        - [Home Page Features](#Home-page-features)
        - [Places to go Page Features](#places-to-go-page-features)

    - [Features for future releases](#Features-for-future-releases)

3. **[Technologies Used](#Technologies-used)**
    - [Languages](#Languages)
    - [Libraries](#Libraries)

4. **[Testing](#Testing)**

5. **[Deployment](#Deployment)**

6. **[Credits](#Credits)**
    - [Images](#Images)
    - [Content](#Content)
    - [Code](#Code)
    - [Acknowledgements](#Acknowledgements)
---

# **UX**
User Experience, and associated UX design, is concerned with how a user interacts with something; throughout this project, consideration has been given to each of the five planes of UX.

## Business Goals
The business expects this website to:
- Provide information regarding the service and give users information on their carts
- Display the products available in each of the cart locations - over time each carts menu will evolve and so will differ from the others
- Allow for addition, editing and deleting of products from the cart menu - only admin/superuser accounts should have this ability
- Have necessary security functionality to ensure users cannot access admin functions
- Record all the details necessary to process a customers order - this will include recording order, user and billing information
- Take payment for a customers order
- Promote their business/brand as a convenient and easy to use

## Target audience
The target audience of this website is:
- Individuals who frequently user coffee carts
- Individuals who have limited time available over their break/lunchtime
- Office groups/departments who make larger orders on a daily basis and want a more convenient method of ordering
    
Users will be expecting information presentation to be:
- Accurate – information needs to be not only factually correct but up to date
- Clear – well presented in a logical fashion
- Engaging – the website should encourage users to want to use it and come back to it
- Intuitive - it should be quick and easy to use

## User Goals
Users of this website expect to be able to:
- select and order coffee from their chosen coffee cart
- customise and pay for their order securely
- find out relevant information about the coffe cart 


## User Stories
The following user stories have been developed to outline some of the benefits the website has to its users:

1. As a customer I expect to be able to find information about where the coffee carts are located
2. As a customer I expect to be able to find out the opening hours of the carts
3. As a customer I expect to be able to see what product is available at each cart location
4. As a customer I expect to be able to search for items directly
5. As a customer I expect to be able to filter/sort products by their type
6. As a customer I expect to be able to find information about each item
7. As a customer I expect to be able to customise my order
8. As a customer I expect to be able to clearly see the costs of the items and total order before payment
9. As a customer I expect to be able to pay for my order through the website
10. As a customer I expect to be able to save my details to speed up my purchasing experience; I also expect to be able to check out with saving my details
11. As a customer I expect to be able to update my details if they have changed since last purchase
12. As a customer I expect to be able to review my past orders
13. As a customer I expect to be able to keep my personal information secure

14. As a business owner I expect to be able to add, edit and remove items from the product range
15. As a business owner I expect to be able to record/store/access all information necessary to take payments for customer orders 
16. As a business owner I expect to be able to have a means to quickly differentiate between customer orders to ensure each customer gets their order correctly
17. As a business owner I expect to be able to be sure that an order is recorded if a user has successfully paid for it (redundancy built in to system)
18. As a business owner I expect to be able to secure the site so only authorised user can access/edit products
19. As a business owner I expect to be able to allow users to access relevant socail media channels


## User considerations
Consideration has been given to the following when developing a website which meets the needs of both the business and the users:

- INSERT ANY USER CONSIDERATIONS

## Wireframe diagrams

### Home Page 

 - [Mobile view](LINK TO MOBILE VIEW)
 - [Tablet view](LINK TO TABLET VIEW)
 - [Desktop view](LINK TO DESKTOP VIEW) 

### Product Page

 - [Mobile view](LINK TO MOBILE VIEW)
 - [Tablet view](LINK TO TABLET VIEW)
 - [Desktop view](LINK TO DESKTOP VIEW)

### Description Page

 - [Mobile view](LINK TO MOBILE VIEW)
 - [Tablet view](LINK TO TABLET VIEW)
 - [Desktop view](LINK TO DESKTOP VIEW)

### Login Page

 - [Mobile view](LINK TO MOBILE VIEW)
 - [Tablet view](LINK TO TABLET VIEW)
 - [Desktop view](LINK TO DESKTOP VIEW)

### Registration Page

 - [Mobile view](LINK TO MOBILE VIEW)
 - [Tablet view](LINK TO TABLET VIEW)
 - [Desktop view](LINK TO DESKTOP VIEW)

### Order Summary Page

 - [Mobile view](LINK TO MOBILE VIEW)
 - [Tablet view](LINK TO TABLET VIEW)
 - [Desktop view](LINK TO DESKTOP VIEW)

### Profile Page

 - [Mobile view](LINK TO MOBILE VIEW)
 - [Tablet view](LINK TO TABLET VIEW)
 - [Desktop view](LINK TO DESKTOP VIEW) 

## Design Considerations

### Colours

These have been selected to give a clean minimal look to the website.  
 - White - #ffffff
 - Dark Grey - #151515
 - Mid Grey - #2f3434
 - Rust - #A75121
 - Light Green - #7AA27F

The combination has been checked on Adobe Colour; no potential conflicts have been found and the swatches are colour blind safe.

### Fonts

- Poiret One - this has been chosen as the brand font for the espressOrders site. It is distinctive enough to stand out but remains readable at all sizes. Poiret One is available only at a weight of 200. It is available from Google fonts nad it it fails it will be replaced with a cursive font within the browser.

- Raleway - this sans-serif font has been chosen to compliment Poret One, with both fonts sharing similar distinctive characters which makes them sit well together. It is being used at weights 200 & 400 across the site. It is available on Google fonts and if it fails it will be replaced with a sans serif font within the browser.

### Icons
The following Font Awesome icons from will be used throughout this website:

- [Mug Hot]( https://fontawesome.com/v5.15/icons/mug-hot?style=solid )
- [Search]( https://fontawesome.com/v5.15/icons/search?style=solid )
- [User Edit]( https://fontawesome.com/v5.15/icons/user-edit?style=solid )
- [User Edit]( https://fontawesome.com/v5.15/icons/user-edit?style=solid )
- [Wrench]( https://fontawesome.com/v5.15/icons/wrench?style=solid )
- [ID Card]( https://fontawesome.com/v5.15/icons/id-card?style=solid )
- [Sign Out]( https://fontawesome.com/v5.15/icons/sign-out-alt?style=solid )
- [User]( https://fontawesome.com/v5.15/icons/user-plus?style=solid )
- [Sign In]( https://fontawesome.com/v5.15/icons/sign-in-alt?style=solid )
- [Shopping Basket](https://fontawesome.com/v5.15/icons/shopping-basket?style=solid )
- [Facebook](https://fontawesome.com/v5.15/icons/facebook?style=brands )
- [Twitter](https://fontawesome.com/v5.15/icons/twitter?style=brands )
- [Instagram](https://fontawesome.com/v5.15/icons/instagram?style=brands )
- [Plus Circle](https://fontawesome.com/v5.15/icons/plus-circle?style=solid )
- [Minus Circle](https://fontawesome.com/v5.15/icons/minus-circle?style=solid )
- [Times Circle](https://fontawesome.com/v5.15/icons/times-circle?style=regular )
- [Exclamation Circle](https://fontawesome.com/v5.15/icons/exclamation-circle?style=solid )
- 

### Styling
The website was styled to give a minimalistic feel.
---

# **Features**
The website will initially be developed as a Minimal Viable Product (MVP) and developed from there with new features being added as time/developer skills allow.

## Initial release features
Based on importance/feasability analysis the following features will be available in the initial release:

- The user will be able to select which cart they are wishing to order from. This will give the site owner the opportunity to be set a list of products which are specific to a cart.
- Useful user information is available on each cart location.
- The user will have the ability to filter the drinks according to type (Hot Drinks/Cold Drinks/Iced Drinks) and by category within these types (Coffee/Rea/Speciality Coffee within the Hot Drinks type). Defining a product by type and category allows for easily managed expansion/diversification of the product line within significant refactoring of the codebase. Selecting an options (type or category) filters the products displayed accordingly.
- The user will have the ability to search within the name / description fields.
- The user will be initially be able to specify the product they wish to order, its size and the quantity. Where products are only available in single size this will be detailed within the product description.
- The users current order will be stored in a bag which is stored in session cookies. This allows the user to continue where they left off with their order if they need to leave/return. Items can be removed from the bag and the bag is cleared once an order has been successfully placed.
- Users can pay for their items using a secure Stripe payment form.
- Users specify at the checkout which cart they want to collect their order from.
- Users can save their default profile information to save them having to complete them if returning. Users can register for a profile to allow them to do this.
- Users can be assured that their order will be recorded if payment is successfuly as the site can record orders through the payment intent/webhook handler if the user form isn't submitted successfully.
- Users can view and update their default profile information.
- Users can also view details on all previous orders (summary and full details).
- Order information a QR Code which the user can use to speed up order collection process.
- Site administrators have the ability to add/edit and delete items from the product line

## Global Features
The following features will persist across all website pages to provide a consitent look and feel:
 - Header section
    - Branding - the espressOrders name will be located in the top left portion of the header; it will provide consistent branding.  Clicking on the logo returns the user to the home page. The branding alter location to the centre on smaller screen sizes as the options collapse under a hamburger menu icon.
    - Navbar - the nav bar is comprised of home elements to the left side of the screen, search box in centre and account/basket info on the right side of screen on desktop. Home button is displayed on all pages apart from the home page itself (where it is not necessary). There is a dropdown menu under the My Account icon housing the Product Management/User Profile and Login/out functionality.
    - The navbar/secondary navbar will size responsively and the icons/menus will drop under a hamburger icon located on left hand side of screen; the basket remains visible on all screen sizes on the right hand side of the display. 
    - Secondary navbar - on all pages (apart from the home page) a secondary navbar exists with the product types/categories. Each houses a dropdown to allow the user to choose a product type/category as appropriate. This also drops under the hamburger icon on smaller screen sizes.
    - Subhead banner - a subheading banner, in contrasting colour, is displayed on all screen sizes. This allows the site administrator to provide promotion/information to site users in a prominent location. 

- Footer Section
    - Sitting above the main footer section, in contrasting colours, are the sicial media icons which take users to site related Facebook, Twitter or Instagram accounts. This is displayed on all screen sizes.
    - The main footer section is broken down into three distinct elements.
    - A types filter (Hot Drinks/Cold Drinks/Iced Drinks) is present on left hand side of branding. Unlike the header there is no dropdown option displaying categories. This element persists on smaller screen sizes.
    - A further branding element exists on larger screen sizes only - clicking the element returns the user to the homepage.
    - Useful information (Home/About Us/Profile) is present to the right hand side of the branding on larger screens and alongside the types filter on smaller screen sizes. 
    - The footer elements will resize responsively.

## Home Page Features
 - HOME PAGE DESCRIPTION AND FEATURES

## OTHER PAGES Features
- OTHER PAGES DESCRIPTION AND FEATURES 


## Features for future releases
The following features will be added to the website in future releases:

- Further customisation options specific to each drink type/category will be available in future releases.
- Additional user payment options will be incorporated into the site to give the user further choice on how they wish to pay for their order.
- Email confirmation of user order with all order information/QR Code being included.
- Information on each cart will integrate Google Maps to show the cart on map and provide user directions from current location.
- The home page will feature a section suitable for information/blog posts to allow site administrator to engage more fully with users.
- Additional seasonal categories e.g. special offers, winter warmers etc. will be added to allow the site administrator to highlight specials and new product lines
- 
---

# **Technologies Used**

## Languages
- HTML5 was used to structure and present the content of this website
- CSS3 was used to style the presentation of the website
- JavaScript was used to control the interactive elements of the website
- INSERT OTHER LANGUAGES USED

## Frameworks/Libraries/Programs
- [BootStrap (4.5.3)](https://getbootstrap.com/) was used to aid with responsive design and increation of some of the project elements
- [jQuery (3.5)](https://api.jquery.com/) was used to aid in the writing of the JavaScript elements
- [Google Fonts](https://fonts.google.com/) was used to provide the Montserrat font
- [Adobe Fonts](https://fonts.adobe.com/) was used to provide the Brandon Grotesque font
- [Font Awesome](https://fontawesome.com/) was used to provide the icons for the project 
- [GitHub](https://github.com/andrewboyd79/CraftGinsNI) was used to hold the P-L-Services repository 
- [GitPod](https://gitpod.io/workspaces/) was used as the dev environment for the project
- INSERT OTHER FRAMWEORKS USED 

---

# **Testing**

A separate [testing.md](documentation/testing.md) file has been created to record the testing.

---

# **Deployment**

INSERT STEPS ON HOW TO DEPLOY TO GITHUB PAGES OR HEROKU 

---

# **Credits**

## Images
The following images have been used for this project:

- [INSERT LOCATION OF IMAGE ON SITE](INSERT WEB ADDRESS FOR IMAGE) - Image by INSERT CONTRIBUTOR NAME from WEBSITE NAME



## Content
- INSERT SOURCES OF ADDITIONAL CONTENT

## Code
- INSERT SOURCES OF ADDITIONAL CODE

## Acknowledgements
- Thanks to my mentor (Aaron Sinnott) for his guidance and help during this project
- Thanks to the Code Instutute Slack community who helped with various articles, suggestions and problem solves