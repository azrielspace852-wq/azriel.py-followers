const username = 'azriel.py';

async function fetchProfile() {
    try {
        const res = await fetch(`/api/profile/${username}`);
        const data = await res.json();
        
        if (data.success) {
            const profile = data.profile;
            document.getElementById('avatar').src = profile.avatar || '';
            document.getElementById('nickname').textContent = profile.nickname || 'Azriel.py';
            document.getElementById('followerCount').textContent = profile.followers.toLocaleString();
            document.getElementById('following').textContent = profile.following.toLocaleString();
            document.getElementById('likes').textContent = profile.likes.toLocaleString();
            document.getElementById('videos').textContent = profile.videos.toLocaleString();
            document.getElementById('statusText').textContent = '🟢 Live';
            document.getElementById('updateTime').textContent = `Update: ${new Date().toLocaleTimeString('id-ID')}`;
        }
    } catch (error) {
        document.getElementById('statusText').textContent = '🔴 Error';
    }
}

fetchProfile();
setInterval(fetchProfile, 10000);