$(document).ready(function() {
    if (window.location.pathname.indexOf("details") >= 0){
        $.ajax({
            url:'/details/ajax/',
            type: "POST",
            data:{csrfmiddlewaretoken:csrf_token},
            success: function (payload) {
                $("#title").html(payload.title);
                $("#author").html(payload.author);
                $("#publication_date").html(payload.publication_date);
                $("#hero").attr("src",payload.hero);
                $("#text").html(payload.text);
                if (payload.article_img){
                    $("#article_img").attr("src",payload.article_img);
                }
            }
        });
    }
});
