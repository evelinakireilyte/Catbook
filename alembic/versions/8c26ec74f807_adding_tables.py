"""adding tables

Revision ID: 8c26ec74f807
Revises: 
Create Date: 2022-01-03 10:38:44.573824

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision = '8c26ec74f807'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_types_id'), 'types', ['id'], unique=False)
    op.create_table('documents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('position', sa.String(), nullable=True),
    sa.Column('img', sa.String(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['type_id'], ['types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_documents_id'), 'documents', ['id'], unique=False)
    # ### end Alembic commands ###
    conn = op.get_bind()
    conn.execute(
        text(
            """
                insert into types 
                (id, name) VALUES (1, 'bank-draft'), (2, 'bill-of-lading'), (3, 'bank-draft-2'), (4, 'bill-of-lading-2'), (5, 'invoice');
            """
        )
    )

    conn.execute(
        text(
            """
                insert into documents 
                (title, position, img, type_id) VALUES ('Bank Draft', 0, 'https://media3.giphy.com/media/OWVrMAxmD9jxe/giphy.gif?cid=ecf05e472hfshuogzur4rpax8dpsfwq7dszvhj81sz55wekq&rid=giphy.gif&ct=g', 1), 
                ('Bill of Lading', 1, 'https://media4.giphy.com/media/ASvQ3A2Q7blzq/giphy.gif?cid=ecf05e47a4hcuu3tnvgvbwpgiv68d2aajemcaw2dy3kowoyj&rid=giphy.gif&ct=g', 2), 
                ('Invoice', 2, 'https://media0.giphy.com/media/11quO2C07Sh2oM/giphy.gif?cid=ecf05e47kwmbq1yor41tnc7vgpgz8dpnpeus3etwar30ekx9&rid=giphy.gif&ct=g', 5), 
                ('Bank Draft 2', 3, 'https://media3.giphy.com/media/ICOgUNjpvO0PC/giphy.gif?cid=ecf05e47x2uj6qsvine5vhxinlv26w4a9rbub1qw60sfntyg&rid=giphy.gif&ct=g', 3), 
                ('Bill of Lading 2', 4, 'https://media2.giphy.com/media/Nm8ZPAGOwZUQM/giphy.gif?cid=ecf05e47ezqojpwxs27qfmn5ea0qpoef1rbylskihcac75gm&rid=giphy.gif&ct=g', 4);
            """
        )
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_documents_id'), table_name='documents')
    op.drop_table('documents')
    op.drop_index(op.f('ix_types_id'), table_name='types')
    op.drop_table('types')
    # ### end Alembic commands ###
