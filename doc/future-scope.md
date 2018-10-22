# Future Scope


## Use Case:
Once deployed suppose this application became very famous and started to receive a ton of traffic. Your application now contains metadata about 5M movies and receives 15M API hits per day both from anonymous as well as authenticated users. Suggest an  architecture to scale up this system to 5x of these specs. You can also think of potential bottlenecks at all layers of the stack and how will you solve for these.


## Recommendations/Analysis:
- Analytics
    + provided by host (e.g: heroku, aws)
    + self exploration of tools that can be run on server (awstats)
    + Django/framework level packages
    + Misc: Google analytics
- Vertical scalability
- Horizontal scalability
- Code
- Documentation
- Rethink on tech-stack:
    + DB
    + programing language
- Access control
    + IP, ddos attack (cloudflare)
    + region level
    + user level (drf throatling):
        * anonymous
        * authenticated
        * superuser
- Optimization:
    + caching: repetitive hits
       * start with memcache and move to redis
       * queueing: celery
   - For deciding priority of requests, user type