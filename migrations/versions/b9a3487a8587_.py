"""empty message

Revision ID: b9a3487a8587
Revises: 31016f937759
Create Date: 2020-12-18 19:28:36.362672

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b9a3487a8587'
down_revision = '31016f937759'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('email', sa.String(length=120), nullable=False))
    op.create_unique_constraint(None, 'cart', ['email'])
    op.add_column('history', sa.Column('email', sa.String(length=120), nullable=False))
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.drop_column('history', 'email')
    op.drop_constraint(None, 'cart', type_='unique')
    op.drop_column('cart', 'email')
    # ### end Alembic commands ###
