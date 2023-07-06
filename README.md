# AWS Cloud Devops Capstone Project

[![CircleCI](https://circleci.com/gh/xuanduy0501/udacity_capstone.svg?style=svg)](https://github.com/xuanduy0501/udacity_capstone)
## _Introduction_

In this project you will apply the skills and knowledge which were developed throughout the Cloud DevOps Nanodegree program. These include:

- Working in AWS Cloud Platform
- Using Circle CI for CICD
- Building pipelines
- Working with Infra as Code (CloudFormation) to deploy infrastructure
- Building Kubernetes clusters
- Building Docker containers in pipelines

## _Application_

My application is a simple webpage based on python script using flask to render.

## _Kubernetes Cluster_

I used AWS CloudFormation to deploy the Kubernetes Cluster.
| File | Description |
| ------ | ------ |
| .circleci/files/network.yml | To create network for cluster, I will create VPC, Internet Gateway, Subnet, Route Table, and Security Group |
| .circleci/files/eks.yml | Creates an EKS (Elastic Kubernetes Service) cluster with a specific version and configuration. It also creates an IAM role and instance profile for the EKS service to use|
| .circleci/files/node-group.yml | It defines an instance profile and IAM role for EC2 instances to join the node group, an EKS security group to allow traffic to and from the node group|

## _Check the script's code with pylint and Hadolint_

Log run lint fail
![Alt text](https://github.com/xuanduy0501/udacity_capstone/blob/master/ScreenShot/SCREENSHOT01_Test_Lint_fail.png?raw=true)

Log run lint success
![Alt text](https://github.com/xuanduy0501/udacity_capstone/blob/master/ScreenShot/SCREENSHOT02_Lint_Success.png?raw=true)

## _Pipelines_

![Alt text](https://github.com/xuanduy0501/udacity_capstone/blob/master/ScreenShot/SCREENSHOT03_CircleCi_Pipeline.png?raw=true)

## _Deployed Instances_

![Alt text](https://github.com/xuanduy0501/udacity_capstone/blob/master/ScreenShot/SCREENSHOT04_Deployed_Instances.png?raw=true)

## _Deployment is successful output_

![Alt text](https://github.com/xuanduy0501/udacity_capstone/blob/master/ScreenShot/SCREENSHOT05_Successfull_Output.png?raw=true)

## _Access the application_

http://a7e587d3f692e4c67be26bd4dbad7f6b-449796964.us-east-1.elb.amazonaws.com/

![Alt text](https://github.com/xuanduy0501/udacity_capstone/blob/master/ScreenShot/SCREENSHOT06_Access_App.png?raw=true)
