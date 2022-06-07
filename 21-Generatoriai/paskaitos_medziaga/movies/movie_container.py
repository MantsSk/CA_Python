from typing import Sequence


class MP4Movie:
    def __init__(self, src_path):
        self.dst_path = src_path.split('.')[0] + '.mp4'
        with open(src_path, mode='rb') as file:  # b is important -> binary
            self.content = file.read()


class MovieContainer:
    def __init__(self, movie_files: Sequence[str]):
        self.movie_files = movie_files

    # Will crash with out of memory

    #def get_files(self) -> Sequence[MP4Movie]:
    #    files = []
    #    for src_path in self.movie_files:
    #        files.append(MP4Movie(src_path))
    #    return files

    def get_files(self) -> Sequence[MP4Movie]:
        for src_path in self.movie_files:
            yield MP4Movie(src_path)
