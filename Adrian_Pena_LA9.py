#--------------------------------------------------------------------------
# IT209_LA9_F23_csv_movies_template.py - Fall 2023 version
#
# This Lab requires that you create a CSV formatted file using data
# in a given Python list, inspect and update it using a text editor,
# read it and placing it in a nested list format, then prompt for
# for a category and display all movie titles in that category.
#
# Specific instructions:
#
# 1.  Read the list of movies given below and write them to
#     file moviesLab9.txt in CSV format:
#       [1939, 'Gone with the Wind', 'drama'] ...
#             is written as "1939,Gone with the Wind,drama"  (w/o quotes)
#       Don't forget the nl control character to separate the lines. 
# 2.  Visually inspect the file using a text editor such as Notepad
#     and add three movies to the end of the file in CSV format:
#         1976, Rocky, drama
#         1997, Titanic, historical
#         2011, The Artist, comedy
# 3.  Read the updated file, split the lines, remove control characters,
#     and create a nested list similar to the one given below
# 4.  Write a while loop to prompt for a category, search the list built 
#     in #4, and display all movie titles in that category.
#
# Gene Shuman     10/21/2023 
#---------------------------------------------------------------------------

movies = [[1939, 'Gone With the Wind', 'drama'],
          [1943, 'Casablanca', 'drama'],
          [1954, 'On the Waterfront', 'drama'],        
          [1957, 'The Bridge on the River Kwai', 'historical'],  
          [1961, 'West Side Story', 'musical'],        
          [1965, 'The Sound of Music', 'musical'],
          [1969, 'Midnight Cowboy', 'drama'],
          [1972, 'The Godfather', 'drama'],
          [1973, 'The Sting', 'comedy'],   
          [1977, 'Annie Hall', 'comedy'],
          [1981, 'Chariots of Fire', 'drama'],
          [1982, 'Gandhi', 'historical'],              
          [1984, 'Amadeus', 'historical'],
          [1986, 'Platoon', 'action'],
          [1988, 'Rain Man', 'drama'],
          [1990, 'Dances with Wolves', 'western'],
          [1991, 'The Silence of the Lambs', 'drama'],  
          [1992, 'Unforgiven', 'western'],
          [1993, 'Schindler s List', 'historical'], 
          [1994, 'Forrest Gump', 'comedy'],
          [1995, 'Braveheart', 'historical'],       
          [1998, 'Shakespeare in Love', 'comedy'],
          [2001, 'A Beautiful Mind', 'historical'],
          [2002, 'Chicago', 'musical'],
          [2009, 'The Hurt Locker', 'action'],
          [2012, 'Argo', 'historical'],
          [2013, '12 Years a Slave', 'drama'],
          [2014, 'Birdman', 'comedy'],
          [2016, 'Moonlight', 'drama'],
          [2017, 'The Shape of Water', 'fantasy'],
          [2018, 'Green Book', 'drama'],               
          [2019, 'Parasite', 'drama'],
          [2020, 'Nomadland', 'drama'],
          [2021, 'CODA', 'drama'],                       
          [2022, 'Everything Everywhere All at Once', 'comedy-drama'] ]  


#1.  Write the list to a moviesLab9.txt in csv format
input('\n1. Hit "Enter" to write the movie list to a file in csv format' )
# ...code goes here...............     
with open('movesLab9.txt', 'w') as f:
    # Write the data from the 'movies' list
    for movie in movies:
        movie_data = ','.join(str(i) for i in movie)
        f.write(movie_data + '\n')


# 2.  Inspect the file just created
print('\n\n\n2. Inspect the csv file just created using a text editor such as Notepad.')
print('Add three new movie records at the end of the file using EXCEL or Notepad: ')
print('1976, Rocky, drama')
print('1997, Titanic, historical')
print('2011, The Artist, comedy')     
print('\nAfter adding, hit "Enter" to continue by reading the file into ')
print(' a nested list similar to the one given, the format: ')
print("[ [1939, 'Gone with the Wind', 'drama'], ")
print("  [1943, 'Casablanca', 'drama'], etc. ")
print('\nKeep the list in sorted order by year ')
input('\n\n"Enter" to continue')
#  ...no code is needed for this step, only manually reading and updating the file


# 3.  Read and print the csv file you just updated
input('\n\n3. "Enter" to read the updated csv format text file and create the movie list ')
#  ...code goes here................
updated_movies = []
with open('movesLab9.txt', 'r') as f:
    for line in f:
        # Split each line into a list and remove the newline character
        movie_data = line.strip().split(',')
        year, title, category = int(movie_data[0]), movie_data[1], movie_data[2]
        updated_movies.append([year, title, category])

# Print the list of movies
print("\nList of Movies:")
for movie in updated_movies:
    print(movie)

# 4.  prompt for a category and display all movie titles in that category
#     Continue prompting for a category until the user signals to quit.
input('\n\n4. "Enter" to begin prompting for a search category \n')
# ...code goes here.................
while True:
    search_category = input("\n4. Enter a category to search for (or 'quit' to exit): ").strip().lower()
    if search_category == 'quit':
        break  # Exit the loop if the user enters 'quit'
    found_movies = []
    for movie in updated_movies:
        if search_category == movie[2].lower():
            found_movies.append(movie[1])  # Add the movie title to the list
    if found_movies:
        print(f"Movies in the '{search_category}' category:")
        for title in found_movies:
            print(title)
    else:
        print(f"No movies found in the '{search_category}' category.")

