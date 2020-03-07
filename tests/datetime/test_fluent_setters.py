from datetime import datetime

import pendulum

from ..conftest import assert_datetime


def test_fluid_year_setter():
    d = pendulum.now()
    new = d.set(year=1995)
    assert isinstance(new, datetime)
    assert 1995 == new.year
    assert d.year != new.year


def test_fluid_month_setter():
    d = pendulum.datetime(2016, 7, 2, 0, 41, 20)
    new = d.set(month=11)
    assert isinstance(new, datetime)
    assert 11 == new.month
    assert 7 == d.month


def test_fluid_day_setter():
    d = pendulum.datetime(2016, 7, 2, 0, 41, 20)
    new = d.set(day=9)
    assert isinstance(new, datetime)
    assert 9 == new.day
    assert 2 == d.day


def test_fluid_hour_setter():
    d = pendulum.datetime(2016, 7, 2, 0, 41, 20)
    new = d.set(hour=5)
    assert isinstance(new, datetime)
    assert 5 == new.hour
    assert 0 == d.hour


def test_fluid_minute_setter():
    d = pendulum.datetime(2016, 7, 2, 0, 41, 20)
    new = d.set(minute=32)
    assert isinstance(new, datetime)
    assert 32 == new.minute
    assert 41 == d.minute


def test_fluid_second_setter():
    d = pendulum.datetime(2016, 7, 2, 0, 41, 20)
    new = d.set(second=49)
    assert isinstance(new, datetime)
    assert 49 == new.second
    assert 20 == d.second


def test_fluid_microsecond_setter():
    d = pendulum.datetime(2016, 7, 2, 0, 41, 20, 123456)
    new = d.set(microsecond=987654)
    assert isinstance(new, datetime)
    assert 987654 == new.microsecond
    assert 123456 == d.microsecond


def test_fluid_setter_keeps_timezone():
    d = pendulum.datetime(2016, 7, 2, 0, 41, 20, 123456, tz="Europe/Paris")
    new = d.set(microsecond=987654)
    assert_datetime(new, 2016, 7, 2, 0, 41, 20, 987654)


def test_fluid_timezone_setter():
    d = pendulum.datetime(2016, 7, 2, 0, 41, 20)
    new = d.set(tz="Europe/Paris")
    assert isinstance(new, datetime)
    assert "Europe/Paris" == new.timezone_name
    assert "Europe/Paris" == new.tzinfo.name


def test_fluid_on():
    d = pendulum.datetime(2016, 7, 2, 0, 41, 20)
    new = d.on(1995, 11, 9)
    assert isinstance(new, datetime)
    assert 1995 == new.year
    assert 11 == new.month
    assert 9 == new.day
    assert 2016 == d.year
    assert 7 == d.month
    assert 2 == d.day


def test_fluid_on_with_transition():
    d = pendulum.datetime(2013, 3, 31, 0, 0, 0, 0, tz="Europe/Paris")
    new = d.on(2013, 4, 1)
    assert isinstance(new, datetime)
    assert 2013 == new.year
    assert 4 == new.month
    assert 1 == new.day
    assert 7200 == new.offset
    assert 2013 == d.year
    assert 3 == d.month
    assert 31 == d.day
    assert 3600 == d.offset


def test_fluid_at():
    d = pendulum.datetime(2016, 7, 2, 0, 41, 20)
    new = d.at(5, 32, 49, 123456)
    assert isinstance(new, datetime)
    assert 5 == new.hour
    assert 32 == new.minute
    assert 49 == new.second
    assert 0 == d.microsecond
    assert 0 == d.hour
    assert 41 == d.minute
    assert 20 == d.second
    assert 123456 == new.microsecond


def test_fluid_at_partial():
    d = pendulum.datetime(2016, 7, 2, 0, 41, 20)
    new = d.at(10)

    assert_datetime(new, 2016, 7, 2, 10, 0, 0, 0)

    new = d.at(10, 30)

    assert_datetime(new, 2016, 7, 2, 10, 30, 0, 0)

    new = d.at(10, 30, 45)

    assert_datetime(new, 2016, 7, 2, 10, 30, 45, 0)


def test_fluid_at_with_transition():
    d = pendulum.datetime(2013, 3, 31, 0, 0, 0, 0, tz="Europe/Paris")
    new = d.at(2, 30, 0)
    assert isinstance(new, datetime)
    assert 3 == new.hour
    assert 30 == new.minute
    assert 0 == new.second


def test_replace_tzinfo():
    d = pendulum.datetime(2016, 7, 2, 0, 41, 20)
    new = d.replace(tzinfo=pendulum.timezone("Europe/Paris"))

    assert new.timezone_name == "Europe/Paris"


def test_replace_tzinfo_dst():
    d = pendulum.datetime(2013, 3, 31, 2, 30)
    new = d.replace(tzinfo=pendulum.timezone("Europe/Paris"))

    assert_datetime(new, 2013, 3, 31, 3, 30)
    assert new.is_dst()
    assert new.offset == 7200
    assert new.timezone_name == "Europe/Paris"
