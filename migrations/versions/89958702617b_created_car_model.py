"""Created Car model

Revision ID: 89958702617b
Revises: 
Create Date: 2022-04-29 10:19:51.431300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89958702617b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('driver', sa.String(), nullable=True),
    sa.Column('team', sa.String(), nullable=True),
    sa.Column('mass_kg', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('car')
    # ### end Alembic commands ###
