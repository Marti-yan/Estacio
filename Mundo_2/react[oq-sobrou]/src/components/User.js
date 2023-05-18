import React from "react";
import { useSelector } from "react-redux";
import { selectUser } from "../redux/userSlice";

const User = () => {
    const { name } = useSelector(selectUser);

    return (
        <>
            <strong><h1>Usuário: {name}</h1></strong>
        </>
    )
}

export default User;