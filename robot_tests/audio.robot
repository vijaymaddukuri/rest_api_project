*** Settings ***
Documentation    Test Rest APIs
Library     workflow.baseworkflow_rest.BaseWorkflow

*** Test Cases ***
CREATE REST SESSION
    start rest session

T1 Test a Multiple of 3 maps to Domain A and assigns role Bing
    ${API_RESPONSE} =   get audio sound   9
    Should be equal as strings     ${API_RESPONSE}     The mapped domain is : A , And The role is : Bing

T2 Test a Multiple of 5 maps to Domain B and assigns role Bang
    ${API_RESPONSE} =   get audio sound   25
    Should be equal as strings     ${API_RESPONSE}     The mapped domain is : B , And The role is : Bang

T3 Test a Multiple of both 3 and 5 maps to Domain A and B and assigns role Boom
    ${API_RESPONSE} =   get audio sound   15
    Should be equal as strings     ${API_RESPONSE}     The mapped domain is : A and B , And The role is : Boom

T4 Test a Multiple of Neither 3 nor 5 doesn't map to any domain and assigns role Meh
    ${API_RESPONSE} =   get audio sound   15
    Should be equal as strings     ${API_RESPONSE}     The mapped domain is : None , And The role is : Meh

CLEAN UP
    Reset Settings
