
# How to Run

docker build -t uniqueid:0.1 .

docker run -t -d -p 8105:8105 --name uniqueid uniqueid:0.1

# Jenkens
* publish: https://jenkins.gtv-jenkins.com/view/%E3%80%905%E3%80%91Dev/job/data-spider-dev/
* k8s machine: https://rancher.gtv-jenkins.com/p/local:p-qm8z2/workload/deployment:dev:uniqueid

# Service
get uuid4: http://k8s-dev-uniqueid-fc495960de-4417dc3c9d629f4b.elb.us-east-1.amazonaws.com:8105/uuid4
get snowid: http://k8s-dev-uniqueid-fc495960de-4417dc3c9d629f4b.elb.us-east-1.amazonaws.com:8105/snowid
get docs: http://k8s-dev-uniqueid-fc495960de-4417dc3c9d629f4b.elb.us-east-1.amazonaws.com:8105/docs
# uniq
