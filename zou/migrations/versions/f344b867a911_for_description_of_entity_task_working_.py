"""For description of entity, task, working_file don't set any length

Revision ID: f344b867a911
Revises: 32f134ff1201
Create Date: 2024-05-22 15:46:07.855818

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f344b867a911"
down_revision = "32f134ff1201"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("entity", schema=None) as batch_op:
        batch_op.alter_column(
            "description",
            existing_type=sa.VARCHAR(length=1200),
            type_=sa.Text(),
            existing_nullable=True,
        )

    with op.batch_alter_table("task", schema=None) as batch_op:
        batch_op.alter_column(
            "description",
            existing_type=sa.VARCHAR(length=200),
            type_=sa.Text(),
            existing_nullable=True,
        )

    with op.batch_alter_table("working_file", schema=None) as batch_op:
        batch_op.alter_column(
            "description",
            existing_type=sa.VARCHAR(length=200),
            type_=sa.Text(),
            existing_nullable=True,
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("working_file", schema=None) as batch_op:
        batch_op.alter_column(
            "description",
            existing_type=sa.Text(),
            type_=sa.VARCHAR(length=200),
            existing_nullable=True,
        )

    with op.batch_alter_table("task", schema=None) as batch_op:
        batch_op.alter_column(
            "description",
            existing_type=sa.Text(),
            type_=sa.VARCHAR(length=200),
            existing_nullable=True,
        )

    with op.batch_alter_table("entity", schema=None) as batch_op:
        batch_op.alter_column(
            "description",
            existing_type=sa.Text(),
            type_=sa.VARCHAR(length=1200),
            existing_nullable=True,
        )

    # ### end Alembic commands ###
