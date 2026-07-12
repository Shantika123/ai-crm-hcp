import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { updateInteraction } from "../redux/interactionSlice";
import api from "../api/api";

function AIChat() {

  const dispatch = useDispatch();

  const interaction = useSelector(
    (state) => state.interaction
  );

  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);


  const [chatHistory, setChatHistory] = useState([
    {
      sender: "ai",
      text: "👋 Hello! Describe your interaction with the HCP."
    }
  ]);



  const addAIMessage = (text) => {

    setChatHistory((prev) => [
      ...prev,
      {
        sender: "ai",
        text,
      },
    ]);

  };



  const addUserMessage = (text) => {

    setChatHistory((prev) => [
      ...prev,
      {
        sender: "user",
        text,
      },
    ]);

  };




  const handleSend = async () => {

    if (!message.trim()) return;


    addUserMessage(message);


    try {

      setLoading(true);


      const response = await api.post(
        "/chat",
        {
          message,
          currentData: interaction,
        }
      );


      console.log(
        "AI RESPONSE:",
        response.data
      );



      if (response.data.error) {

        addAIMessage(
          "❌ " + response.data.error
        );

        setMessage("");

        return;

      }





      // ==========================
      // SUMMARY TOOL
      // ==========================

      if (response.data.summary) {

        addAIMessage(
          response.data.summary
        );

        setMessage("");

        return;

      }





      // ==========================
      // FOLLOW-UP TOOL
      // ==========================

      if (response.data.followup) {

        addAIMessage(
          response.data.followup
        );

        setMessage("");

        return;

      }





      // ==========================
      // HCP INSIGHT TOOL
      // ==========================

      if (response.data.insight) {

        addAIMessage(
          response.data.insight
        );

        setMessage("");

        return;

      }





      // ==========================
      // HISTORY TOOL
      // ==========================

      if (response.data.history) {


        const doctor =
          response.data.doctor || "Doctor";


        const historyText =
          `📋 Interaction History for ${doctor}\n\n` +
          response.data.history
            .map(
              (item) => `• ${item}`
            )
            .join("\n");



        addAIMessage(
          historyText
        );


        setMessage("");

        return;

      }





      // ==========================
      // LOG / EDIT TOOL
      // ==========================

      if (
        response.data.hcpName ||
        response.data.date ||
        response.data.sentiment ||
        response.data.topics
      ) {


        dispatch(
          updateInteraction(
            response.data
          )
        );


        addAIMessage(
          "✅ Interaction updated successfully."
        );


        setMessage("");

        return;

      }





      addAIMessage(
        "Response received."
      );


      setMessage("");



    }

    catch(error) {


      console.error(
        error
      );


      addAIMessage(
        "❌ Failed to contact AI backend."
      );


    }

    finally {

      setLoading(false);

    }

  };





  return (

    <div className="right-panel">


      <h2>
        🤖 AI Assistant
      </h2>




      <div className="chat-box">


        {chatHistory.map(
          (chat, index) => (

            <div
              key={index}
              className={
                chat.sender === "user"
                  ? "user-message"
                  : "ai-message"
              }
            >

              {chat.text}

            </div>

          )
        )}


      </div>





      <div className="input-area">


        <input

          type="text"

          placeholder="Today I met Dr Smith..."

          value={message}

          onChange={
            (e) =>
              setMessage(
                e.target.value
              )
          }


          onKeyDown={
            (e) => {

              if(e.key === "Enter"){

                handleSend();

              }

            }
          }

        />




        <button

          onClick={handleSend}

          disabled={loading}

        >

          {
            loading
              ? "Thinking..."
              : "Send"
          }


        </button>


      </div>



    </div>

  );

}


export default AIChat;