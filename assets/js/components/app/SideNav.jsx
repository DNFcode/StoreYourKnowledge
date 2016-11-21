import React from 'react'
import { Link } from 'react-router'


export default class SideNav extends React.Component {
    render() {
        return (
            <ul id="slide-out" className="side-nav fixed">
                <li className="logo">
                    <Link to="/" className="brand-logo color1">Educate Yourself</Link>
                </li>
                <li className="color2-text"><a href="#!">Goals</a></li>
                <li><a href="#!">Statistics</a></li>
                <li><a href="#!">News</a></li>
                <li><a href="#!">Subscriptions</a></li>
            </ul>
        )
    }
}