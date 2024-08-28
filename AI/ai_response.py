import boto3
import json
from decouple import config


def ai_response(user_input, health_condition):
    client = boto3.client(service_name='bedrock-runtime', region_name="us-east-1",
                          aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
                          aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'))
    # prompt= f'\n\nHuman:{user_input}\n\nAssistant:'
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"You are an AI assistant specialized in pregnancy-related topics. Please provide a"
                                f"very brief, accurate and helpful information for the following question: {user_input}."
                                f"Also put into consideration the following health condition(s): {health_condition}"
                    }
                ]
            }
        ],
        "temperature": 0.7,
        "top_p": 0.9,
        "top_k": 250,

    })
    model_id = 'anthropic.claude-3-sonnet-20240229-v1:0'

    response = client.invoke_model(body=body, modelId=model_id,
                                   accept='application/json', contentType='application/json')
    response_body = json.loads(response['body'].read())
    return response_body['content'][0]['text']
