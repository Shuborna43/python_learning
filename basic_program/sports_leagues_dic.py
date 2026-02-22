sports_leagues = {
"NFL": "National Football League (American football)",
"MLB": "Major League Baseball (Baseball)",
"NBA": "National Basketball Association (Basketball)",
"EPL": "Premier League (Association football)",
"NHL": "National Hockey League (Ice hockey)",
"MLS": "Major League Soccer (Association football)",
"IPL": "Indian Premier League (Twenty20 cricket)",
"AFL": "Australian Football League (Australian rules football)",
"NRL": "National Rugby League (Rugby league football)",
"CFL": "Canadian Football League (Canadian football)"
}


def delete_league(key):
    global sports_leagues
    upper_key = key.upper()
    if upper_key in sports_leagues:
        value = sports_leagues[upper_key]
        sports_leagues.pop(upper_key)
        print(f"The {value} has been removed")
    else:
         print(f"There is no league named {upper_key}")

delete_league("nFl")
print(sports_leagues)

def add_league():
    global sports_leagues
    input_key = input("please enter a key:  ")
    input_value = input("please enter a value:  ")
    upper_input_key = input_key.upper()
    if upper_input_key not in sports_leagues:
        sports_leagues[upper_input_key] = input_value
        print(f"Added {input_key}:{input_value}")
        print(sports_leagues)
    else:
        print(f"Error-{input_key}:{input_value} is already in the dictionary")
add_league()

def get_abbreviations():
    global sports_leagues
    return list(sports_leagues.keys())
print(get_abbreviations())



def get_league_descriptions():
    global sports_leagues
    return tuple(sports_leagues.values())
print(get_league_descriptions())


def get_league_abbreviations_and_descriptions():
    global sports_leagues
    all_items = set(sports_leagues.keys())|set(sports_leagues.values())
    return all_items 
print(get_league_abbreviations_and_descriptions())