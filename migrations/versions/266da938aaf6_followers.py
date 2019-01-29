"""followers

Revision ID: 266da938aaf6
Revises: 8e820c8b8433
Create Date: 2019-01-29 16:49:36.047336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '266da938aaf6'
down_revision = '8e820c8b8433'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
