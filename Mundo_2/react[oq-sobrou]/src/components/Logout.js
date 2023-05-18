import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { logout } from "../redux/userSlice";

const Logout = () => {
    const [name, setName] = useState("");
    const dispatch = useDispatch();

    const handleLogout = () => {
        dispatch(logout(name));
    }

    return (
        <>
        <form>
            <strong><h1>Logout</h1></strong>
            <p>
                <button type="button" onClick={handleLogout}>Logout</button>
            </p>
            <hr />
        </form>
        </>
    );
}

export default Logout;