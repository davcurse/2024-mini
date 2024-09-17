# Exercise: Response time measurement and cloud upload

The LED blinks at random intervals.
The exercise_game.py script measures response time.

## Questions

1. Edit the exercise_game.py code to compute average, minimum, maximum response time for 10 flashes total.
2. Upload the response time data to a cloud service of your choice.

The response to these questions is your unique code and results in Report.md in your team's forked GitHub repository.

## Methods and Results

After importing the urequests and network libraries in lines 9 and 10, the Raspberry Pi can connect to Firebase through these
libraries, it does that specificly at the added command:
urequests.post("https://ec463-mini-project-10f0f-default-rtdb.firebaseio.com/data.json", data=json.dumps(data))
This command was added at line 69 of the code file exercise_game.py
This setup allows us to store the data we collect after each successful run of the code.
