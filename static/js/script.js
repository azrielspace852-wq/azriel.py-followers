const username = 'azriel.py';
const apiBase = '/api';

let updateInterval = null;

// DOM Elements
const avatar = document.getElementById('avatar');
const nickname = document.getElementById('nickname');
const bio = document.getElementById('bio');
const verified = document.getElementById('verified');
const followerCount = document.getElementById('followerCount');
const following = document.getElementById('following');
const likes = document.getElementById('likes');
const videos = document.getElementById('videos');
const statusText = document.getElementById('statusText');
const updateTime = document.getElementById('updateTime');

// Init
document.addEventListener('DOMContentLoaded', () => {
    fetchProfile();
    startAutoUpdate();
});

function startAutoUpdate() {
    updateInterval = setInterval(fetchProfile, 10000);
}

async function fetchProfile() {
    try {
        const res = await fetch(`${apiBase}/profile/${username}`);
        const data = await res.json();
        
        if (data.success) {
            const profile = data.profile;
            
            // Update UI
            if (profile.avatar) {
                avatar.src = profile.avatar;
            }
            nickname.textContent = profile.nickname || 'Azriel.py';
            bio.textContent = profile.bio || '✨';
            
            if (profile.verified) {
                verified.style.display = 'flex';
            } else {
                verified.style.display = 'none';
            }
            
            // Update stats
            followerCount.textContent = profile.followers.toLocaleString();
            following.textContent = profile.following.toLocaleString();
            likes.textContent = profile.likes.toLocaleString();
            videos.textContent = profile.videos.toLocaleString();
            
            // Status
            statusText.textContent = '🟢 Live';
            statusText.style.color = '#4ade80';
            
            const now = new Date();
            updateTime.textContent = `Update: ${now.toLocaleTimeString('id-ID')}`;
            
        } else {
            statusText.textContent = '🔴 Error';
            statusText.style.color = '#ef4444';
            updateTime.textContent = `Error: ${data.error || 'Gagal fetch'}`;
        }
    } catch (error) {
        console.error('Fetch error:', error);
        statusText.textContent = '🔴 Error';
        statusText.style.color = '#ef4444';
        updateTime.textContent = `Error: ${error.message}`;
    }
}