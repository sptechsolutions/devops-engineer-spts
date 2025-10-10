from datetime import datetime
from uuid import UUID
from sqlalchemy import DateTime
from sqlalchemy.orm import registry, Mapped, mapped_column


mapper_reg = registry()

Base = mapper_reg.generate_base()


class Activity(Base):
    __tablename__ = "activity"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str]
    time_start: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    time_end: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
