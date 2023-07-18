

# A cricket game that people can play in Python

# Import random module
import random

# Define the teams
team_a = input("Enter the name of team A: ")
team_b = input("Enter the name of team B: ")

# Define the overs
overs = int(input("Enter the number of overs: "))

# Define the score variables
score_a = 0
score_b = 0
wickets_a = 0
wickets_b = 0

# Define the possible outcomes of a ball
outcomes = [0, 1, 2, 3, 4, 6, "W"]

# Define a function to simulate an over
def over(batting_team, bowling_team, score, wickets):
# Print the over details
print(f"{batting_team} is batting against {bowling_team}.")
print(f"Score: {score}-{wickets}")
# Loop through the six balls of the over
for i in range(1, 7):
# Print the ball number
print(f"Ball {i}: ", end="")
# Ask the player to choose an outcome
outcome = input(f"Choose one of {outcomes}: ")
# Validate the input
while outcome not in outcomes:
print("Invalid input. Try again.")
outcome = input(f"Choose one of {outcomes}: ")
# Check if the outcome is a wicket
if outcome == "W":
# Increment the wickets by one
wickets += 1
# Print that the batsman is out
print("OUT!")
# Check if the batting team is all out
if wickets == 10:
# Print that the innings is over
print(f"{batting_team} is all out.")
# Return the final score and wickets
return score, wickets
else:
# Convert the outcome to an integer
outcome = int(outcome)
# Increment the score by the outcome
score += outcome
# Print the outcome
print(outcome)
# Print the over summary
print(f"End of over. Score: {score}-{wickets}")
# Return the score and wickets after the over
return score, wickets

# Simulate the first innings
print(f"Welcome to the {overs}-over cricket match between {team_a} and {team_b}.")
print(f"{team_a} has won the toss and elected to bat first.")
# Loop through the overs of the first innings
for i in range(overs):
# Call the over function and update the score and wickets for team A
score_a, wickets_a = over(team_a, team_b, score_a, wickets_a)
# Check if team A is all out
if wickets_a == 10:
# Break out of the loop
break

# Print the first innings summary
print(f"End of first innings. {team_a} has scored {score_a}-{wickets_a} in {overs} overs.")

# Simulate the second innings
print(f"{team_b} needs {score_a + 1} runs to win in {overs} overs.")
# Loop through the overs of the second innings
for i in range(overs):
# Call the over function and update the score and wickets for team B
score_b, wickets_b = over(team_b, team_a, score_b, wickets_b)
# Check if team B has reached or exceeded the target
if score_b >= score_a + 1:
# Print that team B has won and break out of the loop
print(f"{team_b} has won by {10 - wickets_b} wickets.")
break
# Check if team B is all out or has run out of overs
if wickets_b == 10 or i == overs - 1:
# Print that team A has won and break out of the loop
print(f"{team_a} has won by {score_a - score_b} runs.")
break

# Print the second innings summary
print(f"End of second innings. {team_b} has scored {score_b}-{wickets_b} in {overs} overs.")

