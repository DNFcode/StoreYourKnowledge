define(['jquery', './goals'], function($, goals) {

    $(document).ready(function () {
        var $bar = $('.horizontal-progress')[0];
        var val = $($bar).text();
        var subject = $($bar).parent().find('.subject-name').text();
        $($bar).text('');
        var bar = goals.create_progress_line($bar, subject);
        bar.animate(parseFloat(val));
    });

});
