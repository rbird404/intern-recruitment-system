import enum


class QuestionType(str, enum.Enum):
    text = "text"
    code = "code"
