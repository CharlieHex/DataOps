FROM python:3.12-slim


# Install required packages
RUN apt-get update && apt-get install -y procps openjdk-17-jdk && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

# Set the working directory
WORKDIR /app

# Copy application files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY Football_Results/ Football_Results/
COPY main.py .

CMD ["python", "main.py"]