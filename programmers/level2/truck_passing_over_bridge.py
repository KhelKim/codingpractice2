from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)

    # bridge init
    time = 1
    current_weight = truck_weights[0]
    trucks_on_bridge = deque([[1, truck_weights.popleft()]])  # truck's enter time & weight

    while truck_weights:
        time += 1

        front_truck_time, front_truck_weight = trucks_on_bridge[0]
        front_truck_location = time - front_truck_time

        if bridge_length <= front_truck_location:
            trucks_on_bridge.popleft()
            current_weight -= front_truck_weight

        waiting_truck_weight = truck_weights[0]

        if current_weight + waiting_truck_weight <= weight:
            current_weight += waiting_truck_weight
            trucks_on_bridge.append([time, waiting_truck_weight])
            truck_weights.popleft()

        # print(time)
        # print(truck_weights)
        # print(trucks_on_bridge)
        # print()
    time += bridge_length  # last truck time
    return time


if __name__ == "__main__":
    bridge_length, weight, truck_weights = 2, 10, [7, 4, 5, 6]
    print(solution(bridge_length, weight, truck_weights))