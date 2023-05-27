import React, { useEffect, useState } from "react";
import "./App.css";
import { myData } from "./myData.jsx";

function App() {
  const [currentPage, setcurrentPage] = useState(1);

  const data = myData;
  const postsPerPage = 15;
  // let currentPage = 1;
  const pageNumbers: number[] = [];

  function showData() {
    const indexOfLastPage = currentPage * postsPerPage;
    const indexOfFirstPage = indexOfLastPage - postsPerPage;
    const currentPosts = data.slice(indexOfFirstPage, indexOfLastPage);
    // try {
    return currentPosts.map(
      (
        item: {
          userId: number;
          title: string;
          completed: boolean;
        },
        index: number,
      ) => {
        return (
          <tbody key={index}>
            <tr>
              <td>{postsPerPage * (currentPage - 1) + index + 1}</td>
              <td>{item.userId}</td>
              <td>{item.title}</td>
              <td>{item.completed.toString()}</td>
            </tr>
          </tbody>
        );
      },
    );
    // } catch (e) {
    //   alert(e.message)
    // }
  }

  function showPagination() {
    const totalPosts = data.length;

    for (let i = 1; i <= Math.ceil(totalPosts / postsPerPage); i++) {
      pageNumbers.push(i);
    }

    const pagination = (pageNumbers: number) => {
      console.log(pageNumbers);

      // currentPage= pageNumbers ;
      setcurrentPage(pageNumbers);
      showData();

      // this.setState({ currentPage: pageNumbers });
    };

    return (
      <nav>
        <ul className="pagination">
          {pageNumbers.map((number) => (
            <li
              key={number}
              className={currentPage === number
                ? "page-item active"
                : "page-item"}
            >
              <button onClick={() => pagination(number)} className="page-link">
                {number}
              </button>
            </li>
          ))}
        </ul>
      </nav>
    );
  }

  useEffect(() => {
  }, []);

  return (
    <div className="App">
      {
        /* <header className="App-header">
      </header> */
      }

      <div className="container">
        <table className="table align-items-center justify-content-center mb-0">
          <thead>
            <tr>
              <th>S/N</th>
              <th>UserId</th>
              <th>Title</th>
              <th>Completed</th>
            </tr>
          </thead>
          {showData()}
        </table>

        <div style={{ float: "right" }}>
          {showPagination()}
        </div>
      </div>
    </div>
  );
}

export default App;
