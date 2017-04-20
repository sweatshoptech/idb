import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
      const textStyle = {
        color: 'white',
      };
      const contentStyle = {
        marginBottom: 3 + 'rem',
      };
      const headingStyle = {
        color: 'white',
        marginTop: 160 + 'px',
        paddingTop: 0 + 'px',
        paddingBottom: 40 + 'px',
        transition: '.5s ease'
      };
      const cardStyle = {
        marginBottom: 0 + 'rem',
        alignSelf: 'center',
      }
      return (
        <div className="card rounded-opacity card-animation" style={cardStyle}> 
            <h1 className="cover-heading" style={headingStyle}>Hello, World!</h1> 
            <div id="carouselContent" className="carousel slide" data-ride="carousel" style={contentStyle}> 
              <div className="carousel-inner" role="listbox"> 
                <div className="carousel-item active text-center" style={textStyle}> 
                  <h3>discover great companies</h3> 
                </div> 
                <div className="carousel-item text-center" style={textStyle}> 
                  <h3>discover great people</h3> 
                </div> 
                <div className="carousel-item text-center" style={textStyle}> 
                  <h3>discover great investors</h3> 
                </div> 
                <div className="carousel-item text-center" style={textStyle}> 
                  <h3>discover great schools</h3> 
                </div> 
              </div> 
              <a className="carousel-control-prev" href="#carouselContent" role="button" data-slide="prev"> 
                <span className="carousel-control-prev-icon" aria-hidden="true"></span> 
                <span className="sr-only">Previous</span> 
              </a> 
              <a className="carousel-control-next" href="#carouselContent" role="button" data-slide="next"> 
                <span className="carousel-control-next-icon" aria-hidden="true"></span> 
                <span className="sr-only">Next</span> 
              </a> 
            </div> 
        </div> 
      );
    }
};

ReactDOM.render(React.createElement(App), document.getElementById('app'));
