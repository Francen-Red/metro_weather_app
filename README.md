The Metro Weather App is based on an algorithm inspired by Programming Fever on YouTube. Through his tutorial, I learned how to use an API key to retrieve weather data from OpenWeatherMap. This project was inspired by my previous capstone project, where I developed a hardware Arduino module with a Nextion touch display. The module displayed air quality components and particulate matter and was compared to the IQAir air quality detector. Although IQAir also provided weather details, my focus back then was primarily on air quality.

With this app, I wanted to bridge that gap by creating a program that retrieves weather information for specific cities in Metro Manila. I customized the app to include visually appealing text colors and ensured it handles HTTP and request errors gracefully, offering a smooth user experience.

1. Install and import the requests module to make API calls to OpenWeatherMap.
2. Store the API key for OpenWeatherMap in a separate file to be read later for security and organization.
3. Define a variable containing a list of cities within the National Capital Region (NCR), as this weather app is specifically for Metro Manila.
4. Use a while-loop to ask the user for the city they want to check the weather for, ensuring the input is in the list of cities in Metro Manila.
5. Define a function that fetches weather data for the city provided by the user. This function reads the API key from the text file and combines it with the parameters needed to construct a URL for fetching data from OpenWeatherMap.
6. In the same function, use the requests module to make a request call to OpenWeatherMap with the URL and parameters. If any errors occur during the request, display an error message.
7. Define another function to display the retrieved weather data, including the city name, temperature, weather description, humidity, and wind speed, all with proper units.
8. After displaying the weather data for the city, ask the user if they want to input another city, restricting the response to "yes" or "no" only.