"""empty message

Revision ID: 88869953e736
Revises: 
Create Date: 2019-10-23 16:48:01.032698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88869953e736'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###