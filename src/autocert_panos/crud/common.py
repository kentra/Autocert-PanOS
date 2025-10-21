# # Create Dirs
# mkdir -p $CONFIG_DIR
# mkdir -p $LOG_DIR
# mkdir -p $CONFIG_DIR
# # Fix permissions
# chmod -R 600 $DOMENESHOP_ENV
# chmod -R 600 $PANOS_ENV
from pathlib import Path
import stat
from log_handler import logger  # your existing Loguru logger


def setup_directories_and_permissions(
    config_dir: str, log_dir: str, domeneshop_env: str, panos_env: str
):
    """
    Creates directories if they don't exist and sets 600 permissions on secret files.

    :param config_dir: Directory for config files (e.g., Certbot)
    :param log_dir: Directory for log files
    :param domeneshop_env: Path to Domeneshop credentials file
    :param panos_env: Path to Palo Alto credentials file
    """
    dirs_to_create = [config_dir, log_dir]

    # Create directories
    for directory in dirs_to_create:
        path = Path(directory)
        try:
            path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Directory ensured: {path}")
        except Exception as e:
            logger.error(f"Failed to create directory {path}: {e}")
            raise

    # Secure environment files
    env_files = [domeneshop_env, panos_env]
    for env_file in env_files:
        file_path = Path(env_file)
        if file_path.exists():
            try:
                file_path.chmod(stat.S_IRUSR | stat.S_IWUSR)  # 600
                logger.info(f"Permissions set to 600 for: {file_path}")
            except Exception as e:
                logger.error(f"Failed to set permissions on {file_path}: {e}")
                raise
        else:
            logger.warning(f"Environment file not found, skipping chmod: {file_path}")
