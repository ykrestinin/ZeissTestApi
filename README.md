# ZeissTestApi

Load test for Zeiss Test Api.

For executing with web interface run: 
```
locust --host https://registry-test.zeiss.services/api
```
Web interface schould be available: http://127.0.0.1:8089/

For command line mode use
```
locust --host https://registry-test.zeiss.services/api --csv=zeisstestapi --no-web -c 1500 -r 300 -t10m
```
Where [csv] - the prefix for csv report file

[-c] - quantity of virtual user 

[-r] - increment of quantity per second

[-t] - time of exeqution

# Docker image can be pulled from Dockerhub:

https://cloud.docker.com/repository/docker/ykrestinin/locust-test-exercise/

Currently the test is run throgh run_test.sh entrypoint in webinterface mode.

To change this run_test.sh should be edited according to requirements.
