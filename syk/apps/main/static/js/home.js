$(document).ready(function(){
    $('.progress-bar-container').each(function(){
        var val = $(this).text();
        var subject = $(this).parent().find('.subject').text();
        $(this).text('');
        var bar = create_progress_circle(this, subject);
        bar.animate(parseFloat(val));
    });
});