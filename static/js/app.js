import ReactDOM from 'react-dom';

class App extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
      return (
        <div class="container"  style="min-height: 89vh">
          <br /><br /><br /><br /><br /><br /><br /><br /><br />
          <div class="card rounded-opacity card-animation" style="margin-bottom: 0rem; align-self: center">
              <h1 class="cover-heading" style="color: white; margin-top: 160px; padding-top: 0px; padding-bottom: 40px; transition: .5s ease;" >Hello, World!</h1>
              <div id="carouselContent" class="carousel slide" data-ride="carousel" style="margin-bottom: 3rem;">
                <div class="carousel-inner" role="listbox">
                  <div class="carousel-item active text-center" style="color: white">
                    <h3>discover great companies</h3>
                  </div>
                  <div class="carousel-item text-center" style="color: white">
                    <h3>discover great people</h3>
                  </div>
                  <div class="carousel-item text-center" style="color: white">
                    <h3>discover great investors</h3>
                  </div>
                  <div class="carousel-item text-center" style="color: white">
                    <h3>discover great schools</h3>
                  </div>
                </div>
                <a class="carousel-control-prev" href="#carouselContent" role="button" data-slide="prev">
                  <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                  <span class="sr-only">Previous</span>
                </a>
                <a class="carousel-control-next" href="#carouselContent" role="button" data-slide="next">
                  <span class="carousel-control-next-icon" aria-hidden="true"></span>
                  <span class="sr-only">Next</span>
                </a>
              </div>
          </div>
        </div>
        <div class="outro">
          © SWEatshop 2017
        </div>
      );
    }
};

ReactDOM.render(<App />, document.querySelector('body'));