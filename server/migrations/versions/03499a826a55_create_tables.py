"""create tables

Revision ID: 03499a826a55
Revises: 
Create Date: 2023-09-21 13:04:59.889952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03499a826a55'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bakery',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('baked_good',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('bakery_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bakery_id'], ['bakery.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('baked_good')
    op.drop_table('bakery')
    # ### end Alembic commands ###
