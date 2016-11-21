import React from 'react'
import ReactDOM from 'react-dom'
import 'css/app/goal.scss'


export class TextArea extends React.Component {

}

export class TextInput extends React.Component {

}


export class Form extends React.Component {
    render() {
        return (
            <div>
                <NavBar title={ this.props.title } authorised={true}/>
                <form className="row container">

                </form>
            </div>
        )
    }

}

Goals.propTypes = {
    title: React.PropTypes.string.isRequired,
    color: React.PropTypes.string.isRequired
};
