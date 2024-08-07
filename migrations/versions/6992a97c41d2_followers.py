"""followers

Revision ID: 6992a97c41d2
Revises: d49dae011ce6
Create Date: 2024-07-03 17:20:20.443028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6992a97c41d2'
down_revision = 'd49dae011ce6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followed_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
