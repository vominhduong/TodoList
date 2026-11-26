from datetime import datetime, timezone

from app import db

STATUS_PENDING = "pending"
STATUS_COMPLETED = "completed"
TITLE_MAX_LENGTH = 100


def utc_now():
    return datetime.now(timezone.utc)


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(TITLE_MAX_LENGTH), nullable=False)
    status = db.Column(db.String(20), nullable=False, default=STATUS_PENDING)
    # Truyền hàm (không gọi) để mỗi task nhận thời gian tạo riêng
    created_at = db.Column(db.DateTime, nullable=False, default=utc_now)

    @property
    def is_completed(self):
        return self.status == STATUS_COMPLETED

    def toggle(self):
        self.status = STATUS_PENDING if self.is_completed else STATUS_COMPLETED

    def __repr__(self):
        return f"<Task {self.id} {self.title!r} {self.status}>"
