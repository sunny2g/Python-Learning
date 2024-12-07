


from datetime import datetime, timedelta 
from config.env_variables import USERNAME
from include.func_file import fetch_github_events, calculate_streak
import json

## Improvements
# Send daily mail with the streak count 
# Send more information like commit info project name timestamp etc.

# fetch_github_events fuction will try to connect with github and login 
events = fetch_github_events(USERNAME)

## Added the code to save json data in file.
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_path = f"data/github_{current_datetime}.json"
with open(file_path, 'w') as file:
    json.dump(events, file, indent=4) 
    print(f"Data has been written to {file_path}")



# Calculate streaks from the fetched events 
streaks = calculate_streak(events)

# Print the streaks 
print("User's Streak (in Days ): " , streaks) 

# Adding Mailing functionality
# SMTP server settings for Gmail
subject = "Github_Streak_Mails"
body = f"User's Streak (in Days ): {streaks}"
from include.func_file import mail_user
mail_user(streaks,subject,body)

