"""add need_sourcing and help_req to article

Revision ID: 59f85960778
Revises: 47f6606cd6c4
Create Date: 2012-06-06 17:29:21.953883

"""

# revision identifiers, used by Alembic.
revision = '59f85960778'
down_revision = '47f6606cd6c4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('needs_sourcing', sa.Boolean(), nullable=False))
    op.add_column('article', sa.Column('help_req_id', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'help_req_id')
    op.drop_column('article', 'needs_sourcing')
    ### end Alembic commands ###
