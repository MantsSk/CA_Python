import os
from typing import Sequence

from movie_container import MovieContainer


def convert_to_mp4(movie_list: Sequence[str]):
    movies = MovieContainer(movie_list)
    for movie in movies.get_files():
        with os.open(movie.dst_path, 'w') as file:
            file.write(to_mp4(movie.content))
