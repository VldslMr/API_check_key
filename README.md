# Docker api-nginx-rtmp

Docker image for RTMP/HLS server API running on nginx.

API implemented for `on_publish` callback function.

`on_publish` is a callback function in `nginx-rtmp-module`. It is triggered when a client starts publishing a stream to the Nginx RTMP server.

The `on_publish` endpoint processes the POST request and returns status code 200 or 404 depending on the availability of stream_key in the database

More details:

- https://github.com/arut/nginx-rtmp-module/wiki/Directives#on_publish
- http://localhost:8000/docs

## Running
Create a network before running

``` $ docker network create -d bridge <name-network> ```

Run a container from a DockerHub image

``` $ docker pull krisstov/api-nginx-rtmp ```

``` $ docker run -d --name api-nginx-rtmp --net <name-network> -p 8000:8000 -v /path/to/API_check_key/api:/app/api krisstov/api-nginx-rtmp:v1```

Run a container with nginx-rtmp

``` $ docker pull ejilay/nginx-rtmp ```

To mount config folder to docker:

``` $  docker run -d --name nginx-rtmp --net <name-network> -e RTMP_PORT=1935 -p 1935:1935 -e HTTP_PORT=8081 -p 8081:8081 -v `pwd`/hls:/var/www/streams -v /path/to//API_check_key/config:/opt/nginx/conf -t ejilay/nginx-rtmp:latest ```

## OBS Configuration
Under broadcast settigns, set the follwing parameters:

- Streaming Service: Custom
- Server: rtmp://localhost:1935/streams
- Play Path/Stream Key: mystream

## Watching the stream
In your favorite RTMP video player connect to the stream using the URL:

- rtmp://localhost:1935/streams/mystream
- http://localhost:8081/streams/mystream/index.m3u8


- rtmp://localhost:1935:1935/streams/mystream2
- http://localhost:1935:8081/streams/mystream2/index.m3u8

## Tested players
- VLC
- omxplayer (Raspberry Pi)


## Logs
API has logs:
- body_request (shows the values of the POST request arguments)
- request_key (shows the result of the function 'search_value')
