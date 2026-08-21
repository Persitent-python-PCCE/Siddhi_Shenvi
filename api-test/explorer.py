from urllib.request import urlopen
from urllib.parse import quote
from urllib.error import HTTPError, URLError
import json

BASE_URL = "https://api.tvmaze.com"

def get_data(url):
    try:
        response = urlopen(url)

        data = response.read().decode("utf-8")

        return json.loads(data)

    except HTTPError as e:
        print("Error:", e.code)
        print("Requested data was not found.")
        return None

    except URLError as e:
        print("Internet connection error.")
        return None

    except json.JSONDecodeError:
        print("Invalid JSON response.")
        return None

def search_show():

    name = input("Enter TV show name: ")

    url = BASE_URL + "/search/shows?q=" + quote(name)

    data = get_data(url)

    if data is None:
        return

    if len(data) == 0:
        print("No shows found.")
        return

    print("\nSearch Results")
    print("-------------------------")

    for item in data:
        show = item["show"]

        print("ID:", show["id"])
        print("Name:", show["name"])

        if show["language"]:
            print("Language:", show["language"])

        print("-------------------------")

def display_show_details():

    show_id = input("Enter show ID: ")

    url = BASE_URL + "/shows/" + show_id

    data = get_data(url)

    if data is None:
        return

    print("\n========== SHOW DETAILS ==========")

    print("ID:", data["id"])
    print("Name:", data["name"])
    print("Language:", data["language"])
    print("Status:", data["status"])
    print("Premiered:", data["premiered"])
    print("Ended:", data["ended"])
    print("Runtime:", data["runtime"])

    print("Genres:", ", ".join(data["genres"]))

    print("Rating:", data["rating"]["average"])

    print("Official Site:", data["officialSite"])

    print("Summary:")

    summary = data["summary"]

    if summary:
        import re

        summary = re.sub("<.*?>", "", summary)

        print(summary)
    else:
        print("No summary available.")

    print("=================================")


def display_episodes():

    show_id = input("Enter show ID: ")

    url = BASE_URL + "/shows/" + show_id + "/episodes"

    data = get_data(url)

    if data is None:
        return

    print("\n========== EPISODES ==========")

    for episode in data:

        print(
            "S" + str(episode["season"]) +
            " E" + str(episode["number"]) +
            " - " + episode["name"]
        )

        print("Air date:", episode["airdate"])
        print("-----------------------------")

def display_cast():

    show_id = input("Enter show ID: ")

    url = BASE_URL + "/shows/" + show_id + "/cast"

    data = get_data(url)

    if data is None:
        return

    print("\n========== CAST ==========")

    for item in data:

        person = item["person"]
        character = item["character"]

        print("Actor:", person["name"])
        print("Character:", character["name"])

        print("--------------------------")


def find_episode():

    show_id = input("Enter show ID: ")

    season = input("Enter season number: ")

    episode_number = input("Enter episode number: ")

    url = (
        BASE_URL
        + "/shows/"
        + show_id
        + "/episodebynumber?season="
        + season
        + "&number="
        + episode_number
    )

    data = get_data(url)

    if data is None:
        return

    print("\n========== EPISODE ==========")

    print("Name:", data["name"])
    print("Season:", data["season"])
    print("Episode:", data["number"])
    print("Air Date:", data["airdate"])
    print("Air Time:", data["airtime"])
    print("Runtime:", data["runtime"])

    if data["summary"]:

        import re

        summary = re.sub("<.*?>", "", data["summary"])

        print("Summary:", summary)

    print("=============================")


def search_person():

    name = input("Enter person's name: ")

    url = BASE_URL + "/search/people?q=" + quote(name)

    data = get_data(url)

    if data is None:
        return

    if len(data) == 0:
        print("No person found.")
        return

    print("\n========== PEOPLE ==========")

    for item in data:

        person = item["person"]

        print("ID:", person["id"])
        print("Name:", person["name"])
        print("Gender:", person["gender"])

        if person["country"]:
            print("Country:", person["country"]["name"])

        print("----------------------------")



def similar_shows():

    show_id = input("Enter show ID: ")

    show_url = BASE_URL + "/shows/" + show_id

    show = get_data(show_url)

    if show is None:
        return

    genres = show["genres"]

    if len(genres) == 0:
        print("This show has no genres.")
        return

    shows_url = BASE_URL + "/shows?page=0"

    all_shows = get_data(shows_url)

    if all_shows is None:
        return

    similar = []

    for other_show in all_shows:

        if other_show["id"] == show["id"]:
            continue

        other_genres = other_show["genres"]

        common_genres = 0

        for genre in genres:
            if genre in other_genres:
                common_genres += 1

        if common_genres > 0:

            similar.append(
                (
                    common_genres,
                    other_show
                )
            )

    similar.sort(
        key=lambda x: x[0],
        reverse=True
    )

    print("\n========== SIMILAR SHOWS ==========")

    if len(similar) == 0:
        print("No similar shows found.")
        return

    count = 0

    for common_genres, other_show in similar:

        print("Name:", other_show["name"])
        print("Genres:", ", ".join(other_show["genres"]))
        print("Common Genres:", common_genres)

        print("----------------------------------")

        count += 1

        if count == 10:
            break


def schedule():

    country = input(
        "Enter country code (example: US, IN, GB): "
    )

    date = input(
        "Enter date (YYYY-MM-DD): "
    )

    url = (
        BASE_URL
        + "/schedule?country="
        + quote(country)
        + "&date="
        + quote(date)
    )

    data = get_data(url)

    if data is None:
        return

    if len(data) == 0:
        print("No episodes scheduled.")
        return

    print("\n========== SCHEDULE ==========")

    for item in data:

        show = item["show"]
        episode = item["name"]

        print("Show:", show["name"])
        print("Episode:", episode)
        print("Time:", item["airtime"])

        print("------------------------------")


def main():

    while True:

        print("\n")
        print("======================TV SHOW EXPLORER======================")

        print("1. Search TV Show")
        print("2. Display Show Details")
        print("3. Display Episodes")
        print("4. Display Cast")
        print("5. Find Episode by Season/Number")
        print("6. Search Person")
        print("7. Similar Shows")
        print("8. Schedule")
        print("9. Exit")

        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            search_show()

        elif choice == "2":
            display_show_details()

        elif choice == "3":
            display_episodes()

        elif choice == "4":
            display_cast()

        elif choice == "5":
            find_episode()

        elif choice == "6":
            search_person()

        elif choice == "7":
            similar_shows()

        elif choice == "8":
            schedule()

        elif choice == "9":
            print("Thank you for using TV Show Explorer!")
            break

        else:
            print("Invalid choice. Please enter 1-9.")


if __name__ == "__main__":
    main()