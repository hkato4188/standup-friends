import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import "./css/styles.css";

const initialState = {
  name: "",
  email: "",
  password: "",
};

function Login({ updateUser }) {
  const [signUp, setSignUp] = useState(false);
  const [formState, setFormState] = useState(initialState);
  const [errors, setErrors] = useState(null);
  const history = useHistory();

  const changeFormState = (event) => {
    const { name, value } = event.target;
    setFormState({ ...formState, [name]: value });
  };

  const handleClick = () => setSignUp((signUp) => !signUp);
  // 3.✅ Finish building the authentication form
  // 3.3 on submit create a POST.
  const postToLoginOrSignup = (event) => {
    event.preventDefault();

    const postRequest = {
      method: "POST",
      headers: {
        "content-type": "application/json",
        accept: "application/json",
      },
      body: JSON.stringify(formState),
    };

    // 3.4 There is a button that toggles the component between login and sign up.
    // if signUp is true use the path '/signup' else use '/login' (we will be writing login soon)
    fetch(
      signUp ? "http://localhost:5555/signup" : "http://localhost:5555/login",
      postRequest
    )
      .then((r) => r.json())
      .then((userData) => {
        if (userData.errors) {
          setErrors(userData.errors);
        } else {
          setErrors(null);
          updateUser(userData);
          history.push("/todolists");
        }
      });
  };
  // 3.4 On a successful POST add the user to state (updateUser is passed down from app through props) and redirect to the Home page.
  // 4.✅ return to server/app.py to build the next route

  return (
    <>
      <h2 style={{ color: "red" }}>
        {" "}
        {errors ? errors.map((error) => <h5>{error}</h5>) : null}
      </h2>
      <h2>Please Log in or Sign up!</h2>
      <h2>{signUp ? "Already a member?" : "Not a member?"}</h2>
      <button onClick={handleClick}>
        {signUp ? "Log In!" : "Register now!"}
      </button>
      <h1>Please enter your username or email to log in:</h1>
      <form className="login-form" onSubmit={postToLoginOrSignup}>
        <label>Username</label>
        <input
          className="login-input"
          type="text"
          name="name"
          placeholder="Enter email or Username"
          value={formState.name}
          onChange={changeFormState}
        />
        <>
          <label>Email</label>
          <input
            className="login-input"
            type="email"
            name="email"
            placeholder="Enter email or Username"
            value={formState.email}
            onChange={changeFormState}
          />
        </>
        <>
          <label>Password</label>
          <input
            className="login-input"
            type="password"
            name="password"
            placeholder="Enter password"
            value={formState.password}
            onChange={changeFormState}
          />
        </>
        <input
          className="login-button"
          type="submit"
          value={signUp ? "Sign Up!" : "Log In!"}
        />
      </form>
    </>
  );
}

export default Login;
