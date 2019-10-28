"""empty message

Revision ID: 0b4543c610dc
Revises: b5aa287a3e0a
Create Date: 2019-10-28 12:07:18.344711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b4543c610dc'
down_revision = 'b5aa287a3e0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('volunteer_opportunity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('opportunity_id', sa.Integer(), nullable=True),
    sa.Column('volunteer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['opportunity_id'], ['opportunity.id'], ),
    sa.ForeignKeyConstraint(['volunteer_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('volunteer_opportunity')
    # ### end Alembic commands ###
