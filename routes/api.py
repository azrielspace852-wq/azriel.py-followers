from flask import Blueprint, jsonify, request, current_app
from core import TikTokScraper
from utils import CacheManager

api_bp = Blueprint('api', __name__, url_prefix='/api')

# Cache dengan TTL 30 detik
cache = CacheManager(ttl_seconds=30)

@api_bp.route('/followers/<username>')
def get_followers(username):
    # Cek cache dulu
    cached = cache.get(f'followers_{username}')
    if cached:
        return jsonify({
            'success': True,
            'username': username,
            'followers': cached,
            'formatted': f"{cached:,}",
            'cached': True
        })
    
    # Fetch fresh
    scraper = TikTokScraper()
    data = scraper.get_profile_data(username)
    
    if data:
        cache.set(f'followers_{username}', data['followers'])
        cache.set(f'profile_{username}', data)
        return jsonify({
            'success': True,
            'username': username,
            'followers': data['followers'],
            'formatted': f"{data['followers']:,}",
            'profile': {
                'nickname': data['nickname'],
                'avatar': data['avatar'],
                'bio': data['bio'],
                'verified': data['verified'],
                'following': data['following'],
                'likes': data['likes'],
                'videos': data['videos']
            },
            'cached': False
        })
    else:
        return jsonify({
            'success': False,
            'username': username,
            'error': 'Gagal mengambil data'
        }), 500

@api_bp.route('/profile/<username>')
def get_profile(username):
    cached = cache.get(f'profile_{username}')
    if cached:
        return jsonify({
            'success': True,
            'profile': cached,
            'cached': True
        })
    
    scraper = TikTokScraper()
    data = scraper.get_profile_data(username)
    
    if data:
        cache.set(f'profile_{username}', data)
        return jsonify({
            'success': True,
            'profile': data,
            'cached': False
        })
    else:
        return jsonify({
            'success': False,
            'error': 'Gagal mengambil data'
        }), 500