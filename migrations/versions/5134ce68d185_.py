"""empty message

Revision ID: 5134ce68d185
Revises: 89958702617b
Create Date: 2022-05-10 09:54:13.911551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5134ce68d185'
down_revision = '89958702617b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('driver',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('team', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('handsome', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('car', sa.Column('driver_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'car', 'driver', ['driver_id'], ['id'])
    op.drop_column('car', 'team')
    op.drop_column('car', 'driver')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('car', sa.Column('driver', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('car', sa.Column('team', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'car', type_='foreignkey')
    op.drop_column('car', 'driver_id')
    op.drop_table('driver')
    # ### end Alembic commands ###
