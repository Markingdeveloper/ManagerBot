import telebot
import requests
from telebot import types

chat_permissions = telebot.types.ChatPermissions(can_send_messages = False,can_send_media_messages = False,can_send_audios = False,can_send_documents = False,can_send_photos = False,can_send_videos = False,can_send_video_notes = False,can_send_voice_notes = False,can_send_polls = False,can_send_other_messages = False,can_add_web_page_previews = False,can_change_info = False,can_invite_users = False,can_pin_messages = False,can_manage_topics = False)

anti_chat_permissions = telebot.types.ChatPermissions(can_send_messages = True,can_send_media_messages = True,can_send_audios = True,can_send_documents = True,can_send_photos = True,can_send_videos = True,can_send_video_notes = True,can_send_voice_notes = True,can_send_polls = True,can_send_other_messages = True,can_add_web_page_previews = True,can_change_info = True,can_invite_users = True,can_pin_messages = True,can_manage_topics = True)

bot = telebot.TeleBot('API_TOKEN')

@bot.message_handler(commands=['start'])
def check_chnl(message):
	bot.send_chat_action(message.chat.id, "typing")
	not_found = False
	try:
		join = bot.get_chat_member(-1001911844496, message.from_user.id)
	except Exception as e:
		if 'user not found' in str(e): not_found = True    
	if (join.status == "kicked") or (join.status == "left") or not_found == True:
		
		channelkey = types.InlineKeyboardMarkup(row_width=1)
		
		channellink = types.InlineKeyboardButton("Feature Channel", url='t.me/BannerNews')
		
		channelkey.add(channellink)
		bot.reply_to(message, f"Hi {message.from_user.first_name}!Looks like you haven't subscribed to our channel yet!To activate the bot,you need subscribe to our channel!", reply_markup=channelkey)
	else:
		bot.reply_to(message, f"Hi {message.from_user.first_name}, welcome back!Thanks for subscribing to our channel!")


	
@bot.message_handler(commands=['id'])
def id(message):
		bot.send_chat_action(message.chat.id, "typing")
		if message.reply_to_message:
		    if message.reply_to_message.from_user.id == 5852107619:
		        bot.send_message(message.chat.id, "Sorry, but I can't share my ID")
		    elif message.reply_to_message.from_user.id ==1110913967:
		        bot.send_message(message.chat.id, "Sorry, but I can't share my developer's ID")
		    else:
		        bot.send_message(message.chat.id, f"ID of {message.reply_to_message.from_user.first_name} is {message.reply_to_message.from_user.id}")
		else:
		    bot.send_message(message.chat.id, f"This chat's ID is {message.chat.id}")
	
@bot.message_handler(content_types=['new_chat_members'])
def news(message):
		for user in message.new_chat_members:
		    bot.send_chat_action(message.chat.id, "typing")
		    if user.id == 5852107619:
		    	bot.send_message(message.chat.id, "Hi all!Thanks for adding me!")
		    else:
		    	bot.restrict_chat_member(message.chat.id, user.id, permissions=telebot.types.ChatPermissions(can_send_messages = False,can_send_media_messages = False,can_send_audios = False,can_send_documents = False,can_send_photos = False,can_send_videos = False,can_send_video_notes = False,can_send_voice_notes = False,can_send_polls = False,can_send_other_messages = False,can_add_web_page_previews = False,can_change_info = False,can_invite_users = False,can_pin_messages = False,can_manage_topics = False))
		    	
		    	captcha = types.InlineKeyboardMarkup(row_width=1)
		    	
		    	click = types.InlineKeyboardButton("Solve CAPTCHA", callback_data = 'captcha')
		    	
		    	captcha.add(click)
		    	bot.reply_to(message, f"Hello {user.first_name}, welcome to the {message.chat.title}!But I want you prove you are not a robot.So you click the button in 3 minutes.If not you will be kicked from the {message.chat.title}!", reply_markup=captcha )
		    	
		    	
@bot.callback_query_handler(func = lambda call: True)
def callback(call):
	if call.message:
		if call.data == 'captcha':
			bot.restrict_chat_member(message.chat.id, message.new_chat_members.id, permissions=telebot.types.ChatPermissions(can_send_messages = True,can_send_media_messages = True,can_send_audios = True,can_send_documents = True,can_send_photos = True,can_send_videos = True,can_send_video_notes = True,can_send_voice_notes = True,can_send_polls = True,can_send_other_messages = True,can_add_web_page_previews = True,can_change_info = True,can_invite_users = True,can_pin_messages = True,can_manage_topics = True))
			bot.answer_callback_query("Congratulations.You solved the CAPTCHA!")

