import os

# Set the secret key from .env
os.environ.setdefault("SECRET_KEY", "ue^bju!*sri179pjueyy4=x8k1u(yy%6zkx6i$km+ph&s%1#9^")  # noqa: E501

# Set the database URL with a fallback default if it's not defined externally
os.environ.setdefault(
    "DATABASE_URL",
    "postgresql://neondb_owner:npg_irBCezH6Noq7@ep-lively-silence-a22bbg2d.eu-central-1.aws.neon.tech/fifth_dial_graph_747368"  # noqa: E501
)
