$(document).ready(function() {
    //ajax update/insert for user-languages
    $(".submit").on('click',function(){
        $.ajax({
            url: "myprofile/add_or_update_user_lanaguages/",
            type: "POST", // http method
            data: {learning_language: $("#learning_language").val(),
                    preferred_language:$('#preferred_language').val()
                    }, // data sent with the post request

            // handle a successful response
            success: function (json) {

            },

            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });

    //it should not be possible to choose the same language for both learning and favorite language
    /*$('#learning_language').on('change',function(){
        var selection = $(this).val();

        $('#preferred_language').children().each(function () {
           $(this).show();
            //console.log(selection);
            //console.log($(this).val());
            if ($(this).attr('selected')=='selected' && $(this).val() == selection) {
                $(this).removeAttr('selected');
                console.log($(this).val());
                console.log(selection);
            }

        });
        $('#preferred_language').children("option[value^=" + $(this).val() + "]").hide();
    });*/
});