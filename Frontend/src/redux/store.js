import { configureStore } from "@reduxjs/toolkit";
import tokenReducer from "./features/token/tokenSlice";
import { accountApi } from "../services/login";
import { setupListeners } from "@reduxjs/toolkit/query";

export const store = configureStore({
  reducer: {
    //token: tokenReducer,
    [accountApi.reducerPath]: accountApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(accountApi.middleware),
});

setupListeners(store.dispatch);
