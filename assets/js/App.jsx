import React from 'react'
import ReactDom from 'react-dom'
import { hashHistory, Router, Route, IndexRoute } from 'react-router'

import materialize_css from 'materialize-css/dist/css/materialize.min.css'
//import materialize_js from 'materialize-css/dist/js/materialize.min'
import font_awesome from 'font-awesome-webpack'

import css from '../css/index.scss'

//import { Header, Main } from './components/main/Structure'
import Welcome from './components/main/Welcome'
import Base from './components/main/Base'
import NavBar from './components/main/NavBar'
import Login from './components/main/Login'
import SignUp from './components/main/SignUp'
import { header } from './components/app'
import Goals from './components/app/Goals'


const App = () => (
  <Router history={hashHistory}>
      <Route path="/" component={Base}>
          <IndexRoute components={{Header: NavBar, Main: Welcome}}/>
          <Route path="login" components={{Header: NavBar, Main: Login}}/>
          <Route path="signup" components={{Header: NavBar, Main: SignUp}}/>
      </Route>
      <Route path="/app" component={Base} moved={true}>
          <IndexRoute components={{Header: header, Main: Goals}}/>
      </Route>
  </Router>
)

export default App;
