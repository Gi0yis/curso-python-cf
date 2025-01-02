# zip

users = ["User1", "User2", "User3"]
courses = ("Python", "Django", "Rails")
scores = [10, 8, 7]

# Se agrupan por indices
# response = list(zip(users, courses, scores))
response = tuple(zip(users, courses, scores))

print(response)