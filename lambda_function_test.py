import boto3
from moto import mock_aws

from src.lambda_function import lambda_handler


@mock_aws
def test_lambda_handler():
    ssm = boto3.client('ssm', region_name='sa-east-1')
    ssm.put_parameter(
        Name='meu_parametro',
        Type='String',
        Value='o valor do meu parametro é abacaxi'
    )
    # Act
    results = lambda_handler('meu_parametro')

    # Assert
    assert results == 'o valor do meu parametro é abacaxi'
