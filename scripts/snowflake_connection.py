import snowflake.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_connection():
    return snowflake.connector.connect(
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        user=os.getenv('SNOWFLAKE_USER'),
        private_key_file=os.path.expanduser(os.getenv('SNOWFLAKE_PRIVATE_KEY_PATH')),
        private_key_passphrase=os.getenv('SNOWFLAKE_PRIVATE_KEY_PASSPHRASE'),
        role=os.getenv('SNOWFLAKE_ROLE'),
        database=os.getenv('SNOWFLAKE_DATABASE'),
        warehouse=os.getenv('SNOWFLAKE_WAREHOUSE')
    )