def to_dict_list(airports, labels):
    dict_list = []
    for airport in airports:
        dict_list.append({labels[0]: airport[0],
            labels[0]: airport[0],
            labels[1]: airport[1],
            labels[2]: airport[2],
            labels[3]: airport[3],
            labels[4]: airport[4],
            labels[5]: airport[5],
            labels[6]: airport[6],
            labels[7]: airport[7],
            labels[8]: airport[8],
            labels[9]: airport[9],
            labels[10]: airport[10],
            labels[11]: airport[11],})
    return dict_list