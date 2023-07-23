FROM elastic/rally:2.8.0
ENV PYTHONUNBUFFERED=1

COPY --chown=1000:0 esrally/client/synchronous.py /rally/esrally/client/synchronous.py

RUN mkdir -p /rally/custom_tracks
COPY --chown=1000:0 custom_tracks/ /rally/custom_tracks/

