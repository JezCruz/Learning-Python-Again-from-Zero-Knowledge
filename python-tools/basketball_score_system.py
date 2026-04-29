team1 = input("Enter the name of Team 1: ")
team2 = input("Enter the name of Team 2: ")

score = {
    team1: 0,
    team2: 0
}

fouls = {
    team1: 0,
    team2: 0
}


def add_points(team, points):
    score[team] += points
    print(f"{team} scored {points} points!")


def add_foul(team):
    fouls[team] += 1
    print(f"Foul added to {team}!")


def show_score():
    print("\n============= SCOREBOARD =============")
    print(f"{team1}: {score[team1]} points, {fouls[team1]} fouls")
    print(f"{team2}: {score[team2]} points, {fouls[team2]} fouls")
    print("=====================================\n")


def declare_winner():
    if score[team1] > score[team2]:
        print(f"{team1} wins!")
    elif score[team2] > score[team1]:
        print(f"{team2} wins!")
    else:
        print("It's a tie!")
    show_score()


def main():
    while True:
        print("1. Add points")
        print("2. Add foul")
        print("3. Show score")
        print("4. Declare winner and exit")
        choice = input("Choose an option: ")

        if choice == '1':
            team = input("Enter the team name: ")
            points = int(input("Enter the points to add (1, 2, or 3): "))
            if team in score and points in [1, 2, 3]:
                add_points(team, points)
            else:
                print("Invalid team name or points.")
        elif choice == '2':
            team = input("Enter the team name: ")
            if team in fouls:
                add_foul(team)
            else:
                print("Invalid team name.")
        elif choice == '3':
            show_score()
        elif choice == '4':
            declare_winner()
            break
        else:
            print("Invalid option. Please try again.")

main()