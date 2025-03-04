import React, { useState } from "react";

import Header from "../partials/Header";
import { LoginCard } from "../partials/Card";

export const Login = () => {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div className="flex h-screen overflow-hidden">
      {/* Content area */}
      <div className="relative flex flex-col flex-1 overflow-y-auto overflow-x-hidden">
        {/*  Site header */}
        <Header sidebarOpen={sidebarOpen} setSidebarOpen={setSidebarOpen} />
        <main className="grow">
          <div className="flex items-center justify-center h-screen px-4 sm:px-6 lg:px-8 py-8 w-full max-w-9xl mx-auto">
            <LoginCard />
          </div>
        </main>
      </div>
    </div>
  );
};
