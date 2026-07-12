import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  hcpName: "",
  date: "",
  time: "",
  interactionType: "",
  topics: "",
  materials: "",
  sentiment: "",
  outcomes: "",
  followUp: ""
};

const interactionSlice = createSlice({
  name: "interaction",
  initialState,

  reducers: {

    updateInteraction: (state, action) => {

      Object.keys(action.payload).forEach((key) => {

        // Update only if value is not empty/null/undefined
        if (
          action.payload[key] !== "" &&
          action.payload[key] !== null &&
          action.payload[key] !== undefined
        ) {
          state[key] = action.payload[key];
        }

      });

    },

    clearInteraction: () => initialState

  }
});

export const {
  updateInteraction,
  clearInteraction
} = interactionSlice.actions;

export default interactionSlice.reducer;