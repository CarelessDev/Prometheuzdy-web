import React from "react";
import "./logout.css"

export default function LogOut() {

    let isLoggedIn = Boolean(localStorage.getItem('access_token'));
    
    // If not logged in, do not render the component
    if (!isLoggedIn || localStorage.getItem('access_token') === 'undefined') {
        return null;
    }


    return (
        <div className="logout">
            <a onClick={logoutfunc} id="logoutButton">
                <i className="material-icons-outlined">logout</i>
            </a>
        </div>
    );
}

function logoutfunc() {
    // Remove the JWT from localStorage
    localStorage.removeItem('access_token');

    // Redirect to login or home page
    window.location.href = '/';
}
