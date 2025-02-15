"""add_acertou_resposta

Revision ID: 5da2f7dbca15
Revises: 01bc05d69e09
Create Date: 2021-06-26 15:32:26.043197

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5da2f7dbca15'
down_revision = '01bc05d69e09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('resposta', sa.Column('acertou', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('resposta', 'acertou')
    # ### end Alembic commands ###
