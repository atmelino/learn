import React, { useEffect, useState } from "react";
import "./App.css";
import { myData } from "./myData.jsx";

function App() {
  const [features, setFeatures] = useState([
    {
      "userId": 1,
      "id": 1,
      "title": "delectus aut autem",
      "completed": false,
    },
  ]);
  const [html1, sethtml1] = useState("");

  // console.log(myData);

  // for (const x of myData) {
  // console.log(x);
  // setFeatures(features.push(x))

  // }

  const data = myData;
  const postsPerPage = 15;
  const currentPage = 1;

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

  useEffect(() => {
    // getFeatures('home')
    //   .then(setFeatures) // chain returned promise and pass setFeatures to update features
    //    setFeatures(myData);

    // sethtml1(showData());
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
          {/* {this.showPagination()} */}
        </div>
      </div>
    </div>
  );
}

export default App;
