import shutil
from pathlib import Path
obj=Path("logs/auth.logs")
shutil.copy(obj,"auth_backup.log")