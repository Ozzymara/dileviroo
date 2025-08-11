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
Dileviroo’s template structure isn’t just functional - it’s layered with intention. From strategic goals to visual polish, each page reflects a commitment to clarity, usability, and personality. Whether users are placing an order or admins are managing the menu, the experience is designed to feel intuitive, responsive, and enjoyable.<br><br>


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
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/navbar_mobile.webp" alt="Navbar" style="width:50%;"></details>
<br>

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

# 🔄 CRUD Functionalities

### 🎯 Key CRUD Features

- **Phone-based Authentication**: Users log in with phone numbers instead of usernames
- **Real-time Cart Updates**: JavaScript handles cart operations with localStorage
- **Admin Controls**: Superusers can manage menu items and view all orders
- **User Ownership**: Users can only edit/delete their reviews
- **Search Functionality**: Real-time search across menu items, reviews, and orders
- **Responsive Design**: All CRUD operations work on mobile and desktop
- **Validation**: Client-side and server-side validation for all forms
- **Confirmation Dialogues**: Critical actions (delete, logout) require confirmation

Below is a comprehensive documentation for various CRUD functionalities.

<details><summary>CRUD for 🛒 Shopping Cart Operations</summary>

| Action | User Interaction | Model | Description |
|--------|------------------|-------|-------------|
| **Create** | Click "Add to cart" button on menu items | `localStorage` | Add items to cart with quantity and price |
| **Read** | Click "Go To Cart" button | `localStorage` | Display all cart items with quantities and total price |
| **Update** | Use "-" or "+" buttons to adjust quantities | `localStorage` | Modify item quantities in cart |
| **Delete** | Click "Clear cart" button | `localStorage` | Remove all items from cart |

</details><br>

<details><summary>CRUD for ⭐ Customer Reviews</summary>

| Action | User Interaction | Model | Description |
|--------|------------------|-------|-------------|
| **Create** | Reviews page → Write comment → Click "Publish" | `Rating` | Authenticated users create reviews |
| **Read** | Visit "Reviews" page | `Rating` | Display all customer reviews with search functionality |
| **Update** | Click "Edit" button on own review → Modify → Save | `Rating` | Users can edit their own reviews only |
| **Delete** | Click "Delete" button on own review → Confirm | `Rating` | Users can delete their own reviews only |

</details><br>

<details><summary>CRUD for 🔍 Search & Filter Operations</summary>

| Feature | User Interaction | Target | Description |
|---------|------------------|--------|-------------|
| **Menu Search** | Type in menu search bar | Menu items | Real-time filtering by item name, description, or category |
| **Review Search** | Type in review search bar | Customer reviews | Filter reviews by content or reviewer name |
| **Order Search** | Type in order search bars | Orders | Filter orders by items, customer, or details |

</details><br>

<details><summary>CRUD for 🔐 Authentication & Authorisation</summary>

| Action | User Interaction | Model | Description |
|--------|------------------|-------|-------------|
| **Login** | Enter phone & password → Click "Log In" | `User` | Phone-based authentication system |
| **Logout** | Click "Logout" → Confirm | Session | Secure logout with confirmation |
| **Access Control** | Various admin functions | Permissions | Role-based access (superuser, authenticated, anonymous) |

</details><br>

<details><summary>CRUD for 📝 Reviews (Rating Model)</summary>

| Action | User Interaction | Description |
|--------|------------------|-------------|
| **Create** | Click "Publish" button after writing a review | Creates a new customer review in the database |
| **Read** | Navigate to Reviews page | Displays all customer reviews with search functionality |
| **Update** | Click "Edit" button on your own review | Allows authenticated users to modify their existing reviews |
| **Delete** | Click "Delete" button on your own review | Removes your review after confirmation dialog |

</details><br>

<details><summary>CRUD for 🛒 Cart Operations (LocalStorage)</summary>

| Action | User Interaction | Description |
|--------|------------------|-------------|
| **Create** | Click "Add to cart" button on menu items | Adds new items to shopping cart |
| **Read** | Navigate to Cart page | Displays all cart items with quantities and total |
| **Update** | Click "-" or "+" buttons in cart | Updates quantity of existing cart items |
| **Delete** | Click "Clear cart" button | Removes all items from cart after confirmation |

</details><br>

<details><summary>CRUD for 📋 Orders (Order Model)</summary>

| Action | User Interaction | Description |
|--------|------------------|-------------|
| **Create** | Click "Place order" button in cart | Creates new order record in database |
| **Read** | Navigate to "My Orders" (users) or "All Orders" (admin) | Displays order history with search functionality |
| **Update** | Admin marks orders as billed | Updates `bill_clear` status when generating bills |
| **Delete** | No direct delete (data integrity) | Orders are preserved for record keeping |

</details><br>

<details><summary>CRUD for 🍽️ Menu Items (MenuItem Model) - Admin Only</summary>

| Action | User Interaction | Description |
|--------|------------------|-------------|
| **Create** | Fill form in "Add Item" page and submit | Creates new menu items with images |
| **Read** | Navigate to Menu page | Displays categorised menu items with search |
| **Update** | Edit through Django Admin panel | Modifies existing menu items |
| **Delete** | Click "Delete" button on menu items (superuser) | Removes menu items from database |

</details><br>

<details><summary>CRUD for 👤 User Profile (User Model)</summary>

| Action | User Interaction | Description |
|--------|------------------|-------------|
| **Create** | Complete signup form | Creates new user account with phone authentication |
| **Read** | Navigate to Profile page | Displays user information and order count |
| **Update** | Click "Edit Profile" and modify details | Updates name, phone, and password |
| **Delete** | No direct delete (account management) | Handled through admin interface |

</details><br>

<details><summary>CRUD for 🧾 Bills (Bill Model) - Admin Only</summary>

| Action | User Interaction | Description |
|--------|------------------|-------------|
| **Create** | Click "Generate Bill" for a table | Consolidates orders into single bill |
| **Read** | Navigate to "View Bills" page | Displays all generated bills with totals |
| **Update** | No direct update (financial integrity) | Bills are immutable once created |
| **Delete** | No direct delete (audit trail) | Bills preserved for accounting records |

</details><br>

<hr><p align="right" dir="auto"><a href="#-table-of-contents">Back to Table of Contents</a></p>

# Entity Relationship Diagram
This section presents a concise overview of the core entities, their purposes, key attributes, relationships, and business logic that form the foundation of the Dileviroo management system's database architecture. It highlights how different components interact to support user management, menu operations, ordering, billing, and customer feedback processes, while addressing data integrity and scalability considerations essential for robust system performance.

<details>
<summary>Click to view EDR diagram</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/ERD.webp" alt=" audio toggle feature" style="width:100%;"></details><br>


**`MenuItem`**
This database schema outlines the core components of the Dileviroo management system, starting with the `MenuItem` table, which serves as the `cafe`'s digital menu, detailing each product's `name`, `category`, `desc`, `price`, and `pic`, with a `list_order` to dictate its display sequence.

**`Order`**
Central to operations is the `Order` table, recording every customer order. Each order has a unique identifier, an `order_id` for potential grouping, and stores the ordered `items_json` which references the `MenuItem` entries. Crucially, it captures customer details like `name` and `phone`, the `table number`, the total `price`, the `order_time`, and a `bill_clear` flag to indicate payment status.

