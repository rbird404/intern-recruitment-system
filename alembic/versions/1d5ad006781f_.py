"""

Revision ID: 1d5ad006781f
Revises: 61f341d5d3da
Create Date: 2023-10-20 21:14:33.494614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d5ad006781f'
down_revision = '61f341d5d3da'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('text', 'code', name='questiontype'), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('codes',
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tests',
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('type', sa.Enum('text', 'code', name='questiontype'), nullable=False),
    sa.Column('creator_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['creator_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('texts',
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('test_cases',
    sa.Column('input', sa.String(), nullable=True),
    sa.Column('output', sa.String(), nullable=True),
    sa.Column('error', sa.String(), nullable=True),
    sa.Column('code_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['code_id'], ['codes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('test_questions',
    sa.Column('test_id', sa.Integer(), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ),
    sa.ForeignKeyConstraint(['test_id'], ['tests.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('email', sa.String(), nullable=False))
    op.create_unique_constraint(None, 'users', ['email'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'email')
    op.drop_table('test_questions')
    op.drop_table('test_cases')
    op.drop_table('texts')
    op.drop_table('tests')
    op.drop_table('codes')
    op.drop_table('questions')
    # ### end Alembic commands ###