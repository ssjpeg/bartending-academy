from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

quiz_answers = [
    {
        "id": "1",
        "answer": "Measuring Alcohol"
    },
    {
        "id": "2",
        "answer": "Mashing Ingredients"
    },
    {
        "id": "3",
        "answer": ["https://www.dolivotastingbar.com/wp-content/uploads/2019/05/manzanilla-olives.jpg",
                    "https://d1h1synnevvfsx.cloudfront.net/pub/media/catalog/product/cache/ebc6733575d5c8d1cd0f057bf2f42791/2/0/2020_10_09_5409.jpg",
                    "https://cdn.shopify.com/s/files/1/0013/2477/7569/products/aag_960x.jpg?v=1597696572"]
    },
    {
        "id": "4",
        "answer": ["Add gin, lemon juice, syrup, and egg white to a shaker and vigorously dry-shake (without ice) for 15 seconds.",
                    "Add 3 ice cubes and shake vigorously until well-chilled.",
                    "Double-strain into a chilled Collins glass",
                    "Add club soda."]
    },
    {
        "id": "5",
        "answer": "Mixing Drinks"
    }
]
data = [
    {
        "id": "1",
        "question": "What is this tool used for?",
        "image": "https://static.restaurantsupply.com/media/catalog/product/cache/58705eee992a0d7bab305099af29f9ee/a/m/american-metalcraft-j202_1_1.jpg",
        "options": ["Mixing Drinks", "Measuring Alcohol", "Peeling Ingredients", "Straining Drinks"],
        "hint": "This tool is called a 'jigger'"
    },
    {
        "id": "2",
        "question": "What is this tool used for?",
        "image": "https://m.media-amazon.com/images/I/51JwNh0iftL._AC_SL1400_.jpg",
        "options": ["Mashing Ingredients", "Measuring Alcohol", "Peeling Ingredients", "Straining Drinks"],
        "hint": "This tool is called a 'muddler'"
    },
    {
         "id": "3",
        "question": "What do you need to make a Martini?",
        "image": "https://3f4c2184e060ce99111b-f8c0985c8cb63a71df5cb7fd729edcab.ssl.cf2.rackcdn.com/media/16258/vodkamartini.jpg",
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
        "image": "https://www.liquor.com/thmb/ER6DAmPfS6RSQo3S4XkopdRpMv0=/720x720/smart/filters:no_upscale()/gin-fizz-720x720-primary-v3-2c1390963d014e35a01d741df2f9ae77.jpg",
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
    global quiz_answers
    return render_template('homepage.html', data=data, quiz_answers=quiz_answers)

@app.route('/quiz/<id>', methods=['GET', 'POST'])
def quiz(id):
    quiz_id = data[int(id)]
    return render_template('quiz.html', quiz_id=quiz_id, data=data)

if __name__ == '__main__':
   app.run(debug = True)

