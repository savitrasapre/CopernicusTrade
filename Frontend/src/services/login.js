import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";


//Temporary BASE_URL string. Depends on where you host this
export const BASE_URL = 'http://localhost:8000';

export const accountApi = createApi({
  reducerPath: "accountApi",
  baseQuery: fetchBaseQuery({ baseUrl: BASE_URL + "/account/" }),
  endpoints: (builder) => ({
    loginUser: builder.query({
      query: ({ username, password }) => `login/${username}/${password}`,
    }),
  }),
});

export const { useLazyLoginUserQuery } = accountApi;
