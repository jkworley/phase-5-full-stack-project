"""empty message

Revision ID: c7c20f3a4b27
Revises: 1cb2eca7f0c8
Create Date: 2023-07-27 16:30:00.174189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7c20f3a4b27'
down_revision = '1cb2eca7f0c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('_password_hash', sa.String(), nullable=True))
        batch_op.drop_column('_password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('_password', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('_password_hash')

    # ### end Alembic commands ###
