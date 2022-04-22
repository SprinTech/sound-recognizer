import React, { useState } from 'react';
import NavBarComponent from './Navigation';
import Dashboard from './Dashboard';
import SideMenu from './SideMenu';
import { Col, Container, Row, Button } from 'react-bootstrap';



const App = () => {
    const [isLogged, setIsLogged] = useState(false)
    const [test, setTest] = useState("")
    const handleOnClick = () => {
        fetch('http://localhost:5000/api/v1/')
            .then(response => response.json())
            .then(data => setTest(data))
        
    }
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
                <Button onClick={handleOnClick}>Click !!!!</Button>
            </Container>
            {test && Object.entries(test).map(([k, v]) => {
                return (
                    <span>{k} : {v}</span>
                )
            })}
        </div>
    );
}

export default App