import requests
url = "https://www.hko.gov.hk/tide/CLKtextPH2020.htm"
response = requests.get(url)
if (response.ok):
    print("Data is ready!")
else:
    print(response.status_code)
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime

# aggregate data
monthly_data = [
    (2024, 1, 6.5), (2024, 2, 6.5), (2024, 3, 24.5), (2024, 4, 319.5),
    (2024, 5, 380.5), (2024, 6, 225.5), (2024, 7, 366.5), (2024, 8, 197.5)
]

# Month and rainfall
months = [datetime(year, month, 1) for year, month, value in monthly_data]
values = [value for year, month, value in monthly_data]

# Create graphs and subgraphs
fig, ax = plt.subplots()
line, = ax.plot(months, values, 'b-', marker='o')
ax.set_xlim(months[0], months[-1])
ax.set_ylim(0, max(values) + 50)
ax.set_xlabel('month')
ax.set_ylabel('Rainfall (mm)')
ax.set_title('Total monthly rainfall in Kai Tak Area in 2024')

# Animation update function
def update(num, months, values, line):
    line.set_data(months[:num], values[:num])
    return line,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(months), fargs=[months, values, line], interval=500, blit=True)

# Save GIF
ani.save('monthly_rainfall_animation.gif', writer='imagemagick')

# Show giFs
plt.show()