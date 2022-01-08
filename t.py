import docker
eval_server = client.containers.create("pysandbox:v1",ports={'5000/tcp': 5000}, detach=True)
eval_server.start()
eval_server.stop()
