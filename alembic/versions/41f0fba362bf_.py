"""

Revision ID: 41f0fba362bf
Revises: cea600476d0b
Create Date: 2023-10-21 09:13:49.519800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41f0fba362bf'
down_revision = 'cea600476d0b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('answers',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('coefficient', sa.Float(), nullable=False),
    sa.Column('test_id', sa.Integer(), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.Enum('text', 'code', name='answertype'), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['test_id'], ['tests.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('answers')
    # ### end Alembic commands ###
