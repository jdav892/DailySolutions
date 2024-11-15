def who_is_online(friends):
    new_dict = {'online': [], 'offline': [], 'away': []}
    
    for friend in friends:
        if friend['status'] == 'offline':
            new_dict['offline'].append(friend['username'])
        elif friend['status'] == 'online':
            if friend['last_activity'] > 10:
                new_dict['away'].append(friend['username'])
            else:
                new_dict['online'].append(friend['username'])
    
    return {key: value for key, value in new_dict.items() if value}

            