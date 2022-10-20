import csv

from config import CSV_ROUTE
from sqlalchemy.orm import Session

from . import models


def create_school_code(db: Session):
    csv_data = open(CSV_ROUTE, "r")
    csv_reader = csv.reader(csv_data)
    school_list = list()
    for line in csv_reader:
        if line[1] == "code":
            continue
        db_school = models.SchoolCode(code=line[1], regulator=line[2], type=line[3])
        db.add(db_school)
        db.commit()
        school_list.append(db_school.code)
    return school_list
