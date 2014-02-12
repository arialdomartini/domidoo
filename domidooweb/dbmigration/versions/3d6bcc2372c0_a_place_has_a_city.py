"""a place has a city

Revision ID: 3d6bcc2372c0
Revises: 4a5efd37543d
Create Date: 2014-02-12 19:22:10.692892

"""

# revision identifiers, used by Alembic.
revision = '3d6bcc2372c0'
down_revision = '4a5efd37543d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('places',
        sa.Column('city', sa.Unicode(50))
    )


def downgrade():
    pass
