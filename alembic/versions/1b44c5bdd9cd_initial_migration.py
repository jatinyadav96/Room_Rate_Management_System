"""Initial migration

Revision ID: 1b44c5bdd9cd
Revises: 
Create Date: 2024-06-23 18:39:27.585801

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b44c5bdd9cd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('room_rates',
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('room_name', sa.String(length=255), nullable=True),
    sa.Column('default_rate', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('room_id')
    )
    op.create_index(op.f('ix_room_rates_room_id'), 'room_rates', ['room_id'], unique=False)
    op.create_index(op.f('ix_room_rates_room_name'), 'room_rates', ['room_name'], unique=False)
    op.create_table('discount_room_rates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_rate_id', sa.Integer(), nullable=True),
    sa.Column('discount_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['discount_id'], ['discounts.discount_id'], ),
    sa.ForeignKeyConstraint(['room_rate_id'], ['room_rates.room_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_discount_room_rates_id'), 'discount_room_rates', ['id'], unique=False)
    op.create_table('overridden_room_rates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_rate_id', sa.Integer(), nullable=True),
    sa.Column('overridden_rate', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('stay_date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['room_rate_id'], ['room_rates.room_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_overridden_room_rates_id'), 'overridden_room_rates', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_overridden_room_rates_id'), table_name='overridden_room_rates')
    op.drop_table('overridden_room_rates')
    op.drop_index(op.f('ix_discount_room_rates_id'), table_name='discount_room_rates')
    op.drop_table('discount_room_rates')
    op.drop_index(op.f('ix_room_rates_room_name'), table_name='room_rates')
    op.drop_index(op.f('ix_room_rates_room_id'), table_name='room_rates')
    op.drop_table('room_rates')
    # ### end Alembic commands ###
