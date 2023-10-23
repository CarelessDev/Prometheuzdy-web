import { useEffect, useState } from 'react';
import md5 from 'blueimp-md5';
import './UserProfile.css'

export default function UserProfile() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem('access_token');
    if (token) {
      fetch('https://prometheuzdy.cloud/api/user', {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
      .then(response => response.json())
      .then(data => {
        setUser(data);

        // Disable Login and Register links
        document.getElementById('loginLink').style.display = 'none';
        document.getElementById('registerLink').style.display = 'none';
      });
    }
  }, []);

  if (!user) {
    return null;
  }

  return (
    <div id="userProfile">
      <img 
        id="avatar" 
        src={`https://www.gravatar.com/avatar/${md5(user.email)}`} 
        alt="Profile Picture" 
        width="37" 
        height="37"
      />
      <a id="username">{user.username}</a>
    </div>
  );
}

