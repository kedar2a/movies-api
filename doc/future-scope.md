# Future Scope


## Use Case:
Once deployed suppose this application became very famous and started to receive a ton of traffic. Your application now contains metadata about 5M movies and receives 15M API hits per day both from anonymous as well as authenticated users. Suggest an  architecture to scale up this system to 5x of these specs. You can also think of potential bottlenecks at all layers of the stack and how will you solve for these.


## Suggestions:
- **Analytics**: To take any decision on scalability, we should have proper diagnosis/analytics data. Which we can achieve through various options available at various levels. Data coming out from analytics would pin point proper bottleneck of the system. This data enables to tie-up the loose ends and take appropriate action on respective module(s).
    + Provided by host (e.g: heroku, aws)
        * Heroku add-ons and AWS marketplace plugin to diagnose various parameters of a web application.
    + Self exploration of tools that can be run on server (e.g: awstats)
    + Django/framework level packages
        * Django also provides various packages for tracking detail information of wide range of parameters.
    + Google analytics:
        * A well established, detailed, clean UI based analytics.
- **Vertical scalability**: Increasing hardware capacity. This includes RAM, processor, HDD, type of HDD etc. We can derive mathematical static formula of no of requests directly proportional to required hardware. Increase processes/workers of nginx, wsgi.
- **Deployment**: Based on business requirements or demanding performance we may switch to respective service provider. There are various players in the market e.g: linode, heroku, droplets and aws. If the business traffic is fluctuating, we may need to have **dynamic hardware allocation with balancer**, which is well supported by AWS. But if traffic is mostly constant then depending on **cost factor** another service provider may be choosen. Various factors needs to be consider while adopting deployer i.e: **cost, requirement, employee-expertise/learning-curve, ease-of-use, customer-support, deployment strategy**. We can start application hosting from heroku. If this becomes very famous and start receiving tons of traffic, we may consider to move to provider like AWS with completely **configurable hardware stack** with load balancer. Based on analytics data, we may also deploy application **geographically** nearest to potential user base. If deployer provides multiple options, we may choose **replication of data** across multiple geolocations.
- **Code**: Optimize the code at it's base. Implement proper data structure and algorithms to store and process data. Data structure and algorithms decision can taken from no of hits and analytics data of which type of CRUD operation happening mostly. If there is an fever write than read, we can afford to have slower write than read. We can write python profiler and checkout line by line performance of a code. Depending on output of python profiler, we may need to work on respective code lines.
- **Rethink on tech-stack**:
    + DB: We can think to replacing sql DB with mongoDB.
        * It provides **horizontal scalability**, collections can be sharded and place on different servers. Increases query thoughput by fetching result from multiple servers in parallel manner. Needs to be implemented with proper shard-key and strategy.
        * Avoid joins, redefining schema to have `MovieDirector` and `MovieGenre` field values as a part of `Movie` class. mongoDB internally handles these nested queries and gives us result which is comparatively faster than complicated RDMBS (multiple types of) joins.
        * As we are creating system only for API and mongoDB stores data internally in BSON format, serialization would be done with less memory, processor consumption.
    + Programing language: 
        * We can use advance features of python like asyncio, threading.
        * Some of the processing can be written as **`C`** modules.
        * If this is still not working we may think to language with better concurrency control like, golang, closure, java etc.
- **Access control**
    + DDoS attack:
        * Realtime analytics is useful to track usage from same IP address.
        * This can be prevented with some of the services through cloudflare.
    + Region level: This can be controlled by some packages.
    + User Level (drf `Throttling` and `Permissions`): Business decision may be taken depending on type of users.
        * anonymous, authenticated, superuser
        * Less than `N` `GET` requests per min.
- **Optimization**:
    + Serving over **HTTP 2.0**
    + **Caching**: Cache output of repetitive calls.
       * Start with `memcache` and move to `Redis`
       * Queueing: `celery` for API. For deciding priority of requests, user type.
- **Documentation**: Writing good documentaion to guide users. This will avoid confusion and prevents from unnecessary hits. Good and comprehensive API Documentation, would allow easy at-one go single or bulk operation without any faul hits.