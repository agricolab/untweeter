import confuse
from typing import List
from pathlib import Path

config = confuse.LazyConfig("untweeter", __name__)
print("Loading configuration from", config.config_dir())


def dump(config: confuse.LazyConfig) -> None:
    fname = Path(config.config_dir()) / "config.yaml"
    yaml = config.dump()
    with fname.open("w") as f:
        f.write(yaml)


def get_keys() -> List[str]:
    keys = []
    for key in [
        "consumer_key",
        "consumer_secret",
        "access_token_key",
        "access_token_secret",
    ]:
        keys.append(config["KEYS"][key].get(str))

    return keys


def get_limits() -> List[int]:
    limits = []
    for key in ["tweets", "faves"]:
        limits.append(config["LIMITS"][key].get(int))
    return limits


def set_fave_limit(limit: int) -> None:
    config["LIMITS"]["faves"].set(int(limit))
    dump(config)


def set_tweet_limit(limit: int) -> None:
    config["LIMITS"]["tweets"].set(int(limit))
    dump(config)


def ask_for_keys() -> None:
    consumer_key = input("consumer_key: ")
    consumer_secret = input("consumer_secret: ")
    access_token_key = input("access_token_key: ")
    access_token_secret = input("access_token_secret: ")
    config["KEYS"]["consumer_key"].set(str(consumer_key))
    config["KEYS"]["consumer_secret"].set(str(consumer_secret))
    config["KEYS"]["access_token_key"].set(str(access_token_key))
    config["KEYS"]["access_token_secret"].set(str(access_token_secret))
    dump(config)
