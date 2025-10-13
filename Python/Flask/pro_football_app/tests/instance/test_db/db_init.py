import sqlite3


def init_db():
    db_abs_path = 'D:\\Source\\Repos\\ProFootball\\Python\\Flask\\pro_football_app\\tests\\instance\\test_db\\test_db.sqlite3'
    conn = sqlite3.connect(db_abs_path)
    c = conn.cursor()

    # --------------------------------------------------
    # Dropping existing tables
    # --------------------------------------------------
    c.execute("DROP TABLE IF EXISTS TeamSeason")
    c.execute("DROP TABLE IF EXISTS LeagueSeason")
    c.execute("DROP TABLE IF EXISTS Game")
    c.execute("DROP TABLE IF EXISTS Team")
    c.execute("DROP TABLE IF EXISTS Division")
    c.execute("DROP TABLE IF EXISTS Conference")
    c.execute("DROP TABLE IF EXISTS League")
    c.execute("DROP TABLE IF EXISTS Season")

    # --------------------------------------------------
    # Creating all tables
    # --------------------------------------------------

    # Creating table 'Season'
    c.execute(
        '''
        CREATE TABLE Season (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            year INTEGER UNIQUE NOT NULL,
            num_of_weeks_scheduled INTEGER NOT NULL DEFAULT 0,
            num_of_weeks_completed INTEGER NOT NULL DEFAULT 0
        )
        '''
    )

    # Creating table 'League'
    c.execute(
        '''
        CREATE TABLE League (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            short_name TEXT UNIQUE NOT NULL,
            long_name TEXT UNIQUE NOT NULL,
            first_season_id INTEGER NOT NULL,
            last_season_id INTEGER NULL,
            FOREIGN KEY (first_season_id) REFERENCES Season(id),
            FOREIGN KEY (last_season_id) REFERENCES Season(id)
        )
        '''
    )

    # Creating table 'Conference'
    c.execute(
        '''
        CREATE TABLE Conference (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            short_name TEXT UNIQUE NOT NULL,
            long_name TEXT UNIQUE NOT NULL,
            league_id INTEGER UNIQUE NOT NULL,
            first_season_id INTEGER NOT NULL,
            last_season_id INTEGER NULL,
            FOREIGN KEY (league_id) REFERENCES League(id),
            FOREIGN KEY (first_season_id) REFERENCES Season(id),
            FOREIGN KEY (last_season_id) REFERENCES Season(id)
        )
        '''
    )

    # Creating table 'Division'
    c.execute(
        '''
        CREATE TABLE Division (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT UNIQUE NOT NULL,
            league_id INTEGER NOT NULL,
            conference_id INTEGER NOT NULL,
            first_season_id INTEGER NOT NULL,
            last_season_id INTEGER NULL,
            FOREIGN KEY (league_id) REFERENCES League(id),
            FOREIGN KEY (conference_id) REFERENCES Conference(id),
            FOREIGN KEY (first_season_id) REFERENCES Season(id),
            FOREIGN KEY (last_season_id) REFERENCES Season(id)
        )
        '''
    )

    # Creating table 'Team'
    c.execute(
        '''
        CREATE TABLE Team (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT UNIQUE NOT NULL
        )
        '''
    )

    # Creating table 'Game'
    c.execute(
        '''
        CREATE TABLE Game (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            season_id INTEGER NOT NULL,
            week INTEGER NOT NULL,
            guest_name TEXT NOT NULL,
            guest_score INTEGER NOT NULL DEFAULT 0,
            host_name TEXT NOT NULL,
            host_score INTEGER NOT NULL DEFAULT 0,
            winner_name TEXT,
            winner_score INTEGER,
            loser_name TEXT,
            loser_score INTEGER,
            is_playoff INTEGER NOT NULL DEFAULT 0,
            notes varchar(256),
            FOREIGN KEY (season_id) REFERENCES Season(id)
        )
        '''
    )

    # Creating table 'LeagueSeason'
    c.execute(
        '''
        CREATE TABLE LeagueSeason (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            league_id INTEGER NOT NULL,
            season_id INTEGER NOT NULL,
            total_games INTEGER NOT NULL DEFAULT 0,
            total_points INTEGER NOT NULL DEFAULT 0,
            average_points REAL,
            FOREIGN KEY (league_id) REFERENCES League(id),
            FOREIGN KEY (season_id) REFERENCES Season(id)
        )
        '''
    )

    # Creating table 'TeamSeason'
    c.execute(
        '''
        CREATE TABLE TeamSeason (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            team_id INTEGER NOT NULL,
            season_id INTEGER NOT NULL,
            league_id INTEGER NOT NULL,
            conference_id INTEGER,
            division_id INTEGER,
            games INTEGER NOT NULL DEFAULT 0,
            wins INTEGER NOT NULL DEFAULT 0,
            losses INTEGER NOT NULL DEFAULT 0,
            ties INTEGER NOT NULL DEFAULT 0,
            winning_percentage REAL,
            points_for INTEGER NOT NULL DEFAULT 0,
            points_against INTEGER NOT NULL DEFAULT 0,
            expected_wins float NOT NULL DEFAULT 0,
            expected_losses float NOT NULL DEFAULT 0,
            offensive_average REAL,
            offensive_factor REAL,
            offensive_index REAL,
            defensive_average REAL,
            defensive_factor REAL,
            defensive_index REAL,
            final_expected_winning_percentage REAL,
            FOREIGN KEY (team_id) REFERENCES Team(id),
            FOREIGN KEY (season_id) REFERENCES Season(id),
            FOREIGN KEY (league_id) REFERENCES League(id),
            FOREIGN KEY (conference_id) REFERENCES Conference(id),
            FOREIGN KEY (division_id) REFERENCES Division(id)
        )
        '''
    )

    # --------------------------------------------------
    # Script has ended
    # --------------------------------------------------

    conn.commit()
    conn.close()

    print("Database is created and initialized.")


if __name__ == '__main__':
    init_db()
