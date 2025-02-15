"""campos

Revision ID: a29870740f1a
Revises: a4b99a6fc851
Create Date: 2021-06-26 19:37:34.280025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a29870740f1a'
down_revision = 'a4b99a6fc851'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'prova', 'professor', ['professor'], ['id'], ondelete='CASCADE')
    op.add_column('resposta', sa.Column('aluno', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'resposta', 'aluno', ['aluno'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'resposta', type_='foreignkey')
    op.drop_column('resposta', 'aluno')
    op.drop_constraint(None, 'prova', type_='foreignkey')
    # ### end Alembic commands ###
