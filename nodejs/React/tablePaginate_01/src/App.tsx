import React from 'react';
import logo from './logo.svg';
import './App.css';
import { myData } from "./myData.jsx"

function App() {


  // console.log(myData);

  const data = myData;
  const postsPerPage = 10;
  const currentPage = 1;

  function showData() {

    const indexOfLastPage = currentPage * postsPerPage;
    const indexOfFirstPage = indexOfLastPage - postsPerPage;
    const currentPosts = data.slice(indexOfFirstPage, indexOfLastPage)

    // try {
    return currentPosts.map((item: { userId: string | number | boolean | React.ReactElement<any, string | React.JSXElementConstructor<any>> | React.ReactFragment | React.ReactPortal | null | undefined; title: string | number | boolean | React.ReactElement<any, string | React.JSXElementConstructor<any>> | React.ReactFragment | React.ReactPortal | null | undefined; completed: { toString: () => string | number | boolean | React.ReactElement<any, string | React.JSXElementConstructor<any>> | React.ReactFragment | React.ReactPortal | null | undefined; }; }, index: number) => {
      return (
        <tbody>
          <tr>
            <td>{postsPerPage * (currentPage - 1) + index + 1}</td>
            <td>{item.userId}</td>
            <td>{item.title}</td>
            <td>{item.completed.toString()}</td>
          </tr>
        </tbody>
      )
    })
    // } catch (e) {
    //   alert(e.message)
    // }
  }

  return (
    <div className="App">
      {/* <header className="App-header">
      </header> */}


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

        <div style={{ float: 'right' }}>
          {/* {this.showPagination()} */}
        </div>

      </div>


    </div>
  );
}

export default App;
