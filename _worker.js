export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    
    // Serve static files
    if (url.pathname === '/' || url.pathname.startsWith('/static/')) {
      return env.ASSETS.fetch(request);
    }
    
    // API requests
    if (url.pathname.startsWith('/api/')) {
      return env.ASSETS.fetch(request);
    }
    
    // Default: index.html
    return env.ASSETS.fetch(request);
  }
};