**`Bill`**
The system then moves to financial tracking with the `Bill` table. This table summarises payments, containing the customer's `phone` and `name`, the `order_items`, the `bill_total`, and the `bill_time` when the transaction occurred. The relationships here are implicit through shared `phone` and `name` fields, where a `bill` is effectively generated for the items in an order, for a specific customer.

**`User`**
Managing access and tracking customer activity is the `User`table. This comprehensive table stores each user's unique `id`, a unique `phone` number which is `phone_verified`, and whether they possess specific roles like `cafe_manager`, `is_staff`, or `is_superuser`, which dictate their permissions. It also logs their `order_count`, a `password` (hashed for security), and timestamps like `last_login` and `date_joined`. Users are linked to both `Order` and `Bill` records by their `phone` and `name`, forming the backbone of customer and staff interactions within the system.

**`Rating`**
Finally, the `Rating` table allows for valuable customer feedback. It captures a `comment` left by a customer, the date of the review (`r_date`), and the `name` of the person who provided it. This table implicitly links back to the `users` and their experiences within the cafe, providing insights for service improvement. Together, these tables form an interconnected system, allowing the cafe to manage its menu, process orders, handle billing, keep track of users, and gather feedback, creating a comprehensive digital environment for cafe operations.

<details>
<summary>Click to read more on logic for entities</summary>

| **Entity**        | **Purpose**                                         | **Key Fields**                                                             | **Relationships**                                                                                   | **Business Logic**                                                   |
|-------------------|----------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| **User**          | Manages customer authentication and profiles       | username, email, password, first_name, last_name, date_joined             | One-to-Many with Orders, Reviews, and Bills                                                     | Central identity hub connecting all user activities                |
| **Menu Item**     | Represents food/beverage products available for purchase | name, description, price, category, image, availability_status, created_date | Many-to-Many with Orders (via OrderItem junction table)                                        | Enables dynamic menu management with categorisation and pricing   |
| **Order**         | Captures customer purchase transactions             | order_id, user_id (FK), order_date, status, total_amount, delivery_address | Many-to-One with User; One-to-Many with OrderItem; One-to-One with Bill                         | Central transaction record linking customers to purchases         |
| **OrderItem**     | Junction table resolving Many-to-Many Orders↔Menu Items | order_id (FK), menu_item_id (FK), quantity, unit_price, subtotal          | Many-to-One with Order; Many-to-One with MenuItem                                              | Captures specific item quantities and pricing at purchase time    |
| **Bill**          | Generates invoices for completed orders             | bill_id, order_id (FK), bill_time, customer_name, phone, bill_total, order_items (JSON) | One-to-One with Order                                                                        | Creates permanent financial records with customer and itemised charges |
| **Review**        | Stores customer feedback and ratings                 | review_id, user_id (FK), menu_item_id (FK, optional), rating, comment, review_date, is_anonymous | Many-to-One with User; Many-to-One with MenuItem (optional)                                  | Enables customer engagement and business insights                  |

</details><br>

<details>
<summary>Click to read description of relationship types</summary>

| **Relationship Type** | **Description**                                                                                   |
|-----------------------|-------------------------------------------------------------------------------------------------|
| One-to-Many           | User → Orders: a single user can place multiple orders                                            |
|                       | User → Reviews: user can submit multiple feedback entries                                        |
|                       | Order → OrderItems: each order has multiple line items                                           |
|                       | User → Bills: user can have multiple billing records                                             |
| Many-to-Many          | Orders ↔ MenuItems: orders contain multiple items; items appear in many orders                  |
|                       | Resolved through OrderItem junction table with additional quantity and pricing data             |
| One-to-One            | Order → Bill: each order has exactly one corresponding invoice                                  |
</details><br>

<details>
<summary>Click to read more on data integrity and constraints</summary>

| **Data Integrity and Constraints**                                |
|-----------------------------------------------------------------|
| Foreign Key constraints ensure referential integrity and prevent orphaned records |
| Automatic order total calculation from OrderItem subtotals        |
| Bill generation triggered upon order completion                   |
| User authentication required for order placement and reviews      |
| Menu item availability checked before processing orders           |

</details><br>

<details>
<summary>Click to read more on scalability considerations</summary>

| **Scalability Considerations**                                   |
|-----------------------------------------------------------------|
| Indexing on primary keys, foreign keys, dates, and user fields for efficient queries |
| Historical order preservation for customer service                |
| Review aggregation for menu item popularity                       |
| Bill retention for financial reporting and tax compliance        |
| Menu item version control to track pricing history                |

</details><br><br>

## 🔄 Agile Development Approach

Dileviroo was developed using an Agile methodology to ensure iterative progress, continuous feedback, and adaptive planning. This approach allowed the project to evolve organically while maintaining a clear focus on user needs, technical robustness, and design integrity.

### 🧩 Sprint Planning & Structure

The project was broken down into manageable sprints, each focused on delivering specific features or improvements. Each sprint began with a planning session to define goals and ended with a review to assess outcomes and gather insights for the next iteration.

| Sprint | Focus Area                  | Key Deliverables                                              |
|--------|-----------------------------|---------------------------------------------------------------|
| 1️⃣     | Project setup, database modeling, menu & order flows      | Django setup, menu & order models              |
| 2️⃣     | Admin dashboard, CRUD operations                        | Admin customisation, order/bill workflows      |
| 3️⃣     | Reviews, billing logic, accessibility                   | Review system, semantic markup, ARIA fixes     |
| 4️⃣     | UI polish, messaging, responsive design                 | Responsive design, fallback messaging          |

### 🔁 Iterative Development

Features were built incrementally, allowing for:

*   Early testing and validation of core functionality
*   Rapid identification and resolution of bugs or UX issues
*   Continuous integration of feedback from mentors and peers

This iterative cycle ensured that each component, from order placement to administrative workflows, was refined for clarity, performance, and usability.

## 📊 Feedback & Retrospectives

Regular retrospectives were held to reflect on:

*   What went well (e.g. clean admin workflows, intuitive UI)
*   What could be improved (e.g. accessibility warnings, edge-case handling)
*   What to try next (e.g. Stripe integration, multi-vendor support)

This feedback loop fostered continuous learning and kept the project aligned with both technical goals and user expectations.

## 🧭 Five Planes of UX

The Five Planes of UX - **Strategy**, **Scope**, **Structure**, **Skeleton**, and **Surface** - guide the development of Dileviroo from abstract goals to tangible interfaces. Each layer builds upon the previous, ensuring a cohesive and user-centred product.

| Plane      | Focus                    | Dileviroo Implementation                                                                                       |
|------------|--------------------------|----------------------------------------------------------------------------------------------------------------|
| 1. Strategy | Why are we building this? | - Seamless takeaway ordering experience   - Showcase full-stack skills   - Tribute to mentors          |
| 2. Scope    | What are we building?     | - Menu, cart, billing, reviews, admin tools   - Content: items, order preview and history, and reviews               |
| 3. Structure| How is it organised?      | - Clear user/admin template separation   - Logical navigation and page grouping                            |
| 4. Skeleton | How does it behave?       | - Accessible forms, buttons, and feedback   - Role-based navigation and fallback messaging                 |
| 5. Surface  | What does it look like?   | - Playful branding, responsive layout   - Semantic HTML and accessible colour contrast              |

<details><summary>1️⃣ Strategy Plane - Why are we building this?</summary>

- **User Needs**
    - Provide a seamless takeaway ordering experience with intuitive flows and clear feedback.
- **Business Goals**
    - Showcase full-stack development skills to potential clients and recruiters.
