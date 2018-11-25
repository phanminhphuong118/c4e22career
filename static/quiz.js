$(document).ready(() => {
    answerClick();
})

const answerClick = () => {
    let totalPoint = 0;
    for (let questionID = 1; questionID <= 10; questionID++) {
        for (let answerID = 0; answerID <= 2; answerID++) {
            $(`#answer_${questionID}_${answerID}`).on('click', () => {
                totalPoint += parseInt($(`#answer_${questionID}_${answerID}`).attr('point'));
                $(`#${questionID}`).css('display','none');
                $(`#${questionID + 1}`).css('display','flex');
                console.log(totalPoint);
                if (questionID == 10) {
                    $.post( "/quiz", {
                        javascript_data: totalPoint 
                    }); 
                }
            });
        }
    }
    
}

