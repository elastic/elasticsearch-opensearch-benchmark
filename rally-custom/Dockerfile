FROM elastic/rally:2.8.0
ENV PYTHONUNBUFFERED=1

# bypass system verifications
COPY --chown=1000:0 esrally/client/synchronous.py /usr/local/lib/python3.8/site-packages/esrally/client/synchronous.py
COPY --chown=1000:0 esrally/min-es-version.txt /usr/local/lib/python3.8/site-packages/esrally/min-es-version.txt

# copy all our custom tracks to /rally/custom_tracks
RUN mkdir -p /rally/custom_tracks
COPY --chown=1000:0 custom_tracks/ /rally/custom_tracks/