- **Tribute Element**
    - Honour mentors through a playful, meaningful brand identity (“Dileviroo”).</details><br>

<details><summary>2️⃣ Scope Plane - What are we building?</summary>

- **Functional Requirements**
    - Menu browsing and order placement
    - Cart management and bill generation
    - Review the system and user authentication
    - Admin tools for order and menu management

- **Content Requirements**
    - Menu items, order preview and history, and user reviews
    - Messaging for empty states, confirmations, and errors</details><br>

<details><summary>3️⃣ Structure Plane - How is it organised?</summary>

- **Interaction Design**
    - Clear navigation between `home`, `menu`, `cart`, and `my_orders`
    - Admin workflows separated via `manage_menu`, `generate_bill`, and `all_orders`

- **Information Architecture**
    - Logical grouping of templates by user role
    - Consistent layout via `base.html` for shared UI elements</details><br>

<details><summary>4️⃣ Skeleton Plane - How does it behave?</summary>

- **Interface Design**
    - Buttons, forms, and links are styled for clarity and accessibility
    - Fallback messaging for empty carts, no reviews, or missing orders

- **Navigation Design**
    - Persistent navbar with role-based links
    - Breadcrumbs or contextual cues for admin pages

- **Information Design**
    - Bills and orders presented in digestible, structured formats
    - Reviews to encourage engagement</details><br>

<details><summary>5️⃣ Surface Plane - What does it look like?</summary>

- **Visual Design**
    - Playful branding with clean typography and intuitive icons
    - Responsive layout for mobile and desktop users

- **Sensory Design**
    - Use of emojis, hover effects, and feedback messages to enhance delight
    - Accessible colour contrasts and semantic HTML for inclusive design</details><br>
<br>
<hr><p align="right" dir="auto"><a href="#-table-of-contents">Back to Table of Contents</a></p>

# 🔒 Security

This project implements robust security measures to protect user data and provide a safe, reliable experience. Because users can register, log in, and interact with the site, it is essential to meet strict security standards as outlined below.

<details><summary>User Authentication and Account Security</summary>

