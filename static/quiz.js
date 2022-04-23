$(document).ready(function(){
    //console.log("document ready")
    /**$("#start-btn").html("start")
    $("#start-btn").click(function (event) {
        console.log("click")
        $("#start-btn").addClass("hide")
        //let quizNumbers = ["1", "2", "3", "4", "5"]
        displayAnswerChoices(data_answers)
    })
    **/

   /** $(function () {
        $('input[name="test"]').on('click', function() {
            $(".answer-text").hide();
            if ($(this).val() == 'ans') {
                $('.exp').show();
            } else {
                $('.red').show();
            }
        })
    });*/ 
    displayAnswerChoices()
})



function displayAnswerChoices(){
    $("#answerChoices").empty()
    let quizForm = $("<form class='q'>")
    let endQuizForm = $("</form>")
    let submitButton = $("<input type='submit' value='Submit'>  ")

    $.each(data_answers, function(quizIndex, data_answers){
        //console.log("data_answers options", data_answers["options"][0])
        let choice1 = data_answers["options"][0]
        let choice2 = data_answers["options"][1]
        let choice3 = data_answers["options"][2]
        let choice4 = data_answers["options"][3]
        let choice5 = data_answers["options"][4]
        let choice6 = data_answers["options"][5]
        let choice7 = data_answers["options"][6]
        let choice8 = data_answers["options"][7]
        let choice9 = data_answers["options"][8]
        let choice10 = data_answers["options"][9]
        //console.log(data_answers[id])
        if (window.location.href === "http://127.0.0.1:5000/quiz/0" && data_answers["id"] === "1"){
            //console.log(data_answers)
            let quizCol = $("<div class='col-md-12'>")
            quizCol.append("<form class='q'>")
            //console.log("data_answers 1", data_answers)
            //console.log(data_answers["options"][0])
            let quizOption1 = $("<input name='test' type='radio' value='ans' />")
            quizOption1.text("")
            //quizOption1.append("A)")
            //quizOption1.append(data_answers)
            quizOption1.append(data_answers["options"][0])
            quizOption1.append("hello")
            quizCol.append(quizOption1)
            let quizOption2 = $("<input name='test' type='radio' value='incl' /> B)")
            quizOption2.append(choice2)
            quizCol.append(quizOption2)
            let quizOption3 = $("<input name='test' type='radio' value='incl' /> C)")
            quizOption3.append(choice3)
            quizCol.append(quizOption3)
            let quizOption4 = $("<input name='test' type='radio' value='incl' /> D)")
            quizOption4.append(choice4)
            quizCol.append(quizOption4)
            quizCol.append(submitButton)
            quizCol.append("</form>")
            $("#answerChoices").append(quizCol)
            console.log(choice1)
        }
        else if (window.location.href === "http://127.0.0.1:5000/quiz/1" && data_answers["id"] === "2"){
            //console.log(data_answers)
            let quizCol = $("<div class='col-md-12'>")
            quizCol.append("<form class='q'>")
            //console.log("data_answers 1", data_answers)
            //console.log(data_answers["options"][0])
            let quizOption1 = $("<input name='test' type='radio' value='ans' />")
            quizOption1.text("")
            //quizOption1.append("A)")
            //quizOption1.append(data_answers)
            quizOption1.append(data_answers["options"][0])
            quizOption1.append("hello")
            quizCol.append(quizOption1)
            let quizOption2 = $("<input name='test' type='radio' value='incl' /> B)")
            quizOption2.append(choice2)
            quizCol.append(quizOption2)
            let quizOption3 = $("<input name='test' type='radio' value='incl' /> C)")
            quizOption3.append(choice3)
            quizCol.append(quizOption3)
            let quizOption4 = $("<input name='test' type='radio' value='incl' /> D)")
            quizOption4.append(choice4)
            quizCol.append(quizOption4)
            quizCol.append(submitButton)
            quizCol.append("</form>")
            $("#answerChoices").append(quizCol)
            console.log(choice1)
    }
    else if (window.location.href === "http://127.0.0.1:5000/quiz/3" && data_answers["id"] === "4"){
        //console.log(data_answers)
        let quizCol = $("<div class='col-md-12'>")
        quizCol.append("<form class='q'>")
        //console.log("data_answers 1", data_answers)
        //console.log(data_answers["options"][0])
        let quizOption1 = $("<input name='test' type='radio' value='ans' />")
        quizOption1.text("")
        //quizOption1.append("A)")
        //quizOption1.append(data_answers)
        quizOption1.append(data_answers["options"][0])
        quizOption1.append("hello")
        quizCol.append(quizOption1)
        let quizOption2 = $("<input name='test' type='radio' value='incl' /> B)")
        quizOption2.append(choice2)
        quizCol.append(quizOption2)
        let quizOption3 = $("<input name='test' type='radio' value='incl' /> C)")
        quizOption3.append(choice3)
        quizCol.append(quizOption3)
        let quizOption4 = $("<input name='test' type='radio' value='incl' /> D)")
        quizOption4.append(choice4)
        quizCol.append(quizOption4)
        quizCol.append(submitButton)
        quizCol.append("</form>")
        $("#answerChoices").append(quizCol)
        console.log(choice1)
    }
    else if (window.location.href === "http://127.0.0.1:5000/quiz/4" && data_answers["id"] === "5"){
        //console.log(data_answers)
        let quizCol = $("<div class='col-md-12'>")
        quizCol.append("<form class='q'>")
        //console.log("data_answers 1", data_answers)
        //console.log(data_answers["options"][0])
        let quizOption1 = $("<input name='test' type='radio' value='ans' />")
        quizOption1.text("")
        //quizOption1.append("A)")
        //quizOption1.append(data_answers)
        quizOption1.append(data_answers["options"][0])
        quizOption1.append("hello")
        quizCol.append(quizOption1)
        let quizOption2 = $("<input name='test' type='radio' value='incl' /> B)")
        quizOption2.append(choice2)
        quizCol.append(quizOption2)
        let quizOption3 = $("<input name='test' type='radio' value='incl' /> C)")
        quizOption3.append(choice3)
        quizCol.append(quizOption3)
        let quizOption4 = $("<input name='test' type='radio' value='incl' /> D)")
        quizOption4.append(choice4)
        quizCol.append(quizOption4)
        quizCol.append(submitButton)
        quizCol.append("</form>")
        $("#answerChoices").append(quizCol)
        console.log(choice1)
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