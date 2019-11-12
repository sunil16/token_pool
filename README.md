# Token Pooling Service
  - get token
  - get stats of tokens

### Tech

 Token Pooling service uses a number of open source projects to work properly:

* [Python] - Python is an interpreted, high-level, general-purpose programming language.
* [Redis] - Redis is an open source , in-memory data structure store, used as a database, cache and message broker.
* [Flask] - The Python micro framework for building web applications

And of course  Token Pooling Service itself is open source with a [public repository][dill]
 on GitHub.

### Configuration

    Update app/config/local.ini file for local development
    Pool Cache Size,  size = 10(integer value)
    Task execution time(to check token expire), wait_time_seconds = 3(secounds)
    redis , [redis] update all field according to machines setup
    cors, [cors] update all field according to the available server  

### Installation

 Token Pooling Service requires [Flask](https://flask.palletsprojects.com/en/1.1.x/) v1.1.1+ to run.

Install the dependencies and devDependencies and start the server.

```sh
$ cd token_pool
$ pip install -r requirements.txt
$ python app.py

```
Verify the deployment by navigating to your server address in your preferred browser.

```sh
http://127.0.0.1:5000/
```

### API Endpoints

* **/get_token** (Get token)
* **/get_stats** (Get all token stats)


License
----

MIT


**Free Software

   [dill]: <https://github.com/sunil16/token_pool.git>
   [git-repo-url]: <https://github.com/sunil16/token_pool.git>
   [Python]: <https://www.python.org/>
   [Redis]: <https://redis.io/>
   [Flask]: <https://flask.palletsprojects.com/en/1.1.x/>
