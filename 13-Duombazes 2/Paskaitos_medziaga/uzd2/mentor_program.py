from typing import Sequence

from db_init import session
from mentor import Mentor
from worker import Worker


def add_worker(name, surname, position):
    session.add(Worker(name, last_name=surname, position=position))
    session.commit()


def set_mentor(mentor_id: int, student_id: int):
    session.add(Mentor(mentor_id, student_id))
    session.commit()


def get_mentor_info(mentor_name, mentor_surname) -> Sequence[dict]:
    
    # Issitraukti is duomenu bazes ir uzpildyti
    return [{
        'mentor_name': mentor_name,
        'mentor_surname': mentor_surname,
        'student_name': student_name,
        'student_surname': student_surname,
        'student_position': student_position
    }]
