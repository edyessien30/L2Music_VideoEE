from logic.Conference import Conference

if __name__ == '__main__':
    all_teams, all_conferences = Conference.read_data()
    print()
    print("All Teams")
    for team in all_teams:
        print(team)
    print("All Conferences")
    for conference in all_conferences:
        print(conference)
