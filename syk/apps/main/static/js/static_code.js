require(["jquery", "ace/ace", "ace/ext/static_highlight", "ace/ext/modelist"], function($, ace, highlight, modelist) {
    var mode = $('.code-language').text().toLowerCase().trim();
    var modes_concurrence = modelist.modes.filter(function(m){
        return m.caption.toLowerCase() == mode;
    });

    mode = modes_concurrence.length ? modes_concurrence[0].mode:'ace/mode/text';

    highlight($('.code')[0], {
        mode: mode,
        theme: "ace/theme/chrome",
        startLineNumber: 1,
        //showGutter: true,
        trim: true
    }, function (highlighted) {

    });
});