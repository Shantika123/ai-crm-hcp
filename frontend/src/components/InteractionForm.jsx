import { useSelector } from "react-redux";

function InteractionForm() {

  const interaction = useSelector((state) => state.interaction);


  // Format YYYY-MM-DD -> DD-MM-YYYY
  const formatDate = (date) => {
    if (!date) return "";

    return date.split("-").reverse().join("-");
  };


  // Format HH:MM:SS -> HH:MM AM/PM
  const formatTime = (time) => {
    if (!time) return "";

    const [hours, minutes] = time.split(":");

    const date = new Date();

    date.setHours(hours);
    date.setMinutes(minutes);

    return date.toLocaleTimeString([], {
      hour: "2-digit",
      minute: "2-digit",
      hour12: true
    });
  };


  return (
    <div className="left-panel">

      <h2>Interaction Details</h2>


      <div className="form-group">
        <label>HCP Name</label>
        <input
          type="text"
          value={interaction.hcpName || ""}
          readOnly
        />
      </div>


      <div className="row">

        <div className="form-group">
          <label>Date</label>

          <input
            type="text"
            value={formatDate(interaction.date)}
            readOnly
          />

        </div>


        <div className="form-group">
          <label>Time</label>

          <input
            type="text"
            value={formatTime(interaction.time)}
            readOnly
          />

        </div>

      </div>


      <div className="form-group">
        <label>Interaction Type</label>

        <input
          type="text"
          value={interaction.interactionType || ""}
          readOnly
        />

      </div>


      <div className="form-group">
        <label>Topics Discussed</label>

        <textarea
          rows="4"
          value={interaction.topics || ""}
          readOnly
        />

      </div>


      <div className="form-group">
        <label>Materials Shared</label>

        <input
          type="text"
          value={interaction.materials || ""}
          readOnly
        />

      </div>


      <div className="form-group">
        <label>Sentiment</label>

        <input
          type="text"
          value={interaction.sentiment || ""}
          readOnly
        />

      </div>


      <div className="form-group">
        <label>Outcomes</label>

        <textarea
          rows="3"
          value={interaction.outcomes || ""}
          readOnly
        />

      </div>


      <div className="form-group">
        <label>Follow-up</label>

        <input
          type="text"
          value={formatDate(interaction.followUp)}
          readOnly
        />

      </div>


    </div>
  );
}

export default InteractionForm;