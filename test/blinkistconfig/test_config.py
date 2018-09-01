import pytest
from pytest_mock import mocker

import blinkistconfig.adapters

import os

@pytest.fixture
def config_class():
    import blinkistconfig
    return blinkistconfig.Config(env="development", adapter_type="ENV", app_name="my_app")

def test_config_get_raises_argument_error_with_more_than_one_default(config_class):
    with pytest.raises(ValueError) as exinfo:
        config_class.get("key", "default1", "default2")
    assert str(exinfo.value) == "wrong number of arguments"

def test_config_infers_the_adapter_from_adapter_type(config_class, mocker):
    assert config_class._adapter().__class__ == blinkistconfig.adapters.ENVAdapter
    assert config_class.adapter.__class__ == blinkistconfig.adapters.ENVAdapter

def test_config_get_returns_default_if_key_does_not_exist(config_class, mocker):
    assert config_class.get("missing_key", "1234") == "1234"

def test_conf_get_returns_adapter_value_if_key_exist(config_class, mocker):
    mocker.patch.dict(os.environ, {"EXISTING_KEY": "12345"})
    assert config_class.get("existing_key", "1234") == "12345"

