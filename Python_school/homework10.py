states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
stations = {
    "one": {"id", "nv", "ut"},
    "two": {"wa", "id", "mt"},
    "three": {"or", "nv", "ca"},
    "four": {"nv", "ut"},
    "five": {"ca", "az"},
}
final_staions = set()
while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_staions.add(best_station)
print(final_staions)