

import requests
from datetime import datetime, timedelta 
from config.env_variables import GITHUB_API_URL,USERNAME,TOKEN

## Improvements
# Send daily mail with the streak count 
# Send more information like commit info project name timestamp etc.

def fetch_github_events(username):
    events_url = f"{GITHUB_API_URL}/users/{username}/events/public"
    headers = {'Authorization' : f'token {TOKEN}'}
    response = requests.get(events_url, headers=headers)
    if response.status_code == 200 :
        print("Able to connect to github")
        return response.json() # Returns event data as a JSON List
    else:
        print("Failed to fetch events data: ", response.status_code)
        return []

events = fetch_github_events(USERNAME)
## print(events)


# Function to process events and calculate streaks 

def calculate_streak(events): 
    contributions = []

    # Extract only the dates of contributions
    for event in events :
        if 'created_at' in events: 
            contribution_date = event['created_at'][:10] # Extract date (YYYY-MM-DD)
            contributions.append(contribution_date)

    # Sort the dates in ascending order 
    contributions = sorted(set(contributions))

    # Calculate streaks 
    streaks = []
    current_streak = 1

    for i in range(1, len(contributions)) :
        current_date = datetime.strftime(contributions[i],"%Y-%m-%d")
        previous_date = datetime.strftime(contributions[i - 1],"%Y-%m-%d")
        if current_date - previous_date == timedelta(days=1) :
            current_streak += 1 
        else :
            streaks.append(current_streak)
            current_streak = 1

    # Append the last streak 
    streaks.append(current_streak)

    return streaks

# Calculate streaks from the fetched events 
streaks = calculate_streak(events)

# Print the streaks 
print("User's Streak (in Days ): " , streaks) 