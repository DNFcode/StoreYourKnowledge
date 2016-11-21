import React from 'react'

import SideNav from './SideNav'
import css from 'css/app/goals.scss'
import Goal from './Goal'
import NavBar from '../main/NavBar'


export default class Goals extends React.Component {
    get_color(name) {
        name = name.toLowerCase();
        let colors = [
            //red
            ['#F44336', '#D32F2F', '#C62828', '#FF5252'],
            //purple
            ['#FF5252', '#7B1FA2', '#6A1B9A', '#AA00FF'],
            //indigo
            ['#3F51B5', '#303F9F', '#283593', '#3D5AFE'],
            //light green
            ['#8BC34A', '#689F38', '#558B2F', '#76FF03'],
            //blue
            ['#2196F3', '#1976D2', '#1565C0', '#2979FF'],
            //orange
            ['#FF9800', '#F57C00', '#EF6C00', '#FF9100'],
            //light blue
            ['#03A9F4', '#0288D1', '#0277BD', '#00B0FF'],
            //cyan
            ['#00BCD4', '#0097A7', '#00838F', '#00E5FF'],
            //teal
            ['#009688', '#00796B', '#00695C', '#1DE9B6'],
            //green
            ['#4CAF50', '#388E3C', '#2E7D32', '#00E676'],
            //yellow
            ['#F57F17', '#FBC02D', '#F9A825', '#FFEA00'],
        ];
        let colors_mixed = []
        for (let i = 0; i<4; i++) {
            colors_mixed.push(...colors.map(color => color[i]));
        }
        colors = colors_mixed;

        let sum = 0;
        for (var i = 0; i < name.length; i++) {
            sum += name.charCodeAt(i);
        }
        let avg = sum / name.length;

        let range = "z".charCodeAt(0) - "a".charCodeAt(0);
        let step = range / colors.length;
        let relative_avg = avg - "a".charCodeAt(0);
        return colors[Math.floor(relative_avg / step)] || colors[colors.length - 1]
    }

    render() {
        const goals = this.props.goals.map(([name, percent]) => {
            return (
                <Goal key={`goal_${name}`} name={name} percent={percent} color={this.get_color(name)}/>
            )
        });

        return (
            <div>
                <NavBar title="Current goals" authorised={true}/>
                <div className="goals row center container">
                    { goals }
                </div>
                <div className="fixed-action-btn" style={{bottom: 45, right: 24}}>
                    <button className="btn-floating btn-large color2">
                        <i className="large material-icons">add</i>
                    </button>
                </div>
            </div>
        )
    }
}

Goals.defaultProps = {
    goals: [
        ['python', 0.8],
        ['react', 0.1],
        ['aloa', 0.5],
        ['haskell', 0.7],
        ['javascript', 0.6]
    ]
};
