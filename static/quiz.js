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
    displayAnswerChoices()

    $(function () {
        $('input[name="test"]').on('click', function() {
            $(".answer-text").hide();
            if ($(this).val() == 'ans') {
                $('.exp').show();
            } else {
                $('.red').show();
            }
        })
    })
    


   /**$("#answerButton").click(function (event){
        $(".answer-text").hide()
        if ($('input[name="test"]').val() == 'ans'){
            $('.exp').show()
        } else {
            $('.red').show()
        }
    })*/
})



function displayAnswerChoices(){
    $("#answerChoices").empty()
    let quizForm = $("<form class='q'>")
    let endQuizForm = $("</form>")
    //let submitButton = $("<input type='submit' value='Submit'>  ")

    $.each(data_answers, function(quizIndex, data_answers){
        if (window.location.href === "http://127.0.0.1:5000/quiz/0" && data_answers["id"] === "1"){
            //console.log(data_answers)
            //console.log("data_answers 1", data_answers)
            //console.log(data_answers["options"][0])
            let quizCol = $("<div class='col-md-4'>")
            let quizRow1 = $("<div class='row'>")
            let quizRow2 = $("<div class='row'>")
            let quizRow3 = $("<div class='row'>")
            let quizRow4 = $("<div class='row'>")
            let correctAnswer = $("<div class='exp answer-text' style='display:none'> correct! </div>")
            let wrongAnswer = $("<div class='red answer-text' style='display:none'> a is the correct answer</div>")
            quizCol.append("<form class='q'>")
            let quizOption1 = $("<input name='test' type='radio' value='ans'> A) Mixing Drinks </>")
            quizRow1.append(quizOption1)
            quizCol.append(quizRow1)
            let quizOption2 = $("<input name='test' type='radio' value='incl'> B) Measuring Alcohol</>")
            quizRow2.append(quizOption2)
            quizCol.append(quizRow2)
            let quizOption3 = $("<input name='test' type='radio' value='incl'> C) Peeling Ingredients </>")
            quizRow3.append(quizOption3)
            quizCol.append(quizRow3)
            let quizOption4 = $("<input name='test' type='radio' value='incl'> D) Straining Drinks</>")
            quizRow4.append(quizOption4)
            quizCol.append(quizRow4)
            quizCol.append(correctAnswer)
            quizCol.append(wrongAnswer)
            quizCol.append("</form>")
            $("#answerChoices").append(quizCol)
        }
        else if (window.location.href === "http://127.0.0.1:5000/quiz/1" && data_answers["id"] === "2"){
            let quizCol = $("<div class='col-md-4'>")
            let quizRow1 = $("<div class='row'>")
            let quizRow2 = $("<div class='row'>")
            let quizRow3 = $("<div class='row'>")
            let quizRow4 = $("<div class='row'>")
            let correctAnswer = $("<div class='exp answer-text' style='display:none'> correct! </div>")
            let wrongAnswer = $("<div class='red answer-text' style='display:none'> a is the correct answer</div>")
            quizCol.append("<form class='q'>")
            let quizOption1 = $("<input name='test' type='radio' value='ans'> A) Mashing Ingredients </>")
            quizRow1.append(quizOption1)
            quizCol.append(quizRow1)
            let quizOption2 = $("<input name='test' type='radio' value='incl'> B) Measuring Alcohol</>")
            quizRow2.append(quizOption2)
            quizCol.append(quizRow2)
            let quizOption3 = $("<input name='test' type='radio' value='incl'> C) Peeling Ingredients </>")
            quizRow3.append(quizOption3)
            quizCol.append(quizRow3)
            let quizOption4 = $("<input name='test' type='radio' value='incl'> D) Straining Drinks</>")
            quizRow4.append(quizOption4)
            quizCol.append(quizRow4)
            quizCol.append(correctAnswer)
            quizCol.append(wrongAnswer)
            quizCol.append("</form>")
            $("#answerChoices").append(quizCol)
            
    }
        else if (window.location.href === "http://127.0.0.1:5000/quiz/3" && data_answers["id"] === "4"){
            let quizCol = $("<div class='col-md-4'>")
            let quizRow1 = $("<div class='row'>")
            let quizRow2 = $("<div class='row'>")
            let quizRow3 = $("<div class='row'>")
            let quizRow4 = $("<div class='row'>")
            let correctAnswer = $("<div class='exp answer-text' style='display:none'> correct! </div>")
            let wrongAnswer = $("<div class='red answer-text' style='display:none'> a is the correct answer</div>")
            quizCol.append("<form class='q'>")
            let quizOption1 = $("<input name='test' type='radio' value='ans'> A) Mixing Drinks </>")
            quizRow1.append(quizOption1)
            quizCol.append(quizRow1)
            let quizOption2 = $("<input name='test' type='radio' value='incl'> B) Measuring Alcohol</>")
            quizRow2.append(quizOption2)
            quizCol.append(quizRow2)
            let quizOption3 = $("<input name='test' type='radio' value='incl'> C) Peeling Ingredients </>")
            quizRow3.append(quizOption3)
            quizCol.append(quizRow3)
            let quizOption4 = $("<input name='test' type='radio' value='incl'> D) Straining Drinks</>")
            quizRow4.append(quizOption4)
            quizCol.append(quizRow4)
            quizCol.append(correctAnswer)
            quizCol.append(wrongAnswer)
            quizCol.append("</form>")
            $("#answerChoices").append(quizCol)
    }
        else if (window.location.href === "http://127.0.0.1:5000/quiz/4" && data_answers["id"] === "5"){
            let quizCol = $("<div class='col-md-4'>")
            let quizRow1 = $("<div class='row'>")
            let quizRow2 = $("<div class='row'>")
            let quizRow3 = $("<div class='row'>")
            let quizRow4 = $("<div class='row'>")
            let correctAnswer = $("<div class='exp answer-text' style='display:none'> correct! </div>")
            let wrongAnswer = $("<div class='red answer-text' style='display:none'> a is the correct answer</div>")
            quizCol.append("<form class='q'>")
            let quizOption1 = $("<input name='test' type='radio' value='ans'> A) Mixing Drinks </>")
            quizRow1.append(quizOption1)
            quizCol.append(quizRow1)
            let quizOption2 = $("<input name='test' type='radio' value='incl'> B) Measuring Alcohol</>")
            quizRow2.append(quizOption2)
            quizCol.append(quizRow2)
            let quizOption3 = $("<input name='test' type='radio' value='incl'> C) Peeling Ingredients </>")
            quizRow3.append(quizOption3)
            quizCol.append(quizRow3)
            let quizOption4 = $("<input name='test' type='radio' value='incl'> D) Straining Drinks</>")
            quizRow4.append(quizOption4)
            quizCol.append(quizRow4)
            quizCol.append(correctAnswer)
            quizCol.append(wrongAnswer)
            quizCol.append("</form>")
            $("#answerChoices").append(quizCol)
}
        else if (window.location.href === "http://127.0.0.1:5000/quiz/2" && data_answers["id"] === "3"){
            let quizCol = $("<div class='col-md-12'>")
            let all_options = $("<div class='row col-md-12'>")

            $(data_answers["options"]).each(function(index, value){
                let answer_drag = $("<img class='img_format_answer' src=" + value + ">")
                $(".img_format_answer").draggable({revert: "invalid", zIndex: 100})
                all_options.append(answer_drag)
            }) 

            let dropzone = $("<div class = 'row col-md-12'> <div class = 'col-md-2 drop_a' id = 'drop1'>1</div> <div class = 'col-md-2 drop_a' id = 'drop2'>2</div> <div class = 'col-md-2 drop_a' id = 'drop3'>3</div> <div class = 'col-md-2 drop_a' id = 'drop4'>4</div></div>")
            
            $(".drop_a").droppable({
                accept: ".img_format_answer",
                classes: {
                    "ui-droppable-hover": "ui-state-hover"
                  },
                over: function(event, ui){
                    console.log(2)
                  },
                drop: function(event, ui){
                    ui.draggable.remove()
                    console.log("asdf")
                }
            })

            quizCol.append(dropzone)
            quizCol.append(all_options)
            $("#answerChoices").append(quizCol)
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