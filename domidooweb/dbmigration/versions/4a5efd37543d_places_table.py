"""places table

Revision ID: 4a5efd37543d
Revises: 4ff2e3c81ff9
Create Date: 2014-02-11 18:37:52.791985

"""

# revision identifiers, used by Alembic.
revision = '4a5efd37543d'
down_revision = '4ff2e3c81ff9'

from alembic import op
import sqlalchemy as sa

def upgrade():
 op.create_table(
        'places',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('name', sa.Unicode(50), nullable=False, unique=True),
    )


def downgrade():
    pass
