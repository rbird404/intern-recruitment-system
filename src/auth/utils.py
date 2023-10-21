import enum


class UserRoleType(str, enum.Enum):
    candidate = "Candidate"
    tech_lead = "TechLead"
    hr = "HR"
