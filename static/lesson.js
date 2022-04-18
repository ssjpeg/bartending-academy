/*$(document).ready(function(){
    console.log("document ready")
    $("#start-btn").html("start")
    $("#start-btn").click(function (event) {
        console.log("click")
        $("#start-btn").addClass("hide")
        let quizNumbers = ["1", "2", "3", "4", "5"]
        displayQuestion(quizNumbers, quiz)
    })
})

function displayQuestion(quizNumbers, quiz){
    $("#searchResultItems").empty()
    console.log("enter display q's")

    $.each(data, function(quizIndex, quizDetails){
        if(quizNumbers.includes(quizDetails["id"])){
            let quizID = quizDetails["id"]
            let quizQuestion = quizDetails["question"]
            //let quizImage = $("<a href='/quiz/" + quizID + "'>")
            quizImage.append("<img src= " + '\u0022' + quizDetails["image"] + '\u0022' + "></img>")
            let quizOptions = quizDetails["options"]
            let quizCol = $("<div class='col-md-12'>")
            let quizRow1 = $("<div class='row'>")
            let quizRow2 = $("<div class='row'>")
            let quizImageRow = $("<div class='row'>")

            quizCol.text("")
            quizCol.append("<br>")
            quizRow1.append("<a href='/quiz/" + quizID + "'>" + quizQuestion)
            quizCol.append(quizRow1)
            quizImageRow.append(quizImage)
            quizCol.append(quizImageRow)
            quizRow2.append("Tags: " + quizOptions)
            quizRow2.append("{% for tags in quiz.options%}<li class='optionsButton'>{{options}}</li>{% endfor %}")
            quizCol.append(quizRow2)
            $("#displayhResultItems").append(quizCol)
        }
    })
}