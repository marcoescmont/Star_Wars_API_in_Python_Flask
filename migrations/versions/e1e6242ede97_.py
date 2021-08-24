"""empty message

Revision ID: e1e6242ede97
Revises: 3bc61b5e68bb
Create Date: 2021-08-24 04:03:12.045735

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e1e6242ede97'
down_revision = '3bc61b5e68bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planet', sa.Column('climate', sa.String(length=150), nullable=False))
    op.add_column('planet', sa.Column('diameter', sa.String(length=150), nullable=False))
    op.add_column('planet', sa.Column('orbital_period', sa.String(length=150), nullable=False))
    op.drop_column('planet', 'terrain')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planet', sa.Column('terrain', mysql.VARCHAR(length=500), nullable=False))
    op.drop_column('planet', 'orbital_period')
    op.drop_column('planet', 'diameter')
    op.drop_column('planet', 'climate')
    # ### end Alembic commands ###
