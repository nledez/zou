"""empty message

Revision ID: 528b27337ebc
Revises: f0567e8d0c62
Create Date: 2018-05-17 15:51:25.513852

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from sqlalchemy.dialects import postgresql
import sqlalchemy_utils
import uuid

# revision identifiers, used by Alembic.
revision = '528b27337ebc'
down_revision = 'f0567e8d0c62'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('asset_instance_link',
    sa.Column('entity_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=False),
    sa.Column('asset_instance_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=False),
    sa.ForeignKeyConstraint(['asset_instance_id'], ['asset_instance.id'], ),
    sa.ForeignKeyConstraint(['entity_id'], ['entity.id'], ),
    sa.PrimaryKeyConstraint('entity_id', 'asset_instance_id')
    )
    op.add_column('asset_instance', sa.Column('scene_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=True))
    op.create_index(op.f('ix_asset_instance_scene_id'), 'asset_instance', ['scene_id'], unique=False)
    op.drop_constraint('asset_instance_name_uc', 'asset_instance', type_='unique')
    op.create_unique_constraint('asset_instance_name_uc', 'asset_instance', ['scene_id', 'name'])
    op.drop_constraint('asset_instance_uc', 'asset_instance', type_='unique')
    op.create_unique_constraint('asset_instance_uc', 'asset_instance', ['asset_id', 'scene_id', 'number'])
    op.drop_index('ix_asset_instance_entity_id', table_name='asset_instance')
    op.drop_index('ix_asset_instance_entity_type_id', table_name='asset_instance')
    op.drop_constraint('asset_instance_entity_id_fkey', 'asset_instance', type_='foreignkey')
    op.drop_constraint('asset_instance_entity_type_id_fkey', 'asset_instance', type_='foreignkey')
    op.create_foreign_key(None, 'asset_instance', 'entity', ['scene_id'], ['id'])
    op.drop_column('asset_instance', 'entity_type_id')
    op.drop_column('asset_instance', 'entity_id')
    op.add_column('output_file', sa.Column('temporal_entity_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=True))
    op.drop_constraint('output_file_uc', 'output_file', type_='unique')
    op.create_unique_constraint('output_file_uc', 'output_file', ['name', 'entity_id', 'asset_instance_id', 'output_type_id', 'task_type_id', 'temporal_entity_id', 'representation', 'revision'])
    op.create_foreign_key(None, 'output_file', 'entity', ['temporal_entity_id'], ['id'])
    op.drop_column('output_file', 'uploaded_movie_name')
    op.drop_column('output_file', 'uploaded_movie_url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('output_file', sa.Column('uploaded_movie_url', sa.VARCHAR(length=600), autoincrement=False, nullable=True))
    op.add_column('output_file', sa.Column('uploaded_movie_name', sa.VARCHAR(length=150), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'output_file', type_='foreignkey')
    op.drop_constraint('output_file_uc', 'output_file', type_='unique')
    op.create_unique_constraint('output_file_uc', 'output_file', ['name', 'entity_id', 'output_type_id', 'task_type_id', 'representation', 'revision'])
    op.drop_column('output_file', 'temporal_entity_id')
    op.add_column('asset_instance', sa.Column('entity_id', postgresql.UUID(), autoincrement=False, nullable=False))
    op.add_column('asset_instance', sa.Column('entity_type_id', postgresql.UUID(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'asset_instance', type_='foreignkey')
    op.create_foreign_key('asset_instance_entity_type_id_fkey', 'asset_instance', 'entity_type', ['entity_type_id'], ['id'])
    op.create_foreign_key('asset_instance_entity_id_fkey', 'asset_instance', 'entity', ['entity_id'], ['id'])
    op.create_index('ix_asset_instance_entity_type_id', 'asset_instance', ['entity_type_id'], unique=False)
    op.create_index('ix_asset_instance_entity_id', 'asset_instance', ['entity_id'], unique=False)
    op.drop_constraint('asset_instance_uc', 'asset_instance', type_='unique')
    op.create_unique_constraint('asset_instance_uc', 'asset_instance', ['asset_id', 'entity_id', 'number'])
    op.drop_constraint('asset_instance_name_uc', 'asset_instance', type_='unique')
    op.create_unique_constraint('asset_instance_name_uc', 'asset_instance', ['entity_id', 'name'])
    op.drop_index(op.f('ix_asset_instance_scene_id'), table_name='asset_instance')
    op.drop_column('asset_instance', 'scene_id')
    op.drop_table('asset_instance_link')
    # ### end Alembic commands ###
