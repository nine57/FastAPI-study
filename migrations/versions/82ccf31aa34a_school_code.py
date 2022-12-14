"""School_code

Revision ID: 82ccf31aa34a
Revises: 79475262bbd4
Create Date: 2022-10-20 16:16:04.480556

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "82ccf31aa34a"
down_revision = "79475262bbd4"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "school_codes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("code", sa.String(), nullable=True),
        sa.Column("regulator", sa.String(length=5), nullable=True),
        sa.Column("type", sa.String(length=3), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_school_codes_code"), "school_codes", ["code"], unique=False
    )
    op.create_index(op.f("ix_school_codes_id"), "school_codes", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_school_codes_id"), table_name="school_codes")
    op.drop_index(op.f("ix_school_codes_code"), table_name="school_codes")
    op.drop_table("school_codes")
    # ### end Alembic commands ###
