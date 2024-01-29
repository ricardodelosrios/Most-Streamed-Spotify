# 🎵 Most Streamed Spotify Dashboard 📊

## Overview

This project offers a deep dive into the trends of the most popular songs from 2017 to 2023, leveraging a comprehensive data set sourced from Kaggle. The dataset provides a wide range of features, allowing for a nuanced analysis of each song's attributes, popularity, and presence on various music platforms.

## Step by Step 🛠️

### **Download the Kaggle Data**
   
The data set summarizes the essence of the music landscape in 2023, covering critical information such as track names, artists, release dates, playlists and Spotify charts, streaming statistics, Apple Music and Deezer presence, Shazam charts and a variety of audio. characteristics.
   
   - [Get the dataset](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023?resource=download).

### **Create an APP in Spotify**

  - Create a Spotify Account:

    - If you don't already have a Spotify account, create one by signing up on the Spotify website.

  - Access the Spotify Developer Dashboard:

    - Go to the Spotify Developer Dashboard.
    - Log in with your Spotify account credentials.
 
  - Create a New App:

    - Once logged in, click on the "Create an App" button.

  - Fill in App Details:

    - Provide the necessary details for your new app, including the name and description.
    - You may need to agree to the terms and conditions.

  - Obtain Client ID and Client Secret:

    - After creating the app, you'll be provided with a Client ID and Client Secret. Keep these credentials secure, as they are essential for authenticating your app with the Spotify API.

Always refer to the latest [Spotify Developer Documentation](https://developer.spotify.com/) for the most up-to-date information and specific details regarding the API, authentication, and other features.

### **Create a `.env` file**

   - Create a `.env` file for the API keys in the project directory.
   - Add the following lines:
      - CLIENT_ID="The 'Client ID' provided by Spotify"
      - CLIENT_SECRET="The 'Client Secret' provided by Spotify"

## **Python Script**

This Python script utilizes the Spotify API to enrich a DataFrame containing Spotify track information by adding the URL of the first image associated with each track's album. The enriched DataFrame is then saved to a new CSV file.

### Importing Libraries:

The code imports necessary libraries
  - '**dotenv**' for loading environment variables.
  - '**os**' for operating system functionalities, base64 for encoding.
  - '**requests**' for making HTTP requests.
  - '**pandas**' for data manipulation.
    
### Loading Environment Variables:

It uses ***load_dotenv()*** to load environment variables from a file, presumably containing **CLIENT_ID** and **CLIENT_SECRET** for Spotify API authentication.

### Getting Spotify Access Token:

The function ***get_token()*** retrieves an access token from the Spotify API using client credentials. It encodes the client ID and client secret in Base64 and sends a POST request to Spotify's token endpoint.

### Searching for a Track:

The function ***search_track(track_name, artist_name, token)*** searches for a track on Spotify using the provided track name and artist name, returning the track ID if a result is found.

### Getting Track Details:

The function ***get_track_details(track_id, token)*** retrieves details of a track from Spotify using the track ID, specifically the URL of the first image associated with the track's album.

### Processing a DataFrame:

The script reads a CSV file named **'spotify-2023.csv'** into a Pandas DataFrame.
It iterates through each row of the DataFrame, searching for track details and updating the DataFrame with the URL of the first image associated with the track's album.
The results are stored in a new column named **'image_url'**.
The updated DataFrame is saved to a new CSV file named **'updated_file.csv'**.

### Printing Columns:

The script prints the column names of the DataFrame to the console.

**Note:**

The script includes error handling for unsuccessful API requests and missing data.
There's a check for the presence of the 'artist(s)_name' column in the DataFrame before proceeding with the search.
Error messages are printed to the console in case of issues.

## Power BI Symphony 🎵

1. **Install Bravo Overture:**
   - Install Bravo, the virtuoso of Power BI.

2. **Date Waltz:**
   - Choreograph the 'Date' waltz, uniting 'released_year,' 'released_month,' and 'released_day.'

3. **Visual Crescendo:**
   - Bravo takes the lead in a visual crescendo – clustered bar charts, line charts, and slicers pirouette across the dashboard.

4. **Measures Composition:**
   - Compose custom measures, turning data into a symphony of insights.

5. **Visual Sonnet:**
   - Conjure HTML poetry for image integration – visuals that resonate like sonnets within Power BI.

6. **Deneb Visual Rhapsody:**
   - Contribute to the visual symphony with Deneb's rhapsody. Express with new measures, aligning notes with provided instructions.

7. **Heatmap Ballroom:**
   - Join the heatmap ballroom, creating new measures and importing JSON templates for a dance of colors.

## Visual Styling Elegance 💅

1. **Theme Couture:**
   - Adorn the dashboard with a bespoke theme, tailored for a visual feast.

2. **Color Palette Symphony:**
   - Craft a color palette symphony, harmonizing the hues for an aesthetic resonance.

3. **Formatting Flourish:**
   - Embellish titles, labels, and formatting with a touch of creative flourish.

## Cards and Drama 🎭

1. **Card Revolution:**
   - Transition to the new card format, casting off the old in favor of a dramatic facelift.

2. **Conditional Drama:**
   - Add a touch of theatrical flair with conditional formatting, where cards express their moods based on the script.

## Project Crescendo 🚀

The PowerBeats 2023 Dashboard, a crescendo of data and visuals, invites you to experience music analytics like never before. 🚀 Let the beats guide you through the symphony of insights and rhythms! 🎉
