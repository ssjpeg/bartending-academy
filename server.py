from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

lesson_tools = {
    "1":{
        "id": "1",
        "name": "JIGGER",
        "description": "A jigger is an hourglass-shaped measuring tool that allows for bartenders to pour accurate amounts of alcohol into every drink. They are usually made of metal and contain two different measuring amounts on the top and bottom.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSX-qPeY0JspE5s3MyRNcI_-Gslmb8yMRCE_w&usqp=CAU",
        "video": "https://images.huffingtonpost.com/2015-09-24-1443125482-6520074-02whippedcreamcocktailshaker-thumb.gif",     
    },
    "2":{
        "id": "2",
        "name": "BAR SPOON",
        "description": "A bar spoon is a long-handled spoon used to stir drinks and to serve as a jigger alternative when necessary. One Bar Spoon is equivalent to 5mL. It is long to ensure that it can reach the bottom of a jug.",
        "image": "https://cdn.shopify.com/s/files/1/0096/0276/0755/products/bp-red-knob-bar-spoon-web-800_700x700.jpg?v=1568655343",
        "video": "https://i.pinimg.com/originals/18/aa/07/18aa070fe3bcc47301aab954eecf75e2.gif",     
    },
    "3":{
        "id": "3",
        "name": "SHAKER",
        "description": "A cocktail shaker is used to mix drinks. The shaker has three pieces: a metal base, a top, and a cap in the top which fits over a built-in strainer. The cap is removed, the ingredients are poured in, the shaker is capped and shaken briskly, and the drink is poured through the strainer.",
        "image": "https://m.media-amazon.com/images/I/51ERQMFQBaL._AC_SX425_.jpg",
        "video": "https://c.tenor.com/9ObzC4ISif4AAAAC/bartender-shake.gif",     
    },
    "4":{
        "id": "4",
        "name": "PEELER",
        "description": "Peelers allow for bartenders to readily peel fruit or vegetables in order to augment the flavor profile of their drinks. These devices must be highly portable and fast working.",
        "image": "https://i5.walmartimages.com/asr/261eb067-0166-456a-969c-a363880644a9_1.fc7b4a4695f342210a0761d6820b7506.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF",
        "video": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Benutzung_eines_Kartoffelsch%C3%A4ler.gif/220px-Benutzung_eines_Kartoffelsch%C3%A4ler.gif",     
    },
    "5":{
        "id": "5",
        "name": "MUDDLER",
        "description": "Muddlers are used to mash fresh ingredients and infuse the flavors with the alcohol. The Muddler material (wooden/steel/plastic) have an impact on the mashing ability.",
        "image": "https://www.ubuy.co.id/productimg/?image=aHR0cHM6Ly9tLm1lZGlhLWFtYXpvbi5jb20vaW1hZ2VzL0kvNjFjRjFNYk9nT0wuX0FDX1NMMTUwMF8uanBn.jpg",
        "video": "https://complex-res.cloudinary.com/image/upload/db12ngcvomggllbofhuy.gif",     
    },
}

