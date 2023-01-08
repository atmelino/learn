import { render } from 'preact';
import { useState } from 'preact/hooks';


const MyButton = () => {
  const [clicked, setClicked] = useState(false)

  const handleClick = () => {
    setClicked(true)
  }

  return (
    <button onClick={handleClick}>
      {clicked ? 'Clicked' : 'No clicks yet'}
    </button>
  )
}
function App() {
  const clicked = () => {
    // increment count by 1 here
  }

  return (
    <div>
      <p class="count">Count:</p>
      <MyButton style={{ color: 'purple' }} onClick={clicked}>Click me</MyButton>
    </div>
  )
}

render(<App />, document.getElementById("app"));



