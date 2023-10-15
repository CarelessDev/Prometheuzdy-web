import React, { useEffect, useState } from "react";
import "./embed.css"

import java_logo from "./java_icon.png";
import bedrock_logo from "./Bedrock_icon.png";
import public_logo from "./public.svg";
import private_logo from "./private.svg";

export default function Embed(props) {

    return (
        <div className="embed">
            <div className="embed-title">
                <h1>{props.title}</h1>

                <div className="embed-techinfo">
                    <p>{props.ip}:{props.port}</p>
                    
                </div>

                <div className="info">
                    <p>{props.info}</p>
                </div>
            </div>

            <div className="version">
                <img 
                    src={props.version === "Java" ? java_logo : bedrock_logo} 
                />
                <img
                    src={props.access === "public" ? public_logo : private_logo}
                />
            </div>
        </div>
    )
}