@bot.message_handler(content_types=['left_chat_member'])
def left(message):
		if message.left_chat_member.id == 5852107619:
			pass
		else:
			bot.send_chat_action(message.chat.id, "typing")
			bot.send_message(message.chat.id, f"Goodbye {message.left_chat_member.first_name}!")

@bot.message_handler(commands=['ban'])
def ban_user(message):
	bot.send_chat_action(message.chat.id, "typing")
	if message.chat.type in ['private']:
		bot.reply_to(message,"This command works only groups and channels.")
	else:
		get = bot.get_chat_member(message.chat.id, message.from_user.id)
		getadmin = bot.get_chat_member(message.chat.id,message.reply_to_message.from_user.id)
		getbot = bot.get_chat_member(message.chat.id, 5852107619)
		if getbot.status in ['administrator']:
			if getbot.can_restrict_members == True:
				if message.reply_to_message:
					if get.status in ["creator", "administrator"]:
						if getadmin.status in ['creator', 'administrator']:
							if message.reply_to_message.from_user.id == 5852107619:
								bot.send_message(message.chat.id, "I can't ban myself...Don't try it again.")
							else:
								bot.reply_to(message, "Admin trying to ban admin...Any last words?")
						else:
							try:
								bot.reply_to(message, "OK.User is banning")
								bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id,revoke_messages=True)
								bot.send_message(message.chat.id, "User banned!")
							except Exception as e:
								print(e)
					else:
						bot.send_message(message.chat.id, "You are not an admin to ban anyone.")
				else:
					bot.reply_to(message,"I can't ban a user without reply...")
			else:
				bot.reply_to(message, "I haven't any permission for banning users.I am admin,but you should allow the banning users permission to ban users.")
		else:
			bot.reply_to(message, "I haven't any permission for this, To ban anyone you should make me admin.")
		
@bot.message_handler(commands=['unban'])
def unban_user(message):
	bot.send_chat_action(message.chat.id, "typing")
	if message.chat.type in ['private']:
		bot.reply_to(message, "This command works only groups and channels.")
	else:
		get = bot.get_chat_member(message.chat.id, message.from_user.id)
		getadmin=bot.get_chat_member(message.chat.id,message.reply_to_message.from_user.id)
		getbot=bot.get_chat_member(message.chat.id, 5852107619)
		if getbot.status in ['administrator']:
			if getbot.can_restrict_members == True:
				if message.reply_to_message:
					if get.status in ['creator', 'administrator']:
						if getadmin.status in ['creator', 'administrator']:
							if message.reply_to_message.from_user.id == 5852107619:
								bot.reply_to(message, "I needn't unban command,I am admin")
							else:
								bot.reply_to(message, "I can't unban an admin,admins cannot be banned.Where did stupid ideas come from?")
						else:
							try:
								bot.reply_to(message, "OK.User is unbanning")
								bot.unban_chat_member(message.chat.id,message.reply_to_message.from_user.id, only_if_banned=True)
								bot.send_message(message.chat.id, "User unbanned!")
							except Exception as e:
								print(e)
					else:
						bot.send_message(message.chat.id, "You are not an admin to unban anyone.")
				else:
					 bot.reply_to(message, "I can't unban a banned user without reply...")
			else:
				bot.reply_to(message, "I haven't any permission for unbanning users.I am admin,but you should allow the banning users permission to unban users.")
		else:
			bot.reply_to(message, "I haven't any permission for this, To unban anyone you should make me admin.")
		    
		
@bot.message_handler(commands=['mute'])
def mute_user(message):
	bot.send_chat_action(message.chat.id, "typing")
	if message.chat.type in ['private']:
		bot.reply_to(message, "This command works only groups and channels.")
	else:
		get = bot.get_chat_member(message.chat.id,message.from_user.id)
		getadmin = bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
		getbot = bot.get_chat_member(message.chat.id, 5852107619)
		if getbot.status in ['administrator']:
			if getbot.can_restrict_members == True:
				if message.reply_to_message:
					if get.status in ['creator', 'administrator']:
						if getadmin.status in ['creator', 'administrator']:
							if message.reply_to_message.from_user.id == 5852107619:
								bot.reply_to(message, "I needn't mute command,thanks!")
							else:
								bot.reply_to(message, "Admins don't want any mute,I think.")
						else:
							try:
								bot.reply_to(message, "OK.User is being muted by admin!")
								bot.restrict_chat_member(message.chat.id,message.reply_to_message.from_user.id,permissions=telebot.types.ChatPermissions(can_send_messages = False,can_send_media_messages = False,can_send_audios = False,can_send_documents = False,can_send_photos = False,can_send_videos = False,can_send_video_notes = False,can_send_voice_notes = False,can_send_polls = False,can_send_other_messages = False,can_add_web_page_previews = False,can_change_info = False,can_invite_users = False,can_pin_messages = False,can_manage_topics = False))
								bot.send_message(message.chat.id, "User muted!")
							except Exception as e:
								print(e)
					else:
						bot.send_message(message.chat.id, "You are not an admin to mute anyone.")
				else:
					bot.reply_to(message, "I can't mute anyone without reply...")
			else:
				bot.reply_to(message, "I haven't any permission for muting users.I am admin,but you should allow the banning users permission to mute users.")
		else:
			bot.reply_to(message, "I haven't any permission for this, To mute anyone you should make me admin.")
		

