import enum


class GradeRequestType(str, enum.Enum):
    entering = "entering"
    tested = "tested"
    completed = "completed"
    department_interview = "department_interview"
    tech_lead_interview = "tech_lead_interview"

