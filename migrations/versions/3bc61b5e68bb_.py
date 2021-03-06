"""empty message

Revision ID: 3bc61b5e68bb
Revises: c8cf7246717f
Create Date: 2021-08-24 04:01:15.230233

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3bc61b5e68bb'
down_revision = 'c8cf7246717f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planet', sa.Column('terrain', sa.String(length=500), nullable=False))
    op.drop_column('planet', 'diameter')
    op.drop_column('planet', 'orbital_period')
    op.drop_column('planet', 'climate')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planet', sa.Column('climate', mysql.VARCHAR(length=150), nullable=False))
    op.add_column('planet', sa.Column('orbital_period', mysql.VARCHAR(length=150), nullable=False))
    op.add_column('planet', sa.Column('diameter', mysql.VARCHAR(length=150), nullable=False))
    op.drop_column('planet', 'terrain')
    # ### end Alembic commands ###
