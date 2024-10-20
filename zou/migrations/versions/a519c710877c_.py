"""empty message

Revision ID: a519c710877c
Revises: 4f2398ebcd49
Create Date: 2019-02-25 13:39:29.662284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a519c710877c"
down_revision = "4f2398ebcd49"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "entity", sa.Column("code", sa.String(length=160), nullable=True)
    )
    op.add_column(
        "project", sa.Column("code", sa.String(length=80), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("project", "code")
    op.drop_column("entity", "code")
    # ### end Alembic commands ###
