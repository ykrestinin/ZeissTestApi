FROM python:3
ADD locustfile.py /
ADD run_test.sh /
RUN chmod +x /run_test.sh
RUN python3 -m pip install locustio
EXPOSE 8089
ENTRYPOINT ["/run_test.sh"]
