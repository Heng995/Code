states = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
stations = {
    "kone": {"id", "nv", "ut"},
    "ktwo": {"wa", "id", "mt"},
    "kthree": {"or", "nv", "ca"},
    "kfour": {"nv", "ut"},
    "kfive": {"ca", "az"},
}
final_staions = set()

while states:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states -= states_covered
    final_staions.add(best_station)
print(final_staions)