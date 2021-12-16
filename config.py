config = {
    "layers" : [
        {
            "name": "Base",
            "values": ["Orange", "Yellow", "Green", "Blue"], # If you want the name of the attribute to be different than the filename change this list. Else keep them the same.
            "path": "\\Layers\\Layer1\\",
            "filename": ["Orange", "Yellow", "Green", "Blue"],
            "weights": [25, 25, 25, 25]
        },
        {
            "name": "Shape",
            "values": ["Square", "Heart", "Triangle"],
            "path": "\\Layers\\Layer2\\",
            "filename": ["Square", "Heart", "Triangle"],
            "weights": [30, 30, 40]
        },
        {
            "name": "Squiggle",
            "values": ["SQ1", "SQ2", "SQ3"],
            "path": "\\Layers\\Layer3\\",
            "filename": ["SQ1", "SQ2", "SQ3"],
            "weights": [30, 30, 40]
        },
        {
            "name": "Inspirational-message",
            "values": ["Live", "Laugh", "Love"],
            "path": "\\Layers\\Layer4\\",
            "filename": ["Live", "Laugh", "Love"],
            "weights": [30, 30, 40]
        }
    ]
}