"""labels

Revision ID: 34a74aec6664
Revises: 12ae8b8882f
Create Date: 2012-08-15 16:26:33.012641

"""

# revision identifiers, used by Alembic.
revision = '34a74aec6664'
down_revision = '12ae8b8882f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('label',
    sa.Column('id', sa.String(length=16), nullable=False),
    sa.Column('prettyname', sa.String(length=32), nullable=False),
    sa.Column('description', sa.String(length=512), nullable=False),
    sa.Column('icon', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('article_label',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label_id', sa.String(length=16), nullable=False),
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.Column('creator_id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], ),
    sa.ForeignKeyConstraint(['creator_id'], ['useraccount.id'], ),
    sa.ForeignKeyConstraint(['label_id'], ['label.id'], ),
    sa.PrimaryKeyConstraint('id', 'label_id', 'article_id')
    )
    op.add_column(u'action', sa.Column('label_id', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'action', 'label_id')
    op.drop_table('article_label')
    op.drop_table('label')
    ### end Alembic commands ###
