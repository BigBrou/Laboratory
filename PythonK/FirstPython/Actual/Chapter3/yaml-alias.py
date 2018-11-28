import yaml

yaml_str = """
#Definition
color_def:
    -&color1 "#FF0000"
    -&color2 "#00FF00"
    -&color3 "#0000FF"

# Select Color
frame_color:
    title: *color1
    logo : *color2

article_color:
    title: *color2
    back : *color3
"""

data = yaml.load(yaml_str)
print(data["frame_color"]["title"])
#print(data["frame_color"]["title"])
