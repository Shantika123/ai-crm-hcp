import Header from "./components/Header";
import InteractionForm from "./components/InteractionForm";
import AIChat from "./components/AIChat";
import "./index.css";

function App() {
  return (
    <>
      <Header />

      <div className="container">
        <InteractionForm />
        <AIChat />
      </div>
    </>
  );
}

export default App;