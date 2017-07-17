# coding: utf-8

import itchat 

itchat.auto_login(hotReload = True)

friendList = itchat.get_friends(update=True)[1:]

genderDict = {}
total = len(friendList)
for friend in friendList:
	if not friend['Sex'] in genderDict:
		genderDict[friend['Sex']] = []
	genderDict[friend['Sex']].append(friend['NickName'])

unknown = len(genderDict[0])
male = len(genderDict[1])
female = len(genderDict[2])

ratio = int (male * 100.0/ (male + female))

print '您共有好友 %s位，\n未知性别信息 %d位，男性 %d位，女性 %d位。\n男女比例 %d: %d' % (total, unknown, male, female, ratio, 100 - ratio)