import random

category_name = ""

movies = [
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    "Pulp Fiction",
    "Forrest Gump",
    "The Matrix",
    "Inception",
    "Interstellar",
    "Fight Club",
    "Goodfellas",
    "The Lord of the Rings",
    "Schindler's List",
    "Gladiator",
    "Saving Private Ryan",
    "Braveheart",
    "Titanic",
    "Avatar",
    "The Avengers",
]

countries = [
    "United States",
    "Canada",
    "United Kingdom",
    "Australia",
    "Germany",
    "France",
    "Japan",
    "China",
    "India",
    "Brazil",
    "Mexico",
    "Russia",
    "South Korea",
    "Italy",
    "Spain",
    "Netherlands",
    "South Africa",
    "Turkey",
    "Argentina",
    "Sweden"
]

actors_actresses = [
    "Tom Hanks",
    "Meryl Streep",
    "Leonardo DiCaprio",
    "Jennifer Lawrence",
    "Robert Downey Jr.",
    "Scarlett Johansson",
    "Denzel Washington",
    "Julia Roberts",
    "Johnny Depp",
    "Angelina Jolie",
    "Brad Pitt",
    "Charlize Theron",
    "Will Smith",
    "Natalie Portman",
    "Chris Hemsworth",
    "Emma Watson",
    "Keanu Reeves",
    "Anne Hathaway",
    "Hugh Jackman",
    "Sandra Bullock"
]

sports = [
    "Soccer",
    "Basketball",
    "Tennis",
    "Baseball",
    "Cricket",
    "Golf",
    "Rugby",
    "Swimming",
    "Volleyball",
    "Ice Hockey",
    "Table Tennis",
    "Badminton",
    "Athletics",
    "Cycling",
    "Boxing",
    "Martial Arts",
    "Wrestling",
    "Skiing",
    "Snowboarding",
    "Gymnastics"
]

word_list = [movies, countries, actors_actresses, sports]


selected_category = random.choice(word_list)

if selected_category is movies:
    category_name = "Movies"
elif selected_category is countries:
    category_name = "Countries"
elif selected_category is actors_actresses:
    category_name = "Actors/Actresses"
elif selected_category is sports:
    category_name = "Sports"
