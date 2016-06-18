$(document).ready(function(){
    var $bar = $('.horizontal-progress')[0];
    var val = $($bar).text();
    var subject = $($bar).parent().find('.subject').text();
    $($bar).text('');
    var bar = create_progress_line($bar, subject);
    bar.animate(parseFloat(val));
});