@bot.message_handler(commands=['unmute'])
def unmute_user(message):
	bot.send_chat_action(message.chat.id, "typing")
	if message.chat.type in ['private']:
		bot.reply_to(message, "This command works only groups and channels.")
	else:
		get = bot.get_chat_member(message.chat.id,message.from_user.id)
		getadmin = bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
		getbot = bot.get_chat_member(message.chat.id, 5852107619)
		if getbot.status in ['administrator']:
			if getbot.can_restrict_members == True:
				if message.reply_to_message:
					if get.status in ['creator', 'administrator']:
						if getadmin.status in ['creator', 'administrator']:
							if message.reply_to_message.from_user.id == 5852107619:
								bot.reply_to(message, "I needn't unmute command.Are you crazy?")
							else:
								bot.reply_to(message, "I thought admins don't need unmute command...")
						else:
							try:
								bot.reply_to(message, "OK.User is being unmuted by admin!")
								bot.restrict_chat_member(message.chat.id,message.reply_to_message.from_user.id,permissions=telebot.types.ChatPermissions(can_send_messages = True,can_send_media_messages = True,can_send_audios = True,can_send_documents = True,can_send_photos = True,can_send_videos = True,can_send_video_notes = True,can_send_voice_notes = True,can_send_polls = True,can_send_other_messages = True,can_add_web_page_previews = True,can_change_info = True,can_invite_users = True,can_pin_messages = True,can_manage_topics = True))
								bot.send_message(message.chat.id, "User unmuted!")
							except Exception as e:
								print(e)
					else:
						bot.send_message(message.chat.id, "You are not an admin to unmute anyone.")
				else:
					bot.send_message(message.chat.id, "I can't unmute anyone without reply.")
			else:
				bot.reply_to(message, "I haven't any permission for unmuting users.I am admin,but you should allow the banning users permission to unmute users.")
		else:
			bot.reply_to(message, "I haven't any permission for this, To unmute anyone you should make me admin.")
		
		
@bot.message_handler(commands=['promote'])
def promote_user(message):
	bot.send_chat_action(message.chat.id, "typing")
	if message.chat.type in ['private']:
		bot.reply_to(message, "This command works only groups and channels.")
	else:
		get=bot.get_chat_member(message.chat.id,message.from_user.id)
		getadmin=bot.get_chat_member(message.chat.id,message.reply_to_message.from_user.id)
		getbot=bot.get_chat_member(message.chat.id,5852107619)
		if getbot.status in ['administrator']:
			if getbot.can_promote_members == True:
				if message.reply_to_message:
					if get.status in ['creator']:
						if getadmin.status in ['creator','administrator']:
							if message.reply_to_message.from_user.id == 5852107619:
								bot.reply_to(message, "I am admin,I needn't any promotes for now.")
							else:
								bot.reply_to(message,f"You needn't promote {message.reply_to_message.from_user.first_name},he is already an admin.")
						else:
							try:
								bot.reply_to(message, "User is being made to an admin...")
								bot.promote_chat_member(message.chat.id,message.reply_to_message.from_user.id,is_anonymous=False,can_manage_chat=True,can_post_messages=True,can_edit_messages=True,can_delete_messages=True,can_manage_video_chats=True,can_restrict_members=True,can_promote_members=False,can_change_info=True,can_invite_users=True,can_pin_messages=True,can_manage_topics=True)
								bot.send_message(message.chat.id, "User promoted to admin sucessfully...")
							except Exception as e:
								print(e)
					else:
						bot.send_message(message.chat.id,f"Only creators of {message.chat.title} can use this command.")
				else:
					bot.send_message(message.chat.id, "I can't promote anyone without reply.")
			else:
				bot.reply_to(message, "I haven't any permission for promoting users.I am admin,but you should allow the add new admins permission to promote users.")
		else:
			bot.reply_to(message, "I haven't any permission for this, To promote users you should make me admin.")
		
