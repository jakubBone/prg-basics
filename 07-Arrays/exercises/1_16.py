# A program that sorts data with the built-in function sorted().
# sorted() returns a new sorted list and does not change the original one,
# while the bubble sort from 1_15.py changes the list in place.

# Sort the data from lowest to highest value
distances_traveled = [120, 150, 180, 90, 200, 175, 160]
print(sorted(distances_traveled))

# Sort the data in descending order, from highest to lowest value
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
# reverse=True changes the order to descending
print(sorted(daily_temperatures, reverse=True))

# Sort the data in ascending order (texts are sorted alphabetically)
file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
              "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]
print(sorted(file_names))
