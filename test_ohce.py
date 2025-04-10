from ohce import Ohce
from datetime import datetime

def test_greeting_morning(mocker):
    mocked_datetime = mocker.patch("datetime.datetime")
    mocked_datetime.now.return_value = datetime(2025, 4, 9, 10, 0)  # 10:00
    ohce = Ohce("Pedro")
    assert ohce.greet() == "¡Buenos días Pedro!"