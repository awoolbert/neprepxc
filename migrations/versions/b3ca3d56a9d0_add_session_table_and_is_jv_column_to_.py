"""Add session table and is_jv column to races table

Revision ID: b3ca3d56a9d0
Revises: ed2054ae4322
Create Date: 2023-04-25 15:52:15.844189

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b3ca3d56a9d0'
down_revision = 'ed2054ae4322'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('session_table')
    op.add_column('races', sa.Column('is_jv', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('races', 'is_jv')
    op.create_table('session_table',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('session_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('data', postgresql.BYTEA(), autoincrement=False, nullable=True),
    sa.Column('expiry', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='session_table_pkey'),
    sa.UniqueConstraint('session_id', name='session_table_session_id_key')
    )
    # ### end Alembic commands ###
