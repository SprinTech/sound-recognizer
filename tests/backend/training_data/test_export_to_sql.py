import pytest
import sqlite3


class TestExportToSQL:
    @pytest.fixture
    def session(): # 1
        connection = sqlite3.connect(':memory:')
        db_session = connection.cursor()
        db_session.execute('''CREATE TABLE audiofile(genre text, path text)''')
        db_session.connection.commit()
        yield db_session
        connection.close()
        
    def test_build_list(self, tmpdir):
        self.genre = []
        self.path = []
        
        genre_path = tmpdir.mkdir("genre").mkdir("blues").join("blues/001.wav")
        
        assert len(genre_path) == 1

