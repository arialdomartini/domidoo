"""a place has an image

Revision ID: fdd4ffda827
Revises: 3d6bcc2372c0
Create Date: 2014-02-24 18:10:42.499236

"""

# revision identifiers, used by Alembic.
revision = 'fdd4ffda827'
down_revision = '3d6bcc2372c0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('places',
            sa.Column('image', sa.Unicode(100)),
    )

def downgrade():
    pass
