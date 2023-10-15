import React, { useEffect, useState } from "react";
import "../styles/components/card.css"

export default function Card(props) {
    const [visible, setVisible] = useState(false);

    useEffect(() => {
        setTimeout(() => {
            setVisible(true);
        }, 1000);
    }, []);

    return (
        <div>
            <div className={`card ${visible ? "visible" : ""}`}>
                <h2>{props.title}</h2>
                <p>{props.description}</p>
            </div>
        </div>
    )
}