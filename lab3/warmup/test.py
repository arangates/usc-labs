# Import the pandas library.
import pandas

# Read in the data.
games = pandas.read_csv("board_games.csv")
# Print the names of the columns in games.
print(games.columns)