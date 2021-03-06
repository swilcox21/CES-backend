"""empty message

Revision ID: f92312ff6286
Revises: 
Create Date: 2020-11-13 15:18:44.049015

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f92312ff6286'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('unit_price', sa.Integer(), nullable=False),
    sa.Column('sub_total', sa.Integer(), nullable=False),
    sa.Column('color', sa.String(length=120), nullable=False),
    sa.Column('size', sa.String(length=120), nullable=False),
    sa.Column('units', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=5000), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('unit_price', sa.Integer(), nullable=False),
    sa.Column('sub_total', sa.Integer(), nullable=False),
    sa.Column('color', sa.String(length=120), nullable=False),
    sa.Column('size', sa.String(length=120), nullable=False),
    sa.Column('units', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=5000), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=120), nullable=False),
    sa.Column('card', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('card')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('street_address', sa.String(length=120), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('the_state', sa.String(length=120), nullable=True),
    sa.Column('zip_code', sa.String(length=120), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('street_address')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('transactions')
    op.drop_table('history')
    op.drop_table('cart')
    # ### end Alembic commands ###
