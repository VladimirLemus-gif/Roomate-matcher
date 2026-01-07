#Roomate_matcher

# Students stored in list as dictionary for clarity and easy scaling
students = [
{'name':'Vladimir', 'year': 'year 1', 'sport': 'basketball', 'music':'R&B'},
 {'name':'Mazin', 'year':'year 1', 'sport': 'soccer', 'music':'Rap'},
 {'name':'Max', 'year': 'year 2', 'sport': 'basketball', 'music':'R&B'},
 {'name':'Eddie', 'year': 'year 1', 'sport': 'basketball', 'music':'R&B'},
 {'name':'Nebi', 'year': 'year 2', 'sport':'soccer', 'music':'Rap'},
 {'name':'Brayan', 'year':'year 1', 'sport':'football', 'music':'Rap'},
 {'name':'Adrianna', 'year':'year 1', 'sport':'soccer', 'music':'R&B'},
 {'name':'Perla', 'year':'year 1', 'sport':'football', 'music':'R&B'},
 {'name':'triss', 'year':'year 1', 'sport':'basketball', 'music':'Rap'},
 {'name':'Amare', 'year':'year 1', 'sport':'basketball', 'music':'R&B'},]



def match(student, students):
    """Matches students with others based on shared preferences. Returns ranked list of potential roommates"""

    matches = []
    for other in students:
        if other ['name'] == student ['name']:
            continue  #avoidng self matching

        score = 0
        if other ['year'] == student ['year']:
            score += 1
        if other ['sport'] == student ['sport']:
            score += 2
        if other ['music'] == student ['music']:
            score += 1
        matches.append({'name': other['name'], 'score':score})

    return sorted(matches, key=lambda x: x['score'], reverse=True) #sorts matches from highest to lowest based on score


target_student = students[3]
results = match(target_student, students)

for r in results:
    print(f"{r['name']} - compatibility score: {r['score']}")




