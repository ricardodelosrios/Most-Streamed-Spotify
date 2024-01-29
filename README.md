# 🎵 Most Streamed Spotify Dashboard 📊

<div style="display: inline_block"><br/>
  <img align="center" alt="Power BI" src="https://img.shields.io/badge/Power%20BI-61DBFB?style=for-the-badge&logo=Power%20BI&labelColor=black" />

 

https://github.com/ricardodelosrios/Most-Streamed-Spotify/assets/133066908/7dea55c6-e577-4706-8464-c743d93e977c





**Link acceso:** [Most Streamed Spotify Power BI](https://app.powerbi.com/view?r=eyJrIjoiMzkzYWYzMWYtYzZhYS00MDZjLWJlMWItMTg2OTc2Y2Y2YzU0IiwidCI6IjViMTU1MDU3LWMxMGEtNDM3Mi04NWU4LTEzZTA3ZGJlMTc3NSJ9).

## Overview

This project offers a deep dive into the trends of the most popular songs from 2017 to 2023, leveraging a comprehensive data set sourced from Kaggle. The dataset provides a wide range of features, allowing for a nuanced analysis of each song's attributes, popularity, and presence on various music platforms.

## Step by Step 🛠️

1. **Download the Kaggle Data**
   - The data set summarizes the essence of the music landscape in 2023, covering critical information such as track names, artists, release dates, playlists and Spotify charts, streaming statistics, Apple Music and Deezer presence, Shazam charts, and a variety of audio characteristics.
   - [Get the dataset.](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023?resource=download)
     

2. **Create an APP in Spotify**
   - Create a Spotify Account:
     - If you don't already have a Spotify account, create one by signing up on the [Spotify website](https://www.spotify.com/).
   - Access the Spotify Developer Dashboard:
     - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
     - Log in with your Spotify account credentials.
   - Create a New App:
     - Once logged in, click on the "Create an App" button.
   - Fill in App Details:
     - Provide the necessary details for your new app, including the name and description.
     - You may need to agree to the terms and conditions.
   - Obtain Client ID and Client Secret:
     - After creating the app, you'll be provided with a Client ID and Client Secret. Keep these credentials secure, as they are essential for authenticating your app with the Spotify API.
   - Always refer to the latest [Spotify Developer Documentation](https://developer.spotify.com/documentation/) for the most up-to-date information and specific details regarding the API, authentication, and other features.

3. **Create a .env file**
   - Create a .env file for the API keys in the project directory.
   - Add the following lines:
     ```env
     CLIENT_ID="The 'Client ID' provided by Spotify"
     CLIENT_SECRET="The 'Client Secret' provided by Spotify"
     ```

4. **Python Script**
   - This Python script utilizes the Spotify API to enrich a DataFrame containing Spotify track information by adding the URL of the first image associated with each track's album. The enriched DataFrame is then saved to a new CSV file.
   - **Importing Libraries:**
     - The code imports necessary libraries: 'dotenv' for loading environment variables, 'os' for operating system functionalities, base64 for encoding, 'requests' for making HTTP requests, and 'pandas' for data manipulation.
   - **Loading Environment Variables:**
     - It uses `load_dotenv()` to load environment variables from a file, presumably containing CLIENT_ID and CLIENT_SECRET for Spotify API authentication.
   - **Getting Spotify Access Token:**
     - The function `get_token()` retrieves an access token from the Spotify API using client credentials.
     - It encodes the client ID and client secret in Base64 and sends a POST request to Spotify's token endpoint.
   - **Searching for a Track:**
     - The function `search_track(track_name, artist_name, token)` searches for a track on Spotify using the provided track name and artist name, returning the track ID if a result is found.
   - **Getting Track Details:**
     - The function `get_track_details(track_id, token)` retrieves details of a track from Spotify using the track ID, specifically the URL of the first image associated with the track's album.
   - **Processing a DataFrame:**
     - The script reads a CSV file named 'spotify-2023.csv' into a Pandas DataFrame.
     - It iterates through each row of the DataFrame, searching for track details and updating the DataFrame with the URL of the first image associated with the track's album.
     - The results are stored in a new column named 'image_url'.
     - The updated DataFrame is saved to a new CSV file named 'updated_file.csv'.
   - **Printing Columns:**
     - The script prints the column names of the DataFrame to the console.
   - **Note:**
     - The script includes error handling for unsuccessful API requests and missing data.
     - There's a check for the presence of the 'artist(s)_name' column in the DataFrame before proceeding with the search.
     - Error messages are printed to the console in case of issues.

5. **Power BI Dashboard**
   - **Bravo Installation:**
     - Begin by installing [Bravo for Power BI](https://bravo.bi/).
   - **Date Handling:**
     - Enhance date analysis by creating a 'Date' column that amalgamates 'released_year,' 'released_month,' and 'released_day.'
   - **Dashboard Visualizations:**
     - Utilize a bar chart to visualize the distribution of tracks based on the number of streams.
     - Implement a line chart to illustrate the correlation between tracks and their release dates.
     - Enhance interactivity by employing slicers to create filters for date, artist, track, and year.
   - **Custom Measures:**
     - Elevate analytical capabilities with custom measures like top song streams, average stream per year, and additional metrics outlined in the provided steps.
   - **Image Integration:**
     - Seamlessly integrate HTML visualizations to showcase images within the Power BI environment.
   - **Deneb Visuals Integration:**
     - Implement specified measures.
     - Integrate Deneb visuals and tailor them according to provided instructions.
   - **Heatmap with Bars:**
     - Augment analysis with a new measure for track count.
     - Import the supplied JSON template for a heatmap with bars.

6. **Power BI Formatting Refinement**
   - **Custom Themes:**
     - Personalize the Power BI theme for a distinctive visual experience.
   - **Color Palette:**
     - Tailor the color palette to align with specified colors for a cohesive and branded appearance.
   - **Formatting Adjustments:**
     - Customize titles, labels, and formatting across the entire dashboard for a polished presentation.
   - **Cards and Conditional Formatting**
     - **Card Formatting:**
       - Modernize card formatting with a transition to a new style, adjusting backgrounds and borders for visual appeal.
     - **Conditional Formatting:**
       - Implement conditional formatting for cards, enhancing data interpretation based on positive or negative values.
      
## References and Credits:

- [Cassete iconos creados por ibrandify - Flaticon](https://www.flaticon.es/iconos-gratis/cassete)
- [Cantante iconos creados por Freepik - Flaticon](https://www.flaticon.es/iconos-gratis/cantante)
- [Calendario iconos creados por Freepik - Flaticon](https://www.flaticon.es/iconos-gratis/calendario)
- [Next track icons created by HAJICON - Flaticon](https://www.flaticon.com/free-icons/next-track)
- [Music and multimedia icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/music-and-multimedia)
- [Rank icons created by Retinaicons - Flaticon](https://www.flaticon.com/free-icons/rank)
  
## Video Reference: 

- [YouTube Video](https://www.youtube.com/watch?v=ZSrVOyKAC4Y&t=800s)
- **Title:** Understanding [Advanced Power BI Project • End-to-End • ChatGPT • Custom Visuals]
- **Author:** [Power BI Park]
- **Published Date:** [28 sept 2023]
- **URL:** [https://www.youtube.com/watch?v=ZSrVOyKAC4Y&t=800s](https://www.youtube.com/watch?v=ZSrVOyKAC4Y&t=800s)
