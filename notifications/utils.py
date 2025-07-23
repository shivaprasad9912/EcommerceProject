from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_order_notification(user_id, message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'notifications_{user_id}',
        {
            'type': 'notification_message',
            'message': message
        }
    )