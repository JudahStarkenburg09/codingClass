def create_teams():
    players = []
    
    # Get player information until "]go[" is entered
    while True:
        name = input("Enter player name (type ']go[' to stop): ")
        if name.lower() == "]go[":
            break

        skill_level = int(input("Enter skill level (1-10) for {}: ".format(name)))
        gender = input("Enter gender (M/F) for {}: ".format(name))
        
        players.append({'name': name, 'skill_level': skill_level, 'gender': gender})

    # Get the number of teams
    num_teams = int(input("Enter the number of teams: "))

    # Sort players by skill level
    players.sort(key=lambda x: x['skill_level'])

    # Divide players into teams based on skill level and gender
    teams = [[] for _ in range(num_teams)]
    for i, player in enumerate(players):
        team_index = i % num_teams
        teams[team_index].append(player)

    # Output the teams
    for i, team in enumerate(teams, 1):
        team_skills = [player['skill_level'] for player in team]
        team_genders = [player['gender'] for player in team]
        avg_skill = sum(team_skills) / len(team) if team else 0

        print("\nTeam {}: ".format(i))
        print("Average Skill Level: {:.2f}".format(avg_skill))
        print("Players: {}".format(", ".join([player['name'] for player in team])))
        print("Genders: {}".format(", ".join(team_genders)))

if __name__ == "__main__":
    create_teams()
