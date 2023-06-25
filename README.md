# AWS Cloud Devops Capstone Project

[![ky0men](https://circleci.com/gh/ky0men/uda-capstone.svg?style=svg)](https://github.com/ky0men/uda-capstone)

## _Introduction_

In this project you will apply the skills and knowledge which were developed throughout the Cloud DevOps Nanodegree program. These include:

- Working in AWS
- Using Circle CI to implement Continuous Integration and Continuous Deployment
- Building pipelines
- Working with CloudFormation to deploy clusters
- Building Kubernetes clusters
- Building Docker containers in pipelines

## _Application_

My application is a simple webpage based on python script using flask to render.

## _Kubernetes Cluster_

I used AWS CloudFormation to deploy the Kubernetes Cluster.
| File | Description |
| ------ | ------ |
| .circleci/files/network.yml | To create resources such as VPC, Internet Gateway, Subnet, Route Table, and Security Group |
| .circleci/files/eks.yml | Creates an EKS (Elastic Kubernetes Service) cluster with a specific version and configuration. It also creates an IAM role and instance profile for the EKS service to use|
| .circleci/files/node-group.yml | It defines an instance profile and IAM role for EC2 instances to join the node group, an EKS security group to allow traffic to and from the node group|

## _Check the script's code with pylint and Hadolint_

Output when lint failed
![Alt text](https://github.com/ky0men/uda-capstone/blob/master/ScreenShot/ScreenShot01_Lint_failed.png?raw=true)

Ouput when lint success
![Alt text](https://github.com/ky0men/uda-capstone/blob/master/ScreenShot/ScreenShot02_Lint_success.png?raw=true)

## _CircleCi - CI/CD Pipelines_

![Alt text](https://github.com/ky0men/uda-capstone/blob/master/ScreenShot/ScreenShot03_CircleCi_Pipeline.png?raw=true)

## _Deployed Instances_

![Alt text](https://github.com/ky0men/uda-capstone/blob/master/ScreenShot/ScreenShot04_Deployed_Instances.png?raw=true)

## _Deployment is successful output_

![Alt text](https://github.com/ky0men/uda-capstone/blob/master/ScreenShot/ScreenShot05_Successfull_output.png?raw=true)

## _Access the application_

http://a70de49e662b349a5adc3984a90a0955-212419026.us-east-1.elb.amazonaws.com/

![Alt text](https://github.com/ky0men/uda-capstone/blob/master/ScreenShot/ScreenShot06_Access_App.png?raw=true)
