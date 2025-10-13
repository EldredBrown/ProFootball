from sqlalchemy.orm import validates

from app.data.sqla import sqla


class Division(sqla.Model):
    """
    Class to represent a pro football division.
    """
    __tablename__ = 'division'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = sqla.Column(sqla.String(50), unique=True, nullable=False)
    league_id = sqla.Column(sqla.String(5), sqla.ForeignKey('league.id'), nullable=False)
    conference_id = sqla.Column(sqla.String(5), sqla.ForeignKey('conference.id'), nullable=False)
    first_season_id = sqla.Column(sqla.SmallInteger, sqla.ForeignKey('season.id'), nullable=False)
    last_season_id = sqla.Column(sqla.SmallInteger, sqla.ForeignKey('season.id'), nullable=True)

    team_seasons = sqla.relationship('TeamSeason', cascade='save-update, delete, delete-orphan, merge')

    @validates('name', 'league_id', 'conference_id', 'first_season_id')
    def validate_not_empty(self, key, value):
        if not value and value != 0:
            raise ValueError(f"{key} is required.")

        if key in ('name', 'league_id', 'conference_id'):
            self.validate_is_unique(
                key, value, error_message=f"Row with {key}={value} already exists in the Division table."
            )
        return value

    def validate_is_unique(self, key, value, error_message=None):
        if Division.query.filter_by(**{key: value}).first() is not None:
            if not error_message:
                error_message = f"{key} must be unique."
            raise ValueError(error_message)
