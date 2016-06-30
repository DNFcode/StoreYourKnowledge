function create_progress_circle(container, subject){
    var bar = new ProgressBar.Circle(container, {
        strokeWidth: 6,
        easing: 'easeInOut',
        duration: 1400,
        color: get_color(subject),
        trailColor: '#eee',
        trailWidth: 1,
        svgStyle: null,
        step: function(state, bar) {
            bar.setText(Math.round(bar.value() * 100) + ' %');
        }
    });
    bar.text.style.color = '#666666';
    return bar;
}

function create_progress_line(container, subject){
    var bar = new ProgressBar.Line(container, {
        strokeWidth: 4,
        easing: 'easeInOut',
        duration: 1400,
        color: get_color(subject),
        trailColor: '#eee',
        trailWidth: 1,
        svgStyle: {width: '100%', height: '100%'},
        text: {
            style: {
              color: '#666666',
              position: 'absolute',
              right: '0',
              left: '0',
              top: '15px',
              padding: 0,
              margin: 0,
              transform: null
            },
            autoStyleContainer: false
        },
        from: {color: '#FFEA82'},
        to: {color: '#ED6A5A'},
        step: function(state, bar) {
            bar.setText(Math.round(bar.value() * 100) + ' %');
        }
    });

    return bar;
}

function get_color(text){
    text = text.toLowerCase();
    var colors = [
        '#EF5350',
        '#7E57C2',
        '#5C6BC0',
        '#69F0AE',
        '#42A5F5',
        '#EEFF41',
        '#26C6DA',
        '#26A69A',
        '#18FFFF',
        '#66BB6A',
        '#448AFF',
        '#E040FB',
        '#C6FF00',
        '#64FFDA',
        '#FFA000',
        '#9CCC65',
        '#D4E157',
        '#FFEE58',
        '#FFA726'
    ];
    var sum = 0;
    for(var i = 0; i<text.length; i++){
        sum += text.charCodeAt(i);
    }
    var avg = Math.round(sum/text.length);

    var range = "z".charCodeAt(0) - "a".charCodeAt(0);
    var step = Math.round(range/colors.length);
    var relative_avg = avg - "a".charCodeAt(0);
    return colors[Math.floor(relative_avg/step)] || colors[colors.length-1]
}