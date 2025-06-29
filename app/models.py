from . import db

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    start_time = db.Column(db.String(20), nullable=False)  # Format: YYYY-MM-DD HH:MM
    end_time = db.Column(db.String(20), nullable=False)
    recurrence = db.Column(db.String(10), nullable=True)  # daily, weekly, monthly, or None

    def to_dict(self):
        """Convert Event object to dictionary for JSON response."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "recurrence": self.recurrence
        }
