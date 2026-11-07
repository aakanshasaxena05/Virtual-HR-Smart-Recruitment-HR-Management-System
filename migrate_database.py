

from sqlalchemy import inspect, text

from database import engine, Base
import models

# Create any missing tables
Base.metadata.create_all(bind=engine)

# Check existing interview table columns
inspector = inspect(engine)

columns = [
    column["name"]
    for column in inspector.get_columns("interviews")
]

# Add candidate_id only if it does not already exist
if "candidate_id" not in columns:
    with engine.begin() as connection:
        connection.execute(
            text(
                "ALTER TABLE interviews "
                "ADD COLUMN candidate_id INTEGER "
                "REFERENCES candidates(id)"
            )
        )

    print("candidate_id column added successfully!")

else:
    print("candidate_id column already exists!")

print("Database migration completed.")
