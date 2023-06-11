"""Update whiskey_token

Revision ID: 2fd414aaeb77
Revises: fabc1f15cdea
Create Date: 2023-06-10 18:49:33.679625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fd414aaeb77'
down_revision = 'fabc1f15cdea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('whiskey', schema=None) as batch_op:
        batch_op.alter_column('whiskey_price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('whiskey', schema=None) as batch_op:
        batch_op.alter_column('whiskey_price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=True)

    # ### end Alembic commands ###
