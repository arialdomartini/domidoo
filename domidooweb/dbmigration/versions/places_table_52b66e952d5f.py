"""places table

Revision ID: 52b66e952d5f
Revises: None
Create Date: 2014-03-07 08:59:36.263323

"""

# revision identifiers, used by Alembic.
revision = '52b66e952d5f'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('places',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.Text(), nullable=True),
        sa.Column('city', sa.Text(), nullable=True),
        sa.Column('image', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('place_name', 'places', ['name'], unique=True)


def downgrade():
    op.drop_index('place_name', 'places')
    op.drop_table('places')
