"""

Revision ID: 76a0dbbee9cf
Revises: d7c669f826da
Create Date: 2023-10-21 01:53:46.165826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76a0dbbee9cf'
down_revision = 'd7c669f826da'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test_questions', sa.Column('point', sa.Integer(), nullable=False))
    op.alter_column('test_questions', 'test_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('test_questions', 'question_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('test_questions', 'question_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('test_questions', 'test_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('test_questions', 'point')
    # ### end Alembic commands ###