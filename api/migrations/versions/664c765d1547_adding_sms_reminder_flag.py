"""adding_sms_reminder_flag

Revision ID: 664c765d1547
Revises: 34df859d1d05
Create Date: 2021-01-25 17:27:12.820675

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utc


# revision identifiers, used by Alembic.
revision = '664c765d1547'
down_revision = '34df859d1d05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('publicuser', 'send_reminders', nullable=True, new_column_name='send_email_reminders')
    op.add_column('publicuser', sa.Column('send_sms_reminders', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('publicuser', 'send_email_reminders', nullable=True, new_column_name='send_reminders')
    op.drop_column('publicuser', 'send_sms_reminders')
    # ### end Alembic commands ###