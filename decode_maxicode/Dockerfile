FROM openjdk:11-jre-slim
RUN apt-get update && apt-get install -y wget unzip
RUN mkdir -p /opt/zxing && \
    wget https://repo1.maven.org/maven2/com/google/zxing/core/3.5.2/core-3.5.2.jar -O /opt/zxing/core.jar && \
    wget https://repo1.maven.org/maven2/com/google/zxing/javase/3.5.2/javase-3.5.2.jar -O /opt/zxing/javase.jar
WORKDIR /opt/zxing
ENTRYPOINT ["java", "-cp", "javase.jar:core.jar", "com.google.zxing.client.j2se.CommandLineRunner"]
