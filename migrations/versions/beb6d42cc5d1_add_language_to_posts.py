"""add language to posts

Revision ID: beb6d42cc5d1
Revises: 6992a97c41d2
Create Date: 2024-07-10 12:15:23.379899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'beb6d42cc5d1'
down_revision = '6992a97c41d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language', sa.String(length=5), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('language')

    # ### end Alembic commands ###
