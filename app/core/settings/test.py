class TestAppSettings(AppSettings):
    # fastapi_kwargs
    debug: bool = True
    title: str = "Test FastAPI example application"

    # back-end app settings
    secret_key: SecretStr = SecretStr("secret-test")
    db_url: PostgresDsn = "postgresql+asyncpg://testuser:testpass@localhost:5432/testdb"
    logging_level: int = logging.DEBUG
