from datetime import datetime, timedelta
from typing import Optional, Any

class CacheManager:
    def __init__(self, ttl_seconds=30):
        self.ttl = timedelta(seconds=ttl_seconds)
        self.cache = {}
        self.last_fetch = {}
    
    def get(self, key: str) -> Optional[Any]:
        if key in self.cache and key in self.last_fetch:
            if datetime.now() - self.last_fetch[key] < self.ttl:
                return self.cache[key]
            else:
                # Expired
                del self.cache[key]
                del self.last_fetch[key]
        return None
    
    def set(self, key: str, value: Any):
        self.cache[key] = value
        self.last_fetch[key] = datetime.now()
    
    def clear(self):
        self.cache.clear()
        self.last_fetch.clear()