import React, { useEffect, useState } from "react";
import "./cards.css"

export default function Cards(props) {
    const [visible, setVisible] = useState(false);

    useEffect(() => {
        // Fetch data from backend /mc_server/server_list
        fetch("https://prometheuzdy.cloud/mc_server/server_list", {
            method: "GET",
        })
        .then(response => response.json())  // Convert the response to JSON
        .then(data => {
            console.log(data);  // Log the data
        })
        .catch(error => {
            console.error("Error fetching data:", error);  // Log any errors
        });
    }, []);
    

    return (
        <div>
            HELLO
        </div>
    )
}