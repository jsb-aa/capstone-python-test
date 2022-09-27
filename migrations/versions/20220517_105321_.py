"""empty message

Revision ID: 1cb7134753e0
Revises:
Create Date: 2022-05-17 10:53:21.911263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cb7134753e1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE SCHEMA goodbyeflask')
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('full_name', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username'),
    schema='goodbyeflask'
    )
    op.create_table('decks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('share', sa.Boolean(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('about', sa.Text(), nullable=True),
    sa.Column('last_study_date', sa.Date(), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('points', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['goodbyeflask.users.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['goodbyeflask.users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='goodbyeflask'
    )
    op.create_table('cards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deck_id', sa.Integer(), nullable=False),
    sa.Column('front', sa.Text(), nullable=False),
    sa.Column('back', sa.Text(), nullable=False),
    sa.Column('seen', sa.Boolean(), nullable=False),
    sa.Column('curr_rating', sa.Integer(), nullable=False),
    sa.Column('numFivesInRow', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['deck_id'], ['goodbyeflask.decks.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='goodbyeflask'
    )
    op.create_table('study_sessions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deck_id', sa.Integer(), nullable=False),
    sa.Column('round_count', sa.Integer(), nullable=False),
    sa.Column('flips_count', sa.Integer(), nullable=False),
    sa.Column('one_count', sa.Integer(), nullable=False),
    sa.Column('two_count', sa.Integer(), nullable=False),
    sa.Column('three_count', sa.Integer(), nullable=False),
    sa.Column('four_count', sa.Integer(), nullable=False),
    sa.Column('five_count', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['deck_id'], ['goodbyeflask.decks.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='goodbyeflask'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_schema('goodbyeflask')
    op.drop_table('study_sessions')
    op.drop_table('cards')
    op.drop_table('decks')
    op.drop_table('users')
    # ### end Alembic commands ###
