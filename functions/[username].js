export async function onRequest(context) {
    const { username } = context.params;
    
    try {
        // Pake cloudscraper di Worker (pake fetch biasa)
        const url = `https://www.tiktok.com/@${username}`;
        const response = await fetch(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        });
        
        const html = await response.text();
        
        // Parse followerCount pake regex
        const match = html.match(/"followerCount":(\d+)/);
        const followers = match ? parseInt(match[1]) : 0;
        
        // Parse data lain
        const nicknameMatch = html.match(/"nickname":"([^"]+)"/);
        const nickname = nicknameMatch ? nicknameMatch[1] : username;
        
        const avatarMatch = html.match(/"avatarLarger":"([^"]+)"/);
        const avatar = avatarMatch ? avatarMatch[1] : '';
        
        return new Response(JSON.stringify({
            success: true,
            profile: {
                username: username,
                nickname: nickname,
                avatar: avatar,
                followers: followers,
                following: 0,
                likes: 0,
                videos: 0,
                bio: '',
                verified: false
            }
        }), {
            headers: { 'Content-Type': 'application/json' }
        });
        
    } catch (error) {
        return new Response(JSON.stringify({
            success: false,
            error: error.message
        }), {
            status: 500,
            headers: { 'Content-Type': 'application/json' }
        });
    }
}