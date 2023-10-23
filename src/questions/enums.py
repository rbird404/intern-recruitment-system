import enum


class QuestionType(str, enum.Enum):
    text = "text"
    code = "code"
    # TODO add types
    # select = "select"
    # block = "block"
