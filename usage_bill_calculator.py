from datetime import timedelta
from enum import Enum


class Shows(Enum):
  GAME_OF_THRONES = 1
  WESTWORLD = 2
  VEEP = 3


COST_PER_HOUR = {
  Shows.GAME_OF_THRONES: 5,
  Shows.WESTWORLD: 3.6,
  Shows.VEEP: 1.2
}


class UsageBillCalculator:

  def __init__(self) -> None:
    self._consumption = {
      Shows.GAME_OF_THRONES: timedelta(seconds=0),
      Shows.WESTWORLD: timedelta(seconds=0),
      Shows.VEEP: timedelta(seconds=0),
    }

  def add_view_time(self, show: Shows, view_time: timedelta) -> None:
    self._consumption[show] += view_time

  def total_bill(self) -> float:
    total_bill = 0
    for media_type, duration in self._consumption.items():
      hours_consumed = duration.total_seconds() / 3600
      total_bill += hours_consumed * COST_PER_HOUR[media_type]