**Django AllAuth**  
[Django AllAuth](https://django-allauth.readthedocs.io/) is integrated for secure user registration, authentication, and permission management. Key steps include:
- Adding AllAuth to workspace dependencies and `INSTALLED_APPS`
- Properly configuring authentication backends in `settings.py`
- Including AllAuth URLs in `urls.py`
- Performing database migrations to support AllAuth features

**Key AllAuth Security Features:**
- Secure user registration and login process
- Password hashing and secure storage
- Flexible backend and URL routing for authentication
- Access control for logged-in users (edit/delete icons, restricted content, etc.)</details><br>

<details><summary>Defensive Design</summary>

Defensive design principles help prevent both user error and malicious actions:
- Input validation is performed on all forms; users receive clear error and feedback messages to guide them
- Unauthenticated users are redirected to the sign-up or login page when trying to access restricted functions
- Only content authors can access the edit and delete functionalities for their account
- Custom error pages guide users out of error states
- Automated and manual testing/validation ensure security-critical features work as intended</details><br>

<details><summary>CSRF Protection</summary>
**Cross-Site Request Forgery (CSRF) Tokens**  
All forms include Django’s built-in CSRF tokens. These tokens are required for every POST request, ensuring that only valid, intentional submissions are processed.  
This protects users from CSRF attacks that could otherwise allow unauthorised commands to run in their session.</details><br>

<details><summary>Notification Messages Overview</summary>

This section outlines key client-side JavaScript and Django framework notifications, detailing their triggers and purposes.

### Client-Side JavaScript Notifications

| **Notification Message**                                               | **When It Appears**                                     | **Purpose**                                | **Preview** |
|-----------------------------------------------------------------------|--------------------------------------------------------|--------------------------------------------|-------------|
| "Password cannot exceed 8 characters!"                               | User types more than 8 characters in password field     | Enforce password length limit               | <details><summary>view notification</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/notifications/Sign up.png" alt="notification" style="width:100%;"></details> |
| "Item added to cart!"                                                 | User clicks "Add to Cart" button                         | Confirm successful cart addition            | <details><summary>view notification</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/notifications/Sign up.png" alt="notification" style="width:100%;"></details> |
| "Please select a table before placing your order!"                   | User tries to place order without selecting table        | Prevent incomplete orders                    | <details><summary>view notification</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/notifications/Sign up.png" alt="notification" style="width:100%;"></details> |
| "Your order has been placed successfully!"                           | Order is successfully submitted                          | Confirm order placement                      | <details><summary>view notification</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/notifications/Sign up.png" alt="notification" style="width:100%;"></details> |
| "Please fill in all required fields!"                                | User submits form with missing data                      | Form validation reminder                     | <details><summary>view notification</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/notifications/Sign up.png" alt="notification" style="width:100%;"></details> |
| "Are you absolutely sure you want to delete this review? This action cannot be undone." | User clicks the delete (submit) button on a review form | Prevent accidental review deletions          | <details><summary>view notification</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/notifications/delete-confirmation.png" alt="Delete Confirmation" style="width:100%;"></details> |
| "Are you sure you want to log out?"                                  | User clicks a logout link                                | Confirm user intent to log out               | <details><summary>view notification</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/notifications/logout-confirmation.png" alt="Logout Confirmation" style="width:100%;"></details> |

### Django Messages Framework

| **Message Context**     | **When It Appears**               | **Purpose**                | **Preview** |
|-------------------------|---------------------------------|----------------------------|-------------|
| Login Success           | Successful user authentication   | Welcome user after login    | <details><summary>view notification</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/notifications/Sign up.png" alt="notification" style="width:100%;"></details> |
| Login Error             | Failed authentication attempt    | Inform user of login failure| <details><summary>view notification</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/notifications/Sign up.png" alt="notification" style="width:100%;"></details> |
| Order Confirmation      | Order successfully placed        | Confirm order submission    | <details><summary>view notification</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/notifications/Sign up.png" alt="notification" style="width:100%;"></details> |
| Form Validation Errors  | Invalid form submission          | Display validation errors   | <details><summary>view notification</summary><img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/notifications/Sign up.png" alt="notification" style="width:100%;"></details> |
</details><br>

<details><summary>Additional Security Practices</summary>

- Passwords are never stored in plain text–Django’s built-in password hashing and salting is enforced by AllAuth.
- Sensitive authentication-related views and resources are restricted to the appropriate user roles.
- Static and media files are served securely (using tools such as WhiteNoise).</details><br>

These combined measures help ensure user data is handled with care and protected from common threats, meeting the requirements for a modern, interactive Django web application.<br>

<hr><p align="right" dir="auto"><a href="#-table-of-contents">Back to Table of Contents</a></p>

# 🛠️ Built With

## 🖥️ Technologies and Languages
<a href="https://www.w3schools.com/css/"><img src="https://img.shields.io/badge/CSS3-Styling-blue?logo=CSS3" alt="CSS3 Styling"></a> Language used for styling and layout of web content.  
<a href="https://www.w3schools.com/html/"><img src="https://img.shields.io/badge/HTML5-Language-orange?logo=HTML5" alt="HTML5 Core"></a> The core language for structuring web content.  
<a href="https://www.w3schools.com/js/default.asp"><img src="https://img.shields.io/badge/JavaScript-Dynamic Language-yellow?logo=javascript" alt="JavaScript"></a> A versatile scripting language used to enable interactivity and dynamic features in browsers  
<a href="https://www.python.org" rel="nofollow"><img src="https://camo.githubusercontent.com/5c168a73382c1e5f4ad3f0a344b5003ebdb56d2efe0e4d47e6dea1c2197f9259/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d677265793f6c6f676f3d707974686f6e266c6f676f436f6c6f723d333737364142" alt="Python" style="max-width: 100%;"></a> Used as the back-end programming language  

## 📚 Libraries and Frameworks
<a href="https://getbootstrap.com/"><img src="https://img.shields.io/badge/Bootstrap-5.3.3-purple?logo=Bootstrap" alt="Bootstrap 5.3.3"></a> A front-end framework for responsive and mobile-friendly design  
<a href="https://www.djangoproject.com/">
  <img src="https://img.shields.io/badge/Django-Web%20Framework-green?logo=django" alt="Django">
</a> A high-level Python web framework for rapid backend web app development, focused on security and clean, pragmatic design.  
<a href="https://fontawesome.com/"><img src="https://img.shields.io/badge/Font%20Awesome-Icons-yellow?logo=FontAwesome" alt="Font Awesome Icons"></a> Provides scalable vector icons for UI design  

## 🧰 Tools and Programs
<a href="https://balsamiq.com/"><img src="https://img.shields.io/badge/Balsamiq-Wireframes-purple?logo=Balsamiq" alt="Balsamiq Wireframes"></a> Used for creating wireframes and planning UI layouts  
<a href="https://code.visualstudio.com/"><img src="https://img.shields.io/badge/VS%20Code-Editor-blue?logo=VisualStudioCode" alt="VS Code Editor"></a> A code editor used for writing, debugging, and version control. Integrates with GitHub to track changes and manage projects efficiently  
<a href="https://github.com/marketplace/actions/flake8-lint"><img src="https://img.shields.io/badge/CI%20Python%20Linter-PEP8CI-green?" alt="CI Python Linter"></a> Used for automated style and error checking of Python code during continuous integration (CI) workflows  
<a href="https://copilot.microsoft.com/"><img src="https://img.shields.io/badge/Microsoft%20Copilot-AI-pink?logo=Microsoft" alt="Microsoft Copilot AI"></a> An AI assistant that enhances productivity and creative workflows  
<a href="https://developer.chrome.com/docs/devtools"><img src="https://img.shields.io/badge/Chrome%20DevTools-Debugging-yellow?logo=GoogleChrome" alt="Chrome DevTools Debugging"></a> A set of web development tools built directly into Google Chrome for debugging and optimising websites   
<a href="https://github.com/"><img src="https://img.shields.io/badge/GitHub-Version%20Control-black?logo=GitHub" alt="GitHub Version Control"></a> A platform for version control and collaborative development  
<a href="https://github.com/features/copilot"><img src="https://img.shields.io/badge/GitHub%20Copilot-AI-black?logo=GitHubCopilot" alt="GitHub Copilot Code Completion"></a> AI-powered code completion to assist with coding tasks  
<a href="https://git-scm.com" rel="nofollow"><img src="https://camo.githubusercontent.com/7ce2dcf67494fc5a19fe2f395392cac6eec7aaa423aea2bd90fe39a861c3b17f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769742d677265793f6c6f676f3d676974266c6f676f436f6c6f723d463035303332" alt="Git" style="max-width: 100%;"></a> Used for version control. (<code>git add</code>, <code>git commit</code>, <code>git push</code>)  
<a href="https://www.heroku.com" rel="nofollow"><img src="https://camo.githubusercontent.com/cb7581eda2a249704e391af31a1c27befeca8b42e5718e5957ce2422e3b0ba5f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4865726f6b752d677265793f6c6f676f3d6865726f6b75266c6f676f436f6c6f723d343330303938" alt="Heroku" style="max-width: 100%;"></a> Used for hosting the deployed back-end site  
<a href="https://www.piclumen.com/"><img src="https://img.shields.io/badge/PicLumen-AI image creator-purple?logo=PicLumen" alt="PicLumen AI image creator"></a> AI text to image creator   

## ⚙️ Related Technologies Used
<a href="https://ui.dev/amiresponsive?url=https://ozzymara.github.io/pyramidescape/index.html"><img src="https://img.shields.io/badge/Am%20I%20Responsive-Responsivenesss-black?logo=ResponsiveDesign" alt="Am I Responsive Preview"></a> A tool for previewing how websites appear on different screen sizes and devices   
<a href="https://fontawesome.com" rel="nofollow"><img src="https://camo.githubusercontent.com/833a4acbee994fa7412559ade09e4955a98abab4521b3c2795b6e9ea501d80a8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f466f6e745f417765736f6d652d677265793f6c6f676f3d666f6e74617765736f6d65266c6f676f436f6c6f723d353238444437" alt="Font Awesome" style="max-width: 100%;"></a> Used for the icons.  
<a href="https://jigsaw.w3.org/css-validator/"><img src="https://img.shields.io/badge/W3C-CSS%20Validator-blue?logo=W3C" alt="W3C CSS Validator"></a> Ensures the code follows web standards for accessibility and correctness  
<a href="https://jshint.com/"><img src="https://img.shields.io/badge/JS Hint-Linter-black?logo=JSHint" alt="JS Hint"></a> JavaScript code quality control  
<a href="https://www.lighthousecharity.org/homepage/"><img src="https://img.shields.io/badge/Lighthouse-Performance%20Testing-orange?logo=Lighthouse" alt="Lighthouse Performance Testing"></a> Used to audit and optimise web applications for speed and accessibility  
<a href="https://www.piliapp.com/syntax-check/es6/"><img src="https://img.shields.io/badge/PiliApp-ES6 Syntax Check-skyblue?logo=Microsoft" alt="PiliApp"></a> ECMAScript 6 Checker  
<a href=""><img src="https://img.shields.io/badge/WAVE-Web Accessibility Evaluation Tools-blue?logo=WAVE" alt="WAVE evaluation result"></a> Evaluation tool that helps authors make their web content more accessible to individuals with disabilities  
<a href="https://validator.w3.org/"><img src="https://img.shields.io/badge/W3C-HTML%20Validator-blue?logo=W3C" alt="W3C HTML Validator"></a> Helps visualise and plan web designs before development  

## Dependencies
External libraries and packages that must be installed or managed to run the project include:

| Package                                                                                     | Purpose                                                                                                     |
|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| <a href="https://pypi.org/project/asgiref/3.9.0/"><img src="https://img.shields.io/badge/asgiref-3.9.0-blue?logo=python" alt="asgiref 3.9.0"></a>             | ASGI (Asynchronous Server Gateway Interface) reference implementation, for async Django.                    |
| <a href="https://pypi.org/project/crispy-bootstrap5/2025.6/"><img src="https://img.shields.io/badge/crispy--bootstrap5-2025.6-blue?logo=bootstrap" alt="crispy-bootstrap5 2025.6"></a> | Django Crispy Forms template pack for Bootstrap 5, improves form rendering.                               |
| <a href="https://pypi.org/project/diff-match-patch/20241021/"><img src="https://img.shields.io/badge/diff--match--patch-20241021-blue?logo=python" alt="diff-match-patch 20241021"></a> | Library to compute the differences and patches between texts.                                               |
| <a href="https://pypi.org/project/dj-database-url/3.0.1/"><img src="https://img.shields.io/badge/dj--database--url-3.0.1-blue?logo=django" alt="dj-database-url 3.0.1"></a>           | Utility to use database URLs in Django settings, simplifies DB config (e.g. for Heroku).                    |
| <a href="https://www.djangoproject.com/download/4.2.23/"><img src="https://img.shields.io/badge/Django-4.2.23-green?logo=django" alt="Django 4.2.23"></a>             | The main Django web framework (long-term support version in 4.2 branch).                                    |
| <a href="https://pypi.org/project/django-allauth/65.10.0/"><img src="https://img.shields.io/badge/django--allauth-65.10.0-blue?logo=django" alt="django-allauth 65.10.0"></a>         | Integrated Django authentication app for registration, login, social auth, etc.                             |
| <a href="https://pypi.org/project/django-crispy-forms/2.4/"><img src="https://img.shields.io/badge/django--crispy--forms-2.4-blue?logo=django" alt="django-crispy-forms 2.4"></a>     | Enhanced Django form rendering with customisable layout support.                                            |
| <a href="https://pypi.org/project/django-debug-toolbar/5.2.0/"><img src="https://img.shields.io/badge/django--debug--toolbar-5.2.0-blue?logo=django" alt="django-debug-toolbar 5.2.0"></a> | Tool to display debug information about the Django app in the browser (dev only).                           |
| <a href="https://pypi.org/project/gunicorn/20.1.0/"><img src="https://img.shields.io/badge/gunicorn-20.1.0-orange?logo=python" alt="gunicorn 20.1.0"></a>           | Production WSGI HTTP server for Python web applications, often used with Django.                            |
| <a href="https://pypi.org/project/Pillow/11.3.0/"><img src="https://img.shields.io/badge/Pillow-11.3.0-red?logo=python" alt="Pillow 11.3.0"></a>                 | Powerful fork of PIL for image processing in Python.                                                        |
| <a href="https://pypi.org/project/psycopg/3.2.9/"><img src="https://img.shields.io/badge/psycopg-3.2.9-blue?logo=postgresql" alt="psycopg 3.2.9"></a>             | Modern PostgreSQL client library for Python, new async support (psycopg3).                                  |
| <a href="https://pypi.org/project/psycopg-binary/3.2.9/"><img src="https://img.shields.io/badge/psycopg--binary-3.2.9-blue?logo=postgresql" alt="psycopg-binary 3.2.9"></a>         | Pre-built binary package version of psycopg3 for easy install.                                              |
| <a href="https://pypi.org/project/psycopg2-binary/2.9.10/"><img src="https://img.shields.io/badge/psycopg2--binary-2.9.10-blue?logo=postgresql" alt="psycopg2-binary 2.9.10"></a>   | Pre-compiled binary version of psycopg2, common PostgreSQL adapter for Python.                              |
| <a href="https://pypi.org/project/setuptools/80.9.0/"><img src="https://img.shields.io/badge/setuptools-80.9.0-blue?logo=python" alt="setuptools 80.9.0"></a>         | Essential utility for packaging and distributing Python packages.                                          |
| <a href="https://pypi.org/project/sqlparse/0.5.3/"><img src="https://img.shields.io/badge/sqlparse-0.5.3-blue?logo=postgresql" alt="sqlparse 0.5.3"></a>           | Non-validating SQL parser for formatting and splitting SQL statements (used by Django).                     |
| <a href="https://pypi.org/project/tablib/3.8.0/"><img src="https://img.shields.io/badge/tablib-3.8.0-blue?logo=python" alt="tablib 3.8.0"></a>                 | Format-agnostic tabular dataset library, used for import/export (e.g., Excel, CSV, JSON).                 |
| <a href="https://pypi.org/project/tzdata/2025.2/"><img src="https://img.shields.io/badge/tzdata-2025.2-blue?logo=python" alt="tzdata 2025.2"></a>               | Up-to-date IANA timezone database for Python.                                                               |
| <a href="https://pypi.org/project/whitenoise/6.9.0/"><img src="https://img.shields.io/badge/whitenoise-6.9.0-blue?logo=python" alt="whitenoise 6.9.0"></a>         | Serves static files directly from WSGI apps, useful for deploying Django on Heroku, etc.                    |

> [!TIP]
> Run `pip3 install -r requirements.txt` to quickly install all project dependencies.

<hr><p align="right" dir="auto"><a href="#-table-of-contents">Back to Table of Contents</a></p>

# 🗃️ File Structure

The project is organised into several key directories and files:

| Path                                      | Description                                    |
|--------------------------------------------|------------------------------------------------|
| `Dileviroo/`                              | Project root folder                            |
| ├─ `cafe/`                                | Django app for cafe features (menus, orders)   |
| │   ├─ `__pycache__/`                      | Compiled Python files                          |
| │   ├─ `migrations/`                       | Database migration files                       |
| │   ├─ `templates/`                        | HTML templates for this app                    |
| │   │   ├─ `all_orders.html`               | Page with all orders                           |
| │   │   ├─ `base.html`                     | Base layout template                           |
| │   │   ├─ `bills.html`                    | Bills display template                         |
| │   │   ├─ `cart.html`                     | Shopping cart page                             |
| │   │   ├─ `delete_rewiews.html`           | Confirmation page to delete a review           |
| │   │   ├─ `edit_profile.html`             | Edit profile page                              |
| │   │   ├─ `edit_review.html`              | Edit review page                               |
| │   │   ├─ `generate_bill.html`            | Bill generation template                       |
| │   │   ├─ `login.html`                    | Login page                                     |
| │   │   ├─ `manage_menu.html`              | Menu management page                           |
| │   │   ├─ `menu.html`                     | Menu display for users                         |
| │   │   ├─ `my_orders.html`                | User's orders page                             |
| │   │   ├─ `profile.html`                  | User profile page                              |
| │   │   ├─ `reviews.html`                  | Reviews page                                   |
| │   │   ├─ `signup.html`                   | Registration page                              |
| │   ├─ `__init__.py`                       | Package initialiser                            |
| │   ├─ `admin.py`                          | Admin configuration                            |
| │   ├─ `apps.py`                           | App-specific config                            |
| │   ├─ `decorators.py`                     | Restricts unauthorised users                   |
| │   ├─ `forms.py`                          | Defines Django form classes                    |
| │   ├─ `manager.py`                        | Custom managers/utilities                      |
| │   ├─ `models.py`                         | Data models (database tables)                  |
| │   ├─ `tests.py`                          | Unit tests                                     |
| │   ├─ `urls.py`                           | URL routing for cafe app                       |
| │   ├─ `views.py`                          | Request handlers                               |
| ├─ `dileviroo/`                            | Project-level settings and code                |
| │   ├─ `__pycache__/`                      | Compiled Python files                          |
| │   ├─ `static/`                           | Static files (CSS/JS/images)                   |
| │   ├─ `__init__.py`                       | Package initialiser                            |
| │   ├─ `asgi.py`                           | ASGI server entry point                        |
| │   ├─ `settings.py`                       | Main settings (db, apps, etc.)                 |
| │   ├─ `urls.py`                           | Project root URL routing                       |
| │   ├─ `wsgi.py`                           | WSGI server entry point                        |
| ├─ `staticfiles/`                          | Collected static files for deployment          |
| ├─ `fimage/`                               | Image uploads/processing                       |
| ├─ `db.sqlite3`                            | SQLite database (dev)                          |
| ├─ `manage.py`                             | Django command-line utility                    |
| ├─ `Procfile`                              | Heroku run instructions                        |
| ├─ `README.md`                             | Project documentation                          |
| ├─ `requirements.txt`                      | Python dependencies                            |
| ├─ `.gitignore`                            | Git ignore rules                               |
| ├─ `.python-version`                       | Python version file                            |
| ├─ `env2.py`                               | Environment variables/settings                 |
<br>

<hr><p align="right" dir="auto"><a href="#-table-of-contents">Back to Table of Contents</a></p>

# 🧪 Testing and Validation

**Overview**  
Throughout the course of the project, testing and validation were conducted to ensure functionality, responsiveness, and usability. Importantly, testing in Incognito Mode is crucial because it provides a clean testing environment without cached data, stored cookies, or browser extensions interfering with the site’s URL. Essentially, it mimics a first-time visitor's experience, making sure the site works as expected for new users without any hidden browser influences.

**Testing Methods**  
• *Debugging and Browser Tools*: Regular debugging and testing were performed using [Chrome DevTools](https://developer.chrome.com/docs/devtools) to analyse and troubleshoot issues efficiently.  
<!-- • Testing Sheet: A structured approach was followed using the MHA testing sheet (Google read-only) to verify compliance and accessibility.   -->
• *Peer Code Review*: My colleagues provided a "fresh set of eyes" through peer code reviews, helping identify potential issues that were overlooked.

## ✅ Manual Testing
**Overview**

This section summarises the results of user interface (UI) element functionality testing for the website. The focus is on key interactive elements such as buttons, links, toggles, menus, cart actions, review functions, and search bars, to ensure they work correctly.

**✅ User experience critera testing**

In-depth testing has been carried out to ensure that user criteria were met.

<details>
<summary>Click to view user experience critera testing results</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/ux.webp" alt="Test grid" style="width:100%;"></details><br>

**✅Responsiveness testing**
   All tests were conducted in [Chrome DevTools](https://developer.chrome.com/docs/devtools), using the device toolbar for the following customised dimensions:

   o Mobile from 360x640 to 414x896  
   o Tablets from 601x962 to 1280x800  
   o Laptops 1280x720 to 1920x1080

<details>
<summary>Click to view responsiveness test grid</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/testgrid.webp" alt="Test grid" style="width:100%;"></details><br>

**✅ Controls testing**

1. **Navigation**  
   o Verified links hover effects  
   o Verified all navigation links work correctly  
   o Tested responsiveness on multiple devices  

**Tested UI Elements**
The following types of UI controls were tested:

*   **Navbar Elements**: Toggles, navigation menus, cart, login, sign up
*   **Buttons**: Add to cart, publish, edit, delete, clear cart, update review, generate bill
*   **Links**: Search links, filtered search
*   **Search Bars**: Search your orders, search reviews, and general filtered search
*   **Admin Functions**: Editing menus, image uploads, adding dishes
*   **Order Operations**: Generate bill, search bill

**Purpose**
The testing aims to verify that each interactive element:

*   Is present and correctly displayed
*   Responds appropriately when clicked or tapped
*   Performs the expected action (e.g., adding to cart, publishing a review)
*   Provides clear feedback (e.g., button changes, result of action)

**Results Summary**
*   All tested elements passed successfully.
*   This indicates the UI components are functioning as intended and meet quality standards.

This test sheet displays the results of responsiveness and validation tests conducted across various devices and browsers.

<details>
<summary>Click to view controls test grid</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/controls.webp" alt="Test grid" style="width:100%;"></details><br>

## [✅ HTML Validation](https://validator.w3.org/#validate_by_input)

The website currently has <span style="color:#39FF14">no errors or warnings</span>.

<details>
<summary>Click to view HTML validation results</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/htmlval.webp" alt="HTML validation results" style="width:50%;">

</details><br>

When MS Copilot generated code, occasional stray elements like <span style="font-family:monospace;">&lt;/span&gt;</span> and other closing tags appeared due to the way it predicted and completed code snippets. These errors were flagged during HTML validation and were corrected in [VS Code](https://code.visualstudio.com/download).

Additionally, the use of explicit ARIA role attributes (e.g. role="button", role="main") on HTML elements was initially guided by recommendations from the WAVE accessibility tool. However, these roles are inherently implied by the semantic HTML5 elements themselves. The Nu HTML Validator correctly flags them as unnecessary. To ensure leaner, more semantic code and to align with modern best practices, we chose to deselect checking redundant role attributes. 

## ✅ CSS Validation
<details>
<summary>Click to view CSS validation results</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/cssval.webp" alt="CSS validation results" style="width:80%;">
</details><br>

<span style="color:#39FF14">No errors found</span>

This document validates as CSS level 3 + SVG.

## ✅ JS Validation

*Process*: JavaScript files were validated using several validators.

The longer the work on a project, the larger the codebase becomes, so by validating JavaScript code regularly, the benefits include:  
•	Catch fundamental errors  
•	Prevents potentially disastrous bugs  
•	Have cleaner, safer, and maintainable code  
•	Speed up the code-writing process  
•	Save many hours of debugging  

To ensure code clarity, consistency, and maintainability across all modern environments, I ran the project through [JS Hint](https://jshint.com/).

<details>
<summary>Click to view JS Hint validation results</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/jshint.webp" alt="JS validation results" style="width:10
%;"></details><br>

Because this project uses a modern script, JS Hint was configured to allow 'New JavaScript features (ES6)'. <span style="color:#39FF14">No errors</span> are found in the current version of the site.

## ✅ WAVE
WAVE (Web Accessibility Evaluation Tool) Accessibility was used to audit the HTML and UI, which scans the rendered page for issues like missing alt text, poor contrast, and improper heading structure. The focus is on the way the output serves users with disabilities. 
<span style="color:#39FF14">No errors or warnings</span> are detected in the current version.

<details>
<summary>Click to view WAVE results</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/wave.webp" alt="Wave results" style="width:100%;"></details><br>


## ✅ Chrome DevTools Lighthouse
• A [Lighthouse](https://developers.google.com/web/tools/lighthouse/) audit was conducted using the tool on Chrome DevTools for each web page.  
• Categories *Accessibility*, *Best Practices*, and *SEO* all have a score of <span style="color:#39FF14">100</span>.
• The *Performance* scores for the various pages ranged between <span style="color:#39FF14">91-100</span>.

**Desktop**
<details>
<summary>Click to view Lighthouse results for desktop</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/lighthouse.webp" alt="Lighthouse results for mobile" style="width:100%;"></details><br>

**Mobile**
<details>
<summary>Click to view Lighthouse results for mobile</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/mobile.webp" alt="Lighthouse results for mobile" style="width:100%;"></details><br>

## ✅ SQL Queries

Using `django-debug-toolbar 5.2.0`, various Django template pages were tested by generating [SQL queries](https://django-debug-toolbar.readthedocs.io/en/latest/changes.html#id2). The tests were run in production mode locally with `DEBUG=True`. 0.1 second is about the limit for having the user feel that the system is reacting instantaneously, meaning that no special feedback is necessary except to display the result. 1.0 second is about the limit for the user's flow of thought to stay uninterrupted. With 1 to 4 queries per page, the load time did remained less than 0.213 ms, which is considered to be highly effective.

<details>
<summary>Click to view test grid</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/sqlquries.webp" alt="Test grid" style="width:100%;"></details><br>

**Findings**
•	Low Query Count: Most pages execute only a few queries (0–3).

•	`Login`/`Signup` Efficiency: These critical paths have zero queries, which translates to swift performance and efficiency during user onboarding and authentication.

•	`Profile`, `Cart`, `Orders`, and `Review`-related pages: Most pages execute 2-3 queries, which is reasonable for standard CRUD operations. The timing (70–115ms) could be considered moderate, but this should be interpreted based on expected user load and desired page responsiveness.

•	`generate_bill.html`: This page executes 5 queries with a total time of over 200 ms. This page represents more complex logic, aggregations, joins, and multiple lookups to generate a bill.

<details>
<summary>Click for detailed timings and SQL structure of database queries for the “generate bill” page.</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/sqlgenbill.webp" alt="Test grid" style="width:100%;">

**Testing Results**
**Breakdown**
•	Title:
SQL queries from 1 connection
Indicates all queries came from a single database connection handling this request.
•	default 213.68 ms (5 queries):
The total time for all 5 SQL queries was 213.68 milliseconds.

**Queries Table**
For each query, the table shows:
•	Query: The SQL command (truncated for display), e.g., SELECT ..., UPDATE, INSERT INTO, etc.
•	Timeline: A colored bar indicating when during the total page load the query was executed. Each query gets a different colour.
•	Time (ms): How long that individual query took, in milliseconds.
•	Action: Buttons for viewing the full SQL ("Sel") or the explain plan ("Expl").

**List of Queries in Order**
1.	SELECT FROM django_session
•	Filters sessions by expire_date and session_key.
•	Time: 37.67 ms
2.	SELECT FROM cafe_user
•	Used to retrieve user info.
•	Time: 37.49 ms
3.	SELECT FROM cafe_order
•	Gets an order that isn’t "bill_clear" and has table = Take Away.
•	Time: 38.96 ms
4.	UPDATE cafe_order
•	Updates an order with new items, table as "Take Away", price, etc.
•	Time: 47.82 ms
5.	INSERT INTO cafe_bill
•	Inserts a new bill record, with items, total, timestamp, etc.
•	Time: 51.74 ms

**Interpretation**
•	**Query Timing**: None of the queries are extremely slow on their own (all under 52 ms).
•	**Type of Queries**: The sequence shows the logical flow: get user/session, check or fetch orders, update them, then record a bill. This matches a bill-generation workflow.
•	**Good Practice**: Having just 5 queries, even for a complex flow like generating a bill, is efficient in terms of logic/structure.

</details><br>

## ✅ CI Python Linter
To check code quality and adherence to python style guidelines, all python files were checked using the [Code Institute’s Python Linter](https://pep8ci.herokuapp.com/), which uses [PEP8](https://peps.python.org/pep-0008/) (8th Python Enhancement Proposal (PEP) document).

The result "<span style="color:#39FF14">All clear, no errors found</span>" across all files means that there are no stylistic or syntax errors and the code complies with Python linting standards.

<details>
<summary>Click to view test grid</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/cipython.webp" alt="Test grid" style="width:100%;"></details><br>

## ✅ Semantic HTML

### Current Semantic HTML Implementation

<details><summary>1. Proper Document Structure </summary>

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="...">
</head>
```
</details><br>

<details><summary>2. Semantic Layout Elements</summary>

- **`<nav>`**: Used for navigation bar with proper ARIA attributes
- **`<main>`**: Wraps the main content area with `flex-grow-1` class
- **`<footer>`**: Contains social media links and copyright information

</details><br>

<details><summary>3. Proper Heading Hierarchy</summary>
Templates follow proper h1 → h2 → h3 structure:

```html
<h1>🍽️ Menu</h1>              <!-- Page title -->
<h2>pizzas:</h2>              <!-- Category -->
<h3 class="card-title">Pizza Name</h3>  <!-- Item name -->
```
</details><br>

<details><summary>4. Form Semantics</summary>
- Proper `<label>` associations with form controls
- Required field indicators
- ARIA attributes for accessibility:

```html
<label for="form3Example3c">Write a comment</label>
<input type="text" name="comment" id="form3Example3c" required>
```
</details><br>

<details><summary>5. Table Semantics</summary>

```html
<table class="table table-bordered">
    <thead>
        <tr>
            <th>Item name</th>
            <th>Qty</th>
            <th>Total</th>
        </tr>
    </thead>
    <tbody>
        <!-- data rows -->
    </tbody>
</table>
```
</details><br>

<details><summary>6. List Semantics</summary>

```html
<ul class="list-group">
    <li class="list-group-item">Menu items</li>
</ul>
```
</details><br>

<details><summary>7. Accessibility Features</summary>

- ARIA labels for screen readers
- Visually hidden labels for search inputs
- Proper button and link semantics
- Focus management and keyboard navigation
</details><br>

### Semantic HTML Benefits in This Project

1. **SEO Optimisation**: Proper heading hierarchy helps search engines understand content structure
2. **Accessibility**: Screen readers can navigate using semantic landmarks
3. **Code Maintainability**: Clear structure makes templates easier to understand and modify
4. **Performance**: Semantic elements provide styling hooks without extra CSS classes
5. **Future-Proofing**: Standards-compliant markup ensures compatibility with new technologies

### Key Semantic Patterns Used

- **Progressive Enhancement**: Forms work without JavaScript
- **ARIA Landmarks**: Navigation, main content, and complementary sections
- **Descriptive Text**: Alt attributes for images, meaningful link text
- **Form Labels**: Proper association between labels and inputs
- **Error Messaging**: ARIA live regions for dynamic content updates

The site demonstrates semantic HTML practices with consistent heading hierarchies, proper form semantics, and accessibility considerations throughout the user interface.

## ✅ Controls testing

**Overview**

This section summarises the results of user interface (UI) element functionality testing for the website. The focus is on key interactive elements such as buttons, links, toggles, menus, cart actions, review functions, and search bars, to ensure they work correctly.

<details>
<summary>Click to view controls test grid</summary>
<img src="https://raw.githubusercontent.com/Ozzymara/docpe/refs/heads/main/assets/controls.webp" alt="Test grid" style="width:100%;"></details><br>

**Tested UI Elements**
The following types of UI controls were tested:

*   **Navbar Elements**: Toggles, navigation menus, cart, login, sign up
*   **Buttons**: Add to cart, publish, edit, delete, clear cart, update review, generate bill
*   **Links**: Search links, filtered search
*   **Search Bars**: Search your orders, search reviews, and general filtered search
*   **Admin Functions**: Editing menus, image uploads, adding dishes
*   **Order Operations**: Generate bill, search bill

**Purpose**
The testing aims to verify that each interactive element:

*   Is present and correctly displayed
*   Responds appropriately when clicked or tapped
*   Performs the expected action (e.g., adding to cart, publishing a review)
*   Provides clear feedback (e.g., button changes, result of action)

**Results Summary**
*   All tested elements passed successfully.
*   This indicates the UI components are functioning as intended and meet quality standards.

<hr><p align="right" dir="auto"><a href="#-table-of-contents">Back to Table of Contents</a></p>

# 🚀 Deployment

<details><summary>1. Initial Setup</summary>
* Create a new folder in your Projects directory for your Django project (use underscores in the name).  
* Open the folder in VS Code (File > Open Folder).</details><br>

<details><summary>2. Git & GitHub</summary>
* On GitHub, create a new repository (same name as your folder for consistency).
* Initialise the repo locally:
    * Open terminal in VS Code.
    * Paste the "create a new repository on the command line" commands from GitHub.        
    * Push your initial commit.
* In VS Code, create a `.gitignore` file and add `.venv/` and `env.py` to it.</details><br>
    
<details><summary>3. Python Environment</summary>
* Create a virtual environment (Command Palette: “Python: Create Environment” > venv).
* Activate the environment.</details><br>

<details><summary>4. Django Installation</summary>
* Install Django (e.g., `pip3 install django~=4.2.1`).
* Add Django to requirements: `pip3 freeze --local > requirements.txt`.</details><br>

<details><summary>5. Create Django Project & App</summary>
* Start your project:
    * `django-admin startproject your_project_name .`
* Create a new app:
    * `python3 manage.py startapp app_name`
* In `settings.py`, add `'app_name'` to `INSTALLED_APPS`.</details><br>

<details><summary>6. Database & Admin Setup</summary>
* Make and apply migrations:
    * `python3 manage.py migrate`
    * `python3 manage.py makemigrations` (if needed)
* Create a superuser: `python3 manage.py createsuperuser`</details><br>

<details><summary>7. Secure Environment Variables</summary>
* Create `env.py` in the project root with your `DATABASE_URL` and `SECRET_KEY`.
* Ensure `env.py` is in `.gitignore`.</details><br>

<details><summary>8. Prepare for Heroku Deployment</summary>
* Install deployment requirements:
    * `pip3 install gunicorn~=20.1`
    * `pip3 freeze --local > requirements.txt`
* Create a `Procfile` with:
        * `web: gunicorn your_project_name.wsgi`  
* Set `DEBUG = False` in `settings.py`.
* Add `'.herokuapp.com'` to `ALLOWED_HOSTS`.</details><br>

<details><summary>9. Deploy on Heroku</summary>
* Log in or sign up at Heroku.
* Create a new app (unique name, select region).
* In Heroku’s “Settings”, use “Reveal Config Vars” to add:
    * `DISABLE_COLLECTSTATIC=1`
    * `DATABASE_URL` (as provided)
    * `SECRET_KEY` (generated)
* Connect Heroku to your GitHub repo (Deploy tab).
* Push your code to GitHub.
* On Heroku, deploy the connected branch and click “View” to see your live site.</details><br>

<details><summary>10. Working With Repos</summary>
* Clone: On GitHub, copy the repo URL; in terminal: `git clone <repository-url>`.
* Fork: On GitHub, click “Fork” to make a copy to your account.</details><br>

<details><summary>11. Run Locally</summary>
* Start server: `python3 manage.py runserver`
* To stop: `CTRL+C` (Windows) or `⌘+C` (Mac)
* Make migrations if needed and apply them as above.
* Create a superuser if needed.</details><br>

<hr><p align="right" dir="auto"><a href="#-table-of-contents">Back to Table of Contents</a></p>

# 🙌 Credits

## ⌨️ Code

• The initial GitHub project was built using the [Code Institute](https://codeinstitute.net/ie/) template to start.  
• The navigation bar, cards, buttons, and the modal form were built with [Bootstrap feature](https://getbootstrap.com/docs/5.3).  
• The website utilises the Bootstrap framework for responsive design and styling components like the navigation bar and cards.  
• I took inspiration from previous projects shared with us, especially from the works of [Jeremy Greig](https://jeremygreig.github.io/CI_Project_1_JG/index.html) and [Megan Otton](https://meganotton.github.io/Mental_Health_Website/).  
• Learning and parts of the code were supplied by GitHub Copilot.

## 📝 Content

The text content was generated using AI and Google search.

## 🎥 Media
Images were either selected from a a vast collection of royalty-free image sites or AI generated using [PicLumen](https://piclumen.com/).
Static badges for README documentation [Shields.io](https://shields.io/badges/static-badge) & [Simple Icons](https://simpleicons.org/)

## **🤖 AI Implementation and Orchestration**

**Use Cases and Reflections** 

**Code Creation** 

*   **Reflection:** AI tools, especially GitHub Copilot, were leveraged to accelerate the development of HTML, CSS, JavaScript, and Python components, Bootstrap layouts, and responsive design patterns. This enabled rapid prototyping and allowed for more time to focus on accessibility and user experience. 
*   **Examples:** Copilot generated initial structures for the navigation bar, information cards, and other interactive buttons. It also provided suggestions for semantic HTML and ARIA attributes to improve accessibility. 

**Debugging** 

*   **Reflection:** AI assistance was instrumental in identifying and resolving validation for HTML, CSS, JavaScript, and Python errors, fixing accessibility issues, and ensuring proper tag nesting and structure. 
*   **Examples:** Copilot Chat helped troubleshoot issues such as unclosed tags, improper heading order, and missing alt text. It also suggested fixes for responsive layout bugs and CSS specificity conflicts. 

**Performance and UX Optimisation** 

*   **Reflection:** AI-driven recommendations were used to enhance site performance and user experience, particularly around responsive design and accessibility best practices. 
*   **Examples:** Copilot suggested improvements like using stronger security and ensuring keyboard navigability for all interactive elements. 

**Automated Testing and Validation** 

*   **Reflection:** AI tools supported the validation process by providing checklists and reminders for HTML and CSS validation, as well as accessibility audits. 
*   **Examples:** Copilot generated code snippets for manual testing steps and validation routines, ensuring that all links, buttons, and navigation elements were accessible and functional across devices. 

**Documentation Writing** 

*   **Reflection:** AI tools streamlined the creation of project documentation, offering clear and concise explanations for setup, deployment, and feature descriptions. 
*   **Examples:** Copilot was used to draft README sections, including installation instructions, feature overviews, and accessibility notes, ensuring the documentation was comprehensive and user-friendly. 

**Overall Impact** 

*   **Efficiency Gains:** The use of AI tools significantly reduced development time, automated repetitive tasks, and improved code quality. This allowed for a greater focus on design, accessibility, and user experience. 
*   **Challenges:** Occasional contextual adjustments were needed for AI-generated code, particularly to align with accessibility standards and project-specific requirements. These were resolved through iterative testing and manual review.

## 🧡 Acknowledgements

• [Dillon](https://github.com/dillon-mccaffrey-ci) - for supporting with debugging, security features, and overall guidance throughout the project.  
• [Kevin](https://github.com/kevin-ci) - for providing tips on logic.  
• [Roo](https://github.com/roomacarthur) - for explaining how to conduct effective testing  
• [Mark](https://github.com/mbriscoe) - for advice on EDR.  
• [Roman]() - for advice on effective use of AI.  
• [Harry]() - for providing feedback on the design, alternative layout, and responsiveness.  
• [Andrea](https://github.com/AndreaFitz) - for providing feedback on the user experience  

## 💡 Future ideas:

● Enhance security measures to prevent unauthorised access during social auth.  
● Support social login via OAuth (Google, GitHub) with account linking/unlinking in profiles.  
● Synchronise Django server time with local time dynamically per user's timezone.  
● Detect and store user time zones for personalised time displays across the app.  
● Enable users to download their data in CSV format from their dashboard.  
● Generate and return CSV files based on user-specific records/models.  
● Implement real-time online user display using WebSocket or Django Channels for scalability.  
● Improve dark mode features with better UI/UX consistency and toggle options.  
● Expand social authentication providers beyond Google and GitHub as needed.  

## 🆕 Recent Updates

Updates have yet to be implemented since the site's deployment on 12th August 2025.

<hr><p align="right" dir="auto"><a href="#-table-of-contents">Back to Table of Contents</a></p>
