import secrets
from pathlib import Path

from PIL import Image


def save_picture(root_path, form_picture) -> str:
    file_name = _rename_picture(form_picture.filename)

    picture_path = Path(root_path, 'static/avatars', file_name)

    picture = _resize_picture(form_picture)
    picture.save(picture_path)

    return str(picture_path.name)


def _rename_picture(original_name: str) -> str:
    random_string = secrets.token_urlsafe(8)
    picture_suffix = Path(original_name).suffix
    return random_string + picture_suffix


def _resize_picture(picture_file):
    output_size = (125, 125)
    i = Image.open(picture_file)
    i.thumbnail(output_size)
    return i
