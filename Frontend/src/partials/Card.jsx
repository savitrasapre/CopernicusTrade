import React, { useEffect, useState } from "react";
import { useLazyLoginUserQuery } from "../services/login";
import { useNavigate } from "react-router-dom";
// Import utilities
//import { adjustColorOpacity, getCssVariable } from '../../utils/Utils';

export const LoginCard = () => {
  const navigate = useNavigate();

  const [formValues, setFormValues] = useState({
    username: "",
    password: "",
  });

  const onValueChangeHandler = (e) => {
    setFormValues({
      ...formValues,
      [e.target.name]: e.target.value,
    });
  };

  const [trigger, { data, isLoading, error }] = useLazyLoginUserQuery();

  const onLoginClick = () => {
    console.log(formValues);
    trigger({
      username: formValues?.username,
      password: formValues?.password,
    });
  };
  useEffect(() => {
    console.log(data);
    if (data) {
      navigate("/dashboard");
    }
  }, [data]);

  return (
    <div class="w-full max-w-xs">
      <form class="bg-white bg-white dark:bg-gray-800 shadow-xs rounded-xl shadow-md rounded px-8 pt-6 pb-8 mb-4">
        <div class="mb-4">
          <label class="block text-white text-sm font-bold mb-2" for="username">
            Username
          </label>
          <input
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="username"
            name="username"
            type="text"
            placeholder="Username"
            onChange={onValueChangeHandler}
          />
        </div>
        <div class="mb-6">
          <label class="block text-white text-sm font-bold mb-2" for="password">
            Password
          </label>
          <input
            class="shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
            id="password"
            name="password"
            type="password"
            placeholder="******************"
            onChange={onValueChangeHandler}
          />
          {error && (
            <p class="text-red-500 text-xs italic">Please choose a password.</p>
          )}
        </div>
        <div class="flex items-center justify-between">
          <button
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            type="button"
            onClick={onLoginClick}
          >
            Sign In
          </button>
          {/* <a
            class="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800"
            href="#"
          >
            Forgot Password?
          </a> */}
        </div>
      </form>
      <p class="text-center text-gray-500 text-xs">
        &copy;2025 Copernicus Inc. All rights reserved.
      </p>
    </div>
  );
};
