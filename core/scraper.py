import cloudscraper
import re
import json
import time
from typing import Optional, Dict

class TikTokScraper:
    def __init__(self):
        self.scraper = cloudscraper.create_scraper(
            browser={
                'browser': 'chrome',
                'platform': 'windows',
                'mobile': False
            }
        )
        self.last_request = 0
        self.min_delay = 3
    
    def get_profile_data(self, username: str) -> Optional[Dict]:
        """Ambil semua data profil sekaligus"""
        url = f"https://www.tiktok.com/@{username}"
        
        # Delay biar aman
        now = time.time()
        if now - self.last_request < self.min_delay:
            time.sleep(self.min_delay - (now - self.last_request))
        
        try:
            res = self.scraper.get(url, timeout=15)
            self.last_request = time.time()
            
            # Cari data dari JSON
            match = re.search(r'<script[^>]*id="__UNIVERSAL_DATA_FOR_REHYDRATION__"[^>]*>(.*?)</script>', res.text)
            if not match:
                return None
                
            data = json.loads(match.group(1))
            
            try:
                user_data = data['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']
                stats = user_data.get('stats', {})
                user = user_data.get('user', {})
                
                return {
                    'username': user.get('uniqueId', username),
                    'nickname': user.get('nickname', ''),
                    'avatar': user.get('avatarLarger', user.get('avatarMedium', user.get('avatarThumb', ''))),
                    'followers': stats.get('followerCount', 0),
                    'following': stats.get('followingCount', 0),
                    'likes': stats.get('heartCount', 0),
                    'videos': stats.get('videoCount', 0),
                    'bio': user.get('signature', ''),
                    'verified': user.get('verified', False)
                }
            except:
                return None
                
        except Exception as e:
            print(f"Scraping error: {e}")
            return None
    
    def get_follower_count(self, username: str) -> Optional[int]:
        data = self.get_profile_data(username)
        return data.get('followers') if data else None