import React, { Component } from 'react';
import { AppBar } from 'react-toolbox';
import { Layout, NavDrawer, Panel, Navigation, IconMenu, MenuItem, Avatar } from 'react-toolbox';
import style from '../styles/app.scss';

export default class LayoutTest extends Component {
  state = {
    drawerActive: false,
    drawerPinned: false,
    sidebarPinned: false
  };

  toggleDrawerActive = () => {
    this.setState({ drawerActive: !this.state.drawerActive });
  };

  toggleDrawerPinned = () => {
    this.setState({ drawerPinned: !this.state.drawerPinned });
  }

  toggleSidebar = () => {
    this.setState({ sidebarPinned: !this.state.sidebarPinned });
  };

  render() {
    return (
      <div>
      <AppBar title="Educate yourself" leftIcon="menu" onLeftIconClick={ this.toggleDrawerActive }>
        <Navigation type="horizontal" className={style.navigation}>
          <Avatar image="https://placeimg.com/80/80/animals"/>
          <IconMenu icon="more_vert" position="topRight" menuRipple>
            <MenuItem value="settings" icon="settings" caption="Settings" />
            <MenuItem value="logout" icon="exit_to_app" caption="Log out" />
          </IconMenu>
        </Navigation>
      </AppBar>
      <Layout>
        <NavDrawer active={this.state.drawerActive} className={style.drawer} onOverlayClick={this.toggleDrawerActive}>
          <Navigation type="vertical">
            a
          </Navigation>
        </NavDrawer>
        <Panel>
          <div>
            a
          </div>
        </Panel>
      </Layout>
      </div>
    );
  }
}
