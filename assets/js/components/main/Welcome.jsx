import React from 'react'
import { Link } from 'react-router'


export default class Welcome extends React.Component {
    render() {
        return (
            <div className="container">
                <div className="index-header center">
                    <h2 className="color2-text text-weight-300">Improve Your Skills</h2>
                    <h3 className="text-weight-200">Learn programming your own way</h3>
                </div>
                <div className="row center">
                    <Link to="/app">
                        <button className="btn-large waves-effect waves-light color2">Start right now!!</button>
                    </Link>
                </div>
                <div className="main row">
                    <div className="col l4 s12 center">
                        <h3><i className="fa fa-database color1-text icon"></i></h3>
                        <h5>Store things you've learned</h5>
                        <p>
                            Create notes with useful information which you want to remember.
                            Save different link, articles and books for further reading.
                            Add code examples! You never know when you may need them.
                        </p>
                    </div>
                    <div className="col l4 s12 center">
                        <h3><i className="fa fa-users color1-text icon"></i></h3>
                        <h5>Use others experience</h5>
                        <p>
                            Search for tasks and notes from people who learned a lot already!
                            Find helpful books and interesting code examples. Also you can contact
                            anyone via online chat. Or even ask someone to be your tutor.
                        </p>
                    </div>
                    <div className="col l4 s12 center">
                        <h3><i className="fa fa-trophy color1-text icon"></i></h3>
                        <h5>Achieve your goals</h5>
                        <p>
                            Create tasks for yourself and other users. Complete your tasks and watch your progress.
                            We will remind you if you will start to forget complete your tasks.
                        </p>
                    </div>
                </div>
            </div>
        )
    }
}
