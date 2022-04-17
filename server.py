from dataclasses import dataclass
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

quiz = [
    {
        "id": "1",
        "question": "What is this tool used for?",
        "image": "https://static.restaurantsupply.com/media/catalog/product/cache/58705eee992a0d7bab305099af29f9ee/a/m/american-metalcraft-j202_1_1.jpg",
        "answer": "Measuring Alcohol",
        "options": ["Mixing Drinks", "Measuring Alcohol", "Peeling Ingredients", "Straining Drinks"],
        "hint": "This tool is called a 'jigger'"
    },
    {
        "id": "2",
        "question": "What is this tool used for?",
        "image": "https://m.media-amazon.com/images/I/51JwNh0iftL._AC_SL1400_.jpg",
        "answer": "Mashing Ingredients",
        "options": ["Mashing Ingredients", "Measuring Alcohol", "Peeling Ingredients", "Straining Drinks"],
        "hint": "This tool is called a 'muddler'"
    },
    {
         "id": "3",
        "question": "What do you need to make a Martini?",
        "options": ["https://www.dolivotastingbar.com/wp-content/uploads/2019/05/manzanilla-olives.jpg",
                    "https://www.absolut.com/globalassets/images/products/absolut-vodka/atlas/atlas_absolut-vodka_1000ml_4x.jpg",
                    "https://theaustralianfoodshop.com/wp-content/uploads/2021/03/bundaberg-ginger-beer-375ml.jpeg",
                    "https://i5.walmartimages.com/asr/9890d72f-c487-42d9-afac-5f1c03c442ff_1.75f6a1d66a12e7d7a4b76f8ea6b47380.jpeg",
                    "https://media.istockphoto.com/photos/slice-of-orange-picture-id185311615?k=20&m=185311615&s=612x612&w=0&h=XRDJ5CC9Irit4uPVLxBkFVK_hZJcGXg4HpAbTKwvTgU=",
                    "https://d1h1synnevvfsx.cloudfront.net/pub/media/catalog/product/cache/ebc6733575d5c8d1cd0f057bf2f42791/2/0/2020_10_09_5409.jpg",
                    "https://products3.imgix.drizly.com/ci-patron-silver-25fa130a809ea038.jpeg?auto=format%2Ccompress&ch=Width%2CDPR&fm=jpg&q=20",
                    "https://www.meijer.com/content/dam/meijer/product/0004/12/5010/20/0004125010200_2_A1C1_1200.png",
                    "https://solidstarts.com/wp-content/uploads/when-can-babies-eat-eggs.jpg",
                    "https://cdn.shopify.com/s/files/1/0013/2477/7569/products/aag_960x.jpg?v=1597696572"],
        "hint": ""
    },
    {
        "id": "4",
        "question": "What is the procedure for making a Gin Fizz?",
        "options": ["Put sugar and water into a small saucepan on low heat and sit until the sugar dissolves.",
                    "Place Lime-salt-sugar on rim of glass.",
                    "Add gin, lemon juice, syrup, and egg white to a shaker and vigorously dry-shake (without ice) for 15 seconds.",
                    "Double-strain into a chilled Collins glass",
                    "Add club soda.",
                    "Stir with a bar spoon and strain into the chilled martini glass.",
                    "Garnish with a fresh olive",
                    "Add 3 ice cubes and shake vigorously until well-chilled."]
    },
    {                                                                                                                                                            
        "id": "5",
        "question": "What is this tool used for?",
        "image": "https://m.media-amazon.com/images/I/61xmg-8MuuL._AC_SL1500_.jpg",
        "answer": "Mixing Drinks",
        "options": ["Mixing Drinks",
                    "Measuring Alcohol",
                    "Peeling Ingredients",
                    "Straining Drinks"],
        "hint": "This tool is called a 'Bar Spoon'"
    },
]

@app.route('/')
def homepage():
    global data
    return render_template('homepage.html', data=data)

@app.route('/quiz/<id')
def quiz(id):
    global data
    global quiz

    id=int(id)

    return render_template('quiz.html', quiz_index=id)

if __name__ == '__main__':
   app.run(debug = True)

