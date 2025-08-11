<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/intro.jpg" alt="hero-image" style="width:100%;"></details><br>

# 🗺️ Project Outline

**Dileviroo** is a fully responsive, immersive, full-stack web application that creates a fictitious online ordering experience through seamless menu browsing, dynamic cart management, and comprehensive order tracking functionality. Designed to bridge the gap between traditional ordering service and modern digital convenience, Dileviroo empowers both customers and administrators with intuitive tools for managing orders, reviews, and business operations.

Built using HTML5, CSS3, JavaScript, jQuery, Bootstrap 5, and the Django Python framework, it showcases dynamic styling and interactive elements that enhance the user experience through real-time search functionality, theme toggling, persistent cart storage, and responsive design patterns. The application demonstrates modern web development principles, including a Django backend with SQLite database integration, a secure login/signup system with role-based access control, and CRUD operations for menu items and order processing.

As part of a portfolio project for the [Code Institute Full Stack Software Developer Bootcamp](https://codeinstitute.net/), the project focuses on implementing Django's Model-View-Template architecture, database relationships, user authentication, and modern frontend technologies to create a user-centric web experience that meets industry best practices in responsiveness, accessibility, and aesthetics. The project showcases practical application of full-stack development skills while solving real-world business challenges in the food service industry, demonstrating both technical proficiency and user experience design principles essential for modern web applications. 🍕✨

> [!NOTE]  
> While the name playfully echoes the popular delivery brand “Deliveroo,” Dileviroo is an acronymical tribute to my three Code Institute mentors - [Dillon](https://github.com/dillon-mccaffrey-ci), [Kevin](https://github.com/kevin-ci), and [Roo](https://github.com/roomacarthur) (Dil-evi-roo) - whose guidance inspired its creation.

🔗 Quick Links  
[Live Site](https://dileviroo-d67d65227b08.herokuapp.com/)  
[User Story Board](https://github.com/users/Ozzymara/projects/14)<br>
<!-- Table of Contents -->
## 📑 Table of Contents

- [🗺️ Project Outline](#-project-outline)
  - [🎯 Project Aims](#-project-aims)
  - [🚀 Goals](#-goals)
  - [🧐 UX Design](#-ux-design)
  - [👤 User Stories & MVP Focus](#-user-stories--mvp-focus)
  - [🎨 Colours](#-colours)
  - [📱 Wireframes](#-wireframes)
- [✨ Features](#-features)
  - [🏷️ Title and Favicon](#-title-and-favicon)
  - [🖼️ Imagery](#-imagery)
  - [🧭 Nav Bar](#-nav-bar)
  - [🔘 Button System](#-button-system)
  - [🔍 Advanced Search Functionality](#-advanced-search-functionality)
  - [🔚 Footer](#-footer)
  - [🕹️ Responsive Website Implementation](#-responsive-website-implementation)
- [🔄 CRUD Functionalities](#-crud-functionalities)
- [🗂️ Entity Relationship Diagram](#entity-relationship-diagram)
- [🔄 Agile Development Approach](#-agile-development-approach)
- [📊 Feedback & Retrospectives](#-feedback--retrospectives)
- [🧭 Five Planes of UX](#-five-planes-of-ux)
- [🔒 Security](#-security)
  - [User Authentication and Account Security](#user-authentication-and-account-security)
  - [Defensive Design](#defensive-design)
  - [CSRF Protection](#csrf-protection)
  - [Notification Messages Overview](#notification-messages-overview)
  - [Additional Security Practices](#additional-security-practices)
- [🛠️ Built With](#-built-with)
  - [🖥️ Technologies and Languages](#-technologies-and-languages)
  - [📚 Libraries and Frameworks](#-libraries-and-frameworks)
  - [🧰 Tools and Programs](#-tools-and-programs)
  - [⚙️ Related Technologies Used](#-related-technologies-used)
  - [Dependencies](#dependencies)
- [🗃️ File Structure](#-file-structure)
- [🧪 Testing and Validation](#-testing-and-validation)
  - [✅ Manual Testing](#-manual-testing)
  - [✅ HTML Validation](#-html-validation)
  - [✅ CSS Validation](#-css-validation)
  - [✅ JS Validation](#-js-validation)
  - [✅ WAVE](#-wave)
  - [✅ Chrome DevTools Lighthouse](#-chrome-devtools-lighthouse)
  - [✅ SQL Queries](#-sql-queries)
  - [✅ CI Python Linter](#-ci-python-linter)
  - [✅ Semantic HTML](#-semantic-html)
  - [✅ Controls testing](#-controls-testing)
- [🚀 Deployment](#-deployment)
- [🙌 Credits](#-credits)
  - [⌨️ Code](#%EF%B8%8F-code)
  - [📝 Content](#-content)
  - [🎥 Media](#-media)
  - [🤖 AI Implementation and Orchestration](#-ai-implementation-and-orchestration)
  - [🧡 Acknowledgements](#-acknowledgements)
  - [💡 Future Ideas](#-future-ideas)
  - [🆕 Recent Updates](#-recent-updates)<br>

## 🎯 Project Aims

*   **Demonstrate Full-Stack Proficiency**: Highlight Django-powered workflows, from models and views to templates and admin customisation.
*   **Engage a Dual Audience**: Appeal to both developers seeking inspiration and clients evaluating full-stack talent.
*   **Celebrate Mentorship**: Embed playful and meaningful gestures for the educators who shaped my journey.<br><br>

## 🚀 Goals

*   **Scalability**: Architect the project to support future features like multi-vendor support, real-time tracking, or payment integration.
*   **Accessibility**: Ensure semantic markup, ARIA best practices, and responsive design for inclusive user experiences.
*   **User Retention**: Create intuitive flows for ordering, reviewing, and interacting with the platform to encourage repeat engagement.
*   **Operational Efficiency:** Streamline admin tasks like order management, bill generation, and review moderation through a customised dashboard.<br><br>

## 🧐 UX Design
Dileviroo’s template structure isn’t just functional - it’s layered with intention. From strategic goals to visual polish, each page reflects a commitment to clarity, usability, and personality. Whether users are placing an order or admins are managing the menu, the experience is designed to feel intuitive, responsive, and enjoyable.


### 👤 User Stories & MVP Focus

Development was guided by user stories that mapped directly to real-world interactions. The MoSCoW method is a popular prioritisation technique used in project management and software development to help decide which requirements or features to focus on. The name stands for 'Must' have, 'Should' have, 'Could' have, and 'Won't' have. This framework helps teams focus on delivering the most important features first and manage stakeholder expectations effectively.

<details><summary>🔴🟠🔵 Click to view MoSCoW table</summary>

| Priority     | Site Owner Perspective                                   | External User Perspective                              |
|--------------|----------------------------------------------------------|-------------------------------------------------------|
| **🔴 MUST HAVE**| 1. Database-Backed Django Application (User Story 2)     | 1. Responsive and Accessible Front-End Design (US 1)  |
|              | 2. CRUD Functionality for Data Management (User Story 5) | 2. Role-Based Authentication and Authorisation (US 7) |
|              | 3. Cloud Deployment of the Application (User Story 10)   | 3. CRUD Functionality for Data Management (User Story 5)|
| **🟠 SHOULD HAVE**| 1. User Notifications for Data Changes (User Story 6)   | 1. User Notifications for Data Changes (User Story 6)  |
|              | 2. Version Control with Git and GitHub (User Story 9)    | 2. Responsive and Accessible Front-End Design (US 1)  |
|              | 3. High-Quality Python Code (User Story 4)                | 3. Automated Testing for Application Features (US 8)  |
| **🔵 COULD HAVE**| 1. AI-Assisted Development Process (User Story 11)       | 1. Agile Project Management (User Story 3)             |
|              | 2. Agile Project Management (User Story 3)                | 2. Version Control with Git and GitHub (User Story 9) |
|              | 3. Automated Testing for Application Features (User Story 8) | 3. AI-Assisted Development Process (User Story 11)    |
</details>
<br>
Using a Kanban board, during development, tasks were organised into three categories: To Do, In Progress, and Done. Tasks were moved across columns during sprints to reflect real-time progress and priorities.

Click here to view the project [Kanban board](https://github.com/users/Ozzymara/projects/14)<br><br>


## 🎨 Colours

The colour palette was carefully selected to enhance the user experience, ensuring both visual appeal and accessibility. Since Dileviroo is an interactive customer experience, the colours play a crucial role in setting the mood, aiding readability, and creating a harmonious yet engaging aesthetic.

To guarantee adherence to accessibility standards, WAVE’s colour contrast check feature, powered by WebAIM, was used to validate contrast levels to ensure WCAG compliance and optimal readability. Under the WCAG, AAA is the highest standard for readability. For normal text smaller than 24px, the luminance ratio between the lighter and darker colours must be at least 7:1 to ensure maximum readability for users with visual impairments.

| Section | Background Colour | Background Hex | Background RGB   | Foreground Colour | Foreground Hex | Foreground RGB  | Ratio  | AAA Result |
|---------|-----------------------|----------------|-----------------|-----------------------|----------------|-----------------|--------|------------|
| Navbar  | Dark Cerulean          | #2D5D81        | 45, 93, 129     | White                 | #FFFFFF        | (255, 255, 255)   | 7.01:1 | ✅ Pass |
| Main    | White                 | #FFFFFF        | 255, 255, 255   | Black       | #000000| (0, 0, 0) | 21:1   | ✅ Pass |

<details>
<summary>Click to view colour palette and contrast results for AAA</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/colour.jpg" alt="colour palette" style="width:100%;"></details><br>


**Navbar**: Utilises Dark Cerulean (#2D5D81) as the background paired with White (#FFFFFF) foreground text, achieving a strong contrast ratio of 7.01:1, surpassing the WCAG AAA standard for normal text. This combination ensures clear visibility and sets a calm yet professional tone for navigation.

**Main Section**: Features a White background (#FFFFFF) with black (#000000), but with an achieved maximum contrast ratio of 21:1, indicating optimal readability and accessibility compliance for all text and interface elements in this area.

By emphasising visual harmony and strict adherence to WCAG AAA contrast requirements, Dileviroo creates an interactive customer experience environment that is both engaging and accessible.<br><br>

## 📱 Wireframes

Wireframes play a crucial role in shaping a website’s architecture, ensuring a cohesive and well-optimised experience for users. The wireframes for this project have been created using [Balsamiq](https://balsamiq.com/) and Chrome extension [Wireframe-Prage](https://chromewebstore.google.com/detail/wireframe-page/bhaaofjcbafngjjneehlganleamobkke) to define the core feature layout, ensuring a user-friendly experience that prioritises clarity and ease of navigation. These mid-fidelity wireframes serve as a foundational guide for structuring the site's design and responsiveness across different screen sizes.

Each template is developed using user-centred principles: prioritising simplicity, searchability, and visually-guided interactions, ensuring an intuitive experience that fulfils business and customer needs.

| Template Name       | Description / Purpose          | Expand Feature to View Image                               |
|---------------------|-------------------------------|------------------------------------------------------------|
| menu.html           | Display categorised menu items with images and prices | <details><summary>view wireframe</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/w-menu.png" alt="wireframe" style="width:100%;"></details> |
| signup.html          | User registration page          | <details><summary>view wireframe</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/Sign up.png" alt="wireframe" style="width:100%;"></details> |
| login.html           | User authentication page        | <details><summary>view wireframe</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/w-login.png" alt="wireframe" style="width:100%;"></details> |
| profile.html         | User profile display and update | <details><summary>view wireframe</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/w-profile.png" alt="wireframe" style="width:100%;"></details> |
| cart.html            | Shopping cart with current orders | <details><summary>view wireframe</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/w-cart.png" alt="wireframe" style="width:100%;"></details> |
| my_orders.html       | User order history and details  | <details><summary>view wireframe</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/w-myorder.png" alt="wireframe" style="width:100%;"></details> |
| reviews.html         | Customer reviews and comments   | <details><summary>view wireframe</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/w-reviews.png" alt="wireframe" style="width:100%;"></details> |
<br>

<hr><p align="right" dir="auto"><a href="#-table-of-contents">Back to Table of Contents</a></p>

# ✨ Features

This website is designed for clarity and ease of use and is structured to encourage interaction.<br><br>

## 🏷️ Title and Favicon

<details>
<summary>Click to view browser title</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/tab.webp" alt="Browser title" style="width:50%;"></details><br>

• The title of the website `🍕 Dileviroo` appears at the top of the browser tab and the top of the page. This makes it easy for users to recognise and understand the site's purpose. Furthermore, the section that the user is visiting is also reflected. For instance, the menu page is shown as `Menu 🍕 Dileviroo`.

• The favicon (the small icon next to the site title in the browser tab) is the Dileviroo logo icon. The icon helps users quickly identify the site when they have multiple tabs open.<br><br>

## 🖼️ Imagery

Dileviroo utilises 42 images that were either selected from a a vast collection of royalty-free image sites or AI generated using [PicLumen](https://piclumen.com/).

<details>
<summary>Click to view collage of images</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/collage.webp" alt="collage of images" style="width:100%;"></details>
<br>

<details>
<summary>Click to view logo</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/logo.png" alt="dileviroo logo" style="width:50%;"></details>
<br>

The site logo was created using [Design.com](https://www.design.com). The logo features a stylised slice of pizza in shades of blue to reinforce the site's colours. Below the pizza, in light-blue capital letters, the slogan reads "TAKE A `<BR>`" - a valuable piece of advice that we were frequently reminded of by Dillon during the capstone project.<br><br>

## 🧭 Nav Bar
• The navigation bar is a menu at the top of the website that stays visible as users scroll. This feature makes it easy to move between sections without needing to scroll back to the top.

• The navbar displays the site's logo and a toggle feature to switch between light and dark modes.
• The navbar includes links to important sections such as the menu, cart, reviews, profile, and my orders, as well as buttons to sign up, log in, and log out.

<details>
<summary>Click to view navbar</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/navbar.webp" alt="Navbar" style="width:100%;"></details><br>
</details>

• The navbar for the admin account includes additional links to edit menu, add item, view all orders, and to generate bills.

<details><summary>Click to view admin navbar</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/admin_navbar.webp" alt="Navbar" style="width:100%;"></details><br>

• On mobile mode, the menu turns into a hamburger menu (three horizontal lines). Users can tap on it to open the menu and access different sections.
<details><summary>Click to view navbar for mobile mode</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/navbar_mobile.webp" alt="Navbar" style="width:50%;"></details><br><br>

## 🔘 Button System

Dileviroo features a comprehensive button system that enhances user experience across all pages with consistent styling and intuitive functionality.

<details><summary>Click to view details on button system</summary>
  
| Category                    | Subcategory / Feature          | Description / Key Features                                                                                         |
|-----------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------|
| **Primary Action Buttons** | **Authentication Buttons**    | Login/Signup: Bootstrap primary buttons with smooth hover transitions; Logout with confirmation modal; Submit forms with validation |
|                             | **Menu & Cart Interactions**   | Add to Cart buttons with instant feedback; Dynamic cart counter in navbar; Clear Cart button; Place Order button; Plus/Minus quantity buttons |
| **Administrative Controls** | **Menu Management**            | Add New Item button (primary style); Edit Items button (warning color); Delete Items button (danger style with confirmation); Submit/Update Dish buttons |
|                             | **Order Management**           | View Bills buttons (outline-success style); Process Orders buttons; All Orders navigation; Database management buttons |
| **Navigation Buttons**      | **Primary Navigation**         | Menu, Cart, Reviews, Profile navigation buttons; Home/Logo button; Mobile hamburger menu toggle |
|                             | **Conditional Navigation**     | Admin-only buttons (Add Item, Orders, Bills); User-specific buttons (My Orders, Profile editing) |
| **Form Control Buttons**    | **Form Actions**               | Submit buttons for all forms; Cancel buttons (secondary style); Save Changes buttons; Form validation triggers |
|                             | **Profile Management**         | Edit Profile button; Update Password button; Delete Account confirmation buttons |
| **Interactive Features**    | **Theme Toggle**               | Dark/Light mode toggle with moon/sun icons (🌙/☀️); Smooth CSS animation; User preference persistence |
|                             | **Search & Filter**            | Search input clear functionality; Real-time search filtering; Category-based filtering |
| **Review System Buttons**   | **Review Actions**             | Add Review button; Edit Review button (✅ Update review); Delete Review button with warning modal; Cancel Review editing |
|                             | **Review Navigation**          | Character counter displays; Form validation feedback; Success/error message close buttons |
| **Cart System Buttons**     | **Cart Management**            | Add to Cart (per item); Remove from Cart; Clear entire Cart; Plus/Minus quantity controls; Go to Cart button |
|                             | **Checkout Process**           | Place Order button; Payment processing; Order confirmation buttons |
| **Responsive Design**       | **Mobile Optimisation**        | Touch-friendly (44px min target); Stacked vertical layout on small screens; Navbar toggler for mobile |
|                             | **Accessibility Features**     | ARIA labels for screen readers; Full keyboard navigation; Visible focus indicators; High contrast ratios |
| **Dynamic Button States**   | **Loading & Feedback**         | Spinner icons during AJAX calls; Disabled states to prevent double submits; Success feedback with temporary states |
|                             | **Contextual Variations**      | User role-based visibility (`{% if user.is_superuser %}`); Authentication-dependent display; Cart counter updates |
| **Alert & Modal Buttons**   | **Dismissible Alerts**         | Alert close buttons (`btn-close`); Message dismissal; Form error clearing |
|                             | **Confirmation Dialogs**       | Logout confirmation; Delete confirmation; Destructive action warnings |
| **Special Integrations**    | **Bootstrap Integration**       | Consistent Bootstrap 5 styling; Colour variants (primary, secondary, success, warning, danger, outline-*) |
|                             | **Custom Enhancements**        | Brand color `#2D5D81`; Icon integration (Font Awesome); Smooth hover transitions |
|                             | **UX Enhancements**            | Toast notifications; Progress indicators; Real-time validation feedback; Character limits |
| **Performance Features**    | **Optimisation**               | Lazy loading; Minimal JavaScript handlers; Hardware-accelerated CSS animations; LocalStorage integration |
|                             | **Security Features**          | CSRF token protection; Form validation; Double-submit prevention; Session management |
</details>

### 🔍 **Advanced Search Functionality**

One of Dileviroo's standout features is its comprehensive search system that enhances user experience across multiple pages:

<details>
<summary>Click to view search feature</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/menusearch.gif" alt="Navbar" style="width:100%;">

| Feature                | Page                | Key Capabilities                                        | No-Results Message                      |
|------------------------|---------------------|---------------------------------------------------------|---------------------------------------|
| **Menu Search**         | menu.html           | Real-time filtering as you type; search by name, description, or category; dynamic category hiding/showing | "No matching menu items found 🍽️"    |
| **Order History Search**| my_orders.html      | Filter by order details, items, or dates; instant search | "No matching orders found 🧾"          |
| **Reviews Search**      | reviews.html        | Search by review content or reviewer name               | "No matching reviews found 💬"         |
| **Bills Search** (Admin)| bills.html          | Search by customer info, amount, or bill details        | "No matching bills found 🧾"         |
</details><br><br>

## 🔚 Footer

Dileviroo features a clean, uncluttered footer that maintains consistent branding and provides essential social media connectivity across all pages.

* The footer includes professionally designed social media icons * Links to the main Dileviroo GitHub repository
* Direct link to the developer's GitHub profile* 
* Consistent colour `#2D5D81` to match the navbar scheme
* All content centred for visual balance

<details>
<summary>Click to view footer</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/footer.webp" alt=" audio toggle feature" style="width:50%;"></details><br><br>

## 🕹️ Responsive Website Implementation

This website is fully responsive, meaning it automatically adjusts to different screen sizes, whether viewed on a mobile phone, tablet, or desktop.

<details>
<summary>Click to view responsiveness
</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/responsiveness.webp" alt="Responsiveness" style="width:100%;"></details>

Implementation Details

• The [Bootstrap framework](https://getbootstrap.com)  allowed for a responsive design without the need for additional CSS or media queries.  
• In some instances, responsiveness required fine-tuning and troubleshooting, particularly with the assistance of GitHub Copilot, an AI-powered coding assistant designed to help developers write code more efficiently. It provides real-time code suggestions, automates repetitive tasks, and helps debug and refactor code.  
• While some awkward elements still exist, the site successfully adapts to various screen sizes.
<br>

<hr><p align="right" dir="auto"><a href="#-table-of-contents">Back to Table of Contents</a></p>
