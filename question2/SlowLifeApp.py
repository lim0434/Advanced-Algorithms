from UDGraph import UDGraph
from Person import Person

class SlowLife:
    def __init__(self):
        self.my_graph = UDGraph()
        self.profiles = []

    def add_new_profile(self, name, biography, gender, privacy="public"):
        person = Person(name, biography, gender, privacy)
        self.my_graph.add_vertex(person)
        self.profiles.append(person)
        return person

    def add_follow(self, follower, following):
        self.my_graph.add_edge(follower, following)

def display_profile_names(app_instance):
    print("\nView All Profile Names:")
    print("=======================")
    for i, person in enumerate(app_instance.profiles, 1):
        print(f"{i}.) {person.get_name()}")

def view_profile_details(app_instance):
    print("\nView Details for Any Profile:")
    print("===========================")
    display_profile_names(app_instance)
    try:
        max_num = len(app_instance.profiles)
        choice = int(input(f"\nSelect whose profile to view (1 - {max_num}): "))
        if 1 <= choice <= max_num:
            person = app_instance.profiles[choice - 1]

            print(f"\nName: {person.get_name()}")
            print(f"Gender: {person.gender}")
            print(f"Biography: {person.biography}")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def view_followed_accounts(app_instance):
    print("\nView Followed Accounts for Any Profile:")
    print("=======================================")
    display_profile_names(app_instance)
    try:
        max_num = len(app_instance.profiles)
        choice = int(input(f"\nSelect whose profile to view following list (1 - {max_num}): "))
        if 1 <= choice <= max_num:
            person = app_instance.profiles[choice - 1]
            following_list = app_instance.my_graph.get_following_list(person)

            print(f"\nFollowing list:")
            if following_list:
                for followed in following_list:
                    print(f"- {followed.get_name()}")
            else:
                print("This user is not following anyone.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def view_followers(app_instance):
    print("\nView Followers for Any Profile:")
    print("=============================")
    display_profile_names(app_instance)
    try:
        max_num = len(app_instance.profiles)
        choice = int(input(f"\nSelect whose profile to view followers (1 - {max_num}): "))
        if 1 <= choice <= max_num:
            person = app_instance.profiles[choice - 1]
            followers_list = app_instance.my_graph.get_followers_list(person)

            print(f"\nFollowers list:")
            if followers_list:
                for follower in followers_list:
                    print(f"- {follower.get_name()}")
            else:
                print("This user has no followers.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def add_user_on_demand(app_instance):
    print("\nAdd New User Profile On-Demand:")
    print("===============================")
    name = input("Enter the new user's name: ").strip()
    biography = input("Enter their biography: ").strip()
    gender = input("Enter their gender: ").strip()

    for p in app_instance.profiles:
        if p.get_name().lower() == name.lower():
            print(f"Error: A user named '{name}' already exists.")
            return

    app_instance.add_new_profile(name, biography, gender)
    print(f"\nSuccess! User '{name}' has been added to Slow Life.")

def main():
    gram = SlowLife()

    katie = gram.add_new_profile("Katie", "Just a normal person", "Female")
    susan = gram.add_new_profile("Susan", "This profile is private.", "Female", privacy="private")
    justin = gram.add_new_profile("Justin", "Just an ordinary manager", "Male")
    chris = gram.add_new_profile("Chris", "Just an ordinary kid", "Male")
    alan = gram.add_new_profile("Alan", "Just a hardworking man", "Male")

    gram.add_follow(katie, susan)
    gram.add_follow(katie, justin)
    gram.add_follow(katie, alan)
    gram.add_follow(alan, katie)
    gram.add_follow(alan, chris)
    gram.add_follow(justin, susan)

    while True:
        print("\nWelcome to Slow Life, Your New Social Media App:")
        print("*" * 50)
        print("1. View names of all profiles")
        print("2. View Details for any profile")
        print("3. View followers of any profile")
        print("4. View followed accounts of any profile")
        print("5. Add a user profile on-demand")
        print("6. Quit")
        print("*" * 50)
        choice = input("Enter your choice (1 - 6): ")

        if choice == '1':
            display_profile_names(gram)
        elif choice == '2':
            view_profile_details(gram)
        elif choice == '3':
            view_followers(gram)
        elif choice == '4':
            view_followed_accounts(gram)
        elif choice == '5':
            add_user_on_demand(gram)
        elif choice == '6':
            print("Exiting Slow Life. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()