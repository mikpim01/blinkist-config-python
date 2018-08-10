import pytest
from blinkistconfig.adapters import EnvAdapter

@pytest.fixture
def config_class():
    import blinkistconfig
    return blinkistconfig.Config

def test_config_allows_setting_the_environment(config_class):
    assert config_class.env == "", "Default env is not blanky"
    config_class.env = "development"
    assert config_class.env == "development", "env should default to the environment"

def test_config_get_raises_argument_error_with_more_than_one_default(config_class):
    with pytest.raises(ValueError) as exinfo:
        config_class.get("key", "default1", "default2")
    assert str(exinfo.value) == "wrong number of arguments"

def test_config_infers_the_adapter_from_adapter_type(config_class):
    config_class.env = "development"
    config_class.adapter_type = "Env"
    config_class.get("a_key")
    assert config_class.adapter.__class__ == EnvAdapter
