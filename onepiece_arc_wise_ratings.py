import matplotlib.pyplot as plt

arcs = [
    "East Blue", "Alabasta", "Skypiea", "Water 7",
    "Thriller Bark", "Marineford", "Fishman Island",
    "Dressrosa", "Whole Cake", "Wano"
]

years = [
    1999, 2001, 2003, 2005,
    2007, 2009, 2011,
    2014, 2017, 2019
]

ratings = [
    8.1, 8.4, 7.8, 9.0,
    8.2, 9.4, 7.6,
    8.7, 8.9, 9.5
]


plt.plot(years, ratings, marker='o', color='red', label='One Piece Ratings')

for i in range(len(arcs)):
    plt.text(years[i], ratings[i]+0.1, arcs[i], rotation=45, ha='right')

plt.xlabel("Year")
plt.ylabel("Rating")
plt.title("One Piece Arc Ratings Over Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
