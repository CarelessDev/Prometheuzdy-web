import React from 'react';
import './MinecraftPromo.css'

// Import Images
import minecraft_server from './minecraft-server.png';

const MinecraftPromo = () => {

  return (
<div className="minecraft-promo">
    <div className="info">
        <h1>Join Our Minecraft Server!</h1>
        <p>Feel free to reach out to us to request access and hang out together in Minecraft by clicking the button below:</p>
        <a href="/mc" className="join-button">Join Now</a>
    </div>
    <div className="image">
        <img src={minecraft_server} alt="Minecraft Background"/>
    </div>
</div>

  );
};

export default MinecraftPromo;