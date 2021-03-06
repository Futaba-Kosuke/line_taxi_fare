"""
距離は全てメートル[m]に換算
時間は全て秒[sec]に換算
"""

import sys
from typing import List, Final

# 1052[m] まで 410[円]
FIRST_MONEY: Final[int] = 410
FIRST_DISTANCE: Final[int] = 1052

# 237[m] ごとに 80[円]
NORMAL_MONEY: Final[int] = 80
NORMAL_DISTANCE: Final[int] = 237

# 10[km/h] 以下なら 90[秒] ごとに 80[円]
SLOW_SPEED: Final[int] = 10 * 1e3
SLOW_SPEED_TIME: Final[int] = 1 * 60 + 30
SLOW_SPEED_MONEY: Final[int] = 80

# 入力を整形
def parse_inputs (lines: List['str']) -> List[List[int]]:

    times_sec = [0] * len(lines)
    distances_meter = [0] * len(lines)

    for i, line in enumerate(lines):
        time, distance = line.split()
        hour, minute, sec = time.split(':')

        if float(hour) > 99 or float(minute) > 60 or float(sec) > 60:
            raise Exception("Doesn't fit the time's constraints.")

        times_sec[i] = float(hour) * 60 * 60 + float(minute) * 60 + float(sec)
        distances_meter[i] = float(distance)

    return times_sec, distances_meter

# 深夜か否か判定
# 通常 - 深夜を跨ぐ場合でも深夜時間帯に走っていた距離が不明となるため、区間の始めと終わりが深夜区間に含まれている場合のみ深夜で判定
def is_midnight (t_begin_sec: int, t_end_sec: int) -> bool:
    return (
            int((t_begin_sec % (24*60*60))/(60*60)) < 5 or 22 <= int((t_begin_sec % (24*60*60))/(60*60))
        ) and (
            int((t_end_sec% (24*60*60))/(60*60)) < 5 or 22 <= int((t_end_sec % (24*60*60))/(60*60))
        )

def calc_money (times_sec: List[float], distances_meter: List[float]) -> int:

    money = 0

    distance_all = 0
    slow_times_all = 0

    # 距離計算
    for i, distance in enumerate(distances_meter):
        if i == 0:
            continue
        elif is_midnight(times_sec[i - 1], times_sec[i]):
            distance_all += distance * 1.25
        else:
            distance_all += distance

    # 低速時間計算
    for i in range(len(times_sec) - 1):
        if distances_meter[i + 1] / (times_sec[i + 1] - times_sec[i]) * 60 * 60 <= SLOW_SPEED:
            if is_midnight(times_sec[i], times_sec[i + 1]):
                slow_times_all += (times_sec[i + 1] - times_sec[i]) * 1.25
            else:
                slow_times_all += (times_sec[i + 1] - times_sec[i])

    # 料金計算
    if distance_all <= FIRST_DISTANCE:
        money += FIRST_MONEY
    else:
        money += FIRST_MONEY + int((distance_all - FIRST_DISTANCE) / NORMAL_DISTANCE) * NORMAL_MONEY

    money += int(slow_times_all / SLOW_SPEED_TIME) * SLOW_SPEED_MONEY

    return money

def main(lines: List['str']) -> None:

    # 入力のデータ形式を調整
    try:
        times_sec, distances_meter = parse_inputs(lines)
    except:
        sys.exit(1)

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
