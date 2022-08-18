import configparser
from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    user: str
    password: str
    database: str
    host: str


@dataclass
class DjangoConfig:
    secret_key: str


@dataclass
class Config:
    database: DatabaseConfig
    django: DjangoConfig


def load_config(path: str) -> Config:
    config = configparser.ConfigParser()
    config.read(path)

    database = config["database"]
    django = config["django"]

    return Config(
            database=DatabaseConfig(
                user=database.get("user"),
                password=database.get("password"),
                database=database.get("database"),
                host=database.get("host"),
            ),
            django=DjangoConfig(
                secret_key=django.get("secret_key")
            )

    )
