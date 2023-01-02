"""empty message

Revision ID: 68c1c1fb5542
Revises: 5f19c113b71e
Create Date: 2023-01-02 17:17:53.962158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68c1c1fb5542'
down_revision = '5f19c113b71e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('influence_band', schema=None) as batch_op:
        batch_op.add_column(sa.Column('genre', sa.String(length=80), nullable=False))
        batch_op.drop_constraint('influence_band_music_genre_name_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'music_genre', ['genre'], ['name'])
        batch_op.drop_column('music_genre_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('influence_band', schema=None) as batch_op:
        batch_op.add_column(sa.Column('music_genre_name', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('influence_band_music_genre_name_fkey', 'music_genre', ['music_genre_name'], ['name'])
        batch_op.drop_column('genre')

    # ### end Alembic commands ###
