# blinkist-config-python
The package simplifies accessing different configuration stores. The current supported stores are:
- ENV
- SSM
## Usge
```python
import blinkistconfig.Config

# First setup the Config to use the ENV as config store
blinkistconfig.Config.env = "production"
blinkistconfig.Config.adapter_type = "Env"

my_config_value = Config.get("some/folder/config")

# This is being translated to ENV["SOME_FOLDER_CONFIG"]

```


## Development

To install development requirements

```bash
pip install -r requirements/dev.txt
pip install -e .
```

To run tests

```bash
pytest --spec
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/blinkist/blinkist-config-python.

## License

The package is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
