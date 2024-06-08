"""Add TETRIO user configuration

迁移 ID: a1195e989cc6
父迁移: b15844837693
创建时间: 2024-06-09 04:20:07.819194

"""

from __future__ import annotations

from typing import TYPE_CHECKING

import sqlalchemy as sa
from alembic import op

if TYPE_CHECKING:
    from collections.abc import Sequence

revision: str = 'a1195e989cc6'
down_revision: str | Sequence[str] | None = 'b15844837693'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade(name: str = '') -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'nonebot_plugin_tetris_stats_tetriouserconfig',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('query_template', sa.String(length=2), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_nonebot_plugin_tetris_stats_tetriouserconfig')),
        info={'bind_key': 'nonebot_plugin_tetris_stats'},
    )
    # ### end Alembic commands ###


def downgrade(name: str = '') -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nonebot_plugin_tetris_stats_tetriouserconfig')
    # ### end Alembic commands ###
