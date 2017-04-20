'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var App = function (_React$Component) {
  _inherits(App, _React$Component);

  function App(props) {
    _classCallCheck(this, App);

    return _possibleConstructorReturn(this, (App.__proto__ || Object.getPrototypeOf(App)).call(this, props));
  }

  _createClass(App, [{
    key: 'render',
    value: function render() {
      var textStyle = {
        color: 'white'
      };
      var contentStyle = {
        marginBottom: 3 + 'rem'
      };
      var headingStyle = {
        color: 'white',
        marginTop: 160 + 'px',
        paddingTop: 0 + 'px',
        paddingBottom: 40 + 'px',
        transition: '.5s ease'
      };
      var cardStyle = {
        marginBottom: 0 + 'rem',
        alignSelf: 'center'
      };
      return React.createElement(
        'div',
        { className: 'card rounded-opacity card-animation', style: cardStyle },
        React.createElement(
          'h1',
          { className: 'cover-heading', style: headingStyle },
          'Hello, World!'
        ),
        React.createElement(
          'div',
          { id: 'carouselContent', className: 'carousel slide', 'data-ride': 'carousel', style: contentStyle },
          React.createElement(
            'div',
            { className: 'carousel-inner', role: 'listbox' },
            React.createElement(
              'div',
              { className: 'carousel-item active text-center', style: textStyle },
              React.createElement(
                'h3',
                null,
                'discover great companies'
              )
            ),
            React.createElement(
              'div',
              { className: 'carousel-item text-center', style: textStyle },
              React.createElement(
                'h3',
                null,
                'discover great people'
              )
            ),
            React.createElement(
              'div',
              { className: 'carousel-item text-center', style: textStyle },
              React.createElement(
                'h3',
                null,
                'discover great investors'
              )
            ),
            React.createElement(
              'div',
              { className: 'carousel-item text-center', style: textStyle },
              React.createElement(
                'h3',
                null,
                'discover great schools'
              )
            )
          ),
          React.createElement(
            'a',
            { className: 'carousel-control-prev', href: '#carouselContent', role: 'button', 'data-slide': 'prev' },
            React.createElement('span', { className: 'carousel-control-prev-icon', 'aria-hidden': 'true' }),
            React.createElement(
              'span',
              { className: 'sr-only' },
              'Previous'
            )
          ),
          React.createElement(
            'a',
            { className: 'carousel-control-next', href: '#carouselContent', role: 'button', 'data-slide': 'next' },
            React.createElement('span', { className: 'carousel-control-next-icon', 'aria-hidden': 'true' }),
            React.createElement(
              'span',
              { className: 'sr-only' },
              'Next'
            )
          )
        )
      );
    }
  }]);

  return App;
}(React.Component);

;

ReactDOM.render(React.createElement(App), document.getElementById('app'));
