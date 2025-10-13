from sqlalchemy.orm import validates

from app.data.models.league import League
from app.data.models.conference import Conference
from app.data.models.division import Division
from app.data.sqla import sqla


class Season(sqla.Model):
    """
    Model to represent a pro football season.
    """
    __tablename__ = 'season'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True, nullable=False)
    year = sqla.Column(sqla.SmallInteger, unique=True, nullable=False)
    num_of_weeks_scheduled = sqla.Column(sqla.SmallInteger, nullable=False, default=0)
    num_of_weeks_completed = sqla.Column(sqla.SmallInteger, nullable=False, default=0)

    leagues_first_season_of = sqla.relationship('League', foreign_keys=[League.first_season_id])
    leagues_last_season_of = sqla.relationship('League', foreign_keys=[League.last_season_id])
    conferences_first_season_of = sqla.relationship('Conference', foreign_keys=[Conference.first_season_id])
    conferences_last_season_of = sqla.relationship('Conference', foreign_keys=[Conference.last_season_id])
    divisions_first_season_of = sqla.relationship('Division', foreign_keys=[Division.first_season_id])
    divisions_last_season_of = sqla.relationship('Division', foreign_keys=[Division.last_season_id])

    games = sqla.relationship('Game', lazy=True)

    @validates('year')
    def validate_not_empty(self, key, value):
        if not value and value != 0:
            raise ValueError(f"{key.capitalize()} is required.")

        if key == 'year':
            self.validate_is_unique(
                key, value, error_message=f"Row with {key}={value} already exists in the Season table."
            )

        return value

    def validate_is_unique(self, key, value, error_message=None):
        if Season.query.filter_by(**{key: value}).first() is not None:
            if not error_message:
                error_message = f"{key} must be unique."

            raise ValueError(error_message)
