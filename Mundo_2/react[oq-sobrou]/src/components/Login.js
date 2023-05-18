import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { changeUser } from "../redux/userSlice";

const Login = () => {
    const [name, setName] = useState("");
    const dispatch = useDispatch();

    const handleLogin = () => {
        dispatch(changeUser(name));
    }

    return (
        <>
        <form>
            <strong><h1>Login</h1></strong>
            <p>
                <input type="text" placeholder="Nome" onChange={(e) => setName(e.target.value)}></input>
                <button type="button" onClick={handleLogin}>Login</button>
            </p>
            <hr />
        </form>
        </>
    );
}

export default Login;