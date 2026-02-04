# Recipe-Book

Recipe Book website is a front-end web application built using HTML, CSS, and JavaScript. The project demonstrates core web development skills such as semantic structuring, responsive styling, client-side interactivity, and basic conversational UI integration. It provides an organized and user-friendly interface for browsing recipes, along with an integrated chatbot that assists users in exploring recipes and navigating the website, focusing on clean design, usability, and dynamic behavior.

Features : 
1) Recipe Search by Name
   Users can search recipes using keywords (e.g., carrot, chicken).
2) Random Recipe Generator
   “Get Random Recipe” button fetches a random meal.
3) AI-Powered Chatbot
   A generalized AI chatbot powered by Hugging Face LLM and Tavily API that:
      Understands natural language queries
      Provides intelligent, context-aware responses
      Assists users with recipe-related questions and general guidance
4) Responsive Design
   Website adapts smoothly to different screen sizes and devices.
5) Recipe Details Modal Popup
   Clicking a recipe opens a modal window.
   Modal shows:
      -> Recipe name
      -> Image
      -> Category
      -> Area (Cuisine)
      -> Ingredients with measurements
      -> Cooking instructions
      -> YouTube recipe link
      -> Original source link (if available)
6) User Feedback Messages
   Informational messages:
      “Searching…”
      “Fetching random recipe…”
   Error messages for:
      No results found
      API failures

Technologies Used :
1) HTML5
   HTML5 is used to structure the Recipe Book website. It defines the layout of the application, including the search form, buttons, recipe cards, chatbot interface, and modal popup. Semantic elements improve       readability and accessibility of the web page.
2) CSS3
   CSS3 is used to design and style the website. It provides responsive layouts using Flexbox and Grid, custom color themes using CSS variables, animations, hover effects, chatbot UI styling, and modal              transitions. CSS ensures the website is visually appealing and mobile-friendly.
3) JavaScript (ES6)
   JavaScript is used to handle user interactions, manage chatbot UI behavior, communicate with APIs, fetch data asynchronously, manipulate the DOM dynamically, and display recipe details in modal popups. Modern    ES6 features improve code readability and efficiency.
4) Hugging Face LLM
   Hugging Face large language models are used to power the generalized chatbot. The LLM processes natural language user queries and generates intelligent, context-aware responses, enabling conversational           interaction beyond rule-based logic.
5) Tavily API
   Tavily is used to enhance the chatbot’s responses by retrieving relevant and up-to-date information. It enables real-time search and retrieval, allowing the chatbot to provide informative and accurate answers    based on external knowledge sources.

How Website Works :
1) User enters a recipe name or clicks Random Recipe.
2) JavaScript sends a request to TheMealDB API.
3) API returns recipe data in JSON format.
4) Recipes are displayed dynamically as cards.
5) User clicks a recipe card to view details.
6) Recipe details are fetched using recipe ID.
7) Details are shown in a modal popup.
8) User can close the modal anytime.
