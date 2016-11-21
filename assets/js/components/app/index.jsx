import React from 'react'
import { Route, IndexRoute } from 'react-router'

import SideNav from './SideNav'

import css from 'css/app/app.scss'


const header = () => {
    return (
        <div>
            <SideNav/>
        </div>
    )
};


//const App = (props) => {
//    return (
//        <Route path={props.path} component={props.component}>
//            <IndexRoute components={{Header: header}}/>
//        </Route>
//    )
//};

export { header };
