## Automation framework for REST API testing.

This framework will use to test the REST API's. And also we can integrate this framework in Jenkins for CI/CD.

Note: Framework design is documented in RobotFramework Document.docx file, which is located in the base directory

Here is workflow:

 - Create jenkins pipeline job in Jenkins server
 - Select pipeline scm project
 - Select project source from GIT and specify the git repo path along with git credentials
 - provide the jenkinsfile path, to execute stages specified in jenkinsfile
    Example: ci\Jenkinsfile
 - Save the project and trigger the build
 - Results will store in Jenkins artifcatory.

Stages in Jenkinsfile:

    - Execute the Dockerfile to create docker container with required packages (eg: Java, python)

    - Execute the stages inside the docker container

        - Stage1:
            - Create python virtual environment
            - Install the require python packages
            - Start the webserver, which will enable rest api's for testing

        - Stage2:
            - Execute the test automation test suite which contains different test cases
            - Save the results in text, html and xml format and upload the results to jenkins artifactory

## We can execute the test suite outside the Jenkins as well, here are the steps to acheive it

#Prerequisites:

    - Python 3.5 or above need to be installed

    - Set the PATH environmental variables:

        Example:  Path: C:\python3.5\;C:\python3.5\Lib;C:\python3.5\Lib\site-packages

    - Set the pythonpath environmental variable with the project base dir

        Example for windows: C:\Users\vijay\rest_api_project
        Example for linux: export PYTHONPATH=$PYTHONPATH:$dir/rest_api_project

### Python Virtual Environment

1. Create Python virtual environment

        $ virtualenv <name-of-folder>

2. Activate virtual environment

        $ source <path-to-folder>/bin/activate

3. Deactivate virtual environment

        $ deactivate

### Install requirements

* Install python project dependencies for dev environment


        $ pip3 install -r requirements.txt


########## How to run? ##########

Go to the robot_test directory and execute the robot file with below command

robot -b debuglogs.txt -L DEBUG:INFO -d logs -x junit.xml --timestampoutputs audio.robot

########## How to check results ? ##########

Results are available in the logs folder in the below location

$dir\rest_api_project\robot_tests\logs