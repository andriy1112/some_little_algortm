states_neded = set(['mt','wa','or','id','nv','ut','ca','cz'])

stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

final_stations = set()
while states_neded:
    best_station = None
    started_cover = set()
    for station, states in stations.items():
        covered = states_neded & states
        if len(covered) > len(started_cover):
            best_station = stations
            started_cover = covered
    states_neded -= started_cover
final_stations.add(best_station)

print(final_stations)