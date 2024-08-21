def title_case(title, minor_words=''):
    new = []
    new_minor = [word.lower() for word in minor_words.split(' ')]
    
    if not len(title):
        return title
    
    for index, word in enumerate(title.split(' ')):
        if index == 0:
            new.append(word.title())
            continue
        
        if word.lower() in new_minor:
            new.append(word.lower())
            continue
        
        new.append(word.title())
        
    return ' '.join(new)

#def title_case(title, minor_words=''):
# title = title.capitalize().split()
# minor_words = minor_words.lower().split()
# return ' '.join([word if word in minor_words else word.capitalize() for word in title])