@bot.message_handler(commands=['demote'])
def demote_user(message):
	bot.send_chat_action(message.chat.id, "typing")
	if message.chat.type in ['private']:
		bot.reply_to(message, "This command works only groups and channels.")
	else:
		get=bot.get_chat_member(message.chat.id,message.from_user.id)
		getadmin=bot.get_chat_member(message.chat.id,message.reply_to_message.from_user.id)
		getbot=bot.get_chat_member(message.chat.id,5852107619)
		if getbot.status in ['administrator']:
			if getbot.can_promote_members == True:
				if message.reply_to_message:
					if get.status in ['creator']:
						if getadmin.status not in ['creator','administrator']:
							bot.reply_to(message,f"You needn't demote {message.reply_to_message.from_user.first_name},He is already a user.")
						else:
							if message.reply_to_message.from_user.id == 5852107619:
								bot.reply_to(message, "I can't demote myself.Nice try!")
							else:
								try:
									bot.reply_to(message, "Admin is being made to a user again...")
									bot.promote_chat_member(message.chat.id,message.reply_to_message.from_user.id,is_anonymous=False,can_manage_chat=False,can_post_messages=False,can_edit_messages=False,can_delete_messages=False,can_manage_video_chats=False,can_restrict_members=False,can_promote_members=False,can_change_info=False,can_invite_users=False,can_pin_messages=False,can_manage_topics=False)
									bot.send_message(message.chat.id, "Admin demoted to user sucessfully...")
								except Exception as e:
									print(e)
					else:
						bot.send_message(message.chat.id,f"Only creators of {message.chat.title} can use this command.")
				else:
					bot.send_message(message.chat.id,"I can't demote an admin without reply...")
			else:
				bot.reply_to(message, "I haven't any permission for demoting admins.I am admin,but you should allow the add new admins permission to demote admins.")
		else:
			bot.reply_to(message, "I am not an admin, first you should make me admin...")

@bot.message_handler(commands=['pin'])
def pin(message):
	bot.send_chat_action(message.chat.id, "typing")
	if message.chat.type in ['private']:
		bot.reply_to(message, "This command works only groups and channels.")
	else:
		get=bot.get_chat_member(message.chat.id,message.from_user.id)
		getbot=bot.get_chat_member(message.chat.id, 5852107619)
		if getbot.status in ['administrator']:
			if getbot.can_pin_messages == True:
				if message.reply_to_message:
					if get.status in ['creator','administrator']:
						try:
							bot.reply_to(message,"Message is being pinned...")
							bot.pin_chat_message(message.chat.id,message.reply_to_message.id,disable_notification=False)
							bot.reply_to(message, "Message is pinned sucessfully!")
						except Exception as e:
							print(e)
					else:
						bot.reply_to(message, "You are not an admin to pin a message.")
				else:
					bot.reply_to(message, "I can't pin a message without reply...")
			else:
				bot.reply_to(message, "I haven't any permission for pinning messages.I am admin,but you should allow the pin messages permission to pin messages.")
		else:
			bot.reply_to(message, "I haven't any permission for this, To pin messages you should make me admin.")
				
@bot.message_handler(commands=['unpin'])
def unpin(message):
	bot.send_chat_action(message.chat.id, "typing")
	if message.chat.type in ['private']:
		bot.reply_to(message, "This command works only groups and channels.")
	else:
		get = bot.get_chat_member(message.chat.id,message.from_user.id)
		getbot = bot.get_chat_member(message.chat.id)
		if getbot.status in ['administrator']:
			if getbot.can_pin_messages == True:
				if message.reply_to_message:
					if get.status in ['creator','administrator']:
						try:
							bot.reply_to(message,"Message is being unpinned...")
							bot.unpin_chat_message(message.chat.id,message.reply_to_message.id)
							bot.reply_to(message, "Message is unpinned sucessfully!")
						except Exception as e:
							print(e)
					else:
						bot.reply_to(message, "You are not an admin to unpin a message.")
				else:
					bot.reply_to(message, "I can't unpin a message without reply...")
			else:
				bot.reply_to(message, "I haven't any permission for unpinning messages.I am admin,but you should allow the pin messages permission to unpin messages.")
		else:
			bot.reply_to(message, "I haven't any permission for this, To unpin messages you should make me admin.")
				
			
print("Bot is running without errors")

bot.infinity_polling()
