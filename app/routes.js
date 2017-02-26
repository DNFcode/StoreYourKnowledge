import React from 'react';
import { Route, IndexRoute } from 'react-router';
import FrontPage from './components/FrontPage';
import App from './components/App';

export default (
  <Route path="/">
    <IndexRoute component={FrontPage} />
      <Route path="app">
        <IndexRoute component={App} />
      </Route>
  </Route>
);
