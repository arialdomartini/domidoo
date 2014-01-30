"""models table

Revision ID: 4ff2e3c81ff9
Revises: None
Create Date: 2014-01-30 09:21:56.518357

"""

# revision identifiers, used by Alembic.
revision = '4ff2e3c81ff9'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'Models',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.Unicode(50), nullable=False),
        sa.Column('value', sa.Unicode(200)),
    )


def downgrade():
    pass
