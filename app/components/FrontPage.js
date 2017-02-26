import React from 'react';
import { Link } from 'react-router';
import style from '../styles/frontpage.scss';
import { AppBar } from 'react-toolbox/lib/app_bar';
import { Navigation } from 'react-toolbox/lib/navigation';
import { Button } from 'react-toolbox/lib/button';
import { Card, CardMedia, CardTitle, CardText } from 'react-toolbox/lib/card';

const FrontPage = () =>
  <div>
    <AppBar title=" " flat>
      <Navigation type="horizontal">
        <Button label="Log in" raised primary/>
      </Navigation>
    </AppBar>
    <h1 className={style.header}>
      Educate yourself
    </h1>
    <p className={style.intro}>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.
      Aenean ullamcorper neque nec dui malesuada vulputate.
      Ut imperdiet mattis leo, sagittis hendrerit neque pretium a.
      Phasellus rhoncus a diam eget lobortis. In id elit pulvinar,
      finibus nisl quis, faucibus diam. Ut accumsan lacus nec porta pulvinar.
      Donec egestas augue at consequat tempor.
    </p>
    <div className={style.buttonWrapper}>
      <Link to="/app">
        <Button className={style.actionButton} label="Let's go!" raised primary/>
      </Link>
    </div>
    <div className={style.cards}>
      <Card style={{width: '350px'}} raised>
        <CardMedia
          aspectRatio="wide"
          image="https://placeimg.com/800/450/nature"
        />
        <CardTitle
          title="Create your learning goals"
        />
        <CardText>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit.
          Aenean ullamcorper neque nec dui malesuada vulputate.
          Ut imperdiet mattis leo, sagittis hendrerit neque pretium a.
        </CardText>
      </Card>
      <Card style={{width: '350px'}} raised>
        <CardMedia
          aspectRatio="wide"
          image="https://placeimg.com/800/450/nature"
        />
        <CardTitle
          title="Find your own way"
        />
        <CardText>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit.
          Aenean ullamcorper neque nec dui malesuada vulputate.
          Ut imperdiet mattis leo, sagittis hendrerit neque pretium a.
        </CardText>
      </Card>
      <Card style={{width: '350px'}} raised>
        <CardMedia
          aspectRatio="wide"
          image="https://placeimg.com/800/450/nature"
        />
        <CardTitle
          title="Get help and help others"
        />
        <CardText>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit.
          Aenean ullamcorper neque nec dui malesuada vulputate.
          Ut imperdiet mattis leo, sagittis hendrerit neque pretium a.
        </CardText>
      </Card>
    </div>
  </div>;

export default FrontPage;
