def outed(meet, boss):
    total = sum(meet.values()) + meet[boss]
    num = len(meet)
    average = total / num
    
    if average <= 5:
        return 'Get Out Now!'
    else:
        return 'Nice Work Champ!'