"""
距離は全てメートル[m]に換算
時間は全て秒[sec]に換算
"""

import sys
from typing import List, Final

FIRST_MONEY: Final[int] = 410
FIRST_DISTANCE: Final[int] = 1052

NORMAL_MONEY: Final[int] = 80
NORMAL_DISTANCE: Final[int] = 237

def parse_inputs (lines: List['str']) -> List[List[int]]:

    times_sec = [0] * len(lines)
    distances_meter = [0] * len(lines)

    for i, line in enumerate(lines):
        time, distance = line.split()
        hour, minute, sec = time.split(':')

        times_sec[i] = float(hour) * 60 * 60 + float(minute) * 60 + float(sec)
        distances_meter[i] = float(distance)

    return times_sec, distances_meter

def calc_money (times_sec: List[float], distances_meter: List[float]) -> int:

    money = 0

    distance_all = 0

    for distance in distances_meter:
        distance_all += distance

    if distance_all <= FIRST_DISTANCE:
        money += FIRST_MONEY
    else:
        money += FIRST_MONEY + int((distance_all - FIRST_DISTANCE) / NORMAL_DISTANCE) * NORMAL_MONEY

    return money

def main(lines: List['str']) -> None:

    # 入力のデータ形式を調整
    times_sec, distances_meter = parse_inputs(lines)

    # 料金を計算
    result = calc_money(times_sec, distances_meter)

    print(result)

    return

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
    sys.exit(0)
