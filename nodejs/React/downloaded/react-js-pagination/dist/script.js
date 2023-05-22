class TodoApp extends React.Component {
  constructor() {
    super();
    this.state = {
      todos: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
      currentPage: 1,
      todosPerPage: 3,
      upperPageBound: 3,
      lowerPageBound: 0,
      isPrevBtnActive: 'disabled',
      isNextBtnActive: '',
      pageBound: 3 };

    this.handleClick = this.handleClick.bind(this);
    this.btnDecrementClick = this.btnDecrementClick.bind(this);
    this.btnIncrementClick = this.btnIncrementClick.bind(this);
    this.btnNextClick = this.btnNextClick.bind(this);
    this.btnPrevClick = this.btnPrevClick.bind(this);
    // this.componentDidMount = this.componentDidMount.bind(this);
    this.setPrevAndNextBtnClass = this.setPrevAndNextBtnClass.bind(this);
  }
  componentDidUpdate() {
    $("ul li.active").removeClass('active');
    $('ul li#' + this.state.currentPage).addClass('active');
  }
  handleClick(event) {
    let listid = Number(event.target.id);
    this.setState({
      currentPage: listid });

    $("ul li.active").removeClass('active');
    $('ul li#' + listid).addClass('active');
    this.setPrevAndNextBtnClass(listid);
  }
  setPrevAndNextBtnClass(listid) {
    let totalPage = Math.ceil(this.state.todos.length / this.state.todosPerPage);
    this.setState({ isNextBtnActive: 'disabled' });
    this.setState({ isPrevBtnActive: 'disabled' });
    if (totalPage === listid && totalPage > 1) {
      this.setState({ isPrevBtnActive: '' });
    } else
    if (listid === 1 && totalPage > 1) {
      this.setState({ isNextBtnActive: '' });
    } else
    if (totalPage > 1) {
      this.setState({ isNextBtnActive: '' });
      this.setState({ isPrevBtnActive: '' });
    }
  }
  btnIncrementClick() {
    this.setState({ upperPageBound: this.state.upperPageBound + this.state.pageBound });
    this.setState({ lowerPageBound: this.state.lowerPageBound + this.state.pageBound });
    let listid = this.state.upperPageBound + 1;
    this.setState({ currentPage: listid });
    this.setPrevAndNextBtnClass(listid);
  }
  btnDecrementClick() {
    this.setState({ upperPageBound: this.state.upperPageBound - this.state.pageBound });
    this.setState({ lowerPageBound: this.state.lowerPageBound - this.state.pageBound });
    let listid = this.state.upperPageBound - this.state.pageBound;
    this.setState({ currentPage: listid });
    this.setPrevAndNextBtnClass(listid);
  }
  btnPrevClick() {
    if ((this.state.currentPage - 1) % this.state.pageBound === 0) {
      this.setState({ upperPageBound: this.state.upperPageBound - this.state.pageBound });
      this.setState({ lowerPageBound: this.state.lowerPageBound - this.state.pageBound });
    }
    let listid = this.state.currentPage - 1;
    this.setState({ currentPage: listid });
    this.setPrevAndNextBtnClass(listid);
  }
  btnNextClick() {
    if (this.state.currentPage + 1 > this.state.upperPageBound) {
      this.setState({ upperPageBound: this.state.upperPageBound + this.state.pageBound });
      this.setState({ lowerPageBound: this.state.lowerPageBound + this.state.pageBound });
    }
    let listid = this.state.currentPage + 1;
    this.setState({ currentPage: listid });
    this.setPrevAndNextBtnClass(listid);
  }
  render() {
    const { todos, currentPage, todosPerPage, upperPageBound, lowerPageBound, isPrevBtnActive, isNextBtnActive } = this.state;
    // Logic for displaying current todos
    const indexOfLastTodo = currentPage * todosPerPage;
    const indexOfFirstTodo = indexOfLastTodo - todosPerPage;
    const currentTodos = todos.slice(indexOfFirstTodo, indexOfLastTodo);

    const renderTodos = currentTodos.map((todo, index) => {
      return /*#__PURE__*/React.createElement("li", { key: index }, todo);
    });

    // Logic for displaying page numbers
    const pageNumbers = [];
    for (let i = 1; i <= Math.ceil(todos.length / todosPerPage); i++) {
      pageNumbers.push(i);
    }

    const renderPageNumbers = pageNumbers.map(number => {
      if (number === 1 && currentPage === 1) {
        return /*#__PURE__*/(
          React.createElement("li", { key: number, className: "active", id: number }, /*#__PURE__*/React.createElement("a", { href: "#", id: number, onClick: this.handleClick }, number)));

      } else
      if (number < upperPageBound + 1 && number > lowerPageBound) {
        return /*#__PURE__*/(
          React.createElement("li", { key: number, id: number }, /*#__PURE__*/React.createElement("a", { href: "#", id: number, onClick: this.handleClick }, number)));

      }
    });
    let pageIncrementBtn = null;
    if (pageNumbers.length > upperPageBound) {
      pageIncrementBtn = /*#__PURE__*/React.createElement("li", { className: "" }, /*#__PURE__*/React.createElement("a", { href: "#", onClick: this.btnIncrementClick }, " \u2026 "));
    }
    let pageDecrementBtn = null;
    if (lowerPageBound >= 1) {
      pageDecrementBtn = /*#__PURE__*/React.createElement("li", { className: "" }, /*#__PURE__*/React.createElement("a", { href: "#", onClick: this.btnDecrementClick }, " \u2026 "));
    }
    let renderPrevBtn = null;
    if (isPrevBtnActive === 'disabled') {
      renderPrevBtn = /*#__PURE__*/React.createElement("li", { className: isPrevBtnActive }, /*#__PURE__*/React.createElement("span", { id: "btnPrev" }, " Prev "));
    } else
    {
      renderPrevBtn = /*#__PURE__*/React.createElement("li", { className: isPrevBtnActive }, /*#__PURE__*/React.createElement("a", { href: "#", id: "btnPrev", onClick: this.btnPrevClick }, " Prev "));
    }
    let renderNextBtn = null;
    if (isNextBtnActive === 'disabled') {
      renderNextBtn = /*#__PURE__*/React.createElement("li", { className: isNextBtnActive }, /*#__PURE__*/React.createElement("span", { id: "btnNext" }, " Next "));
    } else
    {
      renderNextBtn = /*#__PURE__*/React.createElement("li", { className: isNextBtnActive }, /*#__PURE__*/React.createElement("a", { href: "#", id: "btnNext", onClick: this.btnNextClick }, " Next "));
    }
    return /*#__PURE__*/(
      React.createElement("div", null, /*#__PURE__*/
      React.createElement("ul", null,
      renderTodos), /*#__PURE__*/

      React.createElement("ul", { className: "pagination" },
      renderPrevBtn,
      pageDecrementBtn,
      renderPageNumbers,
      pageIncrementBtn,
      renderNextBtn)));



  }}



ReactDOM.render( /*#__PURE__*/
React.createElement(TodoApp, null),
document.getElementById('app'));