from pydantic import BaseModel


class NotificationSchema(BaseModel):
    subject: str
    message: str

    def generate_message(self) -> str:
        return self.subject + "\n" + self.message
