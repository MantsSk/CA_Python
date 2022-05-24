from typing import Sequence


def add_worker(name, surname, position):
    pass


def set_mentor(mentor_id: int, student_id: int):
    pass


def get_mentor_info(mentor_name, mentor_surname) -> Sequence[dict]:
    # Issitraukti is duomenu bazes ir uzpildyti
    return [{
        'mentor_name': mentor_name,
        'mentor_surname': mentor_surname,
        'student_name': student_name,
        'student_surname': student_surname,
        'student_position': student_position
    }]
