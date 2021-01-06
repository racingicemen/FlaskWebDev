"""caching of avatar hashes

Revision ID: 01646904a833
Revises: eed2b0c9c591
Create Date: 2021-01-06 11:44:32.398009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01646904a833'
down_revision = 'eed2b0c9c591'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    # ### end Alembic commands ###
