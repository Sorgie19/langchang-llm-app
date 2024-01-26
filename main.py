import langchain_helper as lch
import streamlit as st

st.title("Band/Music Name Generator")

sub_genres = {
    "Rock": ("Alternative Rock", "Blues Rock", "Folk Rock", "Grunge", "Hard Rock", "Heavy Metal", "Indie Rock", "Progressive Rock", "Psychedelic Rock", "Punk Rock", "Gothic Rock", "Glam Rock", "Southern Rock", "Surf Rock", "Other"),
    "Rap": ("Conscious Rap", "Gangsta Rap", "Trap", "Mumble Rap", "Old School Rap", "East Coast Rap", "West Coast Rap", "Dirty South", "Crunk", "Horrorcore", "Jazz Rap", "Political Rap", "G-Funk", "UK Grime", "Drill", "Cloud Rap", "Abstract Rap", "Battle Rap", "Christian Rap", "Freestyle Rap", "Other"),
    "Country": ("Traditional Country", "Country Pop", "Country Rock", "Bluegrass", "Country Rap", "Outlaw Country", "Alternative Country", "Bro-country", "Contemporary Country", "Country Blues", "Country Folk", "Other"),
    "EDM": ("House", "Techno", "Dubstep", "Drum and Bass", "Trance", "Hardstyle", "Electro House", "Future Bass", "Tropical House", "Deep House", "Tech House", "Progressive House", "Other"),
    "Heavy Metal": ("Thrash Metal", "Death Metal", "Black Metal", "Power Metal", "Doom Metal", "Speed Metal", "Symphonic Metal", "Gothic Metal", "Nu Metal", "Folk Metal", "Glam Metal", "Industrial Metal", "Other"),
    "Hip-Hop": ("East Coast Hip-Hop", "West Coast Hip-Hop", "Gangsta Rap", "Trap", "Mumble Rap", "Old School Hip-Hop", "Crunk", "Dirty South", "Underground Hip-Hop", "Alternative Hip-Hop", "Conscious Hip-Hop", "Other"),
    "Jazz": ("Bebop", "Cool Jazz", "Fusion Jazz", "Gypsy Jazz", "Hard Bop", "Modal Jazz", "Free Jazz", "Swing", "Big Band", "Latin Jazz", "Smooth Jazz", "Jazz Blues", "Jazz Funk", "Other"),
    "Pop": ("Dance Pop", "Electropop", "Teen Pop", "Pop Rock", "Power Pop", "Indie Pop", "K-Pop", "J-Pop", "Adult Contemporary", "Baroque Pop", "Bubblegum Pop", "Chamber Pop", "Other"),
    "Electronic": ("Ambient", "Breakbeat", "Chillwave", "Downtempo", "Electronica", "IDM", "Trip Hop", "Electroclash", "Synthpop", "Eurodance", "Other"),
    "Folk": ("Contemporary Folk", "Folk Rock", "Indie Folk", "Folk Pop", "Progressive Folk", "Celtic Folk", "Americana", "Neofolk", "Anti-Folk", "Folk Punk", "Other"),
    "Classical": ("Baroque", "Chamber Music", "Choral", "Classical Crossover", "Early Music", "Opera", "Orchestral", "Romantic", "Solo Instrumental", "Contemporary Classical", "Other"),
    "Blues": ("Delta Blues", "Chicago Blues", "Country Blues", "Electric Blues", "Acoustic Blues", "Blues Rock", "Soul Blues", "Swamp Blues", "Other"),
    "Reggae": ("Dancehall", "Dub", "Roots Reggae", "Reggaeton", "Ska", "Lovers Rock", "Rocksteady", "Other"),
    "Latin": ("Reggaeton", "Bachata", "Banda", "Cumbia", "Latin Pop", "Salsa", "Merengue", "Tango", "Bossa Nova", "Samba", "Flamenco", "Other"),
    "R&B/Soul": ("Contemporary R&B", "Soul", "Funk", "Disco", "Motown", "Neo-Soul", "Psychedelic Soul", "Quiet Storm", "Other"),
    "World": ("Afrobeat", "Balkan", "Celtic", "Middle Eastern", "Klezmer", "Soca", "Zouk", "K-pop", "Other"),
    "New Age": ("Meditative", "Ambient", "Nature Sounds", "Space Music", "Neoclassical New Age", "Other"),
    "Punk": ("Hardcore Punk", "Post-Punk", "Pop Punk", "Ska Punk", "Anarcho-Punk", "Crust Punk", "Other")
}

# Add an empty default option to the main genre selection
user_main_genre = st.sidebar.selectbox("What genre of music do you make?", [""] + list(sub_genres.keys()))

# Initialize user_sub_genre
user_sub_genre = None

# Only display the subgenre selection if a main genre is selected
if user_main_genre:
    # Add an empty default option to the subgenre selection
    user_sub_genre = st.sidebar.selectbox(f"What sub genre of {user_main_genre} do you make?", [""] + list(sub_genres[user_main_genre]))
    
    # Only proceed if a subgenre has been selected
    if user_sub_genre:
        if user_sub_genre == "Other":
            user_sub_genre = st.sidebar.text_input("Please type in your sub-genre")

        # Add a field to specify the amount of names to generate after a subgenre has been selected
        amount_of_names = st.sidebar.number_input("How many names would you like to generate?", min_value=1, max_value=35, value=10, step=1)

        # Only display the OpenAI key input after the amount of names has been selected (which is always the case since it has a default value)
        openai_key = st.sidebar.text_input("Enter your OpenAI key") if amount_of_names else None

        # Only display the generate button if an OpenAI key has been entered
        if openai_key:
            if st.sidebar.button('Generate'):
                # Pass the amount_of_names to the generate_band_names function
                response = lch.generate_band_names(user_main_genre, user_sub_genre, openai_key, amount_of_names)
                # Assuming the response returns a list of names, iterate and display them
                st.text(response['band_names'])
