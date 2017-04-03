define(['jquery', './goals'], function($, goals){

$(document).ready(function(){
    $('.progress-bar-container').each(function(){
        // var val = $(this).text();
        var val = Math.random();
        var subject = $(this).parent().find('.subject').text();
        $(this).text('');
        var bar = goals.create_progress_circle(this, subject);
        bar.animate(parseFloat(val));
    });
});

});