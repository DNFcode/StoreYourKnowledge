import React from 'react'

import NavBar from './NavBar'
import Login from './Login'

import css from 'css/base.scss'


export default class Base extends React.Component {
    render() {
        const { moved } = this.props.route;
        const { Header, Main } = this.props;
        return (
            <div className={moved ? 'moved-right' : null}>
                <header>
                    { Header }
                </header>
                <main>
                    { Main }
                </main>
            </div>
        )
    }
}
