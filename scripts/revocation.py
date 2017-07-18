# coding: utf-8
import itchat
from itchat.content import *

@itchat.msg_register([TEXT, PICTURE, MAP, CARD, SHARING, RECORDING, ATTACHMENT, VIDEO, FRIENDS])
def deal_message(msg):
	msg_id = msg['MsgId']
	msg_time = msg['CreateTime']
	msg_from = msg['FromUserName']
	msg_type = msg['Type']
	msg_content = None
	msg_url = None

	if msg['Type'] == 'Text':
		msg_content = msg['Text']
	elif msg['Type'] == 'Picture':
		msg_content = msg['FileName']
		msg['Text'](msg['FileName'])


itchat.auto_login(hotReload = True)
itchat.run()