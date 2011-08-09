$(function(){
    $("ul#social-media-icons li img").each(function(){
        var extension = $(this).attr("src").substring($(this).attr("src").lastIndexOf('.'));
        $(this).attr("src", $(this).attr("src").substring(0, $(this).attr("src").lastIndexOf('.')) + "-faded" + extension);
    });

    $("ul#social-media-icons li img").hover(function(){
        var extension = $(this).attr("src").substring($(this).attr("src").lastIndexOf('.'));
        $(this).attr("src", $(this).attr("src").substring(0, $(this).attr("src").lastIndexOf('-faded.')) + extension);
    }, function(){
        var extension = $(this).attr("src").substring($(this).attr("src").lastIndexOf('.'));
        $(this).attr("src", $(this).attr("src").substring(0, $(this).attr("src").lastIndexOf('.')) + "-faded" + extension);
    });
});