define([ 'jquery', 'ace/ace', 'ace/ext/modelist', 'autocomplete', 'css!style/code_editor'],
    function($, ace, modelist, autoComplete){

var editor_id_end = ['code'];
var language_id_end = ['language'];

var html = {
    editor:
    "<div id='code-editor'></div>"
};

$(document).ready(function(){
    var $textarea;
    editor_id_end.forEach(function(el){
        var $text = $('textarea[id$="' + el + '"]');
        if ($text.length > 0)
            $textarea = $($text[0]);
    });

    var $language_input;
    language_id_end.forEach(function(el){
        var $in = $('input[id$="' + el + '"]');
        if ($in.length > 0)
            $language_input = $($in[0]);
    });

    if ($textarea && $language_input) {
        $textarea.after($(html.editor));
        $textarea.hide();

        var editor = ace.edit("code-editor");
        editor.setTheme("ace/theme/chrome");

        var mode = $language_input.val().toLowerCase().trim();
        var modes_concurrence = modelist.modes.filter(function(m){
            return m.caption.toLowerCase() == mode;
        });
        mode = modes_concurrence.length ? modes_concurrence[0].mode:'ace/mode/text';
        editor.getSession().setMode(mode);

        editor.setValue($textarea.text());

        editor.on('change', function(){
            $textarea.text(editor.getValue());
        });

        $(document).on("keypress", 'input', function (e) {
            var code = e.keyCode || e.which;
            if (code == 13) {
                e.preventDefault();
                return false;
            }
        });

        var warning = function(){
            var mode = $language_input.val().toLowerCase();
            var modes_concurrence = modelist.modes.filter(function(m){
                return m.caption.toLowerCase() == mode;
            });
            if (modes_concurrence.length){
                $language_input.parent().parent().removeClass('has-warning');
                editor.getSession().setMode(modes_concurrence[0].mode);
            } else {
                $language_input.parent().parent().addClass('has-warning');
            }
        };

        var autocomplete = new autoComplete({
            selector: '#' + $language_input.attr('id'),
            minChars: 1,
            source: function(term, suggest){
                term = term.toLowerCase();
                var matches = [];
                for (i=0; i<modelist.modes.length; i++)
                    if (~modelist.modes[i].caption.toLowerCase().indexOf(term)) matches.push(modelist.modes[i].caption);
                suggest(matches);
            },
            onSelect: warning
        });

        $language_input.on('input', warning)
    } else {
        console.error("Textarea or input for code editor not found.")
    }
});

});
