import React from 'react'
import { Link } from 'react-router'

export default class NavBar extends React.Component {
    render() {
        const { authorised, title } = this.props;

        return (
            <nav className={`color1 ${title ? "title-nav":null}`}>
                <div className="nav-wrapper">
                    {authorised ? (
                        <ul id="nav-mobile" className="right transparent">
                            <li><Link to="/logout" className="transparent">Log out</Link></li>
                        </ul>
                    ) : null}

                    <div className="container">
                        {title ?
                            <span className="navbar-title">{title}</span> :
                            <Link to="/" className="brand-logo">Educate Yourself</Link>
                        }
                        {!authorised ?  (
                            <ul id="nav-mobile" className="right">
                                <li><Link to="/signup">Sign up</Link></li>
                                <li><Link to="/login">Log in</Link></li>
                            </ul>
                        ) : null}
                    </div>



                </div>

            </nav>
        )
    }
}