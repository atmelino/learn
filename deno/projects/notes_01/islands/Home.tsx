import { useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import TextArea from "../components/Textarea.tsx";
import Counter from "../islands/Counter.tsx";

const Home = () => {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);

  // const onShare = async () => {
  //   setLoading(true);

  //   const res = await fetch("/api/create", {
  //     method: "POST",
  //     body: JSON.stringify({
  //       content: text,
  //       type: language,
  //     }),
  //   });
  //   const data = await res.json();
  //   window.location.pathname = `/${data.id}`;
  // };

  const onShare = () => {
    alert("hello");
  };

  return (
    <div>
      <TextArea
        placeholder="Write a new note..."
        rows={3}
        onChange={(e) => setText((e.target as HTMLInputElement).value)}
      />
      <div class="flex gap-2 w-full mt-4">
        <Button
          onClick={onShare}
          disabled={loading}
          className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded w-1/2"
        >
          {loading ? "Saving..." : "Add"}
        </Button>
      </div>
      <div>
        <Counter start={3} />
      </div>
    </div>
  );
};

export default Home;
