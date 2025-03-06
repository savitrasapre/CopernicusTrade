import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const accountApi = createApi({
  reducerPath: "accountApi",
  baseQuery: fetchBaseQuery({ baseUrl: "http://localhost:8000/account/" }),
  endpoints: (builder) => ({
    loginUser: builder.query({
      query: ({ username, password }) => `login/${username}/${password}`,
    }),
  }),
});

export const { useLazyLoginUserQuery } = accountApi;
