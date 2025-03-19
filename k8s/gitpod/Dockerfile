FROM gitpod/openvscode-server:latest

USER root

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

USER openvscode-server

CMD ["/bin/sh", "-c", "exec ${OPENVSCODE_SERVER_ROOT}/bin/openvscode-server --host 0.0.0.0 --server-base-path /${BASE_URL} --without-connection-token \"${@}\""]