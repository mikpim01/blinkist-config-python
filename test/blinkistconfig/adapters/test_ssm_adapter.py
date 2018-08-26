import pytest

@pytest.fixture
def ssm_client():
    import boto3
    return boto3.client('ssm', region_name='us-east-1')

@pytest.fixture
def ssm_adapter():
    import blinkistconfig.adapters
    return blinkistconfig.adapters.SSMAdapter()

def test_ssm_adapter_get_reads_variable_from_app_scope(ssm_client, ssm_adapter, mocker):
    get_param_stub = mocker.patch.object(ssm_client, 'get_parameter')
    ssm_adapter.get('a_key',app_name="an_app", client=ssm_client)
    get_param_stub.assert_called_once_with(Name=f"/application/an_app/a_key", WithDecryption=True)



