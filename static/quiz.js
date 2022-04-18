$(document).ready(function(){
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
    $("#displayResultItems").empty()
    console.log("enter display q's")

    $.each(data, function(quizIndex, quizDetails){
        if(quizNumbers.includes(quizDetails["id"])){
            let quizID = quizDetails["id"]
            let quizQuestion = quizDetails["question"]
            //let quizImage = $("<a href='/quiz/" + quizID + "'>")
            quizImage.append("<img src= " + '\u0022' + quizDetails["image"] + '\u0022' + "></img>")
            let quizOptions = quizDetails["options"]
            console.log(quizOptions)
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
            quizRow2.append("Options: " + quizOptions)
            quizRow2.append("{% for tags in quiz_id.options%}<li id='tagButton'>{{tags}}</li>{% endfor %}")
            quizCol.append(quizRow2)
            $("#displayResultItems").append(quizCol)
        }
    })
}

function chooseAnswer(){
    //idfk how to do this i cant even think
    //like it should be smth like
    //click button event for tagButton
    //if the answer chosen matches the answer from quiz_answer_id, then 
    //addClass(rightAnswer) to the answerButton
    //else, addClass(wrongAnswer)
    //also still need to add a hint button, next button, and the quiz score
}