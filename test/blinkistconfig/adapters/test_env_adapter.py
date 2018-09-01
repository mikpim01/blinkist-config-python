import os
import blinkistconfig.adapters


def test_env_adapter_get_reads_environment_variable(mocker):
    mocker.patch.dict(os.environ, {"A_KEY": "1"})

    env_adapter = blinkistconfig.adapters.ENVAdapter()
    assert env_adapter.get("A/Key") == '1'
