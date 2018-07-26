$(document).ready(function(){
    $("button[name=set-default-word-set]").on("click",function(){
        var url = $(this).attr("data-ajax-target");
        var button = this
        $.ajax({
            url:url,
            success: function(){
                $("button[name=set-default-word-set]").each(function(){
                   $(this).text('Set Default')
                })
                button.innerHTML = 'Default'
            },

        })

    })
})