"""Create users table

Revision ID: 1790ed35cbd1
Revises: 
Create Date: 2026-04-30 19:57:34.743356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1790ed35cbd1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('email', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('users')
