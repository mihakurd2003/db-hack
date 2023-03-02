import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from argparse import ArgumentParser
import random
from datacenter.models import Schoolkid, Lesson, Commendation, Mark, Chastisement


PRAISE_WORDS = [
    'Молодец!', 'Отлично!', 'Гораздо лучше, чем я ожидал!',
    'Очень хороший ответ!', 'С каждым разом у тебя получается всё лучше!',
]


def get_student(name):
    try:
        return Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько совпадений с именем '{name}'")
    except Schoolkid.DoesNotExist:
        print(f"С именем '{name}' ничего не найдено")


def fix_marks(name):
    student = get_student(name)
    Mark.objects.filter(schoolkid__full_name=student.full_name, points__lt=4).update(points=5)


def remove_chastisements(name):
    student = get_student(name)
    chastisements = Chastisement.objects.filter(schoolkid__full_name=student.full_name)
    chastisements.delete()


def create_commendation(name, subject):
    try:
        student = get_student(name)
        lesson = Lesson.objects.filter(
            group_letter__contains=student.group_letter,
            year_of_study=student.year_of_study,
            subject__title=subject,
        ).order_by('-date').first()

        Commendation.objects.create(
            text=random.choice(PRAISE_WORDS),
            created=lesson.date,
            subject=lesson.subject,
            schoolkid=student,
            teacher=lesson.teacher
        )

    except AttributeError:
        print(f"В базе данных не нашлось урока '{subject}'")


def main():
    arg_parse = ArgumentParser(description='Выбор нужной функции и добавление аргументов к ней')
    arg_parse.add_argument('-U', '--fix_marks', default='',  help='Функция исправления оценок')
    arg_parse.add_argument('-D', '--remove_chastisements', default='', help='Функция удаления плохих замечаний')
    arg_parse.add_argument('-A', '--create_commendation', default='', help='Функция добавления похвальных замечаний')
    args = arg_parse.parse_args()

    if args.fix_marks:
        fix_marks(args.fix_marks)
    if args.remove_chastisements:
        remove_chastisements(args.remove_chastisements)
    if args.create_commendation:
        args = [arg.strip() for arg in args.create_commendation.split(',')]
        create_commendation(args[0], args[1])


if __name__ == '__main__':
    main()
