# Yeah, that's right. I'm a README. What the fuck are you gonna do? Read me? Yeah. I thought not.

If you want to host this somewhere (why?) build the Docker image:

```zsh
docker image build . -t localhost:50055/form10:latest
docker run -p 50055:50055 -it localhost:50055/form10
```
