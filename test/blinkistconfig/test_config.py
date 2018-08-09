import pytest

@pytest.fixture
def config_class():
    import blinkistconfig
    return blinkistconfig.Config

def test_config_allows_setting_the_environment(config_class):
    config_class.env = "development"
    assert config_class.env == "development", "env should default to the environment"
