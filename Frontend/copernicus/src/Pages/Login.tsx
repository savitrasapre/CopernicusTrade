import React from "react";

export const Login = () => {
  return (
    <div className="container-fluid">
      <main className="form-signin">
        <form action="/action_page.php">
          <div className="form-group">
            <label>Email address:</label>
            <input type="email" className="form-control" id="email" />
          </div>
          <div className="form-group">
            <label>Password:</label>
            <input type="password" className="form-control" id="pwd" />
          </div>
          {/* <div className="checkbox">
    <label><input type="checkbox"> Remember me</label>
  </div> */}
          <button type="submit" className="btn btn-primary">
            Submit
          </button>
        </form>
      </main>
    </div>
  );
};
