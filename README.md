<a name="top"></a>
![Logo](documentation\logo.readme.png)


# "Discover Unique Art from Independent Artists"
- Original paintings, fine art prints, and one-of-a-kind pieces curated to inspire and transform your space.

## Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Shop Page Intro Text](#shop-page-intro-text)
- [Wireframes](#wireframes)
- [Custom 404 Page](#custom-404-page)
- [Technologies Used](#technologies-used)
- [Facebook Business Page](#facebook-business-page)
- [Newsletter Signup](#newsletter-signup)
- [E-commerce Business Model and Marketing Strategy](#e-commerce-business-model-and-marketing-strategy)
- [Agile Development and Project Planning](#agile-development-and-project-planning)
- [Deployment](#deployment)
- [Testing the Deployment](#testing-the-deployment)
- [Final Project Feature Checklist](#final-project-feature-checklist)

## About the Project

- Artworks Marketplace - Original Art Online is an e-commerce platform created to support and showcase emerging and independent artists, with a particular focus on the Berlin art scene.

- The platform allows visitors to explore original artworks by medium, artist, or theme, and securely purchase pieces for delivery.

### Features:

- Artist profiles with bio and portfolios
- A modern, responsive design
- User accounts with order tracking and wishlists
- Secure checkout using Stripe
- SEO and marketing integrations to build visibility

## Shop Page Intro Text

 - Explore the Collection
    - Discover new and featured works across mediums. Whether you're searching for a bold centerpiece or a thoughtful gift, you'll find something original and meaningful.

## Newsletter Signup Text

 - Stay Inspired. Get New Art in Your Inbox.
    - Be the first to hear about featured artists, new arrivals, and exclusive offers.
    (No Spam, unsubscribe anytime.)

## 404 Page Text

- Oops! Something's Missing.
    - The page you're looking for might have been moved or no longer exists.
    - "Even artists get lost sometimes. Let’s get you back on track!"

## Wireframes

- The wireframes were designed using Microsoft Word and reflect the core paths users would follow to navigate, browse, and purchase artwork.

### Overview of Wireframes Created:

1. Homepage / Hero Section
    - Introduces the platform with a bold call-to-action, features artworks, navigation menu, and footer. It includes a carousel of new arrivals and a short artist spotlight section.

2. Artworks Listing page
    - Displays a grid of artworks with filters for medium, price, popularity, and artist. Each item card includes an image, title, artist name, price and "Add to Cart" button.

3. Artwork Detail Page
    - Expanded view of a specific artwork, with details such as title, artist info, price, medium, and a purchase button. Related artworks are shown below.

4.  Artist Profile Page
    - Includes artist bio, profile photo, and portfolio. A "Follow" placeholder button is included for future email integrations.

5.  Cart Page
    - Lists selected items with thumbnails, title, price, quantity controls, and a remove button. Includes subtotal, estimated tax, and a checkout button.

6.  Checkout Page
    - Captures user details (billing/shipping), includes secure payment fields, trust badges, and a review summary before final purchase.

7.  Custom 404 Page
    - A friendly error message with brand-consistent visuals and link to navigate users back home or explore artworks.     

---

[Back to Top](#top)



## Custom 404 Page

To enhance user experience, a custom-designed **404 Error Page** was implemented. Rather than displaying a default error, users are shown a creative and on-brand message to keep them engaged:

> "_Even artists get lost sometimes. Let’s get you back on track!_"

- Features colorful imagery using artistic tools (paintbrushes)
- Uses playful, encouraging text
- Links users back to the homepage or suggested pages
- Reflects the tone and theme of the overall website

### Preview:
![Custom 404 Page](documentation/404-page.png)

##  Technologies Used

###  Languages & Frameworks

`HTML5` • `CSS3` • `JavaScript` • `Python 3` • `Django`

###  Front-End Tools

`Bootstrap 5` • `Font Awesome` • `Google Fonts`

###  Back-End Tools

`Django Models` • `SQLite` • `PostgreSQL` 

###  E-Commerce & Marketing

`Stripe` • `Mailchimp (or Brevo)` • `Facebook Page`

###  SEO & UX Features

`robots.txt` • `sitemap.xml` • `Meta Tags` • `Custom 404 Page`

###  Development & Deployment

`VS Code` • `Git` • `GitHub` • `GitHub Projects` • `Heroku` • `Gunicorn` • `Whitenoise`

###  Additional Tools

`Microsoft Word (for wireframes)` • `TinyPNG` • `Google Lighthouse` • `W3C Validators`


## Facebook Business Page

As part of the marketing strategy and assessment requirements, a **Facebook Business Page** was created to promote the Artworks Marketplace brand and simulate a real-world marketing presence.

### Purpose

The Facebook page serves as a demonstration of how the project could use social media for:

* **Brand exposure**
* **Customer engagement**
* **Event promotion**
* **Artwork highlights**

This exercise reinforces the importance of integrating social platforms into a broader e-commerce marketing plan.

### Page Features

* **Custom logo/profile image** created for the project
* **Cover photo** showcasing the theme of original, independent art
* **Welcome post** introducing the brand and its mission
* **Descriptive post** explaining the logo and what the site offers



### Screenshots

![Facebook Page Overview](documentation/facebook-overview.png)
![Welcome Post Screenshot](documentation/facebook-welcome.png)
![Logo Explanation Post](documentation/facebook-logo-post.png)
![Cover and Profile Images](documentation/facebook-cover-profile.png)


### Note for Assessors

As Facebook frequently removes inactive or mock pages, screenshots were taken to verify that this task was completed and should be considered during assessment.

---

[Back to Top](#top)



## Newsletter Signup

To simulate a standard e-commerce email marketing feature, a **newsletter signup form** was included in the application. This feature invites users to subscribe to updates about new artists, collections, and offers.

Although integration with Mailchimp was not completed (due to trial limits), the form is designed to support future integration **with** services such as: 

- [Brevo (formerly Sendinblue)](https://www.brevo.com/)
- [MailerLite](https://www.mailerlite.com/)
- [Moosend](https://mossend.com/)

### Why This Feature Matters:
- Encourage user engagement and retention
- Builds a potential audience for marketing campaigns
- Aligns with real-world best practices in e-commerce

### Form Features:
- Email input with validation
- Clear opt-in messaging
- Confirmation message upon submission
- Privacy reassurance (no spam!)

### Screenshot Example:
![Newsletter Signup Form](documentation/newsletter-signup.png)

## E-commerce Business Model and Marketing Strategy

### Business Model

Artworks Marketplace operates as a **B2C ( Business-to-Consumer)** platform, connecting individual customers with independent and emerging artists. The core goal is to create a curated online space where users can discover, explore, and purchase original art directly from the creators.

Revenue is modeled around:

- Direct sales of physical artworks
- Potential future commission-based earnings from featured artists
- Optional digital products (e.g. prints, downloads, event tickets) in future iterations

### Target Audience

- Art enthusiasts looking for unique, original pieces
- Gift buyers seeking meaningful, creative items
- Home decorators and interior stylists
- Supporters of the Berlin independent art scene

### Core Marketing Strategies

1. **Social Media Engagement**
    - A Facebook Business Page was created to showcase featured artworks and build brand awareness.
    - Future marketing may extend to Instagram for visual content and artist promotion.

2. **Email Marketing**
    - A newsletter signup form allows users to subscribe to updates and offers.
    - Campaigns may include featured artists, upcoming exhibitions, and new arrivals.

3. ****
    - Implementation of:
        - `robots.txt` and `sitemap.xml` for search visibility
        - Descriptive meta tags and rel attributes
        - Keyword-rich content to improve discoverability

4. **Content Marketing**
    - Blog-style content (planned) to share artist interviews, studio visits, and art-buying guides.
    - Helps establish authority and trust while improving SEO.

5. **Trust & Transparency**
    - Use of secure payment processing (Stripe)
    - Clear returns policy and support contact included in footer (planned)
    - Custom 404 page enhances user experience and retains users even on broken links

## Agile Development and Project Planning

This project followed agile methodologies using GitHub Project Board to track tasks and progress through development.

### GitHub Project Board Setup:

- **To Do** - User stories, planned features, and backlog tasks
- **In Progress** - Active development tasks
- **Done** - Completed features, wireframes, and documentation

Each card was based on a specific user story, ensuring a user-centered design approach and feature tracking.

[View GitHub Project Board](https://github.com/kakilian/artworks)

Screenshots of the board before and during development have been included for assessment purposes.

### Sample User Stories Tracked

- As a user, I want to browse artworks by medium so I can find a piece that matches my style.
- As a user, I want to add items to a shopping cart so I can purchase multiple artworks at once.
- As an admin, I want to add new artworks through a form without needing to access the Django admin panel.

### Screenshots

![GitHub Project board Overview](documentation/github-board-overview.png)
![Task Example](documentation/github-task-card.png)

---

[Back to Top](#top)



## Deployment

This application was deployed using **HEROKU**. The live site is available at:

![Live Site URL](https://artworks.herokuapp.com)

- Deployment Steps:

1. **Set Up GitHub Repository**
    - Created a new public GitHub repository and pushed the complete project code
    - Included `README.md`, `.gitignore` and required project structure

2. **Environment & Dependencies**    
    - Set environment variables in the HEROKU dashboard:
        - `SECRET KEY`
        - `DEBUG=False`
        - `DATABASE_URL`
        - `STRIPE_PUBLIC_KEY`, `STRIPE_SECRET_KEY`, `STRIPE_WH_SECRET`
    - Installed necessary packages for deployment:
    ```bash
    pip install gunicorn dj-database-url psycopg2 whitenoise
    ```

3. **Project Configuration**
    - Added `ALLOWED_HOSTS` and `STATIC_ROOT` in `settings.py`
    - Added `WhitenoiseMiddleware` for static file serving
    - Created a `Procfile`:
    ```
    web: gunicorn main.wsgi
    ``` 
    
4. **Static Files Handling**
    - Configured static file paths
    - Ran 
     ```bash
     python manage.py collectstatic
     ```    

5. **Database Migration**
    - Set up Heroku Postgres add-on
    - Ran:
     ```
     python manage.py migrate
     ```

6. **Final Checks**
    - Confirmed:
        - `DEBUG=False` in production
        - Sensitive keys are secured via Heroku Config Vars
        - Stripe test payments functional and visible

## Testing the Deployment

The live deployment was tested to ensure that all core user and e-commerce functionality works as expected.

### Functional Testing Checklist

-  **User Authentication**
    - Registered a new user account
    - Logged in and out successfully
    - Verified session behavior and redirections

- **E-commerce Flow**
    - Added and removed products from the cart
    - Proceeded to checkout using Stripe test card data
    - Verified order success message and confirmation logic

- **Page and Asset Rendering**
    - Confirmed all images and static assets load correctly
    - Ensured wireframes, documentation, and visual assets are visible

- **SEO and UX Enhancements** 
    - `robots.txt` and `sitemap.xml` load at root and are valid
    - Meta tags appear in <head> section, for better search engine indexing
    - Custom `404.html` page displays correctly with theme styling and navigation links

### Additional Manual Testing

Manual walkthroughs were conducted on:

- Mobile and desktop screen sizes (responsive design)
- Broken URL testing to trigger the 404 page
- Invalid form submissions (empty or invalid email in newsletter form)
- Cart session persistence across page refreshes

![Testing](documentation/screenshots/testing)

## Final Project Feature Checklist

Below is a summary of the core requirements and features implemented in this project:

| Requirement                                                                                 | Status   |
|---------------------------------------------------------------------------------------------|----------|
| ✅ At least 3 original custom models                                                        | ✅ Done   |
| ✅ Front-end form with CRUD functionality (non-admin)                                       | ✅ Done   |
| ✅ UI element to delete records from front end                                              | ✅ Done   |
| ✅ Evidence of agile methodology (GitHub Project Board)                                     | ✅ Done   |
| ✅ `robots.txt` file included                                                               | ✅ Done   |
| ✅ `sitemap.xml` file generated                                                             | ✅ Done   |
| ✅ Descriptive `<meta>` tags used                                                           | ✅ Done   |
| ✅ At least one `<a>` link uses `rel` attribute                                             | ✅ Done   |
| ✅ Custom 404 error page implemented                                                        | ✅ Done   |
| ✅ Facebook Business Page (real or mocked with screenshots)                                | ✅ Done   |
| ✅ Newsletter signup form (real or simulated with future integration)                      | ✅ Done   |
| ✅ E-commerce business model & marketing strategy described in README                      | ✅ Done   |
| ✅ `DEBUG=False` in production                                                              | ✅ Done   |
| ✅ User registration, login, and logout functionality                                       | ✅ Done   |
| ✅ Fully functional e-commerce purchase flow using Stripe                                   | ✅ Done   |
| ✅ Detailed testing beyond validation tools                                                 | ✅ Done   |
| ✅ Public GitHub Project board linked                                                       | ✅ Done   |

> 📌 Supporting screenshots, wireframes, and design documentation are located in the `documentation/` folder.

---

[Back to Top](#top)

    


