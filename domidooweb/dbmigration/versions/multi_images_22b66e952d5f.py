"""places multi_images

Revision ID: 22b66e952d5f
Revises: None
Create Date: 2014-03-27 08:59:36.263323

"""

# revision identifiers, used by Alembic.
revision = '22b66e952d5f'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('places',
        sa.Column('id', sa.Text(), nullable=False),
        sa.Column('name', sa.Text(), nullable=True),
        sa.Column('city', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('tags',
        sa.Column('id', sa.Text(), nullable=False),
        sa.Column('name', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('places_tags',
        sa.Column('place_id', sa.Integer(), nullable=True),
        sa.Column('tag_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['place_id'], ['places.id'], ),
        sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], )
    )

    op.create_table('images',
        sa.Column('id', sa.Text(), nullable=False),
        sa.Column('place_id', sa.Text(), nullable=False),
        sa.Column('filename', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id')
#        sa.ForeignKeyConstraint(['image_id'], ['images.id'] )
    )


def downgrade():
    op.drop_table('places')
    op.drop_table('places_tags')
    op.drop_table('tags')

