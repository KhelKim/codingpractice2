import datetime
from dateutil.parser import parse


def parser(log):
    date, complete_time, process_time = log.split()
    hour, minute, seconds = complete_time.split(":")
    process_time = process_time[:-1]  # remove "s"
    return date, (hour, minute, seconds), process_time


def get_interval(parsed_log):
    base = parse('0001-01-01')

    date, (hour, minute, seconds), process_time = parsed_log

    # date
    date_str = f"{date} {hour}:{minute}"
    date_datetime = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    time_delta = date_datetime - base
    date_seconds = int(time_delta.total_seconds() * 1000)

    # second, process_time
    seconds = int(float(seconds) * 1000)
    process_time = int(float(process_time) * 1000)

    end = date_seconds + seconds
    start = end - process_time + 1

    return start, end


def solution(lines):
    check_points = []
    intervals = []
    for log in lines:
        parsed_log = parser(log)
        start, end = get_interval(parsed_log)

        check_points.append(start)
        check_points.append(end)
        intervals.append((start, end))

    max_count = 0
    for point in check_points:
        count = 0
        start_point = point
        end_point = point + 1000
        for start, end in intervals:
            if start_point <= start < end_point or \
                    start_point <= end < end_point:
                count += 1
            elif start < start_point and end_point < end:
                count += 1
        if max_count < count:
            max_count = count
    return max_count


if __name__ == "__main__":
    lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]

    print(solution(lines))