lesson_recipes = {
    "1":{
        "id": "1",
        "name": "MARTINI",
        "purpose": "NYC Evening Bar Visits",
        "ingredients": ["2 oz Gin", "Green Olive", "Vermouth"],
        "steps": ["Add vermouth to a glass, swish around, pour out.",
                    "In a separate mixing glass full of ice, add gin.",
                    "Stir with bar spoon and strain into chilled martini glass.",
                    "Garnish with a fresh olive."
                ],
        "image": "https://bevvyco.s3.amazonaws.com/img/drinks/cq/wcq/gibson-47d7b654b091d531cab0742cff386314-lg.jpg",
    },
    "2":{
        "id": "2",
        "name": "GIN FIZZ",
        "purpose": "Celebatory Drink for Big Events",
        "ingredients": ["2 oz Gin", "1 oz Lemon Juice", "3/4 oz Simple Syrup", "Egg White", "1 oz Club Soda"],
        "steps": ["Add gin, lemon juice, syrup, and egg white to a shaker and vigorously dry-shake (without ice) for 15 seconds.",
                    "Add 3 ice cubes and shake vigorously until well-chilled.",
                    "Double-strain into a chilled Collins glass.", 
                    "Add club soda to the glass."
                ],
        "image": "https://i.pinimg.com/originals/26/cb/a2/26cba2cc8a60a146fd955d950dab3467.jpg",
    },
    "3":{
        "id": "3",
        "name": "TEQUILA SUNRISE",
        "purpose": "Hot Brunch Days",
        "ingredients": ["1 oz Tequila", "3/4 cup Orange Juice", "Grenadine Syrup", "Orange", "Cherry"],
        "steps": ["Add Tequila and OJ to a shaker and shake.",
                    "Fill a chilled 12 oz glass with ice cubes and add the mixture mixture.",
                    "Add Grenadine", 
                    "Garnish with a slice of orange and a maraschino cherry."
                ],
        "image": "https://www.averiecooks.com/wp-content/uploads/2015/08/tequilasunrise-16.jpg",
    },
    "4":{
        "id": "4",
        "name": "MARGARITA",
        "purpose": "A Casual, Healthy Drink",
        "ingredients": ["2 oz Blanqo Tequila", "1/2 oz Orange Liquer", "1 oz Lime Juice", "1/2 oz Agave Syrup", "Lime Wheel", "Kosher Salt"],
        "steps": ["Add tequila, orange liqueur, lime juice and agave syrup to a cocktail shaker filled with ice.",
                    "Shake until well-chilled."
                    "Strain into a rocks glass over fresh ice.",
                    "Garnish with a lime wheel and kosher salt rim."
                ],
        "image": "https://www.seriouseats.com/thmb/PIVqgfUtdn74p6KurPXlrNwlxKs=/1125x1125/smart/filters:no_upscale()/__opt__aboutcom__coeus__resources__content_migration__serious_eats__seriouseats.com__recipes__images__2015__04__20150323-cocktails-vicky-wasik-margarita-c84b154e757d43688de15dc8f8ca0de9.jpg",
    },
    "5":{
        "id": "5",
        "name": "MOJITO",
        "purpose": "Warm Summer Evenings",
        "ingredients": ["3 Mint Leaves", "1/2 oz Simple Syrup", "2 oz White Rum", "3/4 oz Lime Juice", "Club Soda", "Mint Sprig", "Lime Wheel"],
        "steps": ["Lightly muddle the mint with the simple syrup in a shaker.",
                    "Add the rum, lime juice and ice, and give it a brief shake.",
                    "Strain into a highball glass over fresh ice.", 
                    "Top with the club soda and garnish with a mint sprig and lime wheel."
                ],
        "image": "https://cdn.loveandlemons.com/wp-content/uploads/2020/07/mojito.jpg",
    },


}
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
data_answers = [
    {
        "id": "1",
        "options": ["Mixing Drinks", "Measuring Alcohol", "Peeling Ingredients", "Straining Drinks"]
    },
    {
        "id": "2",
        "options": ["Mashing Ingredients", "Measuring Alcohol", "Peeling Ingredients", "Straining Drinks"] 
    },
    {
        "id": "3",
        "options": ["https://www.dolivotastingbar.com/wp-content/uploads/2019/05/manzanilla-olives.jpg",
                    "https://www.absolut.com/globalassets/images/products/absolut-vodka/atlas/atlas_absolut-vodka_1000ml_4x.jpg",
                    "https://theaustralianfoodshop.com/wp-content/uploads/2021/03/bundaberg-ginger-beer-375ml.jpeg",
                    "https://i5.walmartimages.com/asr/9890d72f-c487-42d9-afac-5f1c03c442ff_1.75f6a1d66a12e7d7a4b76f8ea6b47380.jpeg",
                    "https://media.istockphoto.com/photos/slice-of-orange-picture-id185311615?k=20&m=185311615&s=612x612&w=0&h=XRDJ5CC9Irit4uPVLxBkFVK_hZJcGXg4HpAbTKwvTgU=",
                    "https://d1h1synnevvfsx.cloudfront.net/pub/media/catalog/product/cache/ebc6733575d5c8d1cd0f057bf2f42791/2/0/2020_10_09_5409.jpg",
                    "https://products3.imgix.drizly.com/ci-patron-silver-25fa130a809ea038.jpeg?auto=format%2Ccompress&ch=Width%2CDPR&fm=jpg&q=20",
                    "https://www.meijer.com/content/dam/meijer/product/0004/12/5010/20/0004125010200_2_A1C1_1200.png",
                    "https://solidstarts.com/wp-content/uploads/when-can-babies-eat-eggs.jpg",
                    "https://cdn.shopify.com/s/files/1/0013/2477/7569/products/aag_960x.jpg?v=1597696572"]
    },
    {
        "id": "4",
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
        "options": ["Mixing Drinks",
                    "Measuring Alcohol",
                    "Peeling Ingredients",
                    "Straining Drinks"]
    }
]
data = [
    {
        "id": "1",
        "question": "What is this tool used for?",
        "image": "https://static.restaurantsupply.com/media/catalog/product/cache/58705eee992a0d7bab305099af29f9ee/a/m/american-metalcraft-j202_1_1.jpg",
        "hint": "This tool is called a 'jigger'"
    },
    {
        "id": "2",
        "question": "What is this tool used for?",
        "image": "https://m.media-amazon.com/images/I/51JwNh0iftL._AC_SL1400_.jpg",
        
        "hint": "This tool is called a 'muddler'"
    },
    {
         "id": "3",
        "question": "What do you need to make a Martini?",
        "image": "https://3f4c2184e060ce99111b-f8c0985c8cb63a71df5cb7fd729edcab.ssl.cf2.rackcdn.com/media/16258/vodkamartini.jpg",
       
        "hint": ""
    },
    {
        "id": "4",
        "question": "What is the procedure for making a Gin Fizz?",
        "image": "https://www.liquor.com/thmb/ER6DAmPfS6RSQo3S4XkopdRpMv0=/720x720/smart/filters:no_upscale()/gin-fizz-720x720-primary-v3-2c1390963d014e35a01d741df2f9ae77.jpg",
        
    },
    {                                                                                                                                                            
        "id": "5",
        "question": "What is this tool used for?",
        "image": "https://m.media-amazon.com/images/I/61xmg-8MuuL._AC_SL1500_.jpg",
       
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
    quiz_answer_id = quiz_answers[int(id)]
    return render_template('quiz.html', quiz_id=quiz_id, data=data, quiz_answers=quiz_answers, quiz_answer_id=quiz_answer_id, data_answers=data_answers)

@app.route('/lesson/tools/<id>')
def tools(id = None):
    global lesson_tools
    tool = lesson_tools[id]
    return render_template('tool.html', tool=tool)

@app.route('/lesson/tools/')
def toolsLanding(id = None):
    global lesson_tools
    tools = lesson_tools
    return render_template('toolLanding.html', tools=tools)

@app.route('/lesson/recipes/<id>')
def recipes(id = None):
    global lesson_recipes
    recipe = lesson_recipes[id]
    return render_template('recipe.html', recipe=recipe)

@app.route('/lesson/recipes/')
def recipesLanding(id = None):
    global lesson_recipes
    recipes = lesson_recipes
    return render_template('recipeLanding.html', recipes=recipes)

if __name__ == '__main__':
   app.run(debug = True)

