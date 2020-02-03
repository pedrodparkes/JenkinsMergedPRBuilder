from log_cfg import logger
import json
import os
import requests

TRIGGER_BRANCHES=os.environ["TRIGGER_BRANCHES"]
MASTER_BRANCHES_LIST=TRIGGER_BRANCHES.split(",")
JENKINS_USER=os.environ["JENKINS_USER"]
JENKINS_USER_TOKEN=os.environ["JENKINS_USER_TOKEN"]
JENKINS_URL=os.environ["JENKINS_URL"]
JENKINS_PIPELINE_NAME=os.environ["JENKINS_PIPELINE_NAME"]

def trigger(event, context):
    # print(json.dumps(event))
    headers = event['headers']
    data    = json.loads(event['body'])
    body={}
    body["EventType"]=headers['X-GitHub-Event']
    if headers['X-GitHub-Event'] == 'pull_request':
        body["PrNumber"]=data['number']
        body["Branch2Compare"]=data['pull_request']['head']['ref']
        body["BaseBranch"]=data['pull_request']['base']['ref']
        body["SettingsTriggerBranches"]=str(MASTER_BRANCHES_LIST)
        if data['action'] == 'closed':
            body["PrStatus"]=data['action']
            if data['pull_request']['merged'] == True:
                body["IsPrMerged"]=data['pull_request']['merged']
                if data['pull_request']['base']['ref'] in MASTER_BRANCHES_LIST:
                    print("Lets build")
                    body["design"]="build"
                    response = curl(body["BaseBranch"])
                    body["Response"] = str(response)

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def curl(branch_name):
    return requests.post(JENKINS_URL+'/job/'+JENKINS_PIPELINE_NAME+'/job/'+branch_name+'/build', auth=(JENKINS_USER, JENKINS_USER_TOKEN))
