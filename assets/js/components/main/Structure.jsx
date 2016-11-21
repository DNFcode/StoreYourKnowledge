import React from 'react'

export const Header = (props) => {
    return (
        <header>
            { props.children }
        </header>
    )
};

export const Main = (props) => {
    return (
        <main>
            { props.children }
        </main>
    )
};