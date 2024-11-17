def find_common_participants(group1, group2, delimiter=","):

    set1 = set(participant.strip() for participant in group1.split(delimiter))
    set2 = set(participant.strip() for participant in group2.split(delimiter))

    common = set1.intersection(set2)

    return sorted(common)