import React from 'react'


export default class SignUp extends React.Component {
    render() {
        return (
            <div className="row container">
                <div className="row center">
                    <h2 className="text-weight-200">Join us</h2>
                </div>
                <div className="row">
                    <form className="col l6 offset-l3 m10 offset-m1 s12">
                        <div className="row">
                            <div className="input-field col s12">
                              <input id="login" type="text" className="validate"/>
                              <label for="login">Login</label>
                            </div>
                        </div>
                        <div className="row">
                            <div className="input-field col s12">
                              <input id="email" type="email" className="validate"/>
                              <label for="email">Email</label>
                            </div>
                        </div>
                        <div className="row">
                            <div className="input-field col s12">
                              <input id="password" type="password" className="validate"/>
                              <label for="password">Password</label>
                            </div>
                        </div>
                        <div className="row">
                            <div className="input-field col s12">
                              <input id="password-repeat" type="password" className="validate"/>
                              <label for="password-repeat">Repeat password</label>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col s12">
                                <button className="btn waves-effect waves-light color2 right">Sign up</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        )
    }
}