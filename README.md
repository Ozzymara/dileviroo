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


