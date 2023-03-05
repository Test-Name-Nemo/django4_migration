import json
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from school.models import Teacher, Student


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('school.json', 'r', encoding="utf-8") as f:
            file_content = json.load(f)

            for line in file_content:
                if line["model"] == "school.teacher":
                    new_teacher = Teacher.objects.create(
                        name=line.get("fields").get("name"),
                        subject=line.get("fields").get("name"),
                    )


                elif line["model"] == "school.student":
                    new_student = Student.objects.create(
                        name=line.get("fields").get("name"),
                        Teacher=line.get("fields").get("teacher"),
                        group=line.get("fields").get("group"),

                    )
        pass
