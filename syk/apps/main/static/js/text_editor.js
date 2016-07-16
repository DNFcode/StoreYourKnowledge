define(['jquery', 'quill', 'css!style/text_editor'],
    function( $, Quill) {

var ids_end = ['description', 'text'];

var html = {
    toolbar:
    '<div class="toolbar" id="editor-toolbar">' +
        '<span class="ql-format-group">' +
            '<span title="Bold" class="ql-format-button ql-bold"></span>' +
            '<span class="ql-format-separator"></span>' +
            '<span title="Italic" class="ql-format-button ql-italic"></span>' +
            '<span class="ql-format-separator"></span>' +
            '<span title="Underline" class="ql-format-button ql-underline"></span>' +
            '<span class="ql-format-separator"></span>' +
            '<span title="Strikethrough" class="ql-format-button ql-strike"></span>' +
        '</span>' +
        '<span class="ql-format-group">' +
            '<span title="List" class="ql-format-button ql-list"></span>' +
            '<span class="ql-format-separator"></span>' +
            '<span title="Bullet" class="ql-format-button ql-bullet"></span>' +
            '<span class="ql-format-separator"></span>' +
        '</span>' +
        '<span class="ql-format-group">' +
            '<span title="Link" class="ql-format-button ql-link"></span>' +
        '</span>' +
    '</div>',

    editor: '<div id="text-editor"></div>'
};

$(document).ready(function () {
    var $textarea;
    ids_end.forEach(function (el) {
        var $text = $('textarea[id$="' + el + '"]');
        if ($text.length > 0)
            $textarea = $($text[0]);
    });

    if ($textarea) {
        $textarea.after($(html.editor));
        $textarea.after($(html.toolbar));
        $textarea.hide();

        var quill = new Quill('#text-editor', {
            modules: {
                'toolbar': {container: '#editor-toolbar'},
                'link-tooltip': true
            },
            theme: 'snow'
        });

        quill.setHTML($textarea.text());

        quill.on('text-change', function (delta, source) {
            $textarea.text(quill.getHTML());
        });
    } else {
        console.error("Textarea for text editor not found.")
    }
});

});