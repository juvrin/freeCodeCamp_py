def image_search(images, term):
    result = []
    for i in images:
        name, format = i.split(".")
        if term.upper() in name.upper() or term.upper() in format.upper():
            result.append(i)
    return result


test = image_search(["Sunset.jpg", "Beach.png", "sunflower.jpeg"], "sun")
print(test)

test2 = image_search(
    ["Moon.png", "sun.jpeg", "stars.png"], "PNG"
)  # should return ["Moon.png", "stars.png"]
print(test2)
