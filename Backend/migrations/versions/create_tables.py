"""Create tables"""

from alembic import op
import sqlalchemy as sa

revision = 'create_tables'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():

    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(length=64), nullable=False),
        sa.Column('email', sa.String(length=120), nullable=False),
        sa.Column('password', sa.String(), nullable=False),  # Adicionando campo senha
        sa.Column('team', sa.String(length=64), nullable=False),
        sa.Column('createdAt', sa.DateTime(), nullable=False, server_default=sa.func.now()),  # Adicionando campo createdAt
        sa.Column('updatedAt', sa.DateTime(), nullable=False, server_default=sa.func.now(), onupdate=sa.func.now()),  # Adicionando campo updatedAt
        sa.Column('role', sa.Integer(), nullable=False),  # Adicionando campo role
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('roles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('role', sa.String(length=64), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('positions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('position', sa.String(length=64), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('athletes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=64), nullable=False),
        sa.Column('number', sa.Integer(), nullable=False),
        sa.Column('birthDate', sa.Date(), nullable=False),
        sa.Column('position', sa.String(length=64), nullable=False),
        sa.Column('createdAt', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column('updatedAt', sa.DateTime(), nullable=False, server_default=sa.func.now(), onupdate=sa.func.now()),
        sa.PrimaryKeyConstraint('id')
    )

    op.execute(
        """
        INSERT INTO positions (position) 
        VALUES 
            ('Goleiro'),
            ('Zagueiro'),
            ('Lateral Direito'),
            ('Lateral Esquerdo'),
            ('Volante'),
            ('Meia'),
            ('Centroavante'),
            ('Atacante'),
            ('Ponta')
        """
    )

    op.execute(
        """
        INSERT INTO roles (role) 
        VALUES
            ('ADMIN'),
            ('FISIOTERAPEUTA'),
            ('ESTAGIÁRIO')
        """
    )

def downgrade():
    op.drop_table('positions')

    op.drop_table('users')

    op.drop_table('athletes')

    op.drop_table('roles')


