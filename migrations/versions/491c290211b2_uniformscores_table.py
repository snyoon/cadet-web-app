"""UniformScores Table

Revision ID: 491c290211b2
Revises: 444fe84b4fdc
Create Date: 2019-11-21 05:06:33.155165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '491c290211b2'
down_revision = '444fe84b4fdc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('uniform_scores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('week1score', sa.Integer(), nullable=True),
    sa.Column('week2score', sa.Integer(), nullable=True),
    sa.Column('week3score', sa.Integer(), nullable=True),
    sa.Column('week4score', sa.Integer(), nullable=True),
    sa.Column('week5score', sa.Integer(), nullable=True),
    sa.Column('week6score', sa.Integer(), nullable=True),
    sa.Column('week7score', sa.Integer(), nullable=True),
    sa.Column('week8score', sa.Integer(), nullable=True),
    sa.Column('week9score', sa.Integer(), nullable=True),
    sa.Column('week10score', sa.Integer(), nullable=True),
    sa.Column('week11score', sa.Integer(), nullable=True),
    sa.Column('week12score', sa.Integer(), nullable=True),
    sa.Column('week13score', sa.Integer(), nullable=True),
    sa.Column('week14score', sa.Integer(), nullable=True),
    sa.Column('week15score', sa.Integer(), nullable=True),
    sa.Column('week16score', sa.Integer(), nullable=True),
    sa.Column('week17score', sa.Integer(), nullable=True),
    sa.Column('week18score', sa.Integer(), nullable=True),
    sa.Column('week19score', sa.Integer(), nullable=True),
    sa.Column('week20score', sa.Integer(), nullable=True),
    sa.Column('week21score', sa.Integer(), nullable=True),
    sa.Column('week22score', sa.Integer(), nullable=True),
    sa.Column('week23score', sa.Integer(), nullable=True),
    sa.Column('week24score', sa.Integer(), nullable=True),
    sa.Column('week25score', sa.Integer(), nullable=True),
    sa.Column('week26score', sa.Integer(), nullable=True),
    sa.Column('week27score', sa.Integer(), nullable=True),
    sa.Column('week28score', sa.Integer(), nullable=True),
    sa.Column('week29score', sa.Integer(), nullable=True),
    sa.Column('week30score', sa.Integer(), nullable=True),
    sa.Column('week31score', sa.Integer(), nullable=True),
    sa.Column('week32score', sa.Integer(), nullable=True),
    sa.Column('week33score', sa.Integer(), nullable=True),
    sa.Column('week34score', sa.Integer(), nullable=True),
    sa.Column('week35score', sa.Integer(), nullable=True),
    sa.Column('week36score', sa.Integer(), nullable=True),
    sa.Column('week37score', sa.Integer(), nullable=True),
    sa.Column('week38score', sa.Integer(), nullable=True),
    sa.Column('week39score', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('uniform_score')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('uniform_score',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('year', sa.INTEGER(), nullable=True),
    sa.Column('week1score', sa.INTEGER(), nullable=True),
    sa.Column('week2score', sa.INTEGER(), nullable=True),
    sa.Column('week3score', sa.INTEGER(), nullable=True),
    sa.Column('week4score', sa.INTEGER(), nullable=True),
    sa.Column('week5score', sa.INTEGER(), nullable=True),
    sa.Column('week6score', sa.INTEGER(), nullable=True),
    sa.Column('week7score', sa.INTEGER(), nullable=True),
    sa.Column('week8score', sa.INTEGER(), nullable=True),
    sa.Column('week9score', sa.INTEGER(), nullable=True),
    sa.Column('week10score', sa.INTEGER(), nullable=True),
    sa.Column('week11score', sa.INTEGER(), nullable=True),
    sa.Column('week12score', sa.INTEGER(), nullable=True),
    sa.Column('week13score', sa.INTEGER(), nullable=True),
    sa.Column('week14score', sa.INTEGER(), nullable=True),
    sa.Column('week15score', sa.INTEGER(), nullable=True),
    sa.Column('week16score', sa.INTEGER(), nullable=True),
    sa.Column('week17score', sa.INTEGER(), nullable=True),
    sa.Column('week18score', sa.INTEGER(), nullable=True),
    sa.Column('week19score', sa.INTEGER(), nullable=True),
    sa.Column('week20score', sa.INTEGER(), nullable=True),
    sa.Column('week21score', sa.INTEGER(), nullable=True),
    sa.Column('week22score', sa.INTEGER(), nullable=True),
    sa.Column('week23score', sa.INTEGER(), nullable=True),
    sa.Column('week24score', sa.INTEGER(), nullable=True),
    sa.Column('week25score', sa.INTEGER(), nullable=True),
    sa.Column('week26score', sa.INTEGER(), nullable=True),
    sa.Column('week27score', sa.INTEGER(), nullable=True),
    sa.Column('week28score', sa.INTEGER(), nullable=True),
    sa.Column('week29score', sa.INTEGER(), nullable=True),
    sa.Column('week30score', sa.INTEGER(), nullable=True),
    sa.Column('week31score', sa.INTEGER(), nullable=True),
    sa.Column('week32score', sa.INTEGER(), nullable=True),
    sa.Column('week33score', sa.INTEGER(), nullable=True),
    sa.Column('week34score', sa.INTEGER(), nullable=True),
    sa.Column('week35score', sa.INTEGER(), nullable=True),
    sa.Column('week36score', sa.INTEGER(), nullable=True),
    sa.Column('week37score', sa.INTEGER(), nullable=True),
    sa.Column('week38score', sa.INTEGER(), nullable=True),
    sa.Column('week39score', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('uniform_scores')
    # ### end Alembic commands ###
