"""empty message

Revision ID: 53833c43136a
Revises: ae54e998afc8
Create Date: 2023-04-12 19:13:33.121419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53833c43136a'
down_revision = 'ae54e998afc8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('login', sa.String(length=180), nullable=False))
        batch_op.add_column(sa.Column('password_hash', sa.String(length=150), nullable=False))
        batch_op.create_unique_constraint("uq_user_login", ['login'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint("uq_user_login", type_='unique')
        batch_op.drop_column('password_hash')
        batch_op.drop_column('login')

    # ### end Alembic commands ###