import React, { useState } from 'react';
import NavBarComponent from './Navigation';
import Dashboard from './Dashboard';
import SideMenu from './SideMenu';
import { Col, Container, Row } from 'react-bootstrap';


const App = () => {
    const [isLogged, setIsLogged] = useState(false)
    return (
        <div>
            <NavBarComponent isLogged={isLogged} />
            <Container >
            <h1>This is my React app!</h1>
                <Row>
                    <Col md={4}>
                        <SideMenu />
                    </Col>
                    <Col md={8}>
                        <Dashboard />
                    </Col>
                </Row>
            </Container>
        </div>
    );
}

export default App