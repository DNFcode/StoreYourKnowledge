import React from 'react'
import ProgressBar from 'progressbar.js'
import ReactDOM from 'react-dom'
import 'css/app/goal.scss'


export default class Goals extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            bar: null,
            edit: props.edit,
            name: props.name
        };
        this.nameSubmit = this.nameSubmit.bind(this);
    }

    nameSubmit(event) {

    }

    render() {
        return (
            <a className="goal-progress-bar col l4 m4 s6 center">
                <div ref="container" className="progress-bar-container"></div>
                {this.state.edit ?
                    <form onSubmit={ this.nameSubmit } className="center">
                      <input ref="name" type="text" placeholder="Goal name"/>
                    </form>
                    :
                    <div className="subject">{ this.state.name }</div>
                }
            </a>
        )
    }

    componentDidMount() {
        let bar = new ProgressBar.Circle(
            this.refs.container,
            {
            strokeWidth: 6,
            easing: 'easeInOut',
            duration: 1400,
            color: this.props.color,
            trailColor: '#eee',
            trailWidth: 1,
            svgStyle: null,
            step: function (state, bar) {
                bar.setText(Math.round(bar.value() * 100) + ' %');
            }
        });
        bar.animate(this.props.percent);
    }
}

Goals.propTypes = {
    percent: React.PropTypes.number.isRequired,
    name: React.PropTypes.string.isRequired,
    color: React.PropTypes.string.isRequired
};
