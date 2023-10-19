import { useContext, useEffect } from "react";
import { useHistory } from "react-router-dom";
import { UserContext } from "../context/user";
import Login from "./Login";
import Main from "./Main";

function Authenticate() {
  const { user, updateUser } = useContext(UserContext);
  const history = useHistory();

  const fetchUser = () => {
    fetch("/auto_login").then((r) => {
      if (r.status === 200) {
        r.json().then((usr) => {
          updateUser(usr);
        });
      } else {
        console.log("no user logged in");
        history.push("/login");
      }
    });
  };

  useEffect(() => {
    fetchUser();
  }, []);

  if (user) {
    return <Main />;
  } else {
    return <Login />;
  }
}

export default Authenticate;
