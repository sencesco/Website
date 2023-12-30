import requests
from bs4 import BeautifulSoup
import time

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_archieve_page = response.text

soup = BeautifulSoup(web_archieve_page, 'html.parser')

# This list start first idex  with movies number 100 and last index is movies number 1
movie_list_unsorted = [ movies.getText() for movies in soup.find_all(name='h3', class_="title")]

#------------------Solution1-------------------------------------------
# Record the start time
start_time_1 = time.time()
# Start append from number movies number 1 by list slice
movies = movie_list_unsorted[::-1]
with open("movies_revest_list_slice.txt", "w", encoding='utf-8')  as file:
  for movie_name in movies:
    file.write(f"{movie_name}\n")
  # Record the end time
  end_time_1 = time.time()
  # Calculate the elapsed time
  elapsed_time = end_time_1 - start_time_1
  # Record time in file
  file.write(f"Elapsed time: {elapsed_time} seconds")
  # Print the elapsed time
  print(f"Elapsed time: {elapsed_time} seconds")    # Elapsed time: 0.0019683837890625 seconds
  
#------------------Solution2-------------------------------------------
start_time_2 = time.time() 
with open("movies_revert_list.pop().txt", "w", encoding='utf-8')  as file:
  for movies in range(len(movie_list_unsorted)):
    text = movie_list_unsorted.pop()
    file.write(f"{text}\n")
  end_time_2 = time.time()
  elapsed_time = end_time_2 - start_time_2
  file.write(f"Elapsed time: {elapsed_time} seconds")
  print(f"Elapsed time: {elapsed_time} seconds")    # Elapsed time: 0.00099945068359375 seconds

""""Solution2 is better in this case, Becuae we not actually need to revese a list,
    we just need sort oreder and write in file.
    
    Why Solution2 is better than Solution1, Becuase 2 is pop elements from the original list one by one, 
    which doesn't create an additional copy of the list
    
"""

  
