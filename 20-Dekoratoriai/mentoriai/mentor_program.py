from functools import wraps
from typing import Sequence

from db_init import init_session, close_session
from mentor import Mentor
from worker import Worker


# Naudojamas be dekoratoriaus
def handle_session(fnc, *args, **kwargs):
    session = init_session()
    fnc(session, *args, **kwargs)
    session.commit()
    close_session()


# Dekoratorius
def session_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        session = init_session()
        temp = func(session, *args, **kwargs)
        session.commit()
        close_session()
        return temp

    return wrapper


@session_decorator
def add_worker(session, name, surname, position):
    """
    Adds a new worker
    :param session:
    :param name:
    :param surname:
    :param position:
    :return:
    """
    session.add(Worker(name, last_name=surname, position=position))


@session_decorator
def set_mentor(session, mentor_id: int, student_id: int):
    session.add(Mentor(mentor_id, student_id))


@session_decorator
def get_mentor_info(session, mentor_name, mentor_surname) -> Sequence[dict]:
    mentor = session.query(Worker).filter(Worker.name == mentor_name).filter(
            Worker.last_name == mentor_surname).all()[0]
    mentor_id = mentor.id
    mentorships = session.query(Mentor).filter(Mentor.mentor_id == mentor_id).all()

    student_list = [_get_student_by_id(session, mentorship.student_id) for mentorship in
                    mentorships]
    results = [_form_results_from_student_and_mentor(student, mentor) for student in student_list]

    return results


def _get_student_by_id(session, id):
    return session.query(Worker).filter(Worker.id == id).first()


def _form_results_from_student_and_mentor(student, mentor):
    return {
        'mentor_name': mentor.name,
        'mentor_surname': mentor.last_name,
        'student_name': student.name,
        'student_surname': student.last_name,
        'student_position': student.position
    }
