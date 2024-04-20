"""rename RaceResult to RaceScore

Revision ID: 6892897160a4
Revises: 7cbb7dde1960
Create Date: 2023-04-27 13:45:48.848398

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6892897160a4'
down_revision = '7cbb7dde1960'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('race_scores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('race_id', sa.Integer(), nullable=False),
    sa.Column('winner_id', sa.Integer(), nullable=False),
    sa.Column('loser_id', sa.Integer(), nullable=False),
    sa.Column('winner_score', sa.Integer(), nullable=True),
    sa.Column('loser_score', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['loser_id'], ['teams.id'], ),
    sa.ForeignKeyConstraint(['race_id'], ['races.id'], ),
    sa.ForeignKeyConstraint(['winner_id'], ['teams.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('race_result')
    op.drop_table('session_table')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('session_table',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('session_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('data', postgresql.BYTEA(), autoincrement=False, nullable=True),
    sa.Column('expiry', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='session_table_pkey'),
    sa.UniqueConstraint('session_id', name='session_table_session_id_key')
    )
    op.create_table('race_result',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('race_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('winner_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('loser_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('loser_score', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('winner_score', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['loser_id'], ['teams.id'], name='race_result_loser_id_fkey'),
    sa.ForeignKeyConstraint(['race_id'], ['races.id'], name='race_result_race_id_fkey'),
    sa.ForeignKeyConstraint(['winner_id'], ['teams.id'], name='race_result_winner_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='race_result_pkey')
    )
    op.drop_table('race_scores')
    # ### end Alembic commands ###