# Recipe-Book

Recipe Book website is a front-end web application built using HTML, CSS, and JavaScript, the project demonstrates core web development skills such as semantic structuring, responsive styling, and client-side interactivity. It provides an organized and user-friendly interface for browsing recipes, focusing on clean design, usability, and basic dynamic behavior.

Features : 
1) Recipe Search by Name - Users can search recipes using keywords (e.g., carrot, chicken).
2) Random Recipe Generator - "Get Random Recipe" button fetches a random meal.
3) Responsive Design
4) Recipe Details Modal Popup - Clicking a recipe opens a modal window. Modal shows:
   -> Recipe name
   -> Image
   -> Category
   -> Area (Cuisine)
   -> Ingredients with measurements
   -> Cooking instructions
   -> YouTube recipe link
   -> Original source link (if available)
5) User Feedback Messages
   Informational messages:
      “Searching…”
      “Fetching random recipe…”
   Error messages for:
      No results found
      API failures

Technologies Used :
1) HTML5 - HTML5 is used to structure the Recipe Book website. It defines the layout of the application, including the search form, buttons, recipe cards, and modal popup. Semantic elements improve readability and accessibility of the web page.
2) CSS3 - CSS3 is used to design and style the website. It provides responsive layouts using Flexbox and Grid, custom color themes using CSS variables, animations, hover effects, and modal transitions. CSS ensures the website is visually appealing and mobile-friendly.
3) Javascript (ES6) - JavaScript adds interactivity and dynamic behavior to the website. It is used to handle user events, fetch data asynchronously from APIs using fetch and async/await, manipulate the DOM dynamically, and display recipe details in a modal window. ES6 features improve code efficiency and readability.


How Website Works :
1) User enters a recipe name or clicks Random Recipe.
2) JavaScript sends a request to TheMealDB API.
3) API returns recipe data in JSON format.
4) Recipes are displayed dynamically as cards.
5) User clicks a recipe card to view details.
6) Recipe details are fetched using recipe ID.
7) Details are shown in a modal popup.
8) User can close the modal anytime.
